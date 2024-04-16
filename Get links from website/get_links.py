# Creating a program that takes in a website and returns all the links on the website

import requests

website_link = input("Enter the website link: ")

response = get(website_link)

if response.ok: 
    response = response.text

print(response)
