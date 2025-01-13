from sklearn.model_selection import cross_val_score

def cross_validation(df):
    """
    Effectue une validation croisée pour évaluer le modèle
    """
    from sklearn.linear_model import LinearRegression
    df_train = df[df['annee'] == 2021].copy()
    X = df_train[['ecrans', 'fauteuils', 'population_commune']]
    y = df_train['entrees_annuelles']
    model = LinearRegression()
    scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_absolute_error')
    print(f"Score moyen MAE : {-scores.mean():.0f}")
    return scores

def tune_ridge_regression(df):
    """
    Optimise les paramètres de régularisation de la régression Ridge
    """
    from sklearn.linear_model import Ridge
    df_train = df[df['annee'] == 2021].copy()
    X = df_train[['ecrans', 'fauteuils', 'population_commune']]
    y = df_train['entrees_annuelles']
    best_alpha = 0
    best_score = float('-inf')
    for alpha in [0.1, 1.0, 10.0, 100.0]:
        model = Ridge(alpha=alpha)
        model.fit(X, y)
        y_pred = model.predict(X)
        r2 = r2_score(y, y_pred)
        if r2 > best_score:
            best_score = r2
            best_alpha = alpha
    print(f"Meilleur alpha trouvé : {best_alpha} avec R² de {best_score:.3f}")
    return best_alpha, best_score
