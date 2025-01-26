import sys
import requests
import json
from requests.auth import HTTPBasicAuth
from urllib.parse import quote
import re
import json
import os

# Retrieve environment variables
user = os.getenv('BINDUSER')
password = os.getenv('BINDPASSWORD')
tool_user = os.getenv('TOOLUSER')
tool_password = os.getenv('TOOLPASS')

a = r"{user}"
b = r"{password}"
c = r"{tool_user}"
d = r"{tool_password}"

print(f"User: {a}")
print(f"Password: {b}")
print(f"Tool_User: {c}")
print(f"Tool_Password: {d}")

if a == "user()*" or b =="pass" :
    print("Authentication successful!") 
else :
    print("Failed")
