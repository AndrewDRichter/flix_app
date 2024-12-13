import requests as re

response = re.get('https://andrewrichter.pythonanywhere.com/api/v1/movies')
print(response.content)