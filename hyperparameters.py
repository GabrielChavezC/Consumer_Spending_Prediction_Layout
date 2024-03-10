"""
    Preferible guardar los resultados de RandomizedSearchCV
    como diccionarios y no predictions.best_params_
    porque vuelve a ejecutarse el entrenamiento de hiperparámetros
    y cambia los diccionarios que da
    
    Usar este archivo en el notebook
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV


global df_traffic

probando = df_traffic.copy()

X = probando.drop('transactionRevenue',axis=1)
y = probando['transactionRevenue'].apply(
    lambda x: 0 if x == 0 else 1
)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

hurdle_model = RandomForestClassifier(
    n_estimators=100, random_state=43
)
hurdle_model.fit(X_train, y_train)
modelo_clasificacion = hurdle_model


# Entrenar para regresión

X = probando.drop('transactionRevenue',axis=1)
X['clasificacion'] = hurdle_model.predict(X)
y = probando.transactionRevenue.copy()
train_x, test_x, train_y, test_y = train_test_split(
    X, y, test_size=0.30, random_state = 42
)


def xgboost_randomizedsearch():
    
    import xgboost as xgb
    
    param_random_xgb = {
        'n_estimators': [210, 220, 230],
        'learning_rate': [0.046, 0.048, 0.05],
        'max_depth': [6, 7],
        'min_child_weight': [4, 5],
        'gamma': [0.095, 0.1, 0.105],
        'subsample': [0.86, 0.88, 0.9],
        'colsample_bytree': [0.86, 0.88, 0.9],
        'reg_alpha': [0.009, 0.01, 0.011],
        'reg_lambda': [0.095, 0.1, 0.105],
        'random_state': [42]
    }


    # Inicializar RandomizedSearchCV
    random_cv_xgb = RandomizedSearchCV(
        xgb.XGBRegressor(),
        param_random_xgb,
        n_iter=40,
        cv=5,
        scoring='neg_root_mean_squared_error',
        n_jobs=-1
    )

    predictions = random_cv_xgb.fit(train_x, train_y)

    print(predictions.best_params_)
    print('-------')
    print(predictions.best_score_)



def lightgbm_randomizedsearch():
    import lightgbm as lgb
    
    param_grid = {
    'num_leaves': [16, 17],
    'learning_rate': [0.040, 0.041],
    'max_depth': [5, 6],
    'min_child_samples': [12, 13],
    'subsample': [0.66, 0.67],
    'colsample_bytree': [0.64, 0.65],
    'reg_alpha': [0.027, 0.028],
    'reg_lambda': [0.029, 0.030]
    }


    random_cv_lgbm = RandomizedSearchCV(
        lgb.LGBMRegressor(verbosity=-1),
        param_grid,
        n_iter=20,
        cv=5,
        scoring='neg_root_mean_squared_error',
        n_jobs=-1
    )

    predictions = random_cv_lgbm.fit(train_x, train_y)

    print(predictions.best_params_)
    print('-----')
    print(predictions.best_score_)

# xgboost_randomizedsearch()
# lightgbm_randomizedsearch()