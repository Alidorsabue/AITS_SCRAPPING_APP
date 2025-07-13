import streamlit as st
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from scrapping_nonnettoyage import scrape_villas
from scrapping_nonnettoyage import scrape_terrains
from scrapping_nonnettoyage import scrape_appartements
import seaborn as sns
import matplotlib.pyplot as plt

st.markdown(
    """
    <style>
    .main {
        background: url('https://www.transparenttextures.com/patterns/diamond-upholstery.png'), #009999;
        background-size: cover;
    }
    .block-container {
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    .stButton>button {
        width: 80%;
        margin: 1em auto;
        border-radius: 10px;
        font-size: 18px;
        background-color: #b0b0b0;
        color: #222;
    }
    """,
    unsafe_allow_html=True
)

# Fonction de loading des données
def load_(dataframe, title, key, download_filename=None):
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)

    if st.button(title, key):
        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
        st.dataframe(dataframe, use_container_width=True)
        if download_filename:
            st.download_button(
                label=f"Télécharger {title} (CSV)",
                data=dataframe.to_csv(index=False).encode('utf-8'),
                file_name=download_filename,
                mime="text/csv"
            )

def scrape_vil(scrap_function, pages, title, key, download_filename=None):
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)

    if st.button(title, key):
        # Lancer le scraping
        df = scrape_villas(start_page=1, end_page=pages, delay=2)
        st.success("Scraping terminé !")
        st.write('Data dimension: ' + str(df.shape[0]) + ' rows and ' + str(df.shape[1]) + ' columns.')
        st.dataframe(df, use_container_width=True)
        if download_filename:
            st.download_button(
                label=f"Télécharger {title} (CSV)",
                data=df.to_csv(index=False).encode('utf-8'),
                file_name=download_filename,
                mime="text/csv"
            )
def scrape_ter(scrap_function, pages, title, key, download_filename=None):
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)

    if st.button(title, key):
        # Lancer le scraping
        df1 = scrape_terrains(start_page=1, end_page=pages, delay=2)
        st.success("Scraping terminé !")
        st.write('Data dimension: ' + str(df1.shape[0]) + ' rows and ' + str(df1.shape[1]) + ' columns.')
        st.dataframe(df1, use_container_width=True)
        if download_filename:
            st.download_button(
                label=f"Télécharger {title} (CSV)",
                data=df1.to_csv(index=False).encode('utf-8'),
                file_name=download_filename,
                mime="text/csv"
            )
def scrape_appa(scrap_function, pages, title, key, download_filename=None):
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)

    if st.button(title, key):
        # Lancer le scraping
        df2 = scrape_appartements(start_page=1, end_page=pages, delay=2)
        st.success("Scraping terminé !")
        st.write('Data dimension: ' + str(d2.shape[0]) + ' rows and ' + str(df2.shape[1]) + ' columns.')
        st.dataframe(df2, use_container_width=True)
        if download_filename:
            st.download_button(
                label=f"Télécharger {title} (CSV)",
                data=df2.to_csv(index=False).encode('utf-8'),
                file_name=download_filename,
                mime="text/csv"
            )

# définir quelques styles liés aux box
st.markdown('''<style> .stButton>button {
    font-size: 12px;
    height: 3em;
    width: 50em;
}</style>''', unsafe_allow_html=True)

with st.sidebar:
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            background-color: #a3c6f1;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown("## User Input Features")
    option = st.selectbox("Options", ["Data scraping", "Display & download dataset", "Dashbaord & visualization", "Fill app Evaluation form"])
    if option == "Data scraping" :
        pages = st.selectbox("Pages indexes", list(range(1, 10001)), index=0)

# Affichage principal sur toute la largeur (hors sidebar)
if option == "Display & download dataset" :
    
    st.markdown("<h1 style='text-align: center; color: black;'>MY DATA SCRAPER APP</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style='text-align: center; color: white;'>
            <p>
                This app performs webscraping of data from dakar-auto over multiples pages. And we can also download scraped data from the app directly without scraping them.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    tab1, tab2, tab3 = st.tabs(["Villas Dataset", "Terrains Dataset", "Appartements Dataset"])

    with tab1:
        st.markdown("### Villas Dataset")
        df1 = pd.read_csv('data/Villas_data.csv')
        load_(df1, 'Villas data', '1', download_filename="Villas_data.csv")

    with tab2:
        st.markdown("### Terrains Dataset")
        df2 = pd.read_csv('data/Terrains_data.csv')
        load_(df2, 'Terrains data', '2', download_filename="Terrains_data.csv")


    with tab3:
        st.markdown("### Appartements Dataset")
        df3 = pd.read_csv('data/Appartements_data.csv')
        load_(df3, 'Appartements data', '3', download_filename="Appartements_data.csv")

if option == "Data scraping" :
    st.markdown("<h1 style='text-align: center; color: black;'>MY DATA SCRAPER APP</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style='text-align: center; color: white;'>
            <p>
                This app performs webscraping of data from dakar-auto over multiples pages. And we can also download scraped data from the app directly without scraping them.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    tab1, tab2, tab3 = st.tabs(["Données des Villas", "Données des Terrains", "Données des appartement"])

    with tab1:
        st.markdown("### Données des villas")
        scrape_vil(scrap_function=scrape_villas,pages=pages,title="Lancer le scraping des villas",key="scraping_villas_btn",download_filename="resultats_villas.csv")

    with tab2:
        st.markdown("### Données des terrains")
        scrape_ter(scrap_function=scrape_terrains,pages=pages,title="Lancer le scraping des terrains",key="scraping_terrains_btn",download_filename="resultats_terrains.csv")

    with tab3:
        st.markdown("### Données des appartements")
        scrape_appa(scrap_function=scrape_appartements,pages=pages,title="Lancer le scraping des appartements",key="scraping_appartements_btn",download_filename="resultats_appartements.csv")

if option == "Dashbaord & visualization" :
    st.markdown("<h1 style='text-align: center; color: black;'>MY DATA SCRAPER APP</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style='text-align: center; color: white;'>
            <p>
                This app performs webscraping of data from dakar-auto over multiples pages. And we can also download scraped data from the app directly without scraping them.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    tab1, tab2 = st.tabs(["Dashboard des Villas", "Dashboard des Terrains"])

    with tab1:
        st.markdown("### 📊 Statistiques")
        cols = st.columns([1, 2])
        col1, col2 = st.columns(2)
        # Graphique 1 : Distribution des prix
        with col1:
            df = pd.read_csv("cleaned_data/Villas_data.csv", sep=';')
            df['salle_bain'] = pd.to_numeric(df['salle_bain'], errors='coerce')
            df['Nbre_pieces'] = pd.to_numeric(df['Nbre_pieces'], errors='coerce')
            df['superficie'] = pd.to_numeric(df['superficie'], errors='coerce')
            df.dropna()
            st.markdown("###### 🛏️ Distribution des villas par adresse")
            fig1, ax1 = plt.subplots(figsize=(12, 8))
            sns.countplot(df['adresse'], color='skyblue', ax=ax1)
            ax1.set_xlabel("Adresses")
            ax1.set_ylabel("Nombre d'annonces")
            st.pyplot(fig1)

        # Graphique 2 : Répartition des pièces
        with col2:
            st.markdown("###### 🛏️ Répartition du nombre de pièces")
            fig2, ax2 = plt.subplots(figsize=(12, 6))
            piece_counts = df['Nbre_pieces'].value_counts().sort_index()
            sns.barplot(x=piece_counts.index, y=piece_counts.values, palette="viridis", ax=ax2)
            ax2.set_xlabel("Nombre de pièces")
            ax2.set_ylabel("Nombre d'annonces")
            st.pyplot(fig2)
        cols = st.columns([1, 2])
        col1, col2 = st.columns(2)

        # Graphique 1 : Distribution des prix
        with col1:
            st.markdown("###### 🛏️ Distribution de pièces par superficie")
            moyenne_pieces_superficie = (df.dropna(subset=['superficie', 'Nbre_pieces'])
            .groupby('superficie')['Nbre_pieces'].mean().reset_index().sort_values(by='superficie'))
            fig3, ax3 = plt.subplots(figsize=(12, 6))
            ax3.plot(moyenne_pieces_superficie['superficie'], moyenne_pieces_superficie['Nbre_pieces'], marker='o')
            ax3.set_xlabel("Superficie (m²)")
            ax3.set_ylabel("Nombre moyen de pièces")
            ax3.set_title("🛏️ Nombre de pièces moyens selon la superficie")
            st.pyplot(fig3)

        # Graphique 2 : Répartition des pièces
        with col2:
            st.markdown("###### 🛏️ Répartition des salles de bain")
            fig4, ax4 = plt.subplots(figsize=(12, 6))
            piece_counts = df['salle_bain'].value_counts().sort_index()
            sns.barplot(x=piece_counts.index, y=piece_counts.values, palette="viridis", ax=ax4)
            ax4.set_xlabel("Salles de bain")
            ax4.set_ylabel("Nombre")
            st.pyplot(fig4)
        
    with tab2:
        st.markdown("### 📊 Statistiques")
        cols = st.columns([1, 2])
        col1, col2 = st.columns(2)
        # Graphique 1 : Distribution des prix
        with col1:
            st.markdown("###### 💰 Distribution de prix moyen par superficie")
            df1 = pd.read_csv("cleaned_data/Terrains_data.csv", sep=';')
            df1['price'] = pd.to_numeric(df1['price'], errors='coerce')
            df1['superficie'] = pd.to_numeric(df1['superficie'], errors='coerce')
            df1.dropna()
            prix_moyen_superficie = (df1.dropna(subset=['superficie', 'price'])
            .groupby('superficie')['price'].mean().reset_index().sort_values(by='superficie'))
            fig3, ax3 = plt.subplots(figsize=(12, 6))
            ax3.plot(prix_moyen_superficie['superficie'], prix_moyen_superficie['price'], marker='o')
            ax3.set_xlabel("Superficie (m²)")
            ax3.set_ylabel("Prix moyen par superficie")
            ax3.set_title("🛏️ Prix moyen selon la superficie")
            st.pyplot(fig3)
        # Graphique 2 : Répartition des pièces
        with col2:
            st.markdown("###### 🛏️ Distribution des terrains par adresse")
            fig1, ax1 = plt.subplots(figsize=(12, 8))
            sns.countplot(df1['adresse'], color='skyblue', ax=ax1)
            ax1.set_xlabel("Adresses")
            ax1.set_ylabel("Nombre d'annonces")
            st.pyplot(fig1)

if option == "Fill app Evaluation form" :

    st.markdown("## 📝 FORMULAIRE D'EVALUATION DE L'APPLICATION")

    st.info("Utilisez le formulaire ci-dessous pour évaluer l'application et donner vos observations/suggestion.")

    kobo_url = "https://ee.kobotoolbox.org/x/62PKKnD9"

    st.components.v1.iframe(kobo_url, height=800, scrolling=True)
