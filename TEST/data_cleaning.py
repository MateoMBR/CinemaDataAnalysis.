# data_cleaning.py
import pandas as pd
import matplotlib.pyplot as plt

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

def display_basic_stats(df: pd.DataFrame):
    """
    Affiche les statistiques descriptives de base
    """
    print("\nStatistiques descriptives des variables principales:")
    stats = df[['fauteuils', 'ecrans', 'entrees_annuelles', 'population_commune']].describe()
    print(stats)
    
    print("\nNombre de cinémas par région:")
    print(df.groupby('region').size().sort_values(ascending=False))

def analyse_entrees_par_region(df: pd.DataFrame, annee: int):
    """
    Analyse les entrées moyennes par fauteuil pour chaque région
    """
    df_annee = df[df['annee'] == annee].copy()
    df_annee['entrees_par_fauteuil'] = df_annee['entrees_annuelles'] / df_annee['fauteuils']
    resultats_regions = df_annee.groupby('region')['entrees_par_fauteuil'].mean().sort_values(ascending=False)
    
    plt.figure(figsize=(12, 6))
    resultats_regions.plot(kind='bar')
    plt.title(f'Entrées moyennes par fauteuil par région ({annee})')
    plt.xlabel('Région')
    plt.ylabel('Entrées par fauteuil')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    
    return resultats_regions

def build_predictive_model(df: pd.DataFrame):
    """
    Construit et évalue un modèle prédictif pour les entrées annuelles
    """
    df_train = df[df['annee'] == 2021].copy()
    
    X = df_train[['ecrans', 'fauteuils', 'population_commune']]
    y = df_train['entrees_annuelles']
    
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import r2_score, mean_absolute_error
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    print("\nÉvaluation du modèle:")
    print(f"R²: {r2_score(y_test, y_pred):.3f}")
    print(f"Erreur absolue moyenne: {mean_absolute_error(y_test, y_pred):.3f}")
    
    return model
