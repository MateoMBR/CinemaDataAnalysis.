import pandas as pd

def load_and_clean_data(file_path: str) -> pd.DataFrame:
    """
    Charge et nettoie les données du fichier CSV avec séparateur point-virgule
    """
    try:
        # Lire le fichier en spécifiant le séparateur point-virgule
        df = pd.read_csv(file_path, 
                        sep=';',  # Utiliser le point-virgule comme séparateur
                        encoding='utf-8',
                        decimal=',',
                        thousands=' ')
        
        print("Colonnes disponibles dans le fichier:")
        print(df.columns.tolist())
        
        # Convertir les colonnes numériques
        numeric_columns = {
            'population de la commune': 'float64',
            'écrans': 'float64',
            'fauteuils': 'float64',
            'entrées 2022': 'float64',
            'entrées 2021': 'float64'
        }

        for col, dtype in numeric_columns.items():
            if col in df.columns:
                df[col] = pd.to_numeric(df[col].astype(str).str.replace(' ', '').str.replace(',', '.'), 
                                      errors='coerce')
        
        # Créer un DataFrame plus propre
        df_clean = df.rename(columns={
            'région administrative': 'region',
            'commune': 'commune',
            'population de la commune': 'population_commune',
            'écrans': 'ecrans',
            'fauteuils': 'fauteuils',
            'entrées 2022': 'entrees_2022',
            'entrées 2021': 'entrees_2021'
        })
        
        # Convertir en format long
        id_vars = ['region', 'commune', 'population_commune', 'ecrans', 'fauteuils']
        value_vars = ['entrees_2021', 'entrees_2022']
        
        df_long = pd.melt(df_clean[id_vars + value_vars],
                         id_vars=id_vars,
                         value_vars=value_vars,
                         var_name='annee',
                         value_name='entrees_annuelles')
        
        # Extraire l'année
        df_long['annee'] = df_long['annee'].str.extract(r'(\d{4})').astype(int)
        
        # Supprimer les lignes avec des valeurs manquantes
        df_clean_final = df_long.dropna()
        
        print("\nAperçu du DataFrame nettoyé:")
        print(df_clean_final.head())
        print("\nNombre de lignes:", len(df_clean_final))
        
        return df_clean_final
        
    except Exception as e:
        print(f"Erreur lors du chargement du fichier: {str(e)}")
        
        # Diagnostic supplémentaire
        print("\nDiagnostic des premières lignes:")
        with open(file_path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if i < 5:  # Afficher les 5 premières lignes
                    print(f"Ligne {i+1}: {line.strip()}")
        raise

