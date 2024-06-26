import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import urllib.parse

class Bulletin_SDE :
    def Bulletin_Statistique_Dette_Ex(year, month, directory):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {
            "download.default_directory": directory,
            "download.prompt_for_download": False,
            "plugins.always_open_pdf_externally": True})
        options.add_argument("--headless")  # Execute in headless mode

        # Set up ChromeDriver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        URL = 'https://www.finances.gov.ma/fr/Pages/publications-dette.Aspx?fiche=2'
        driver.get(URL)

        driver.maximize_window()
        driver.implicitly_wait(5)

        a_tags = driver.find_elements(By.XPATH, "//a")

        for a in a_tags:
            search_text = f"Bulletin statistique de la dette extérieure du trésor -{month} {year}-"
            if search_text.lower() in a.text.lower():
                a.click()
                href = a.get_attribute("href")
                print("FILE FOUND")
                break  # Exit loop once the file is found

        download_path = directory
        file_name = href.split("/")[-1]
        file_name = urllib.parse.unquote(file_name)
        file_path = os.path.join(download_path, file_name)
        print(file_path)
        while not os.path.exists(file_path):  # Wait until the file is downloaded
            time.sleep(1)

        print("Download Completed Successfully")
        driver.quit()

if __name__ == "__main__":
    Bulletin_SDE.Bulletin_Statistique_Dette_Ex(year="2023", month="Juin")