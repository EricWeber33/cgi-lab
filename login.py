#!/usr/bin/env python3

import cgi
import os
from templates import login_page, secret_page


def parse_cookies(cookie_string):
    cookies = cookie_string.split(";")
    result = {}
    for cookie in cookies:
        split_cookie = cookie.split("=")
        result[split_cookie[0]] = split_cookie[1]
    return result

cookies = parse_cookies(os.environ["HTTP_COOKIE"])
form = cgi.FieldStorage()
username = form.getfirst("username")
password = form.getfirst("password")
header = ""
header += "Content-Type: text/html\r\n" # HTML is following

body = ""

if username is not None or ("logged" in cookies and cookies["logged"] == "True"):
    body += secret_page(username, password)
    header += "Set-Cookie: logged=True; Max-Age=60\r\n"
    header += "Set-Cookie: cookie=nom\r\n"
    body += "<h1>A terrible secret</h1>"
else:
    body += login_page()
print(header)
print()
print(body)

