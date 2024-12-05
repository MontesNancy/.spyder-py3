# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:49:08 2024

@author: NANCY
"""

#CONEXIÓN API Y BUSQUEDA DE REDDIT'S CON PALABRA CLAVE EN VARIABLE "STORIES" E IMPRPESION EN CONSOLA
import getpass
import requests
import requests.auth
from time import sleep

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

'''
# Imprimir el token de acceso
if token:
    access_token = token.get('access_token')
    print(f"Access Token: {access_token}")

    # Hacer una solicitud a la API de Reddit usando el token de acceso
    subreddit = "worldnews"
    url = f"https://oauth.reddit.com/r/{subreddit}"
    headers = {"Authorization": f"bearer {access_token}", "User-Agent": USER_AGENT}
    response = requests.get(url, headers=headers)
    
    # Verifica si la respuesta es exitosa
    if response.status_code == 200:
        result = response.json()
        for story in result['data']['children']:
            print(story['data']['title'])
    else:
        print(f"Error: {response.status_code} - {response.text}")
else:
    print("Failed to retrieve access token")

'''
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
#=====IMPORTANTE=====
#AQUI SE AGREGA EL TITULO A BUSCAR EN LOS REDDITS#
#=====IMPORTANTE=====

if token:
    #AQUI CAMBIAR WORLDNEWS POR LA PALABRA A BUSAR EN LOS REDDITS
    stories = get_links("worldnews", token)
    print(stories)
else:
    print("Failed to retrieve access token")
