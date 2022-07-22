# Import Libraries
import os
import sys
import requests
image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"

#Change working directory into whatever directory your Python script is located
os.chdir(sys.path[0])

# Get the current working directory
cwd = os.getcwd()

# Print the current working directory
print("Current working directory: {0}".format(cwd))


# URL of the image to be downloaded is defined as image_url
r = requests.get(image_url) # create HTTP response object
  
# send a HTTP request to the server and save
# the HTTP response in a response object called r
with open("python_logo.png",'wb') as f:
  
    # Saving received content as a png file in
    # binary format
  
    # write the contents of the response (r.content)
    # to a new file in binary mode.
    f.write(r.content)