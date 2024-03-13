import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Rapport_Politique_Monétaire :
    def Rapport_PM(year):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {
            "download.default_directory": "D:\PFE\PDF_Analysis",
            "download.prompt_for_download": False,
            "plugins.always_open_pdf_externally": True})
        options.add_argument("--headless")  # Execute in headless mode

        # Set up ChromeDriver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        URL = f'https://www.bkam.ma/Publications-et-recherche/Documents-d-analyse/Rapport-sur-la-politique-monetaire/Rapport-sur-la-politique-monetaire-{year}'
        driver.get(URL)

        driver.maximize_window()
        driver.implicitly_wait(5)

        a_tags = driver.find_elements(By.XPATH, "//a")

        for a in a_tags:
            search_text = f"Rapport sur la politique monétaire - Décembre {year}"
            if search_text.lower() in a.text.lower():
                a.click()
                href = a.get_attribute('href')
                print("FILE FOUND")
                break  # Exit loop once the file is found

        download_path = "D:\PFE\PDF_Analysis"
        file_name = href.split("/")[-1]
        file_path = os.path.join(download_path, file_name)
        print(file_path)
        while not os.path.exists(file_path):  # Wait until the file is downloaded
            time.sleep(1)

        print("Download Completed Successfully")
        driver.quit()

if __name__ == "__main__":
    year = int(input("Enter the year: "))
    Rapport_Politique_Monétaire.Rapport_PM(year)