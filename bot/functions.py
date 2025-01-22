from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
import requests
import shutil
import os
import PIL
import numpy as np
import json
from .keys import dataBaseName


def download_img(link, file_name):
    res = requests.get(link, stream = True)
    
    if res.status_code == 200:
        with open(file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ',file_name)
        return 1
    else:
        print('Image Couldn\'t be retrieved')
        return 0

def load_data_base():
    f = open(dataBaseName,"r") 
    char_list = json.load(f) 
    f.close() 
    return char_list

def update_characters_list():
    url = "https://wuthering.wiki/"
    page = requests.get(url)
    if page.status_code != 200:
        return 0
    
    soup = BeautifulSoup(page.content)
    epic = soup.find_all("div", {"class": "itementry quality-4"})
    leg = soup.find_all("div", {"class": "itementry quality-5"})
    characters = leg + epic
    
    char_list = load_data_base()

    for char in characters:
        name = char["data-name"].replace("-", "_")
        if not (name in char_list):
            icon = url + char.find("img")["src"]
            element = char["data-element"]
            rarity = char["data-rarity"]
            char_list[name] = [rarity, element]

            download_img(icon, f"./images/characters/{name}.png")
            im = Image.open(f"./images/characters/{name}.png")
            im1 = im.resize((100, 100))
            im1.save(f"./images/characters/100x100/{name}.png")

    out_file = open(dataBaseName, "w") 
    json.dump(char_list, out_file, indent = 6) 
    out_file.close()
    return 1