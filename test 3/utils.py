import pandas as pd

def load_and_clean_data(file_path):
    """
    Charge et nettoie le fichier CSV
    """
    df = pd.read_csv(file_path)
    # Nettoyage des données (gestion des valeurs manquantes, conversion des types, etc.)
    df = df.dropna()  # Exemple de nettoyage : suppression des valeurs manquantes
    return df

def display_basic_stats(df):
    """
    Affiche des statistiques de base sur le dataframe
    """
    print("\nStatistiques de base :")
    print(df.describe())
