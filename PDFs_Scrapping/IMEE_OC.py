import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import urllib.parse

class IMEE_OC:
    def IMEE(year):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {
            "download.default_directory": "D:\PFE\PDF_Analysis",
            "download.prompt_for_download": False,
            "plugins.always_open_pdf_externally": True})
        options.add_argument("--headless")  # Execute in headless mode

        # Set up ChromeDriver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        URL = 'https://www.oc.gov.ma/fr/publications#wow-book/'
        driver.get(URL)

        driver.maximize_window()
        driver.implicitly_wait(5)


        #search_text = "IMEE année 2023_1.pdf"
        
        a_tags = driver.find_elements(By.XPATH, "//a")
        
        for a in a_tags:

            if "IMEE" in a.get_attribute("href") and "ann" in a.get_attribute("href") and f"{year}" in a.get_attribute("href") :
                a.click()
                href = a.get_attribute("href")
                print("FILE FOUND")
                break  # Exit loop once the file is found

        download_path = "D:\PFE\PDF_Analysis"
        file_name = href.split("/")[-1]
        file_name = urllib.parse.unquote(file_name)
        file_path = os.path.join(download_path, file_name)
        print(file_path)
        while not os.path.exists(file_path):  # Wait until the file is downloaded
            time.sleep(1)

        print("Download Completed Successfully")
        driver.quit()

if __name__ == "__main__":
    IMEE_OC.IMEE(year=2023)