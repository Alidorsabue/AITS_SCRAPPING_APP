import pandas as pd
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def scrape_villas(start_page=1, end_page=14, delay=2):
    """
    Scrape les annonces de villas sur CoinAfrique (Sénégal) entre les pages spécifiées.
    
    Paramètres :
    - start_page (int) : page de début (par défaut 1)
    - end_page (int) : page de fin incluse (par défaut 14)
    - delay (int) : délai d'attente après chargement de chaque page (en secondes)

    Retour :
    - df (DataFrame) : les résultats concaténés pour toutes les pages
    """
    df = pd.DataFrame()

    for p_index in range(start_page, end_page + 1):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)

        try:
            url = f'https://sn.coinafrique.com/categorie/villas?page={p_index}.html'
            driver.get(url)
            time.sleep(delay)

            containers = driver.find_elements(By.CSS_SELECTOR, "[class='col s6 m4 l3']")
            data = []

            for container in containers:
                try:
                    type_annonce = container.find_element(By.CSS_SELECTOR, ".ad__card-description").text.split()[0]
                    nb_piece = re.sub(r'\D', '', container.find_element(By.CSS_SELECTOR, ".ad__card-description").text)
                    price = container.find_element(By.CSS_SELECTOR, ".ad__card-price").text.replace(" ", "").replace("CFA", "")
                    adresse = " ".join(container.find_element(By.CSS_SELECTOR, ".ad__card-location").text.split()[-2:])
                    image_link = container.find_element(By.CSS_SELECTOR, "img.ad__card-img").get_attribute("src")

                    dic = {
                        'Type_annonce': type_annonce,
                        'Nbre_piece': nb_piece,
                        'price': price,
                        'adresse': adresse,
                        'image_link': image_link
                    }
                    data.append(dic)
                except Exception:
                    continue

            DF = pd.DataFrame(data)
            df = pd.concat([df, DF], axis=0).reset_index(drop=True)

        finally:
            driver.quit()

    return df

def scrape_terrains(start_page=1, end_page=14, delay=2):
    """
    Scrape les annonces de villas sur CoinAfrique (Sénégal) entre les pages spécifiées.
    
    Paramètres :
    - start_page (int) : page de début (par défaut 1)
    - end_page (int) : page de fin incluse (par défaut 14)
    - delay (int) : délai d'attente après chargement de chaque page (en secondes)

    Retour :
    - df (DataFrame) : les résultats concaténés pour toutes les pages
    """
    df2 = pd.DataFrame()

    for p_index in range(start_page, end_page + 1):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)

        try:
            url = f'https://sn.coinafrique.com/categorie/terrains?page={p_index}.html'
            # obtenir l'url
            driver.get(url)
            time.sleep(delay)

            containers = driver.find_elements(By.CSS_SELECTOR, "[class='col s6 m4 l3']")
            data = []

            for container in containers:
                try:
                    superficie = " ".join(container.find_element(By.CSS_SELECTOR, "[class ='ad__card-description']").text.split()[1])
                    price = container.find_element(By.CSS_SELECTOR, "[class ='ad__card-price']").text.replace(" ", "").replace("CFA","")
                    adresse = " ".join(container.find_element(By.CSS_SELECTOR, "[class ='ad__card-location']").text.split()[1:])
                    image_link = container.find_element(By.CSS_SELECTOR, 'img.ad__card-img').get_attribute("src")
                    dic = {
                        'superficie' : superficie,
                        'price': price, 
                        'adresse': adresse, 
                        'image_link': image_link
                    }
                    data.append(dic)
                except Exception:
                    continue
            DF2 = pd.DataFrame(data)
            df2 = pd.concat([df2, DF2], axis = 0).reset_index(drop = True)

        finally:
            driver.quit()

    return df2

def scrape_appartements(start_page=1, end_page=14, delay=2):
    """
    Scrape les annonces de villas sur CoinAfrique (Sénégal) entre les pages spécifiées.
    
    Paramètres :
    - start_page (int) : page de début (par défaut 1)
    - end_page (int) : page de fin incluse (par défaut 14)
    - delay (int) : délai d'attente après chargement de chaque page (en secondes)

    Retour :
    - df (DataFrame) : les résultats concaténés pour toutes les pages
    """
    df3 = pd.DataFrame()

    for p_index in range(start_page, end_page + 1):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)

        try:
            url = f'https://sn.coinafrique.com/categorie/appartements?page={p_index}.html'
            # obtenir l'url
            driver.get(url)
            time.sleep(delay)

            containers = driver.find_elements(By.CSS_SELECTOR, "[class='col s6 m4 l3']")
            data = []

            for container in containers:
                try:
                    nbre_piece = re.sub(r'\D', '', container.find_element(By.CSS_SELECTOR, ".ad__card-description").text)
                    price = container.find_element(By.CSS_SELECTOR, "[class ='ad__card-price']").text.replace(" ", "").replace("CFA","")
                    adresse = " ".join(container.find_element(By.CSS_SELECTOR, "[class ='ad__card-location']").text.split()[1:])
                    image_link = container.find_element(By.CSS_SELECTOR, 'img.ad__card-img').get_attribute("src")
                    dic = {
                        'nbre_piece' : nbre_piece,
                        'price': price, 
                        'adresse': adresse, 
                        'image_link': image_link
                    }
                    data.append(dic)
                except Exception:
                    continue
            DF3 = pd.DataFrame(data)
            df3 = pd.concat([df3, DF3], axis = 0).reset_index(drop = True)

        finally:
            driver.quit()

    return df3