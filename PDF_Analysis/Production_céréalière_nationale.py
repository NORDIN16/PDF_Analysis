import pypdfium2 as pdfium
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
from easyocr import Reader
import re
import fitz
import PyPDF2
from langchain_community.document_loaders import UnstructuredFileLoader
import tempfile

# Load model for the English language
language_reader = Reader(["fr"])

class extract_pdf_page : 
    def extract_pdf_page(pdf_path, page_number):
        # Crée un fichier temporaire pour stocker la page extraite
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file_path = temp_file.name

            # Ouvre le fichier PDF en mode lecture binaire
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                
                # Vérifie si le numéro de page est valide
                if page_number < 0 or page_number >= len(reader.pages):
                    print("Invalid page number.")
                    return None
                
                # Écrit la page spécifiée dans le fichier temporaire
                writer = PyPDF2.PdfWriter()
                writer.add_page(reader.pages[page_number])
                writer.write(temp_file)

        # Retourne le chemin vers le fichier PDF extrait
        return temp_file_path

class convert_pdf_to_images :
    def convert_pdf_to_images(file_path, scale=300/72):
    
        pdf_file = pdfium.PdfDocument(file_path)  
        page_indices = [i for i in range(len(pdf_file))]
        
        renderer = pdf_file.render(
            pdfium.PdfBitmap.to_pil,
            page_indices = page_indices, 
            scale = scale,
        )
        
        list_final_images = [] 
        
        for i, image in zip(page_indices, renderer):
            
            image_byte_array = BytesIO()
            image.save(image_byte_array, format='jpeg', optimize=True)
            image_byte_array = image_byte_array.getvalue()
            list_final_images.append(dict({i:image_byte_array}))
        
        return list_final_images

class extract_text_with_easyocr :
    def extract_text_with_easyocr(list_dict_final_images):
    
        image_list = [list(data.values())[0] for data in list_dict_final_images]
        image_content = []
        
        for index, image_bytes in enumerate(image_list):
            
            image = Image.open(BytesIO(image_bytes))
            raw_text = language_reader.readtext(image)
            raw_text = "\n".join([res[1] for res in raw_text])
                        
            image_content.append(raw_text)
        
        return "\n".join(image_content)

class clean_text :
    def clean_text(text):
        # Supprimer les caractères spéciaux et les éléments non pertinents
        cleaned_text = re.sub(r"[\n']", " ", text)
        cleaned_text = re.sub(r"\s+", " ", cleaned_text)  # Supprimer les espaces en double
        return cleaned_text.strip()
    
class convert_pdf_page_to_image :
    def convert_pdf_page_to_image(pdf_path, page_number):
        # Ouvre le document PDF
        pdf_document = fitz.open(pdf_path)
        
        # Vérifie si le numéro de page est valide
        if page_number < 0 or page_number >= len(pdf_document):
            print("Numéro de page invalide.")
            return None
        
        # Sélectionne la page spécifiée
        page = pdf_document[page_number]
        
        # Convertit la page en une image
        pix = page.get_pixmap()
        
        # Crée un objet Image à partir des données de l'image
        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        
        return image

class extract_text_with_langchain_pdf :
    def extract_text_with_langchain_pdf(pdf_file):
    
        loader = UnstructuredFileLoader(pdf_file)
        documents = loader.load()
        pdf_pages_content = '\n'.join(doc.page_content for doc in documents)
        
        return pdf_pages_content

class extract_exchange_rate_info :
    def extract_exchange_rate_info(text):
        pattern = r"(baisse|hausse) de ([\d,]+)% en (\d{4})"
        matches = re.findall(pattern, text)

        exchange_rate_info = {}

        for match in matches:
            change_type = match[0]
            percentage = match[1]
            year = match[2]
            
            # Remplacer "baisse" par "-" et "hausse" par "+"
            if change_type == "baisse":
                percentage = "-" + percentage
            elif change_type == "hausse":
                percentage = "+" + percentage

            if year not in exchange_rate_info:
                exchange_rate_info[year] = []
            exchange_rate_info[year].append(percentage)

        return exchange_rate_info

class extract_production_cerealiere : 
    def extract_production_info(text):
        # Expression régulière pour extraire les informations pertinentes
        pattern = r"production céréalière de (\d+) millions de quintaux en (\d{4}) contre (\d+) millions de quintaux en (\d{4})"

        # Recherche de correspondances dans le texte
        matches = re.findall(pattern, text)

        # Création d'un dictionnaire pour stocker les informations
        infos_production = {}

        # Boucle sur les correspondances trouvées
        for match in matches:
            production_1 = match[0]
            annee_1 = match[1]
            production_2 = match[2]
            annee_2 = match[3]
            infos_production[annee_1] = [production_1]
            infos_production[annee_2] = [production_2]

        return infos_production

class extract_solde_courant :
    def extract_solde_courant(text):
        pattern = r"(compte courant) .*?(déficit|excédent) .*?([\d,]+)% "
        matches = re.findall(pattern, text)
        
        results = []
        for match in matches:
            account_type = match[0]
            percentage = match[1]
            deficit_or_surplus = match[2]
            
            results.append({
                "type": account_type,
                "percentage": percentage,
                "deficit_or_surplus": deficit_or_surplus
            })
        return results