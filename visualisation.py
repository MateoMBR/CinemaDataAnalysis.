# visualisation.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation_analysis(df, annee):
    """
    Analyse et visualise les corrélations entre infrastructures et fréquentation
    """
    df_annee = df[df['annee'] == annee]
    corr_ecrans = df_annee['ecrans'].corr(df_annee['entrees_annuelles'])
    corr_fauteuils = df_annee['fauteuils'].corr(df_annee['entrees_annuelles'])
    print(f"Corrélations pour {annee}:")
    print(f"Écrans vs Entrées: {corr_ecrans:.3f}")
    print(f"Fauteuils vs Entrées: {corr_fauteuils:.3f}")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    sns.regplot(data=df_annee, x='ecrans', y='entrees_annuelles', ax=ax1)
    ax1.set_title(f'Relation Écrans vs Entrées ({annee})')
    ax1.set_xlabel('Nombre d\'écrans')
    ax1.set_ylabel('Entrées annuelles')
    
    sns.regplot(data=df_annee, x='fauteuils', y='entrees_annuelles', ax=ax2)
    ax2.set_title(f'Relation Fauteuils vs Entrées ({annee})')
    ax2.set_xlabel('Nombre de fauteuils')
    ax2.set_ylabel('Entrées annuelles')
    
    plt.tight_layout()
    plt.show()

def plot_residuals(df, model, annee=2022):
    """
    Affiche les résidus du modèle prédictif
    """
    df_annee = df[df['annee'] == annee]
    X = df_annee[['ecrans', 'fauteuils', 'population_commune']]
    y_true = df_annee['entrees_annuelles']
    y_pred = model.predict(X)
    
    residuals = y_true - y_pred
    
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=y_pred, y=residuals)
    plt.axhline(y=0, color='r', linestyle='--')
    plt.title(f"Résidus du modèle pour l'année {annee}")
    plt.xlabel('Prédictions')
    plt.ylabel('Résidus')
    plt.tight_layout()
    plt.show()
