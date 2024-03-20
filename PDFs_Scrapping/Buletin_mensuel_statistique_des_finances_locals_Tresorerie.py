import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Buletin_Mensuelle_SFL :

    def Buletin_mensuelle_statistique_finances_locals(year, month, directory):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {
            "download.default_directory": directory,
            "download.prompt_for_download": False,
            "plugins.always_open_pdf_externally": True})
        options.add_argument("--headless")  # Execute in headless mode

        # Set up ChromeDriver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        URL = 'https://www.tgr.gov.ma/wps/portal/Publication/Bulletins/Bulletin%20mensuel%20des%20statistiques%20des%20finances%20locales/!ut/p/b1/vZHbjoIwEIafxQfQTimFcllgXTxQtVCV3hj2GEHUZI2np1_YbLKJRLnZ0F41-Wa-mb9Io6SLHUKpbRGboSXS2_S4_kwP69023VRvba3YKLSYizmwMQPgM-FNo_6MPD-REkhKAO4cDo_qgeLf-j_AFxUQTxkfUQBJmvwLlLi1JjVLYxN9g9TH-AEe7dm0qQh2xTtKSsy-O4syUIyWYK6i7LIfXPOrzK4yPGTuUGTuAGIFkToqofJzKCY49hXG2XwU5V_GIeYgYC-ECKZvc6lc7p_laWI0CXHbQrtlITbbFTrQcqTSqyJN_KYc2v5pTFoWBvDvwiHS65eid3otetBzKGYMO7ZhAhBa5rnwUKE3_fGlm0smPm5vyDudbyCm3_s!/dl4/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_8KM68B1A08L800AQNCPSFQ3RC7/ren/p=WCM_PI=1/p=ns_Z7_8KM68B1A08L800AQFBNCPSFQFB3RC7_WCM_PreviousPageSize.60fd737f-f0a4-4a38-9fc9-3ecf5fd53dcd=25/p=ns_Z7_8KM68B1A08L800AQFBNCPSFQFB3RC7_WCM_Page.60fd737f-f0a4-4a38-9fc9-3ecf5fd53dcd=1/p=CTX=QCPtgr-internetQCPTGRQCPPublicationQCPPublicationQCPBulletinsQCPBulletinQCAmensuelQCAdesQCAstatistiquesQCAdesQCAfinancesQCAlocalesQCPBMFLQCAjuilletQCA2013/-/'
        driver.get(URL)

        driver.maximize_window()
        driver.implicitly_wait(5)

        a_tags = driver.find_elements(By.XPATH, "//a")

        for a in a_tags:
            search_text = f"Bulletin mensuel de statistiques des finances locales - {month} {year}"
            if search_text.lower() in a.text.lower():
                a.click()
                print("FILE FOUND")
                break  # Exit loop once the file is found

        download_path = directory
        file_name = f"BMSFL+{month}+{year}.pdf"
        file_path = os.path.join(download_path, file_name)
        print(file_path)
        while not os.path.exists(file_path):  # Wait until the file is downloaded
            time.sleep(1)

        print("Download Completed Successfully")
        driver.quit()

if __name__ == "__main__":
    year = int(input("Donner l'année :"))
    month = input("Donner le mois :")
    Buletin_Mensuelle_SFL.Buletin_mensuelle_statistique_finances_locals(year, month)