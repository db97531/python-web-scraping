import requests
params = {'firstname': 'Ryan', 'lastname': 'Mitchell'}
r = requests.post(
    "http://pythonscraping.com/files/precessing.php"
)
print(r.text)
