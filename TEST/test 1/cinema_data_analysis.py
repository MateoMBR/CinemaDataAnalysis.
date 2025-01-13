import pandas as pd

# Charger le fichier CSV avec tolérance aux erreurs
def load_and_clean_data(file_path):
    try:
        # Lecture tolérante en sautant les lignes problématiques
        df = pd.read_csv(file_path, on_bad_lines='skip', sep=';')  # Mise à jour du séparateur
        print("Fichier chargé avec les lignes problématiques ignorées.")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return None

    # Afficher les premières lignes pour vérifier la structure
    print("Premières lignes du dataset:")
    print(df.head())

    # Vérifier les noms de colonnes
    print("\nColonnes du dataset:")
    print(df.columns)

    # Vérifier les valeurs manquantes
    print("\nValeurs manquantes par colonne:")
    print(df.isnull().sum())

    # Vérification et nettoyage des colonnes clés
    required_columns = ['écrans', 'fauteuils', 'entrées 2022', 'entrées 2021']
    for col in required_columns:
        if col not in df.columns:
            print(f"Attention : La colonne '{col}' est absente du dataset.")
        else:
            # Renommer les colonnes si nécessaire
            if 'entrées 2022' in df.columns and 'entrées 2021' in df.columns:
                df.rename(columns={'entrées 2022': 'entrees_2022', 'entrées 2021': 'entrees_2021'}, inplace=True)

    # Filtrer les données pour les années 2021 et 2022 si elles existent
    if 'entrees_2022' in df.columns and 'entrees_2021' in df.columns:
        df = df.dropna(subset=['écrans', 'fauteuils', 'entrees_2022', 'entrees_2021'])
        print("\nStatistiques descriptives des colonnes numériques principales:")
        print(df[['fauteuils', 'écrans', 'entrees_2022', 'entrees_2021']].describe())
    else:
        print("Colonnes essentielles pour les statistiques descriptives manquantes.")

    # Exporter le fichier nettoyé
    output_path = 'cleaned_cinemas.csv'
    df.to_csv(output_path, index=False)
    print(f"\nFichier nettoyé exporté sous le nom '{output_path}'.")

    return df

# Appel de la fonction avec le fichier cinemas.csv
file_path = './cinemas.csv'  # Remplacez par le chemin exact du fichier
cleaned_data = load_and_clean_data(file_path)
