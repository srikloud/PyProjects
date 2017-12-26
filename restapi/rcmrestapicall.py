import json
import requests
import urllib.request
url = "https://rcm-api.admin.mp.mo.sap.corp/job/?limit=20"
request = urllib.request.Request(url, headers={'Authorization': 'Token 8SmPx5419BQ0qYMFy4N6Y4tFVaAq7DbK'})
response = urllib.request.urlopen(request)
print (response.read().decode('utf-8'))