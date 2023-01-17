#!/usr/bin/env python3

import os
import json
import urllib.parse

from templates import login_page

# display the environment variables as JSON
# print("Content-Type: application/json\n")
# print(json.dumps(dict(os.environ)))

# display the query parameters as HTML
# print("Content-Type: text/html\n")
# print("<html><body>")
# print("<h1>Query Parameters</h1>")
# print("<ul>")
# for key, value in urllib.parse.parse_qs(os.environ["QUERY_STRING"]).items():
#     print(f"<li><b>{key}</b>: {value}</li>")
# print("</ul>")

# print("<h1>Browser Agent</h1>")
# user_agent = os.environ["HTTP_USER_AGENT"]
# print(f"<p>{user_agent}</p>")
# print("</body></html>")

# login page
print("Content-Type: text/html\n")
print(login_page())