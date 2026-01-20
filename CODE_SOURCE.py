import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import RandomOverSampler

# Configuration du style visuel
sns.set(style="whitegrid")

def main():
    # --- Étape 2 : Chargement des données ---
    try:
        df = pd.read_csv("bank-data.csv")
        print("Dataset chargé avec succès.")
        print(df.head())
    except FileNotFoundError:
        print("Erreur : Le fichier 'bank-data.csv' est introuvable.")
        return

    # --- Étape 3 : Préparation des données ---
    # Encodage de la cible (pep) : YES -> 1, NO -> 0
    df['pep'] = df['pep'].map({'NO': 0, 'YES': 1})
    
    # Encodage du sexe : MALE -> 0, FEMALE -> 1
    df['sex'] = df['sex'].map({'MALE': 0, 'FEMALE': 1})
    
    # Extraction et encodage de l'ID (ex: "ID12101" -> 12101)
    df['id_encoded'] = df['id'].astype(str).str.extract('(\d+)').astype(int)

    # Sélection des variables pertinentes
    features_selection = ['id_encoded', 'age', 'income', 'children', 'sex', 'pep']
    df = df[features_selection]
    
    # Suppression des lignes avec données manquantes
    df.dropna(inplace=True)
    
    print("\nDonnées après préparation :")
    print(df.head())

    # --- Étape 4 : Analyse exploratoire (EDA) ---
    plt.figure(figsize=(6, 4))
    sns.countplot(x='pep', data=df)
    plt.title("Répartition globale des décisions (0: Refusé, 1: Accepté)")
    plt.xlabel("Décision")
    plt.ylabel("Nombre de clients")
    plt.show()

    # --- Étape 5 : Modélisation (Exemple de base) ---
    X = df.drop('pep', axis=1)
    y = df['pep']

    # Division Entraînement / Test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entraînement du modèle RandomForest
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Score de précision
    score = model.score(X_test, y_test)
    print(f"\nPrécision du modèle sur le jeu de test : {score:.2%}")

    # --- Étape 6 : Visualisation de l'importance des variables ---
    importances = model.feature_importances__
    indices = np.argsort(importances)

    plt.figure(figsize=(8, 5))
    plt.title('Importance des variables dans la décision')
    plt.barh(range(len(indices)), importances[indices], color='b', align='center')
    plt.yticks(range(len(indices)), [X.columns[i] for i in indices])
    plt.xlabel('Importance Relative')
    plt.show()

if __name__ == "__main__":
    main()
