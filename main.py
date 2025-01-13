from src.visualisation import plot_correlation_analysis, plot_residuals
from src.clean_data import load_and_clean_data
from src.display_stats import display_basic_stats
from src.predict import build_predictive_model
from src.analyze_data import analyse_entrees_par_region

def main():
    try:
        # Chargement et nettoyage des données
        df = load_and_clean_data('data/cinemas.csv')
        
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
        plot_residuals(df, model)
        
    except Exception as e:
        print(f"Erreur dans le programme principal: {str(e)}")
        print("Veuillez vérifier le format de votre fichier CSV.")

if __name__ == "__main__":
    main()
