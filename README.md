# Analyse de la Fréquentation des Cinémas

## Objectif du projet

Ce projet analyse la fréquentation des cinémas dans la région **Île-de-France**. L'objectif est de comprendre comment des facteurs comme le nombre d'écrans, de fauteuils, et la population influencent le nombre d'entrées dans les cinémas.

## Données utilisées

Les données incluent :
- **Région** : Où se situe le cinéma.
- **Commune** : Le nom de la ville où se trouve le cinéma.
- **Population de la commune** : Nombre de personnes vivant dans la commune.
- **Nombre d'écrans et de fauteuils** dans chaque cinéma.
- **Entrées annuelles** : Le nombre de billets vendus chaque année.

## Analyse réalisée

1. **Corrélations** : Nous avons examiné la relation entre le nombre d'écrans et de fauteuils avec les entrées.
   - **Corrélation Écrans vs Entrées** : Très forte (0.880).
   - **Corrélation Fauteuils vs Entrées** : Forte aussi (0.845).
   
2. **Statistiques** : Nous avons observé les valeurs moyennes et les écarts types des principales variables pour comprendre les tendances générales.

3. **Modèle prédictif** : Un modèle a été créé pour prédire les entrées en fonction des écrans, fauteuils et population. Ce modèle a une **précision de 65.8%** pour prédire les entrées annuelles.

## Comment utiliser ce projet avec Git

### 1. Cloner le projet

Pour commencer à utiliser le projet, vous devez d'abord le télécharger sur votre ordinateur. Ouvrez votre terminal (ou invite de commandes) et exécutez la commande suivante :

```bash
git clone https://github.com/nom-utilisateur/nom-du-repository.git
```
Cela va créer une copie du projet sur votre ordinateur.

2. Travailler sur le projet
Si vous avez des modifications à apporter, vous pouvez les faire directement dans les fichiers.
Après avoir modifié un fichier, vous pouvez ajouter les modifications en utilisant la commande :
```bash
git add .
```
Cela va ajouter toutes les modifications que vous avez faites à l'index de Git.

3. Commiter les changements
Ensuite, vous devez enregistrer ces modifications avec un message expliquant ce que vous avez fait :

```bash
git commit -m "Message décrivant les modifications"
```
4. Pousser les changements sur GitHub
Une fois vos modifications enregistrées, vous pouvez les envoyer sur le dépôt GitHub avec cette commande :

```bash
git push origin main
```
5. Mettre à jour votre copie locale
Si quelqu'un d'autre a modifié le projet pendant que vous travailliez, vous pouvez mettre à jour votre copie locale avec :

```bash
git pull origin main
```
Cela récupère les dernières modifications du projet.

# Réponses aux questions

- ### Exercice 3 : Corrélation entre infrastructures et fréquentation
Filtrage des données pour 2022 : Nous avons filtré pour l'année 2022 afin d'analyser l'impact des infrastructures sur la fréquentation cette année-là.

Corrélation :

Écrans et entrées annuelles : Corrélation de 0.880, forte relation positive.
Fauteuils et entrées annuelles : Corrélation de 0.845, également forte mais moins que les écrans.
Nuage de points et régression linéaire : Graphiques montrant la tendance positive entre écrans/fauteuils et les entrées annuelles.

Impact sur les entrées : Le nombre d'écrans a plus d'impact sur les entrées que les fauteuils, selon la corrélation plus élevée.

- ### Exercice 4 : Modèle prédictif des entrées annuelles
Diviser les données : Variables explicatives : écrans, fauteuils, population. Variable cible : entrées annuelles.

Entraînement du modèle : Modèle de régression linéaire créé.

Évaluation : R² et MAE montrent de bonnes performances du modèle.

Test sur 2022 : Les prédictions pour 2022 sont proches des valeurs réelles.

Le nombre d'écrans vs fauteuils : Les deux sont de bons prédicteurs, mais les écrans ont un plus grand impact sur les entrées.

- ### Exercice 5 : Recommandations stratégiques
Stratégie pour augmenter les entrées : Augmenter le nombre d'écrans, car les écrans ont un impact plus important sur les entrées que les fauteuils.

Justification : Augmenter les écrans, selon la forte corrélation avec les entrées, serait plus efficace pour attirer plus de spectateurs.

Résumé des recommandations pour un cinéma fictif
Nous avons aussi effectué des calculs pour estimer comment augmenter les entrées dans un cinéma fictif. En fonction des données, voici ce qu'on recommande :

Ajouter des écrans : Plus d'écrans entraînent généralement plus de spectateurs.
Ajouter quelques fauteuils : Bien que les fauteuils soient aussi importants, l'augmentation du nombre d'écrans est plus cruciale pour attirer davantage de spectateurs.
Conclusion
Ajouter des écrans est la meilleure stratégie pour attirer plus de spectateurs.
La diversification des films proposés et une meilleure communication peuvent aussi aider à augmenter la fréquentation.
C'est un résumé du projet et un guide simple pour utiliser Git. N'hésitez pas à poser des questions si quelque chose n'est pas clair !
