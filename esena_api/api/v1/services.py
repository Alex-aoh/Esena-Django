import requests
import json


from django.shortcuts import get_object_or_404
from authz.auth0.auth0_management_token import requestToken

from json import JSONDecodeError
from common.exceptions import ServiceUnavailable




def username_check_available(username):
        print(username)
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
                    return False
                else:
                    return False
        else:
            raise ServiceUnavailable
        
def email_check_available(email):
    # request server check
        url = f"https://esena-app.us.auth0.com/api/v2/users?q=email%3A{email}"
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
                        if data['email'] == email:
                            return True
                    return False
                else:
                    return False
        else:
            raise ServiceUnavailable