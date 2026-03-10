# 📖 Guide Pratique Git & GitHub

## 1. Les Fondements de Git
Git s'articule autour de 3 espaces de travail principaux. Bien les comprendre permet de savoir exactement où se trouvent tes fichiers à tout moment :
* **Le répertoire de travail (Working Directory) :** Les fichiers que tu modifies actuellement sur ton ordinateur.
* **L'index (Staging Area) :** La zone de préparation où tu ajoutes les modifications qui feront partie du prochain commit.
* **Le dépôt (Repository / `.git`) :** La base de données Git où l'historique est enregistré de manière permanente.

> **Note sur le fichier `README.md` :**
> Il sert de documentation au projet. Il doit généralement contenir un sommaire, les objectifs du code, et les étapes à suivre pour installer le projet en local.

---

## 2. Démarrer un Projet (Configuration et Clonage)

| Action | Commande |
| :--- | :--- |
| **Cloner un repo (dossier par défaut)** | `git clone https://github.com/user/repo.git` |
| **Cloner un repo (dossier personnalisé)** | `git clone https://github.com/user/repo.git Nom_dossier` |

> **Astuce Sécurité :** Privilégie le clonage via **SSH** plutôt que HTTPS. C'est beaucoup plus sécurisé et, dans beaucoup d'entreprises, le HTTPS est verrouillé.

---

## 3. Gérer ses Fichiers (Staging & Index)

Avant de sauvegarder, il faut préparer ses fichiers. Pour vérifier l'état du dépôt à tout moment (et avoir les suggestions de Git), utilise :

```bash
git status
```

**Ajouter des fichiers à l'index (Staging) :**
* `git add -A` : Ajoute **tous** les fichiers (nouveaux, modifiés, supprimés).
* `git add -u` : Ajoute **uniquement** les fichiers déjà connus par Git (ignorera les nouveaux fichiers créés).
* `git add [fichier]` : Ajoute un fichier spécifique.

**Retirer des fichiers de l'index (Unstage) :**
* `git rm --cached [fichier]` ou `git restore --staged [fichier]` : Enlève un fichier du staging area sans supprimer tes modifications locales.

**Gérer les fichiers suivis :**
* `git rm [fichier]` : Supprime le fichier de Git et de ton disque.
* `git mv [ancien-nom] [nouveau-nom]` : Renomme ou déplace un fichier dans Git.

---

## 4. Sauvegarder et Consulter l'Historique (Commits)

Une fois tes fichiers dans l'index, il est temps de créer un commit.
> **Ressource :** [Bonnes pratiques pour les messages de commit](https://gist.github.com/luismts/495d982e8c5b1a0ced4a57cf3d93cf60)

```bash
git commit -m "Message clair et descriptif de tes changements"
```

**Consulter l'historique :**
* `git log` : Historique complet de tous les commits.
* `git log --oneline` : Historique condensé (affiche le hash et le message sur une ligne). *(ex: `a3f5c21 Fix bug login`)*
* `git show [hash-du-commit]` : Affiche les modifications et les métadonnées d'un commit précis.
*(Note : tu peux utiliser un alias comme `git lg` si tu l'as configuré au préalable).*

---

## 5. Travailler avec les Branches

Les branches te permettent de développer des fonctionnalités sans toucher au code principal (`main`).

| Action | Commande |
| :--- | :--- |
| **Lister les branches** | `git branch` (locales) ou `git branch -a` (locales et distantes) |
| **Créer une branche** | `git branch [nom_branche]` |
| **Changer de branche** | `git checkout [nom_branche]` |
| **Revenir à la branche précédente** | `git checkout -` |
| **Créer ET basculer sur une branche** | `git checkout -b [nom_branche]` |
| **Supprimer une branche (locale)** | `git branch -d [nom_branche]` |

---

## 6. Synchroniser avec le Dépôt Distant (GitHub/GitLab)

* **`git pull`** : Récupère l'historique depuis GitHub et met à jour ta copie de travail locale.
* **`git fetch --prune`** : Récupère l'historique sans modifier tes fichiers locaux et nettoie les références des branches distantes supprimées.
* **`git push`** : Envoie tes commits sur GitHub.

**Pousser une nouvelle branche locale pour la première fois :**

```bash
git push --set-upstream origin [nom_branche]
# ou sa version courte : git push -u origin [nom_branche]
```

*(Explication : `origin` est le raccourci/nom par défaut de l'adresse de ton dépôt en ligne. Une fois le `-u` utilisé, Git mémorise le lien et un simple `git push` suffira les fois suivantes).*

> **💡 L'astuce Pro pour les branches "Upstream" :**
> Si tu en as marre du message *"fatal: The current branch has no upstream branch"*, tape cette commande une seule fois pour modifier ta configuration globale :
> `git config --global push.autoSetupRemote true`
> Tes `git push` fonctionneront ensuite tout le temps automatiquement !

### 💡 L'instant clarté : Fetch vs Pull

La confusion la plus classique en Git se résume à une équation :
**`git pull = git fetch + git merge`**

* **`git fetch` (La boîte aux lettres) :** Git se connecte à GitHub et télécharge tout le nouvel historique (nouveaux commits, nouvelles branches de tes collègues). **Il ne touche pas à tes fichiers locaux.** C'est 100% sécurisé pour t'informer de ce qui a changé en ligne avant d'agir.
* **`git pull` (Le bureau) :** Git va chercher les nouveautés (`fetch`) ET les fusionne immédiatement avec ton travail en cours (`merge`).

**Exemple d'usage :** Utilise `git fetch --prune` pour mettre à jour la liste de tes branches et nettoyer celles qui ont été supprimées en ligne par tes collègues, le tout sans risquer de casser le code que tu es en train d'écrire !

---

## 7. Workflows et Collaboration en Entreprise

### Le Workflow Feature Branch (Le standard de l'industrie)

**Règles d'or :** Ne jamais commiter directement sur `main`. Toujours tester après un rebase.

1.  **Partir d'un `main` propre :**

    ```bash
    git checkout main
    git pull origin main
    ```

2.  **Créer une branche pour ta fonctionnalité :**

    ```bash
    git checkout -b feature/ma-nouvelle-feature
    ```

3.  **Travailler et sauvegarder :**

    ```bash
    git add .
    git commit -m "Ajout du script de pipeline"
    ```

4.  **Mettre à jour sa branche (Rebase) avant d'envoyer (si le `main` a évolué) :**

    ```bash
    git fetch origin
    git rebase origin/main
    # En cas de conflit : ouvrir les fichiers en rouge, corriger, puis :
    # git add .
    # git rebase --continue
    ```

5.  **Pousser sur GitHub :**

    ```bash
    git push -u origin feature/ma-nouvelle-feature
    # Si tu as fait un rebase après un premier push, il faudra forcer : git push -f
    ```

6.  **Ouvrir une Pull Request (PR) :**
    * Aller sur GitHub > *Pull Requests* > *New PR* (de ta branche vers `main`).
    * Vérifier le code dans l'onglet *Files changed*.
    * Envoyer la PR à un collègue pour review.
    * Une fois validée, **Merger** la PR.
    * Supprimer ta branche locale (`git branch -d feature/ma-nouvelle-feature`).

---

## 8. Revenir en Arrière (Oops!)

Git pardonne presque tout, à condition d'utiliser la bonne commande.

**1. Annuler des modifications locales non commitées :**
* `git restore .` (ou `git checkout -- .`) : Annule TOUTES les modifications en cours et remet les fichiers dans l'état du dernier commit.

**2. Explorer un ancien état (sans rien casser) :**
* `git checkout [hash-du-commit]` : Permet de voir à quoi ressemblait le projet à ce moment-là (tu seras en mode *detached HEAD*). Pour revenir au présent : `git checkout main`.

**3. Annuler publiquement (Recommandé en équipe) :**
* `git revert [hash-du-commit]` : Crée un *nouveau* commit qui fait exactement l'inverse du commit ciblé. C'est la méthode sûre si le code a déjà été poussé (partagé avec d'autres).

**4. Effacer les derniers commits (DANGER ⚠️) :**
*Ces commandes suppriment l'historique. À utiliser uniquement sur ta branche locale non partagée.*
* `git reset --hard HEAD~1` (ou `HEAD^`) : Revient 1 commit en arrière et **supprime** définitivement les modifications. (Remplace `1` par `2` pour reculer de 2 commits, etc.).
* `git reset --hard [hash-du-commit]` : Remet le projet *exactement* dans l'état du commit ciblé, en effaçant tout ce qui s'est passé après.

**5. La commande de la dernière chance :**
* `git reflog` : Git garde un historique temporaire de *toutes* tes actions (même les `reset --hard` !). Permet de retrouver le hash d'un commit perdu pour pouvoir faire un `git reset --hard [hash-retrouvé]` et le ressusciter.

---

## 9. Mettre de côté temporairement (Git Stash)

Le `stash` (la "planque") agit comme un tiroir de bureau : tu y glisses tes brouillons en cours pour retrouver un espace de travail propre, et tu pourras les ressortir plus tard. Très utile pour changer de branche en urgence sans commiter du code non terminé.

| Action | Commande |
| :--- | :--- |
| **Mettre de côté les modifications en cours** | `git stash` (ou `git stash push -m "description"` pour s'en souvenir facilement) |
| **Lister tout ce qui est dans le tiroir** | `git stash list` |
| **Récupérer les modifications ET les enlever du tiroir** | `git stash pop` (applique le stash le plus récent par défaut) |
| **Récupérer les modifications SANS les enlever du tiroir** | `git stash apply` |
| **Supprimer un brouillon spécifique du tiroir** | `git stash drop stash@{0}` (remplace `0` par le numéro du stash) |
| **Vider entièrement le tiroir** | `git stash clear` |

**Exemple de workflow d'urgence classique :**
1. Tu codes sur ta branche `feature/nouvel-algo`, on te signale un bug urgent sur main.
2. Tu ranges tes brouillons : `git stash`.
3. Tu bascules : `git checkout main` (tu corriges, commit et push).
4. Tu reviens sur ta branche : `git checkout feature/nouvel-algo`.
5. Tu ressors tes brouillons : `git stash pop`.