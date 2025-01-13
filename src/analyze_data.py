import matplotlib.pyplot as plt
import pandas as pd

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
