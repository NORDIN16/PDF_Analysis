import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Chomage :
    def Rapport_Annuel_HCP(year, directory):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {
            "download.default_directory": directory,
            "download.prompt_for_download": False,
            "plugins.always_open_pdf_externally": True})
        options.add_argument("--headless")  # Execute in headless mode

        # Set up ChromeDriver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        URL = 'https://www.hcp.ma/downloads/?tag=Ch%C3%B4mage'
        driver.get(URL)

        driver.maximize_window()
        driver.implicitly_wait(5)

        a_tags = driver.find_elements(By.XPATH, "//a")

        for a in a_tags:
            search_text = f"Activité, emploi et chômage"
            if search_text.lower() in a.text.lower() and f"{year}" in a.text:
                a.click()
                file_name = a.text + ".pdf"
                print("FILE FOUND")
                break  # Exit loop once the file is found

        download_path = directory
        #file_name = f"Activité, emploi et chômage, résultats annuels {year}.pdf"
        file_path = os.path.join(download_path, file_name)
        print(file_path)
        while not os.path.exists(file_path):  # Wait until the file is downloaded
            time.sleep(1)

        print("Download Completed Successfully")
        driver.quit()

if __name__ == "__main__":
    year = int(input("Enter the year: "))
    Chomage.Rapport_Annuel_HCP(year)