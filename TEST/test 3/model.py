from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

def build_predictive_model(df):
    """
    Crée un modèle prédictif (régression linéaire)
    """
    df_train = df[df['annee'] == 2021].copy()
    X = df_train[['ecrans', 'fauteuils', 'population_commune']]
    y = df_train['entrees_annuelles']
    model = LinearRegression()
    model.fit(X, y)
    return model

def ridge_regression(df):
    """
    Crée et évalue un modèle de régression Ridge
    """
    df_train = df[df['annee'] == 2021].copy()
    X = df_train[['ecrans', 'fauteuils', 'population_commune']]
    y = df_train['entrees_annuelles']
    model = Ridge(alpha=1.0)
    model.fit(X, y)
    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)
    mae = mean_absolute_error(y, y_pred)
    print(f"R² : {r2:.3f}, MAE : {mae:.0f}")
    return model
