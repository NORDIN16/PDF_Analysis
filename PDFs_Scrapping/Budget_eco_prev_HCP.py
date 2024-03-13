import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Budget_economique_prev :
    def Budget_economique_previsionnel(year):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {
            "download.default_directory": "D:\PFE\PDF_Analysis",
            "download.prompt_for_download": False,
            "plugins.always_open_pdf_externally": True})
        options.add_argument("--headless")  # Execute in headless mode

        # Set up ChromeDriver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        URL = 'https://www.hcp.ma/downloads/?tag=Conjoncture+et+pr%C3%A9vision+%C3%A9conomique'
        driver.get(URL)

        driver.maximize_window()
        driver.implicitly_wait(5)

        a_tags = driver.find_elements(By.XPATH, "//a")

        for a in a_tags:
            search_text = f"budget économique prévisionnel {year} : la situation économique en {year - 1} et ses perspectives en {year} (version français)"
            if search_text.lower() in a.text.lower():
                a.click()
                print("FILE FOUND")
                break  # Exit loop once the file is found

        download_path = "D:\PFE\PDF_Analysis"
        file_name = f"Budget économique prévisionnel {year} _ La situation économique en {year-1} et ses perspectives en {year} (version français).pdf"
        file_path = os.path.join(download_path, file_name)
        print(file_path)
        while not os.path.exists(file_path):  # Wait until the file is downloaded
            time.sleep(1)
            print('slm')

        print("Download Completed Successfully")
        driver.quit()

if __name__ == "__main__":
    year = int(input("Enter the year: "))
    Budget_economique_prev.Budget_economique_previsionnel(year)