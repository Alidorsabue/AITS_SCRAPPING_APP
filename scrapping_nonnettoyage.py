import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def scrape_villas(start_page=1, end_page=14):
    df = pd.DataFrame()

    for p_index in range(start_page, end_page + 1):
        url = f'https://sn.coinafrique.com/categorie/villas?page={p_index}.html'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        containers = soup.select(".col.s6.m4.l3")
        data = []

        for container in containers:
            try:
                description = container.select_one(".ad__card-description").text.strip()
                type_annonce = description.split()[0]
                nb_piece = re.sub(r'\D', '', description)
                price = container.select_one(".ad__card-price").text.replace("CFA", "").replace(" ", "")
                adresse = " ".join(container.select_one(".ad__card-location").text.strip().split()[-2:])
                image_link = container.select_one("img.ad__card-img")["src"]

                dic = {
                    'Type_annonce': type_annonce,
                    'Nbre_piece': nb_piece,
                    'price': price,
                    'adresse': adresse,
                    'image_link': image_link
                }
                data.append(dic)
            except:
                continue

        df = pd.concat([df, pd.DataFrame(data)], axis=0).reset_index(drop=True)

    return df

def scrape_terrains(start_page=1, end_page=14):
    df = pd.DataFrame()

    for p_index in range(start_page, end_page + 1):
        url = f'https://sn.coinafrique.com/categorie/terrains?page={p_index}.html'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        containers = soup.select(".col.s6.m4.l3")
        data = []

        for container in containers:
            try:
                description = container.select_one(".ad__card-description").text.strip()
                superficie = re.search(r'(\d+)\s?m²', description)
                superficie = superficie.group(1) if superficie else None

                price = container.select_one(".ad__card-price").text.replace("CFA", "").replace(" ", "")
                adresse = " ".join(container.select_one(".ad__card-location").text.strip().split()[1:])
                image_link = container.select_one("img.ad__card-img")["src"]

                dic = {
                    'superficie': superficie,
                    'price': price,
                    'adresse': adresse,
                    'image_link': image_link
                }
                data.append(dic)
            except:
                continue

        df = pd.concat([df, pd.DataFrame(data)], axis=0).reset_index(drop=True)

    return df

def scrape_appartements(start_page=1, end_page=14):
    df = pd.DataFrame()

    for p_index in range(start_page, end_page + 1):
        url = f'https://sn.coinafrique.com/categorie/appartements?page={p_index}.html'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        containers = soup.select(".col.s6.m4.l3")
        data = []

        for container in containers:
            try:
                description = container.select_one(".ad__card-description").text.strip()
                nbre_piece = re.sub(r'\D', '', description)
                price = container.select_one(".ad__card-price").text.replace("CFA", "").replace(" ", "")
                adresse = " ".join(container.select_one(".ad__card-location").text.strip().split()[1:])
                image_link = container.select_one("img.ad__card-img")["src"]

                dic = {
                    'nbre_piece': nbre_piece,
                    'price': price,
                    'adresse': adresse,
                    'image_link': image_link
                }
                data.append(dic)
            except:
                continue

        df = pd.concat([df, pd.DataFrame(data)], axis=0).reset_index(drop=True)

    return df
