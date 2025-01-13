import pandas as pd

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
