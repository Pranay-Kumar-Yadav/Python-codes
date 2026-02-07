#url is valid or not using regular expression
import re

url = input("Enter URL: ")

pattern = r'^(https?:\/\/)?(www\.)?[a-zA-Z0-9\-]+\.[a-zA-Z]{2,}([\/\w\.-]*)*\/?$'

if re.match(pattern, url):
    print("Valid URL")
else:
    print("Invalid URL")
