from django.conf import settings
from jose import jwt
import requests
import http.client
import json
from .models import Auth0ManagementApiToken

def requestToken():
    obj_all = Auth0ManagementApiToken.objects.all()
    if not obj_all:
        newT = askNewToken()
        return newT
    else:
        obj = Auth0ManagementApiToken.objects.all()[:1].get()
        _, valid = isValidToken(obj.token)
        if valid == True:
            return obj.token
        else:
            newT = askNewToken()
            obj.delete()
            return newT.token


def askNewToken():
    conn = http.client.HTTPSConnection(settings.AUTH0_DOMAIN)
    
    ## CHECK!!1
    payload = "{\"client_id\":\"kY0oU4Lf1THGKM9G8ianbp0yDTQX0Yc5\",\"client_secret\":\"yAz5myhpPkF66dbKIBii05-AAgEsf1B4UoJN7_G5RZyS0vfrsd-DlhaPeuIDEedA\",\"audience\":\"https://esena-app.us.auth0.com/api/v2/\",\"grant_type\":\"client_credentials\"}"

    headers = {'content-type': "application/json"}

    conn.request("POST", "/oauth/token", payload, headers)

    res = conn.getresponse()
    data = res.read()

    datajson = json.loads(data.decode("utf-8"))
    token = Auth0ManagementApiToken(token=datajson['access_token'])
    token.save()    
    return token


def isValidToken(token):
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
                audience=settings.AUTH0_MANAGEMENT_API_AUDIENCE,
                issuer='https://'+settings.AUTH0_DOMAIN+'/'
            )
            return payload, True
        except jwt.ExpiredSignatureError:
            print('Token is expired')
            return "ExpiredSignatureError", False

        except jwt.JWTClaimsError:
            print(
                'Incorrect claims, please check the audience and issuer'
            )
            return "JWTClaimsError", False
        except Exception as e:
            print(
                'Unable to parse authentication'
            )
            return "Exception", False

    return {}, False
