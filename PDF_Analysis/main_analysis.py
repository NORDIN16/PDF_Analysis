from Production_céréalière_nationale import extract_pdf_page
from Production_céréalière_nationale import convert_pdf_page_to_image
from Production_céréalière_nationale import extract_text_with_easyocr
from Production_céréalière_nationale import clean_text
from Production_céréalière_nationale import convert_pdf_to_images
from Production_céréalière_nationale import extract_production_cerealiere
from Production_céréalière_nationale import extract_text_with_langchain_pdf
from Production_céréalière_nationale import extract_exchange_rate_info

from easyocr import Reader
#import re
#import json

def main():
    # Load model for the English language
    language_reader = Reader(["fr"])

    # Production Céréalière Nationale
    pdf_path = 'D:/PFE/PDF_Analysis/attachments/03-Rapport-economique-financier_Fr.pdf'
    page_number = 123  
    pdf_page = extract_pdf_page.extract_pdf_page(pdf_path, page_number)
    image = convert_pdf_to_images.convert_pdf_to_images(pdf_page)
    text = extract_text_with_easyocr.extract_text_with_easyocr(image)
    clean_txt = clean_text.clean_text(text)
    production_cerealiere = extract_production_cerealiere.extract_production_info(clean_txt)
    print(production_cerealiere)


    #Taux de change effectif reel

    pdf_path = 'D:/PFE/PDF_Analysis/attachments/DEE_RPM_T4.pdf'
    page_number = 8
    pdf_page = extract_pdf_page.extract_pdf_page(pdf_path, page_number)
    text_langchain = extract_text_with_langchain_pdf.extract_text_with_langchain_pdf(pdf_page)
    Taux_de_change_effectif_reel = extract_exchange_rate_info.extract_exchange_rate_info(text_langchain)
    print(Taux_de_change_effectif_reel)

    #Solde courant

    pdf_path = 'D:/PFE/PDF_Analysis/attachments/Budget économique prévisionnel 2024.pdf'
    page_number = 16
    pdf_page = extract_pdf_page.extract_pdf_page(pdf_path, page_number)
    text_langchain = extract_text_with_langchain_pdf.extract_text_with_langchain_pdf(pdf_page)
    cleaned = clean_text.clean_text(text_langchain)
    Taux_de_change_effectif_reel = extract_exchange_rate_info.extract_exchange_rate_info(cleaned)
    print(Taux_de_change_effectif_reel)

if __name__ == "__main__":
    main()
