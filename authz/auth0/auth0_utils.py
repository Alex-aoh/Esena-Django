from django.conf import settings
from .auth0_management_token import requestToken
import json
import requests
from requests.exceptions import RequestException, HTTPError, URLRequired


# Authentication API | User Info endpoint
def get_auth0_authtentication_user_info(token):
    url = 'https://' + settings.AUTH0_DOMAIN + '/userinfo'
    params = {'access_token': token}
    resp = requests.get(url, params)
    data = resp.json()
    print(data)
    return data

# Management API | Get User endpoint - use with auth0user model
def get_auth0_managemenet_user(auth0user):
    url = 'https://' + settings.AUTH0_MANAGEMENET_API_ROUTE + f'users/{auth0user.auth0_id}'  
    token = requestToken()
    headers = {
        'content-type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    try:
        res = requests.get(url, headers=headers)
        return res.json(), res
    except HTTPError as e:
        print(f'HTTPError: {str(e.code)} {str(e.reason)}')
        return f'HTTPError: {str(e.code)} {str(e.reason)}', res
    except URLRequired as e:
        print(f'URLRequired: {str(e.reason)}')
        return f'URLRequired: {str(e.reason)}', res
    except RequestException as e:
        print(f'RequestException: {e}')
        return f'RequestException: {e}', res
    except Exception as e:
        print(f'Generic Exception: {e}')
        return f'Generic Exception: {e}', res
