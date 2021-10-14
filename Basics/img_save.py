import requests
response = requests.get('https://media.istockphoto.com/photos/child-hands-formig-heart-shape-picture-id951945718?s=612x612')
with open('img.png', 'bw') as file:
    file.write(response.content)