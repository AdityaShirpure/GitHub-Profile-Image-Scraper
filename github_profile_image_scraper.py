import requests
from bs4 import BeautifulSoup as bs

# Assigning a variable to collect that Github user
github_user = input('Input the Github User: ')

# Sending request to URL 
url = 'https://github.com/' + github_user 
req = requests.get(url)

# Checking if the request was successful
if req.status_code == 200:
  soup = bs(req.content,'html.parser')
  profile_image = soup.find('img',{'alt':'Avatar'})
  if profile_image:
    image_src = profile_image['src']
    print(image_src)
  else:
    print("Profile image not found.")
else:
  print("Invalid username or URL.")
