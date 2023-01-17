#!/usr/bin/env python3

import os
import secret
import urllib.parse
import cgi

from templates import after_login_incorrect, secret_page

form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")

login = False

# check if cookie is set
cookie = os.environ["HTTP_COOKIE"]
if "login=true" in cookie:
    login = True

# set cookie if username and password are correct
if username == secret.username and password == secret.password or login:
    print("Set-Cookie: login=true")
    login = True
else:
    print("Set-Cookie: login=false")


print("Content-Type: text/html\n")

# display posted data as HTML
# print("<html><body>")
# print("<h1>Posted Data</h1>")
# print("<ul>")
# print(f"<li><b>username</b>: {username}</li>")
# print(f"<li><b>password</b>: {password}</li>")
# print("</ul>")
# print("</body></html>")

if login:
    print(secret_page(secret.username, secret.password))
else:
    print(after_login_incorrect())


