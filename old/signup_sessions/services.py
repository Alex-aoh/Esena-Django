import requests
import json


from django.shortcuts import get_object_or_404
from authz.auth0.auth0_management_token import requestToken

from json import JSONDecodeError
from .models import SignUpSession,UsernameSignUpSession, EmailSignUpSession, PasswordSignUpSession
from common.exceptions import ServiceUnavailable

# --- Sign Up Session Username Check ---
def username_signup_session_check(auth0user, username):
    # auth0user, Username String
    session, _ = SignUpSession.objects.get_or_create(auth0user=auth0user)

    username_query = UsernameSignUpSession.objects.filter(username=username)
    if username_query:
        if username_query.last().signup_session == session:
            return False
        else:
            return True
    else:
        # request server check
        url = f"https://esena-app.us.auth0.com/api/v2/users?q=username%3A{username}"
        payload={}
        headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {requestToken()}'
        }
        # REQUEST Retry loop
        for i in range(5):
            for attempt in range(5):
                try:
                    response = requests.request("GET", url, headers=headers, data=payload)
                except requests.exceptions.ConnectionError:
                    continue
                except requests.exceptions.RequestException:
                    raise ServiceUnavailable
                else:
                    break
            else:
                raise ServiceUnavailable
        # REQUEST Check response 
        if response.text:
            try:
                json_data = response.json()
            except ValueError:
                raise ServiceUnavailable
            else:
                if json_data:
                    for data in json_data:
                        # Username already exist in Auth0
                        if data['username'] == username:
                            return True
                    # Username Create
                    try:
                        actual_username = UsernameSignUpSession.objects.get(signup_session=session)
                    except Exception:
                        username_session, _ = UsernameSignUpSession.objects.get_or_create(signup_session=session, username=username)
                    # Username Update
                    else:
                        actual_username.username = username
                        actual_username.save()
                    return False
                else:
                    # Username Create
                    try:
                        actual_username = UsernameSignUpSession.objects.get(signup_session=session)
                    except Exception:
                        username_session, _ = UsernameSignUpSession.objects.get_or_create(signup_session=session, username=username)
                    # Username Update
                    else:
                        actual_username.username = username
                        actual_username.save()
                    return False
        else:
            raise ServiceUnavailable
        
# --- Sign Up Session Username Update ---
def username_signup_session_update(auth0user, username):
    # auth0user, Username String
    username_query = UsernameSignUpSession.objects.filter(username=username)

    if username_query:
        return True
    else:
        # request server check
        url = f"https://esena-app.us.auth0.com/api/v2/users?q=username%3A{username}"
        payload={}
        headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {requestToken()}'
        }
        for i in range(5):
            for attempt in range(5):
                try:
                    response = requests.request("GET", url, headers=headers, data=payload)
                except requests.exceptions.ConnectionError:
                    continue
                except requests.exceptions.RequestException:
                    raise ServiceUnavailable
                else:
                    break
            else:
                raise ServiceUnavailable
            
        if response.text:
            try:
                json_data = response.json()
            except ValueError:
                raise ServiceUnavailable
            else:
                session, _ = SignUpSession.objects.get_or_create(auth0user=auth0user)
                if json_data:
                    for data in json_data:
                        if data['username'] == username:
                            return True
                    username_session, _ = UsernameSignUpSession.objects.get_or_create(signup_session=session, username=username)
                    return False
                else:
                    username_session, _ = UsernameSignUpSession.objects.get_or_create(signup_session=session, username=username)
                    return False
        else:
            raise ServiceUnavailable
    
