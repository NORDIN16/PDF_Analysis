from Production_céréalière_nationale import extract_pdf_page
from Production_céréalière_nationale import extract_text_with_easyocr
from Production_céréalière_nationale import clean_text
from Production_céréalière_nationale import convert_pdf_to_images
from Production_céréalière_nationale import extract_production_cerealiere
from Production_céréalière_nationale import extract_text_with_langchain_pdf
from Production_céréalière_nationale import extract_exchange_rate_info

from easyocr import Reader
import csv
#import re
#import json

class main_text :
    def main_text(directory):
        # Load model for the English language
        #language_reader = Reader(["fr"])

        ### Production Céréalière Nationale

        # Chemin du fichier CSV de sortie
        csv_file1 = 'production_cerealiere.csv'
        # Définir les noms de colonnes
        fieldnames1 = ['année', 'production céréalière en million de quintaux']

        pdf_path1 = directory + '/03-Rapport-economique-financier_Fr.pdf'
        page_number1 = 123  
        pdf_page = extract_pdf_page.extract_pdf_page(pdf_path1, page_number1)
        image = convert_pdf_to_images.convert_pdf_to_images(pdf_page)
        text = extract_text_with_easyocr.extract_text_with_easyocr(image)
        clean_txt = clean_text.clean_text(text)
        production_cerealiere = extract_production_cerealiere.extract_production_info(clean_txt)
        #print(production_cerealiere)

        # Écrire les données JSON dans le fichier CSV
        with open(csv_file1, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames1)
            
            # Écrire l'en-tête du CSV
            writer.writeheader()
            
            # Écrire chaque ligne de données
            for year, production in production_cerealiere.items():
                writer.writerow({'année': year, 'production céréalière en million de quintaux': production[0]})


        #Taux de change effectif reel
                
        # Chemin du fichier CSV de sortie
        csv_file2 = 'taux_de_change_effectif_reel.csv'
        # Définir les noms de colonnes
        fieldnames2 = ['année', 'taux_de_change_effectif_reel']

        pdf_path2 = directory + '/DEE_RPM_T4.pdf'
        page_number2 = 8
        pdf_page = extract_pdf_page.extract_pdf_page(pdf_path2, page_number2)
        text_langchain = extract_text_with_langchain_pdf.extract_text_with_langchain_pdf(pdf_page)
        Taux_de_change_effectif_reel = extract_exchange_rate_info.extract_exchange_rate_info(text_langchain)
        #print(Taux_de_change_effectif_reel)
        
        # Écrire les données JSON dans le fichier CSV
        with open(csv_file2, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames2)
            
            # Écrire l'en-tête du CSV
            writer.writeheader()
            
            # Écrire chaque ligne de données
            for year, production in Taux_de_change_effectif_reel.items():
                writer.writerow({'année': year, 'taux_de_change_effectif_reel': production[0]})

        #Solde courant

        # Chemin du fichier CSV de sortie
        csv_file = 'solde_courant.csv'

        # Définir les noms de colonnes
        fieldnames = ['type', 'percentage', 'deficit_or_surplus']

        pdf_path = directory + '/Budget économique prévisionnel 2024 _ La situation économique en 2023 et ses perspectives en 2024 (version française)'
        page_number = 16
        pdf_page = extract_pdf_page.extract_pdf_page(pdf_path, page_number)
        text_langchain = extract_text_with_langchain_pdf.extract_text_with_langchain_pdf(pdf_page)
        cleaned = clean_text.clean_text(text_langchain)
        solde_courant = extract_exchange_rate_info.extract_exchange_rate_info(cleaned)
        #print(solde_courant)
        # Écrire les données JSON dans le fichier CSV
        with open(csv_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            # Écrire l'en-tête du CSV
            writer.writeheader()
            
            # Écrire chaque ligne de données
            for row in solde_courant:
                writer.writerow(row)
                
if __name__ == "__main__":
    main_text()