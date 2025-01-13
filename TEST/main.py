# main.py
import pandas as pd
from visualisation import plot_correlation_analysis, plot_residuals
from data_cleaning import load_and_clean_data, display_basic_stats, analyse_entrees_par_region, build_predictive_model

def main():
    try:
        # Chargement et nettoyage des données
        df = load_and_clean_data('cinemas.csv')
        
        # Exercice 1 : Exploration des données
        display_basic_stats(df)
        
        # Exercice 2 : Analyse par région
        resultats_regions = analyse_entrees_par_region(df, 2022)
        print("\nTop 3 des régions (entrées/fauteuil):")
        print(resultats_regions.head(3))
        print("\nBottom 3 des régions (entrées/fauteuil):")
        print(resultats_regions.tail(3))
        
        # Exercice 3 : Analyse des corrélations
        plot_correlation_analysis(df, 2022)
        
        # Exercice 4 : Modèle prédictif
        model = build_predictive_model(df)
        
    except Exception as e:
        print(f"Erreur dans le programme principal: {str(e)}")
        print("Veuillez vérifier le format de votre fichier CSV.")

if __name__ == "__main__":
    main()
