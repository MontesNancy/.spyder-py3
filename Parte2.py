# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:50:14 2024

@author: NANCY
"""

#CONEXIÓN API Y EXTRACCIÓN DE HTML EN CARPETA RAW
import getpass
import requests
import requests.auth
from time import sleep
import os
import hashlib

CLIENT_ID = "cMcYPTz3cR65e5MCsCqYog"
CLIENT_SECRET = "lDIXw934DkacA5TdkBHR-zDVcgFmow"
USER_AGENT = "python:Clustering new Articles (by /u/JournalistFun8006)"

USERNAME = "JournalistFun8006"
PASSWORD = "holamundo123"

def login(username, password):
    if password is None:
        password = getpass.getpass("Enter reddit password for user {}: ".format(username))
    
    headers = {"User-Agent": USER_AGENT}
    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {"grant_type": "password", "username": username, "password": password}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    
    # Verifica si la respuesta es exitosa
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Obtener el token de acceso
token = login(USERNAME, PASSWORD)

def get_links(subreddit, token, n_pages=5):
    stories = []
    after = None
    for page_number in range(n_pages):
        headers = {"Authorization": "bearer {}".format(token['access_token']), "User-Agent": USER_AGENT}
        url = "https://oauth.reddit.com/r/{}?limit=100".format(subreddit)
        if after:
            url += "&after={}".format(after)
        response = requests.get(url, headers=headers)
        
        # Verifica si la respuesta es exitosa
        if response.status_code == 200:
            try:
                result = response.json()
                after = result['data']['after']
                stories.extend([(story['data']['title'], story['data']['url'], story['data']['score'])
                                for story in result['data']['children']])
            except ValueError:
                print("Error decoding JSON response")
                continue
        else:
            print(f"Error: {response.status_code} - {response.text}")
            break
        sleep(2)
    return stories

# Verificar si el token es válido antes de llamar a get_links
if token:
    stories = get_links("worldnews", token)
    print(stories)
else:
    print("Failed to retrieve access token")

# Obtener la ruta del directorio del script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Directorio de destino para los archivos
data_folder = os.path.join(script_dir, "raw")

# Crear el directorio si no existe
os.makedirs(data_folder, exist_ok=True)

number_errors = 0
for title, url, score in stories:
    output_filename = hashlib.md5(url.encode()).hexdigest()
    fullpath = os.path.join(data_folder, output_filename + ".txt")
    try:
        response = requests.get(url)
        data = response.text
        with open(fullpath, 'w', encoding='utf-8') as outf:
            outf.write(data)
    except Exception as e:
        number_errors += 1
        print(e)
