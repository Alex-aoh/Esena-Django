import requests
from django.conf import settings
from django.contrib.auth import get_user_model
from jose import jwt
from rest_framework import exceptions
from rest_framework.authentication import (BaseAuthentication,
                                           get_authorization_header)

from authz.models import Auth0User
from authz.auth0.auth0_utils import  get_auth0_authtentication_user_info

User = get_user_model()

def is_valid_auth0token(token):
    # TODO: remove request and make the `json` file as part of the project to save the request time
    resp = requests.get('https://'+settings.AUTH0_DOMAIN +
                        '/.well-known/jwks.json')
    jwks = resp.json()
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}
    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=settings.AUTH0_ALGORITHMS,
                audience=settings.AUTH0_API_AUDIENCE,
                issuer='https://'+settings.AUTH0_DOMAIN+'/'
            )
            return payload, True
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token is expired')
        except jwt.JWTClaimsError:
            raise exceptions.AuthenticationFailed(
                'Incorrect claims, please check the audience and issuer'
            )
        except Exception as e:
            raise exceptions.AuthenticationFailed(
                'Unable to parse authentication'
            )

    return {}, False





class Auth0TokenAuthentication(BaseAuthentication):
    '''
    Auth0 token based authentication.
    Clients should authenticate by passing the token key in the 'Authorization'
    HTTP header, prepended with the string 'Bearer '.  For example:
        Authorization: Bearer <token data>
    '''

    keyword = 'Bearer'
    err_msg = 'Invalid token headers'

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            raise exceptions.AuthenticationFailed(self.err_msg)

        if len(auth) > 2:
            raise exceptions.AuthenticationFailed(self.err_msg)
        token = auth[1]
        return self.authenticate_credentials(token)

    def authenticate_credentials(self, token):
        payload, is_valid = is_valid_auth0token(token)
        if not is_valid:
            raise exceptions.AuthenticationFailed(self.err_msg)
        # Access token payload auth0_id
        auth0_id = payload['sub']

        # Check auth0user existance in DB
        auth0user = Auth0User.objects.filter(auth0_id=auth0_id).last()
        if not auth0user:
            # Get User Info
            user_data = get_auth0_authtentication_user_info(token)

            # Email
            email = user_data.get('email')
            if not email:
                raise exceptions.AuthenticationFailed(self.err_msg)
            
            # Email verified bool
            email_verified = user_data.get('email_verified')
            if email_verified == None:
                raise exceptions.AuthenticationFailed(self.err_msg)
            

            # Django User get or create
            user, _ = User.objects.get_or_create(
                email=email, username=auth0_id)
            
            
            # Auth0 User get or create
            auth0user, _ = Auth0User.objects.get_or_create(
                auth0_id=auth0_id,
                user=user, email=email, email_verified=email_verified)
            
        return auth0user.user, token

