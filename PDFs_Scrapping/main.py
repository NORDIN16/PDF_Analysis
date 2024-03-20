from IMEE_OC import IMEE_OC
from Buletin_mensuel_statistique_des_finances_locals_Tresorerie import Buletin_Mensuelle_SFL
from Note_Presenation_MFinance import Note_Pres
from Rapport_Sur_Politique_Monétaire_BKAM import Rapport_Politique_Monétaire
from Budget_eco_prev_HCP import Budget_economique_prev
from Rapport_Annuel_HCP import Chomage
from Rapport_economique_financier_MFinance import Rapport_Economique_Financier
from main_analysis import main_text

import os
import shutil
import tempfile

import os
import shutil
import tempfile

# Importez vos scripts ici

def main():
    # Créer un répertoire temporaire
    temp_directory = tempfile.mkdtemp()
    print("Répertoire temporaire créé:", temp_directory)

    try:
        print("début du Scraping")
        IMEE_OC.IMEE(year=2023, directory=temp_directory)
        Buletin_Mensuelle_SFL.Buletin_mensuelle_statistique_finances_locals(year=2024, month="Janvier", directory=temp_directory)
        Note_Pres.Note_Presentation(year=2023, directory=temp_directory)
        Rapport_Politique_Monétaire.Rapport_PM(year=2023, directory=temp_directory)
        Budget_economique_prev.Budget_economique_previsionnel(year=2024, directory=temp_directory)
        Chomage.Rapport_Annuel_HCP(year=2022, directory=temp_directory)
        Rapport_Economique_Financier.Rapport_Eco_Fin(directory=temp_directory)

        print("Extraction du texte terminée")
        main_text.main_text(directory=temp_directory)

        print("Traitement terminé.")

    finally:
        # Supprimer le répertoire temporaire et tous ses contenus
        shutil.rmtree(temp_directory)
        print("Répertoire temporaire supprimé:", temp_directory)

if __name__ == "__main__":
    main()