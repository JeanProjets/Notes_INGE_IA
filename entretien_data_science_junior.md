# 🎯 Questions d'entretien Data Science — Junior

> Guide exhaustif pour préparer un premier entretien d'embauche ou test technique en Data Science.

---

## 📊 1. Statistiques & Probabilités

### 1.1 Statistiques descriptives
- Quelle est la différence entre moyenne, médiane et mode ? Quand utiliser l'une plutôt que l'autre ?
- Qu'est-ce que l'écart-type ? La variance ? Quelle est la relation entre les deux ?
- Qu'est-ce qu'un quartile ? Un percentile ? Comment les calculer ?
- Comment détecter des outliers dans un jeu de données ? (IQR, Z-score, boxplot)
- Qu'est-ce que la skewness (asymétrie) et la kurtosis (aplatissement) ?
- Quelle est la différence entre une variable qualitative et quantitative ?
- Qu'est-ce qu'une variable ordinale vs nominale ?
- Comment résumer graphiquement une distribution ? (histogramme, KDE, boxplot)

### 1.2 Probabilités
- Qu'est-ce qu'une probabilité conditionnelle ? Donnez un exemple.
- Énoncer et expliquer le théorème de Bayes. Donnez un cas d'application concret.
- Quelle est la différence entre probabilité fréquentiste et bayésienne ?
- Qu'est-ce qu'une variable aléatoire ? Discrète vs continue ?
- Qu'est-ce que l'espérance mathématique ? La variance d'une variable aléatoire ?
- Citez les principales lois de probabilité et leurs cas d'usage :
  - Loi normale (gaussienne)
  - Loi de Bernoulli / Binomiale
  - Loi de Poisson
  - Loi uniforme
  - Loi exponentielle
- Qu'est-ce que le théorème central limite ? Pourquoi est-il important ?
- Qu'est-ce que la loi des grands nombres ?
- Deux événements indépendants : qu'est-ce que cela signifie mathématiquement ?

### 1.3 Statistiques inférentielles
- Qu'est-ce qu'un test d'hypothèse ? (H0 vs H1)
- Qu'est-ce que la p-value ? Comment l'interpréter ?
- Qu'est-ce qu'une erreur de type I ? De type II ?
- Qu'est-ce que la puissance d'un test ?
- Quand utiliser un test de Student (t-test) ? Un test du Chi² ? Un test ANOVA ?
- Qu'est-ce qu'un intervalle de confiance ? Comment le calculer pour une moyenne ?
- Quelle est la différence entre corrélation et causalité ?
- Qu'est-ce que le coefficient de corrélation de Pearson ? De Spearman ? Quand utiliser l'un ou l'autre ?
- Qu'est-ce qu'un test paramétrique vs non-paramétrique ?
- Qu'est-ce que le test de Kolmogorov-Smirnov ? Le test de Shapiro-Wilk ?
- Qu'est-ce que la correction de Bonferroni ? Pourquoi est-elle nécessaire ?

### 1.4 Échantillonnage
- Quelle est la différence entre un échantillon et une population ?
- Qu'est-ce que le biais d'échantillonnage ?
- Citez différentes méthodes d'échantillonnage (aléatoire simple, stratifié, par grappes).
- Qu'est-ce que le bootstrap ? À quoi sert-il ?

---

## 🤖 2. Machine Learning — Fondamentaux

### 2.1 Concepts généraux
- Quelle est la différence entre apprentissage supervisé, non-supervisé et par renforcement ?
- Quelle est la différence entre classification et régression ?
- Qu'est-ce que le biais et la variance ? Expliquer le compromis biais-variance (bias-variance tradeoff).
- Qu'est-ce que le sur-apprentissage (overfitting) ? Le sous-apprentissage (underfitting) ? Comment les détecter et les combattre ?
- Qu'est-ce que la validation croisée (cross-validation) ? Expliquer k-fold, stratified k-fold, leave-one-out.
- Pourquoi séparer les données en train/validation/test ? Quelles proportions typiques ?
- Qu'est-ce qu'une fonction de coût (loss function) ? Citez des exemples.
- Qu'est-ce que la descente de gradient ? Gradient stochastique (SGD) ? Mini-batch ?
- Qu'est-ce que le learning rate ? Que se passe-t-il s'il est trop grand ou trop petit ?
- Qu'est-ce que la régularisation ? À quoi sert-elle ?
- Quelle est la différence entre L1 (Lasso) et L2 (Ridge) ? ElasticNet ?
- Qu'est-ce qu'un hyperparamètre vs un paramètre ?
- Comment optimiser les hyperparamètres ? (Grid Search, Random Search, Bayesian Optimization)
- Qu'est-ce que le curse of dimensionality ?
- Qu'est-ce que le No Free Lunch Theorem ?

### 2.2 Modèles supervisés — Régression
- Expliquer la régression linéaire simple et multiple. Quelles sont ses hypothèses ?
- Comment interpréter les coefficients d'une régression linéaire ?
- Qu'est-ce que le R² ? Le R² ajusté ? La MSE, RMSE, MAE, MAPE ?
- Qu'est-ce que la multicolinéarité ? Comment la détecter (VIF) et la traiter ?
- Qu'est-ce que la régression polynomiale ?
- Qu'est-ce que la régression Ridge, Lasso, ElasticNet ?

### 2.3 Modèles supervisés — Classification
- Expliquer la régression logistique. Est-ce un modèle de régression ou de classification ?
- Qu'est-ce que la fonction sigmoïde ? La fonction softmax ?
- Qu'est-ce qu'un arbre de décision ? Comment fonctionne-t-il ? (Gini, entropie, gain d'information)
- Qu'est-ce que le pruning (élagage) d'un arbre ?
- Expliquer Random Forest. Pourquoi est-il souvent meilleur qu'un simple arbre ?
- Qu'est-ce que le bagging ? Le boosting ? Quelle est la différence ?
- Expliquer Gradient Boosting (GBM), XGBoost, LightGBM, CatBoost. Quelles différences ?
- Qu'est-ce qu'un SVM (Support Vector Machine) ? Qu'est-ce que le kernel trick ?
- Expliquer k-NN (k-Nearest Neighbors). Quels sont ses avantages et inconvénients ?
- Qu'est-ce que le Naive Bayes ? Pourquoi "naïf" ? Dans quels cas est-il performant ?

### 2.4 Modèles non-supervisés
- Expliquer K-Means. Comment choisir K ? (Méthode du coude, silhouette score)
- Qu'est-ce que le clustering hiérarchique ? Agglomératif vs divisif ?
- Expliquer DBSCAN. Quels sont ses avantages par rapport à K-Means ?
- Qu'est-ce que la PCA (Analyse en Composantes Principales) ? À quoi sert-elle ?
- Combien de composantes garder en PCA ? (Variance expliquée)
- Qu'est-ce que t-SNE ? UMAP ? Quand les utiliser ?
- Qu'est-ce que l'analyse en composantes indépendantes (ICA) ?
- Qu'est-ce qu'un algorithme de détection d'anomalies ? (Isolation Forest, One-Class SVM, LOF)

### 2.5 Métriques d'évaluation
- **Classification** :
  - Expliquer la matrice de confusion (TP, TN, FP, FN).
  - Qu'est-ce que l'accuracy ? Pourquoi peut-elle être trompeuse ?
  - Qu'est-ce que la précision ? Le rappel (recall/sensitivity) ? Le F1-Score ?
  - Qu'est-ce que la courbe ROC ? L'AUC-ROC ? Comment les interpréter ?
  - Qu'est-ce que la courbe Precision-Recall ? Quand la préférer à la ROC ?
  - Qu'est-ce que le log-loss (cross-entropy loss) ?
  - Comment gérer des classes déséquilibrées ? (SMOTE, poids de classes, under/oversampling)
- **Régression** :
  - MSE, RMSE, MAE, MAPE, R² — quand utiliser laquelle ?
  - Qu'est-ce que le RMSLE ?

### 2.6 Feature Engineering & Selection
- Qu'est-ce que le feature engineering ? Pourquoi est-il crucial ?
- Comment gérer les valeurs manquantes ? (Imputation par moyenne/médiane/mode, KNN imputer, suppression)
- Comment encoder les variables catégorielles ? (One-Hot, Label Encoding, Target Encoding, Ordinal Encoding)
- Quand utiliser One-Hot vs Label Encoding ?
- Qu'est-ce que la normalisation (Min-Max) ? La standardisation (Z-score) ? Quand les appliquer ?
- Qu'est-ce que le feature scaling ? Quels modèles en ont besoin ?
- Comment sélectionner les features les plus importantes ? (Corrélation, importance des features, méthodes wrapper/filter/embedded)
- Qu'est-ce que la réduction de dimensionnalité ? PCA vs sélection de features ?
- Comment créer de nouvelles features à partir de données existantes ?
- Comment gérer les variables temporelles (date/heure) en features ?

---

## 🐍 3. Python & Programmation

### 3.1 Python — Fondamentaux
- Quels sont les types de données primitifs en Python ?
- Quelle est la différence entre une liste et un tuple ?
- Qu'est-ce qu'un dictionnaire ? Un set ?
- Qu'est-ce qu'une list comprehension ? Donnez un exemple.
- Qu'est-ce qu'un générateur ? Quelle est la différence avec une liste ?
- Qu'est-ce qu'un décorateur en Python ?
- Qu'est-ce que `*args` et `**kwargs` ?
- Quelle est la différence entre une copie superficielle (shallow copy) et une copie profonde (deep copy) ?
- Qu'est-ce qu'un context manager (`with`) ?
- Qu'est-ce que le GIL (Global Interpreter Lock) ?
- Quelle est la différence entre `==` et `is` ?
- Qu'est-ce qu'un environnement virtuel ? Pourquoi les utiliser ?
- Comment gérer les exceptions en Python ? (`try/except/finally`)
- Qu'est-ce que la programmation orientée objet (POO) ? Classes, héritage, polymorphisme ?
- Qu'est-ce qu'une lambda function ?
- Qu'est-ce que `map()`, `filter()`, `reduce()` ?

### 3.2 NumPy
- Qu'est-ce qu'un ndarray ? Quelle différence avec une liste Python ?
- Comment créer un array NumPy ? (`np.array`, `np.zeros`, `np.ones`, `np.arange`, `np.linspace`)
- Qu'est-ce que le broadcasting en NumPy ?
- Comment effectuer des opérations vectorisées ?
- Comment accéder aux éléments d'un array ? (Indexing, slicing, fancy indexing, boolean indexing)
- Qu'est-ce que le reshaping ? Comment l'utiliser ?

### 3.3 Pandas
- Quelle est la différence entre une Series et un DataFrame ?
- Comment charger un fichier CSV ? Excel ? JSON ? Parquet ?
- Comment sélectionner des colonnes ? Des lignes ? (`loc`, `iloc`, filtrage conditionnel)
- Comment gérer les valeurs manquantes ? (`isnull`, `dropna`, `fillna`)
- Comment grouper des données ? (`groupby`, `agg`, `transform`, `apply`)
- Qu'est-ce qu'un merge ? Un join ? Un concat ? Quelles différences ?
- Comment créer un pivot table ?
- Comment gérer les doublons ? (`duplicated`, `drop_duplicates`)
- Comment appliquer une fonction à chaque ligne/colonne ? (`apply`, `map`, `applymap`)
- Qu'est-ce que le MultiIndex ?
- Comment optimiser les performances avec Pandas ? (dtypes, chunking)
- Comment gérer les données temporelles avec Pandas ? (`to_datetime`, `resample`, `rolling`)

### 3.4 Matplotlib & Seaborn
- Comment créer un graphique linéaire, un scatter plot, un bar chart ?
- Comment personnaliser un graphique ? (titres, labels, légendes, couleurs)
- Comment créer des subplots ?
- Quand utiliser Matplotlib vs Seaborn ?
- Comment créer une heatmap de corrélation avec Seaborn ?
- Comment créer un pairplot ?
- Comment sauvegarder un graphique ?

### 3.5 Scikit-learn
- Comment structurer un pipeline ML avec scikit-learn ?
- Qu'est-ce qu'un `Pipeline` ? Un `ColumnTransformer` ?
- Comment faire du train-test split ?
- Comment faire de la cross-validation ?
- Comment utiliser `GridSearchCV` et `RandomizedSearchCV` ?
- Comment sauvegarder et charger un modèle ? (`joblib`, `pickle`)
- Comment utiliser les transformers personnalisés ?

---

## 🗄️ 4. SQL & Bases de données

### 4.1 SQL — Fondamentaux
- Quelle est la différence entre `WHERE` et `HAVING` ?
- Expliquer les différents types de `JOIN` (INNER, LEFT, RIGHT, FULL, CROSS).
- Qu'est-ce qu'une sous-requête (subquery) ? Corrélée vs non-corrélée ?
- Qu'est-ce que `GROUP BY` ? `ORDER BY` ? `DISTINCT` ?
- Comment utiliser les fonctions d'agrégation ? (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`)
- Qu'est-ce qu'une CTE (Common Table Expression) ? `WITH ... AS` ?
- Qu'est-ce qu'une window function ? (`ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LEAD`, `LAG`, `OVER`, `PARTITION BY`)
- Comment filtrer sur un rang (ex : top 3 par catégorie) ?
- Quelle est la différence entre `UNION` et `UNION ALL` ?
- Qu'est-ce qu'un index ? Pourquoi et quand en créer ?
- Comment optimiser une requête SQL lente ?
- Qu'est-ce qu'une vue (view) ? Une vue matérialisée ?
- Qu'est-ce que la normalisation ? Les formes normales (1NF, 2NF, 3NF) ?
- Quelle est la différence entre `DELETE`, `TRUNCATE` et `DROP` ?
- Qu'est-ce qu'une clé primaire ? Une clé étrangère ?
- Qu'est-ce qu'une transaction ? Les propriétés ACID ?
- Que fait `CASE WHEN` en SQL ?
- Comment gérer les NULLs en SQL ? (`IS NULL`, `COALESCE`, `IFNULL`)

### 4.2 SQL — Questions pratiques (exercices types)
- Écrire une requête pour trouver le 2e salaire le plus élevé.
- Écrire une requête pour trouver les doublons dans une table.
- Écrire une requête pour calculer un cumul glissant (running total).
- Écrire une requête pour pivoter des données (lignes → colonnes).
- Écrire une requête pour trouver les clients qui n'ont pas commandé.
- Écrire une requête avec une jointure sur 3+ tables.

### 4.3 Bases de données — Concepts
- Quelle est la différence entre SQL et NoSQL ?
- Citez des exemples de bases NoSQL (MongoDB, Redis, Cassandra). Quand les utiliser ?
- Qu'est-ce qu'un data warehouse ? Un data lake ? Un data lakehouse ?
- Qu'est-ce qu'un schéma en étoile ? En flocon ?

---

## 🧠 5. Deep Learning

### 5.1 Réseaux de neurones — Fondamentaux
- Qu'est-ce qu'un neurone artificiel ? Comment fonctionne-t-il ?
- Qu'est-ce qu'une fonction d'activation ? Citez les principales (ReLU, Sigmoid, Tanh, Softmax, Leaky ReLU). Quand utiliser laquelle ?
- Qu'est-ce que la backpropagation ? Comment fonctionne-t-elle ?
- Qu'est-ce que le vanishing/exploding gradient problem ?
- Qu'est-ce qu'un réseau de neurones feedforward (MLP - Multi-Layer Perceptron) ?
- Qu'est-ce qu'une époque (epoch) ? Un batch ? Un mini-batch ?
- Citez des optimiseurs courants (SGD, Adam, RMSProp, AdaGrad). Quelles différences ?
- Qu'est-ce que le dropout ? Pourquoi est-ce une forme de régularisation ?
- Qu'est-ce que la batch normalization ?
- Qu'est-ce que l'early stopping ?
- Qu'est-ce que le transfer learning ? Pourquoi est-il utile ?
- Qu'est-ce que le fine-tuning ?
- Qu'est-ce que le data augmentation ?

### 5.2 CNN (Réseaux de neurones convolutifs)
- Qu'est-ce qu'une convolution ? Un filtre/kernel ?
- Qu'est-ce que le stride ? Le padding ? Le pooling (max pooling, average pooling) ?
- Expliquer l'architecture d'un CNN typique.
- Citez des architectures célèbres (LeNet, AlexNet, VGG, ResNet, Inception). Qu'apportent les skip connections dans ResNet ?
- Quels sont les cas d'usage typiques des CNN ?

### 5.3 RNN (Réseaux de neurones récurrents)
- Qu'est-ce qu'un RNN ? Pour quels types de données est-il adapté ?
- Qu'est-ce que le problème du vanishing gradient dans les RNN ?
- Qu'est-ce qu'un LSTM ? Un GRU ? Quelle différence ?
- Qu'est-ce qu'un réseau bidirectionnel ?

### 5.4 Transformers & Attention
- Qu'est-ce que le mécanisme d'attention (self-attention) ?
- Qu'est-ce qu'un Transformer ? Expliquer l'architecture encoder-decoder.
- Qu'est-ce que BERT ? GPT ? Quelles différences ?
- Qu'est-ce que le positional encoding ? Pourquoi est-il nécessaire ?
- Qu'est-ce que la tokenization ?

### 5.5 Frameworks
- Quelle est la différence entre TensorFlow et PyTorch ?
- Comment définir un modèle avec Keras ? Avec PyTorch ?
- Comment sauvegarder et charger un modèle entraîné ?

---

## 📝 6. NLP (Natural Language Processing)

- Qu'est-ce que la tokenization ? Le stemming ? La lemmatisation ?
- Qu'est-ce qu'un stopword ? Pourquoi les supprimer (ou pas) ?
- Qu'est-ce que le Bag of Words (BoW) ? TF-IDF ?
- Qu'est-ce qu'un word embedding ? (Word2Vec, GloVe, FastText)
- Quelle est la différence entre un embedding statique et contextuel ?
- Qu'est-ce que le sentiment analysis ? Comment l'aborder ?
- Qu'est-ce que le Named Entity Recognition (NER) ?
- Qu'est-ce que le text classification ?
- Qu'est-ce qu'un modèle de langage (language model) ?
- Comment évaluer un modèle NLP ? (BLEU, ROUGE, perplexity)
- Qu'est-ce que le text preprocessing pipeline typique ?
- Comment gérer le multilinguisme en NLP ?

---

## 👁️ 7. Computer Vision

- Qu'est-ce qu'une image pour un ordinateur ? (Pixels, canaux RGB)
- Qu'est-ce que la classification d'images ? La détection d'objets ? La segmentation ?
- Quelle est la différence entre segmentation sémantique et d'instance ?
- Qu'est-ce que l'IoU (Intersection over Union) ? Le mAP ?
- Citez des architectures de détection d'objets (YOLO, SSD, Faster R-CNN).
- Qu'est-ce que l'augmentation de données en vision ? Quelles transformations appliquer ?
- Qu'est-ce que le transfer learning en vision ? (ImageNet pretrained models)
- Comment utiliser OpenCV pour des tâches basiques ? (Lecture d'image, redimensionnement, filtrage)

---

## 🔧 8. MLOps & Déploiement

### 8.1 Workflow ML en production
- Qu'est-ce que le MLOps ? Pourquoi est-il important ?
- Décrivez le cycle de vie complet d'un projet ML.
- Qu'est-ce qu'un pipeline ML ?
- Comment versionner des données ? Des modèles ? (DVC, MLflow)
- Qu'est-ce que le monitoring de modèle ? Pourquoi est-il nécessaire ?
- Qu'est-ce que le model drift ? Le data drift ? Le concept drift ?
- Comment détecter et gérer le drift ?
- Qu'est-ce qu'un A/B test pour un modèle ML ?

### 8.2 Déploiement
- Comment déployer un modèle ML via une API REST ? (Flask, FastAPI)
- Qu'est-ce que Docker ? Pourquoi l'utiliser pour le ML ?
- Qu'est-ce que le CI/CD dans le contexte ML ?
- Qu'est-ce que le batch inference vs real-time inference ?
- Citez des plateformes cloud pour le ML (AWS SageMaker, GCP Vertex AI, Azure ML).
- Comment sérialiser un modèle ? (pickle, joblib, ONNX, TorchScript)
- Qu'est-ce que Streamlit ? Gradio ? Quand les utiliser ?

### 8.3 Outils & bonnes pratiques
- Qu'est-ce que Git ? Les commandes essentielles ?
- Qu'est-ce que MLflow ? À quoi servent ses composants (Tracking, Projects, Models, Registry) ?
- Qu'est-ce qu'un notebook Jupyter vs un script Python ? Quand utiliser l'un ou l'autre ?
- Comment structurer un projet de Data Science ? (Cookiecutter, structure de dossiers)
- Qu'est-ce que le logging ? Pourquoi est-il important ?
- Qu'est-ce que l'idempotence dans un pipeline de données ?

---

## 📐 9. Mathématiques (Algèbre linéaire & Calcul)

### 9.1 Algèbre linéaire
- Qu'est-ce qu'un vecteur ? Une matrice ? Un tenseur ?
- Comment multiplier deux matrices ? Quelles conditions de compatibilité ?
- Qu'est-ce que la transposée d'une matrice ? L'inverse ?
- Qu'est-ce qu'un déterminant ?
- Qu'est-ce que les valeurs propres et vecteurs propres ? Application en PCA ?
- Qu'est-ce que la décomposition en valeurs singulières (SVD) ?
- Qu'est-ce que la norme d'un vecteur ? (L1, L2, Linf)
- Qu'est-ce que le produit scalaire ? Le produit vectoriel ?
- Qu'est-ce qu'un espace vectoriel ?

### 9.2 Calcul / Analyse
- Qu'est-ce qu'une dérivée ? Une dérivée partielle ?
- Qu'est-ce que le gradient ? Le jacobien ? Le hessien ?
- Comment la dérivée est-elle utilisée dans la descente de gradient ?
- Qu'est-ce qu'un point selle ? Un minimum local vs global ?
- Qu'est-ce que la règle de la chaîne (chain rule) ? Lien avec la backpropagation ?

---

## 📊 10. Data Engineering & Big Data (Notions)

- Qu'est-ce que le ETL ? ELT ? Quelle différence ?
- Qu'est-ce qu'Apache Spark ? PySpark ? Pourquoi les utiliser ?
- Qu'est-ce que MapReduce ?
- Qu'est-ce que le traitement batch vs streaming ?
- Qu'est-ce qu'Apache Kafka ? Apache Airflow ?
- Qu'est-ce que le format Parquet ? Pourquoi est-il préféré au CSV ?
- Qu'est-ce que le partitionnement de données ?
- Qu'est-ce que Hadoop ? HDFS ?
- Qu'est-ce qu'un cloud data warehouse ? (BigQuery, Redshift, Snowflake)

---

## 🧪 11. Exercices pratiques & Tests techniques types

### 11.1 Coding challenges
- Implémenter une régression linéaire from scratch (sans scikit-learn).
- Implémenter K-Means from scratch.
- Implémenter une descente de gradient.
- Écrire une fonction pour calculer la distance euclidienne, de Manhattan, cosine.
- Implémenter le Naive Bayes from scratch.
- Écrire un KNN from scratch.
- Manipulation de données avec Pandas (nettoyage, agrégation, jointures sur un dataset réel).
- Créer une visualisation complète à partir d'un jeu de données.

### 11.2 Case studies / Projets
- On vous donne un dataset : faites une analyse exploratoire complète (EDA).
- Construisez un modèle de prédiction de churn client.
- Construisez un système de recommandation simple.
- Prédiction de prix immobilier : quelles features utiliser ? Quel modèle ?
- Classification de spam : décrivez votre approche de bout en bout.
- Détection de fraude : comment gérer le déséquilibre de classes ?
- Prédiction de séries temporelles : quelles méthodes utiliser ?
- On vous donne un modèle déjà entraîné : comment l'améliorer ?

### 11.3 Questions de design / système
- Comment construiriez-vous un système de recommandation pour un site e-commerce ?
- Comment feriez-vous de la détection de fraude en temps réel ?
- Comment géreriez-vous un dataset de 100 Go qui ne tient pas en mémoire ?
- Comment mettriez-vous en production un modèle qui doit servir 1000 requêtes/sec ?

---

## 🧩 12. Éthique & IA Responsable

- Qu'est-ce que le biais algorithmique ? Donnez des exemples.
- Qu'est-ce que le fairness en ML ? Comment le mesurer ?
- Qu'est-ce que l'explicabilité d'un modèle ? (SHAP, LIME, feature importance)
- Quelle est la différence entre un modèle boîte noire et un modèle interprétable ?
- Qu'est-ce que le RGPD ? Quel impact sur les projets Data Science ?
- Qu'est-ce que la confidentialité différentielle (differential privacy) ?
- Qu'est-ce que le data leakage ? Comment le prévenir ?

---

## 💬 13. Questions comportementales & Soft Skills

### 13.1 Présentation de projets
- Parlez-moi d'un projet Data Science que vous avez réalisé. (Méthodologie, challenges, résultats)
- Quel a été votre plus gros challenge technique ? Comment l'avez-vous résolu ?
- Comment avez-vous géré un dataset de mauvaise qualité ?
- Comment communiquez-vous vos résultats à des non-techniques ?
- Décrivez une situation où votre modèle ne donnait pas les résultats attendus. Qu'avez-vous fait ?

### 13.2 Méthodologie & collaboration
- Comment structurez-vous un nouveau projet Data Science de A à Z ?
- Comment priorisez-vous vos tâches sur un projet ?
- Comment travaillez-vous en équipe ? Avec des développeurs ? Des métiers ?
- Comment faites-vous de la veille technologique ?
- Comment gérez-vous les deadlines serrées ?

### 13.3 Questions de motivation
- Pourquoi la Data Science ? Qu'est-ce qui vous passionne ?
- Où vous voyez-vous dans 3-5 ans ?
- Quels sont vos points forts / axes d'amélioration ?
- Quel sujet en Data Science vous intéresse le plus actuellement ?
- Comment restez-vous à jour avec les dernières avancées ?

---

## 🧮 14. Séries temporelles

- Qu'est-ce qu'une série temporelle ?
- Qu'est-ce que la stationnarité ? Comment la tester ? (Test de Dickey-Fuller)
- Qu'est-ce que la décomposition d'une série temporelle ? (Tendance, saisonnalité, résidu)
- Qu'est-ce que ARIMA ? Ses paramètres (p, d, q) ?
- Qu'est-ce que SARIMA ? Prophet ? Quand les utiliser ?
- Comment valider un modèle de série temporelle ? (Walk-forward validation)
- Qu'est-ce que l'autocorrélation ? L'autocorrélation partielle ?
- Comment gérer les valeurs manquantes dans une série temporelle ?
- Qu'est-ce que le lag ? Le rolling mean ? Le rolling std ?

---

## 🔬 15. A/B Testing & Expérimentation

- Qu'est-ce qu'un A/B test ? Comment le mettre en place ?
- Comment calculer la taille d'échantillon nécessaire ?
- Qu'est-ce que la significativité statistique dans un A/B test ?
- Qu'est-ce que le Minimum Detectable Effect (MDE) ?
- Quels sont les pièges courants des A/B tests ? (Peeking problem, multiple testing)
- Qu'est-ce qu'un test multi-variés (MVT) ?

---

## 🏗️ 16. Systèmes de recommandation

- Quels sont les deux grands types de systèmes de recommandation ? (Filtrage collaboratif, basé sur le contenu)
- Expliquer le filtrage collaboratif user-based vs item-based.
- Qu'est-ce que la factorisation matricielle ? (SVD, ALS)
- Qu'est-ce que le cold start problem ? Comment le résoudre ?
- Qu'est-ce qu'un système de recommandation hybride ?
- Comment évaluer un système de recommandation ? (Precision@K, Recall@K, NDCG, MAP)

---

## 🧬 17. IA Générative (Bonus, questions possibles en 2025-2026)

- Qu'est-ce qu'un GAN (Generative Adversarial Network) ? Comment fonctionne-t-il ?
- Qu'est-ce qu'un VAE (Variational Autoencoder) ?
- Qu'est-ce qu'un LLM (Large Language Model) ? Comment sont-ils entraînés ?
- Qu'est-ce que le fine-tuning d'un LLM ? LoRA ? QLoRA ?
- Qu'est-ce que le RAG (Retrieval-Augmented Generation) ?
- Qu'est-ce qu'un prompt engineering ?
- Qu'est-ce qu'un embedding vectoriel ? Un vector database ?
- Qu'est-ce que le RLHF (Reinforcement Learning from Human Feedback) ?
- Quels sont les risques et limitations des LLMs ? (Hallucinations, biais, coûts)
- Qu'est-ce que la distillation de modèle ? La quantization ?

---

## 📋 Checklist de préparation

- [ ] Maîtriser les stats et probas de base
- [ ] Savoir expliquer chaque algorithme ML courant (intuition + maths)
- [ ] Être à l'aise en Python (Pandas, NumPy, Scikit-learn)
- [ ] Savoir écrire des requêtes SQL complexes (window functions, CTEs, jointures)
- [ ] Comprendre les bases du Deep Learning
- [ ] Avoir au moins 2-3 projets à présenter en détail
- [ ] S'entraîner sur des exercices de coding (LeetCode, HackerRank, StrataScratch)
- [ ] Préparer des réponses aux questions comportementales
- [ ] Connaître les bases du déploiement (API, Docker, CI/CD)
- [ ] Réviser les maths (algèbre linéaire, calcul)
- [ ] Être au courant des tendances actuelles (LLMs, IA générative)

---

> 💡 **Conseil** : Pour chaque concept, soyez capable de (1) l'expliquer simplement, (2) donner un exemple concret, (3) citer ses avantages et inconvénients, et (4) dire quand l'utiliser vs ne pas l'utiliser.
