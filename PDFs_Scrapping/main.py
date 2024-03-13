import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


from IMEE_OC import IMEE_OC
from Buletin_mensuel_statistique_des_finances_locals_Tresorerie import Buletin_Mensuelle_SFL
from Note_Presenation_MFinance import Note_Pres
from Rapport_Sur_Politique_Monétaire_BKAM import Rapport_Politique_Monétaire
from Budget_eco_prev_HCP import Budget_economique_prev
from Rapport_Annuel_HCP import Chomage
from Rapport_economique_financier_MFinance import Rapport_Economique_Financier

def main():
    print("Options:")
    print("1. Indicateurs des échanges extérieurs au titre de l’année 2023")
    print("2. Buletin mensuel de statistiques des finances locales")
    print("3. Projet de Loi de Finances pour l’année budgétaire 2023 - Note de présentation")
    print("4. Rapport du la politique monétaire")
    print("5. Budget économique prévisionnel")
    print("6. Rapport économique et financier")

    choice = input("Choisissez votre choix: ")

    if choice == "1":
        year = int(input("Enter the year: "))
        IMEE_OC.IMEE(year)
    elif choice == "2":
        year = int(input("Donner l'année :"))
        month = input("Donner le mois :")
        Buletin_Mensuelle_SFL.Buletin_mensuelle_statistique_finances_locals(year, month)
    elif choice == "3" :
        Note_Pres.Note_Presentation(year=2023)
    elif choice == "4" :
        Rapport_Politique_Monétaire.Rapport_PM(year=2023)
    elif choice == "5" :
        Budget_economique_prev.Budget_economique_previsionnel(year=2024)
    elif choice == "6" :
        Chomage.Rapport_Annuel_HCP(year=2022)
    elif choice == "7" :
        Rapport_Economique_Financier.Rapport_Eco_Fin()
    else:
        print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()