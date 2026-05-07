# 💡 Réponses : Sélections clés pour l'entretien Data Science — Junior

> Compte tenu de l'exhaustivité des questions (plus de 350 !), ce document rassemble les réponses de type "Cheat Sheet" aux questions incontournables, avec les concepts clés et les pièges à éviter lors de l'entretien.

---

## 📊 1. Statistiques & Probabilités

**Moyenne vs Médiane vs Mode :**
- *Moyenne* : Sensible aux valeurs extrêmes (outliers).
- *Médiane* : Valeur centrale. Robuste aux outliers. À utiliser pour les variables asymétriques (ex: salaires, prix de l'immobilier).
- *Mode* : Valeur la plus fréquente. Principalement pour variable catégorielle ou valeurs discrètes.

**Détecter les Outliers :**
- *Boxplot (IQR)* : Valeurs en dehors de `[Q1 - 1.5*IQR, Q3 + 1.5*IQR]` où IQR = Q3 - Q1.
- *Z-score* : Mesure combien d'écarts-types séparent une valeur de la moyenne. Si |Z| > 3, on le considère souvent comme outlier (valable si la distribution est normale).

**Théorème de Bayes :**
$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$
*Exemple concret* : Quelle est la probabilité d'avoir réellement le Covid (A) sachant qu'un test est positif (B) ? Le théorème corrige le résultat selon la prévalence de la maladie dans la population globale $P(A)$.

**Théorème Central Limite (TCL) :**
Peu importe la forme de la distribution d'origine des données. Si on prend des échantillons aléatoires de taille suffisante ($N \ge 30$), la distribution de la *moyenne* de ces échantillons convergera toujours vers une distribution Normale (Gaussienne).

**P-value :**
C'est la probabilité d'obtenir un résultat au moins aussi extrême que celui observé sur notre échantillon, en supposant que l'Hypothèse Nulle ($H_0$) soit vraie. Si p-value < 0.05, le résultat est statistiquement significatif -> on rejette $H_0$.

**Corrélation vs Causalité :**
Deux événements peuvent évoluer de la même façon (corrélation) sans que l'un entraîne l'autre (causalité). Il peut y avoir une 3ème variable cachée (variable confusionnelle). *Exemple*: Vente de lunettes de soleil et vente de glaces; la cause des deux est l'été/soleil (corrélation $\neq$ causalité).

---

## 🤖 2. Machine Learning — Cœur

**Compromis Biais-Variance (Le plus important en ML) :**
- *Biais (Erreur d'hypothèse)* : Trop grand, le modèle est trop simple (Underfitting). Ex: Régression linéaire sur des données sinusoïdales.
- *Variance (Sensibilité au bruit)* : Trop grande, le modèle apprend par cœur les données d'entraînement, y compris le bruit (Overfitting). Ex: Arbre de décision non élagué.
- *Objectif* : Trouver le "Sweet Spot" (hyperparamètres optimaux) minimisant l'Erreur Totale (Biais² + Variance + Bruit irrédutible).

**Combattre l'Overfitting (Sur-apprentissage) :**
1. Ajouter plus de données ou faire de la "Data Augmentation".
2. Simplifier le modèle (élaguer les arbres, réduire le nb de couches/neurones).
3. Utiliser la **Régularisation** (L1/Lasso, L2/Ridge).
4. Faire un "Early Stopping" lors de la descente de gradient.
5. Utiliser du Dropout dans les réseaux de neurones.
6. Utiliser des techniques ensemblistes (Random Forest, Boosting).

**Valider son modèle : Cross-Validation (K-Fold) :**
Diviser le dataset `Train` en $K$ morceaux (folds). Entraîner sur $K-1$ morceaux, évaluer sur le morceau restant. Recommencer ainsi $K$ fois. Le score final est la moyenne des $K$ scores. L'avantage est que chaque donnée sert 1 fois de validation.
*(Piège : On garde **toujours** le split "Test set" totalement de côté au tout début pour simuler la mise en production).*

**Régularisation L1 (Lasso) vs L2 (Ridge) :**
- *L1* : Ajoute la valeur absolue des poids à la fonction de coût. A tendance à forcer certains poids à 0. Très utile pour la **Sélection de Features**.
- *L2* : Ajoute le carré des poids à la Loss. Pousse les poids à être très petits sans être nuls. Mieux en général pour empêcher l'overfit et les multi-colinéarités (quand des variables sont très liées entre elles).

**Random Forest vs Gradient Boosting (Ex: XGBoost) :**
- *RF (Bagging)* : Entraîne $N$ arbres de décisions profonds en **parallèle** sur des sous-échantillons (Bootstrap). La moyenne de leurs votes réduit drastiquement la *Variance*. Moins sujet à l'overfitting, facile à paralléliser.
- *GBM (Boosting)* : Entraîne séquentiellement de petits arbres (stumps) où chacun essaie de corriger les erreurs résiduelles de l'arbre précédent. Réduit le *Biais*. Plus puissant, mais plus de risque d'overfitting si on pousse trop loin, plus dur à tuner.

**Encodage Catégorique (One-Hot vs Label) :**
- Ne jamais utiliser le *Label Encoder* $(Rouge=1, Vert=2, Bleu=3)$ pour une modèle de Régression ou un SVM/KNN. L'algorithme ferait "Bleu est 3 fois plus grand que Rouge".
- À la place, on utilise le *One-Hot Encoder* (Crée une colonne binaire 0/1 par couleur).

---

## 📈 3. Métriques d'évaluation & Cas pratiques

**Classification Déséquilibrée (Ex: Fraude Bancaire - 99.9% Légitime, 0.1% Fraude) :**
- **Piège majeur : L'Accuracy (Précision globale)**. Prédire "toujours légitime" donne une Accuracy de 99.9%, c'est inutile.
- Utiliser la **Matrice de Confusion** et ces métriques :
  - *Precision* (parmi mes alertes fraudes, combien sont vraies ? Utile si l'analyse manuelle coûte cher). $\frac{TP}{TP + FP}$
  - *Recall / Sensibilité* (parmi toutes les vraies fraudes, combien ai-je bloqué ? Utile en médical/fraude pour ne rien rater). $\frac{TP}{TP + FN}$
  - *F1-Score* : Moyenne harmonique des deux. $\frac{2 * Precision * Recall}{Precision + Recall}$
- *Stratégies Dataset* : Utiliser SMOTE (Synthetic Minority Oversampling), sous-échantillonner la majorité, ou attribuer des poids de classe (pénaliser mathématiquement une faute sur la classe rare 100x plus fort).

**Courbe ROC et AUC :**
La courbe ROC trace le Taux de Vrais Positifs (Recall) sur l'axe Y par rapport au Taux de Faux Positifs sur l'axe X, pour **différents seuils de rejet** de probabilité (ex: seuil à 0.5, puis 0.6...).
*AUC (Area Under Curve)* : l'aire sous cette courbe. Valeur 1.0 (parfait), 0.5 (aléatoire total comme lancer une pièce). Excellent pour comparer 2 modèles classifier (RF vs SVM).

**Régression (Cas de prédiction de prix) :**
- *MSE / RMSE* : L'erreur quadratique moyenne. Elle punit très violemment les erreurs extrêmes (à cause du carré). En unité monétaire d'origine pour la RMSE.
- *MAE (Absolute Error)* : Plus "doux" avec les outliers, donne une erreur "en moyenne absolue" en euros.

---

## 🐍 4. Python & Pandas

**Les types et listes :**
- Différence *List vs Tuple* : Tuple est `immuable` (immutable) -> il ne peut pas être modifié une fois créé. Plus rapide et peut servir de clé de dictionnaire. List est `mutable`.
- *Generators* (`yield`) : Plutôt que de charger une liste de 10 millions d'images en RAM, le générateur calcule et retourne le premier, met la fonction "en pause", puis à l'appel suivant donne le 2e. Évite le $Out Of Memory$.

**Différence `loc` et `iloc` (Pandas) :**
- `.loc[]` : Cherche par le *nom/label* de l'index ou nom de colonne.
- `.iloc[]` : Cherche par l'index entier *positionnel* (`0` pour 1ère ligne, jusqu'à `N-1`).

**`Merge` vs `Concat` (Pandas) :**
- `pd.concat` : Empile ou colle littéralement deux dataframes un à côté de l'autre (si alignement des index).
- `pd.merge` : Fait une jointure façon base de données (SQL INNER/LEFT JOIN) sur une ou plusieurs colonnes qu'ils ont en commun (une clé étrangère).

---

## 💾 5. SQL

**HAVING vs WHERE :**
Le `WHERE` filtre les données brutes de la table *avant* de grouper (`GROUP BY`). Le `HAVING` filtre le lot aggloméré *après* le groupage (ex: trouver les groupes ayant `SUM(ventes) > 1000`).

**Window Functions (ex: ROW_NUMBER(), RANK()) :**
Très demandées ! Permettront de faire une agrégation ou des rangs sans réduire le nombre de lignes (contrairement à GROUP BY). Ex: `RANK() OVER (PARTITION BY departement ORDER BY salaire DESC)` pour trouver la personne la mieux payée par département sans perdre les autres colonnes.

---

## 🧠 6. Deep Learning & Computer Vision (Résumé rapide)

**CNN (Convolutional Neural Networks) - Pourquoi pas un Dense network classique ?**
Sur une image 200x200px, aplatir les pixels donne en entrée 40 000 dimensions (sans la couleur). Trop de paramètres, perte de la forme géométrique. Le **Filtre de Convolution** passe localement sur l'image en extrayant des motifs (bords, formes) en 2D en partageant un tout petit volume de poids ($3x3 = 9$ paramètres par filtre). Invariable par translation "Feature Map".

**Pourquoi ReLU (max(0, x)) est si populaire ?**
Parce que sa dérivée est ultra-simple à calculer en Backpropagation (1 si $>0$, sinon 0) et surtout car il **ne sature pas du côté positif**, ce qui évite le fléau de l'évanouissement du gradient (Vanishing Gradient) commun aux vieilles fonctions Sigmoïdes dans les couches très profondes. Pour résoudre le fait que $ReLU = 0$ parfois "tue" le neurone ('Dying ReLU'), on utilise `Leaky ReLU` qui donne $0.01 * x$ en négatif.

---

## 🏗️ 7. Mise en situation / Exercice

*Question : "J'ai un dataset CSV qui pèse 50 Go, mais le PC pro qu'on vous donne a 16 Go de RAM. Comment analysez-vous les données ou entraînez-vous un modèle dessus ?"*

**Réponse attendue :**
1. **Bibliothèques adaptées :** Ne pas faire un vulgaire `import pandas` ! Pandas load tout en RAM + surcoût. Utiliser **Dask** (DataFrame paresseux en chuncks), ou **PySpark**.
2. **Format de stockage :** Transformer le CSV très verbeux en format binaire optimisé par colonnes, le **Format Parquet**. Il prend 3x moins d'espace et permet de ne lire qu'une colonne à la fois en RAM (impossible avec un fichier texte Ligne "CSV").
3. **Training :** Faire du traitement en *Batch* (Mini-batch Gradient Descent via scikit-learn `partial_fit` ou les générateurs Keras) : charger 1 million, calculer loss et maj poids, décharger, passer au million suivant.
4. (Bonus cloud) : Exporter le calcul sur une instance EC2/Sagemaker plus puissante dans le Cloud de l'entreprise.
