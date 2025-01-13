import pandas as pd

def display_basic_stats(df: pd.DataFrame):
    """
    Affiche les statistiques descriptives de base
    """
    print("\nStatistiques descriptives des variables principales:")
    stats = df[['fauteuils', 'ecrans', 'entrees_annuelles', 'population_commune']].describe()
    print(stats)
    
    print("\nNombre de cinémas par région:")
    print(df.groupby('region').size().sort_values(ascending=False))
