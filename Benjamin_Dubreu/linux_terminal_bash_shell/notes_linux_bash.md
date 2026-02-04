````markdown
# Notes Linux

## Commandes de base

- `ls -a` : afficher les fichiers cachés
- `whoami` : afficher l’utilisateur courant
- `pwd` : *print working directory*, affiche le répertoire courant

---

## Navigation

- `cd`  
  → revenir au répertoire personnel
- `cd -`  
  → revenir au répertoire précédent
- `cd /`  
  → aller à la racine (*root directory*)

---

## VIM

- `i` : passer en mode insertion
- `Esc` : sortir du mode insertion
- `:w` : sauvegarder
- `:q` : quitter
- `:wq` ou `:x` : sauvegarder et quitter
- `:q!` : quitter sans sauvegarder
- `:w !sudo tee % > /dev/null`  
  → écrire le fichier avec les droits sudo sans afficher la sortie

---

## Création et manipulation de fichiers

- `touch nouveau_fichier1 nouveau_fichier2`  
  → créer plusieurs fichiers

- `touch jour{1..10}`  
  → créer 10 fichiers (`jour1` à `jour10`)

- Écrire dans un fichier (en écrasant le contenu) :
  ```bash
  echo pas_mal_les_bzez > jeff_bezos.txt
````

* Écrire dans un fichier (en ajoutant à la fin) :

  ```bash
  echo pas_mal_les_bzez >> jeff_bezos.txt
  ```

* Afficher le contenu d’un fichier :

  ```bash
  cat nom_du_fichier
  ```

* Afficher tous les shells disponibles :

  ```bash
  cat /etc/shells
  ```

---

## Dossiers

* Créer un dossier :

  ```bash
  mkdir dossier
  ```

* Créer plusieurs dossiers :

  ```bash
  mkdir {1..10}
  ```

* Créer une arborescence :

  ```bash
  mkdir -p folder/sousfolder
  ```

* Supprimer un dossier vide :

  ```bash
  rmdir dossier
  ```

* Supprimer un dossier avec son contenu :

  ```bash
  rm -r dossier
  ```

* Supprimer avec confirmation :

  ```bash
  rm -ri dossier
  ```

---

## Copier, déplacer, renommer

* Copier un fichier :

  ```bash
  cp fichier_apprentissage.txt /mnt/c/Users/jb-14/Documents/
  ```

* Sur WSL, accéder aux documents Windows :

  ```bash
  /mnt/c/Users/jb-14/Documents/
  ```

* Déplacer un fichier ou un dossier :

  ```bash
  mv fichier dossier/
  ```

* Renommer un fichier :

  ```bash
  mv ancien_nom nouveau_nom
  ```

---

## Enchaîner des commandes

```bash
cd .. && touch fichier_test.txt && echo "blop" >> fichier_test.txt && ls -a
```

---

## Affichage détaillé

```bash
ls -lh
```

---

## Droits et exécutables

* Ajouter le droit d’exécution :

  ```bash
  chmod u+x first_script.sh
  ```

* Localiser un exécutable :

  ```bash
  which bash
  ```

* Exécuter un script :

  ```bash
  ./first_script.sh
  ```

---

## Scripts bash

* Définir une variable avec la date :

  ```bash
  now=$(date)
  ```

* Exécuter un script Python depuis un script bash :

  ```bash
  python3 script.py
  ```

---

## Python et terminal

* Exécuter un script Python :

  ```bash
  python3 script.py
  ```

> ⚠️ `./script.py` ne fonctionne pas par défaut car le terminal l’interprète comme un script bash.

* Ajouter le droit d’exécution à un fichier Python :

  ```bash
  chmod u+x script.py
  ```

* Savoir quelle version de Python est utilisée :

  ```bash
  which python
  ```

* Lister les versions de Python installées :

  ```bash
  ls -lh /usr/bin/python*
  ```

* Connaître la version de Python dans un script :

  ```python
  print(sys.version)
  print(sys.version_info)
  ```

---

## Variables d’environnement (Python & Bash)

* En Python :

  ```python
  from os import environ
  print(environ["HOME"])
  ```

* Créer ou modifier une variable d’environnement :

  ```bash
  export WEATHER=beautiful
  ```

* Modifier le PATH (temporairement, pour la session en cours) :

  ```bash
  export PATH="/Users/jean-baptistevayssade/Documents/dossier_contenant_le_bash_de_la_commande:$PATH"
  ```

> ⚠️ Les variables exportées ne persistent pas entre les sessions.

---

## Shebang

Au début d’un fichier Python :

```bash
#!/usr/bin/python3
```

Permet d’exécuter le fichier directement sans écrire `python3` devant.

---

## Gestion des processus

* Interrompre un processus :

  ```
  Ctrl + C
  ```

* Suspendre un processus :

  ```
  Ctrl + Z
  ```

* Reprendre le processus :

  ```bash
  fg
  ```

* Moniteur système :

  ```bash
  sudo htop
  ```

  (puis `k` → `SIGKILL` pour tuer un processus)

---

## Redirections

* Envoyer la sortie standard vers la poubelle :

  ```bash
  ls > /dev/null
  ```

* Envoyer les erreurs vers la poubelle :

  ```bash
  ls commande_inexistante 2> /dev/null
  ```

* Rediriger les erreurs d’un script Python vers un fichier de log :

  ```bash
  python3 script.py 2> python_log.txt
  ```

---

## Historique

```bash
history
```

---

## Réseau

```bash
ping www.google.com
```

Permet de tester la connexion Internet.

---

## Compression

```bash
zip nom_du_fichier_destination.zip nom_fichier_a_zipper
```

---

## Aide

```bash
man ls
```

affiche le manuel de la commande.

