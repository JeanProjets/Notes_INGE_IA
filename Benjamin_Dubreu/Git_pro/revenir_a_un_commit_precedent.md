# Revenir à un état précédent avec Git

## 1. Voir l’historique des commits

Pour voir les commits existants :

```bash
git log --oneline
```

Exemple :

```
a3f5c21 Fix bug login
9c2d1ab Add authentication
4e8a912 Initial commit
```

Chaque ligne correspond à un **commit identifié par son hash**.

---

# 2. Revenir temporairement à un ancien commit

Si tu veux simplement **voir ou tester un ancien état du projet** :

```bash
git checkout 9c2d1ab
```

⚠️ Tu seras en **detached HEAD** (pas sur une branche).

Pour revenir à ta branche :

```bash
git checkout main
```

---

# 3. Revenir en arrière et supprimer les derniers commits

Si ton dernier commit casse le projet :

```bash
git reset --hard HEAD~1
```

Signification :

* `HEAD~1` → revenir 1 commit en arrière
* `HEAD~2` → revenir 2 commits en arrière

⚠️ Cette commande **supprime les modifications définitivement**.

---

# 4. Revenir à un commit précis

```bash
git reset --hard 9c2d1ab
```

Le projet reviendra **exactement dans l’état de ce commit**.

---

# 5. Annuler un commit sans casser l’historique (recommandé en équipe)

Si le code est déjà partagé (GitHub, collaboration) :

```bash
git revert 9c2d1ab
```

Git crée un **nouveau commit qui annule les modifications du précédent**.

---

# 6. Annuler des modifications locales non commit

Si tu as modifié des fichiers mais **pas encore fait de commit** :

```bash
git restore .
```

ou

```bash
git checkout -- .
```

---

# 7. Retrouver des commits perdus

Même après un `reset --hard`, Git garde souvent l’historique temporairement :

```bash
git reflog
```

Tu peux retrouver **des commits supprimés et revenir dessus**.

---

# Workflow courant quand le code est cassé

```bash
git log --oneline
git reset --hard HEAD~1
```
