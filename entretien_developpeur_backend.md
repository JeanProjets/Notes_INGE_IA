# 🎯 Questions d'entretien Développeur — Backend / Système (Java, C++, Linux)

> Guide exhaustif pour préparer un premier entretien d'embauche ou test technique basé sur la fiche de poste de Développeur Backend / Système (C++, Java, Multi-threading, Linux, CI/CD).

---

## ☕ 1. Langages Principaux : Java & C++

### 1.1 Java
- Quelles sont les principales différences entre Java et C++ par rapport à la gestion de la mémoire ?
- Qu'est-ce que la JVM, le JRE et le JDK ?
- Comment fonctionne le Garbage Collector en Java ? Citez certains algorithmes (ex: G1, ZGC).
- Qu'est-ce qu'une fuite mémoire (memory leak) en Java et comment peut-elle survenir malgré le Garbage Collector ?
- Quelle est la différence entre une classe abstraite et une interface (notamment depuis Java 8 avec les méthodes par défaut) ?
- Qu'est-ce que le polymorphisme, l'encapsulation et l'héritage ?
- Quelle est la différence entre `==` et `.equals()` pour les objets (ex: `String`) ?
- Comment gérez-vous les exceptions en Java ? Quelle est la différence entre *Checked* et *Unchecked Exceptions* ?
- Qu'est-ce que l'API Stream introduite dans Java 8 et quelle est sa différence avec les Collections classiques ?
- À quoi sert la classe `Optional` ?
- Qu'est-ce que la "Type Erasure" au niveau des Generics en Java ?

### 1.2 C++
- Quelle est la différence majeure entre le C et le C++ ?
- Qu'est-ce qu'un pointeur ? Une référence ? Quelle est la différence entre les deux ?
- Qu'est-ce que le paradigme RAII (Resource Acquisition Is Initialization) ? Pourquoi est-ce central en C++ ?
- Qu'est-ce qu'un pointeur intelligent (*Smart Pointer*) introduit avec C++11 ? Détaillez `std::unique_ptr`, `std::shared_ptr` et `std::weak_ptr`.
- Qu'est-ce qu'une fonction virtuelle pure et une classe abstraite en C++ ?
- Qu'est-ce que le constructeur de copie, l'opérateur d'affectation et le *move constructor* (C++11) ?
- Qu'est-ce que la "Règle des Trois" (Rule of Three) ou la "Règle des Cinq" (Rule of Five) ?
- Comment fonctionne l'héritage multiple en C++ et quel est le "problème du diamant" ? Comment le résoudre ?
- Que signifie le mot-clé `const` appliqué à une méthode de classe (`void myFunction() const`) ?
- À quoi servent les *templates* en C++ et quel est le rôle de la STL (Standard Template Library) ?
- Comment gérez-vous manuellement la mémoire en C++ (`new`, `delete`) et quels sont les risques associés (dangling pointers, memory leaks) ?

---

## 🧵 2. Programmation Concurrente (Multi-threading)

### 2.1 Concepts fondamentaux
- Quelle est la différence entre un processus (*process*) et un *thread* (fil d'exécution) ?
- Qu'est-ce qu'une *Race Condition* (situation de compétition) et comment l'éviter ?
- Qu'est-ce qu'un *Deadlock* (interblocage) ? Proposez une stratégie pour l'empêcher.
- Expliquer la différence entre un Mutex (Mutual Exclusion), un Sémaphore et une Spinlock.
- Qu'est-ce que le changement de contexte (*context switch*) et pourquoi a-t-il un coût en performance ?
- Qu'est-ce que l'opération matérielle "Compare-And-Swap" (CAS) et la programmation *lock-free* ?

### 2.2 Implémentation en C++ et Java
- **Java** : Comment créer un Thread ? (`Runnable`, `Callable`, extension de `Thread`).
- **Java** : À quoi sert le mot-clé `synchronized` ? Et `volatile` ?
- **Java** : Qu'est-ce que l'Executor Framework (`ExecutorService`) ?
- **Java** : Quelle est la différence entre `wait()`, `notify()`, `notifyAll()` liés aux moniteurs et `Thread.sleep()` ?
- **C++11** : Comment lancer un thread avec `std::thread` ?
- **C++11** : Comment protéger des ressources partagées (`std::mutex`, `std::lock_guard`, `std::unique_lock`) ?
- **C++11** : Qu'est-ce qu'une Condition Variable (`std::condition_variable`) ?
- **C++11** : À quoi servent `std::future` et `std::async` ?

---

## 🐧 3. Système d'Exploitation Linux & Réseau

### 3.1 Linux
- Comment trouver un fichier spécifique récursivement dans un répertoire (`find`) ?
- Comment chercher une chaîne de caractères dans des fichiers (`grep`) ?
- Comment surveiller les processus en cours d'exécution en temps réel (`top`, `htop`) ?
- Qu'est-ce qu'un *inode* sous Linux ? Différence entre un lien symbolique (*symlink*) et un lien dur (*hardlink*) ?
- Différence entre l'Espace Utilisateur (*User Space*) et l'Espace Noyau (*Kernel Space*) ?
- Comment fonctionnent les permissions de fichiers sous Linux (`chmod`, `chown`) ? Que signifie `chmod 755` ?
- Qu'est-ce qu'un descripteur de fichier (*File Descriptor*) sous Linux ? Que sont le 0, 1 et 2 ?
- Comment rediriger la sortie standard et la sortie d'erreur d'une commande (ex: vers `/dev/null`) ?
- À quoi servent les signaux sous Linux (ex: `SIGKILL`, `SIGTERM`, `SIGINT`) ? Différence entre `kill -9` et `kill -15` ?

### 3.2 Réseau
- Quelles sont les couches du Modèle OSI ? Comment le comparer au modèle TCP/IP ?
- Quelle est la différence fondamentale entre TCP et UDP ? Dans quels cas privilégier UDP (ou TCP) ?
- Comment s'établit une connexion TCP (*Three-way handshake* : SYN, SYN-ACK, ACK) ? Comment se termine-t-elle ?
- Qu'est-ce qu'un paquet, une trame, un datagramme ?
- Différence entre une adresse IPv4 et IPv6 ?
- Qu'est-ce que le routage, un masque de sous-réseau, une passerelle (*gateway*) et le NAT ?
- Qu'est-ce qu'un port réseau ? Quels ports sont généralement associés à SSH, HTTP, HTTPS, DNS ?
- Comment fonctionne brièvement TLS/SSL pour sécuriser HTTP en HTTPS ?

---

## 🕵️ 4. Moyens d'Investigation Bas Niveau (Profiling & Debugging)

### 4.1 Investigations Générales & Réseau
- Vous avez une application qui consomme 100% du CPU sous Linux, comment diagnostiquez-vous le problème étape par étape ?
- Mêmes questions pour une consommation mémoire anormale (Out of Memory/OOM Killer).
- Comment utiliseriez-vous `tcpdump` pour capturer le trafic réseau ? Pouvez-vous écrire un filtre de base (ex: filtrer sur un port et une IP) ?
- Comment analysez-vous un fichier de capture `.pcap` (ex: avec Wireshark ou `tshark`) ?
- À quoi servent des commandes comme `netstat` (ou `ss`), `ping`, `traceroute`, `curl`, `nc` (netcat) pour le diagnostic réseau ?

### 4.2 Outils Spécifiques
- **C++ / Système** : À quoi sert l'outil `strace` (trace des appels système) ? Et `ltrace` (appels bibliothèques dynamiques) ?
- **C++** : Avez-vous déjà utilisé `Valgrind` ou des *Sanitizers* (MemorySanitizer, AddressSanitizer) ? Pour en faire quoi ?
- **C++** : Comment compilez-vous avec les symboles de debug et comment attachez-vous `gdb` à un processus ?
- **Linux** : Qu'est-ce qu'un "Core dump" sous Linux et comment l'analyser post-crash ? À quoi sert `perf` pour le profiling CPU ?
- **Java** : Comment extraire et analyser un Thread Dump (pour débloquer un deadlock) ou un Heap Dump (pour une fuite mémoire) ? Quels outils utiliser (ex: `jstack`, `jmap`, VisualVM, Eclipse MAT) ?

---

## 🚢 5. CI/CD, DevSecOps, Docker & Kubernetes (K8s)

### 5.1 CI/CD & DevSecOps
- Que signifient CI (Continuous Integration) et CD (Continuous Deployment / Delivery) ?
- Quel est le flux classique d'un pipeline d'intégration (Linting -> Tests Unitaires -> Build -> Tests End-to-End -> Publication) ?
- Posiérez-vous une expérience avec GitLab CI ? Qu'est-ce qu'un *Runner* ?
- Qu'est-ce que l'approche DevSecOps par rapport au DevOps classique ?
- Comment intégreriez-vous la sécurité dans une CI ? (ex: SAST pour le code métier comme SonarQube, Scan des dépendances/images tierces avec Trivy).

### 5.2 Conteneurisation (Docker)
- Quelle est la différence entre une Machine Virtuelle (VM) classique et un conteneur (Docker) ? (Isolation niveau OS vs isolation matérielle).
- Comment optimisez-vous la taille et la sécurité d'une image Docker ? (multi-stage builds, utiliser des images de base minimales comme Alpine ou distroless, ne pas tourner en root).
- Pouvez-vous expliquer le but des instructions `FROM`, `RUN`, `CMD`, `ENTRYPOINT` et `COPY` dans un Dockerfile ? Différence entre `CMD` et `ENTRYPOINT` ?
- Comment faites-vous pour persister des données écrites par un conteneur ? (Volumes, bind mounts).
- À quoi sert Docker Compose ?

### 5.3 Orchestration (Kubernetes)
- Pourquoi utiliser Kubernetes (K8s) au lieu de faire tourner de simples conteneurs Docker en production ?
- Définissez : Un Noeud (*Node*), un Pod, un Cluster. (Un Pod étant l'unité la plus petite déployable).
- Différence entre un `Deployment` (stateless), un `StatefulSet` (stateful) et un `DaemonSet` ?
- Comment exposez-vous une application à l'intérieur puis à l'extérieur du cluster Kubernetes ? (Différence entre ClusterIP, NodePort, LoadBalancer et Ingress).
- Comment gérez-vous la configuration et les secrets dans K8s ? (ConfigMap, Secrets).
- Connaissez-vous les commandes basiques `kubectl` (`get`, `describe`, `logs`, `exec`, `apply -f`) ?

---

## 🌟 6. Langages "Bonus" (Go, Rust, Python, TypeScript)

*(Si vous les avez sur votre CV ou s'ils sont listés en "plus" dans la fiche)*

- **Rust** : Qu'est-ce que le *Borrow Checker* et la notion d'*Ownership* ? En quoi cela empêche-t-il les *data races* à la compilation et permet-il de se passer d'un Garbage Collector ?
- **Go** : Qu'est-ce qu'une *goroutine* ? Comment communiquent-elles souvent de manière sécurisée (par canaux / *Channels* plutôt que par état partagé) ?
- **Python** : Qu'est-ce que le GIL (Global Interpreter Lock) en Python ? Comment écrire du code Python multithreadé efficace malgré cela (Multiprocessing) ? Qu'est-ce que le paradigme du "Duck Typing" ?
- **TypeScript** : Qu'est-ce que TypeScript apporte par rapport au JavaScript nativement (typage fort statique) et qu'est-ce que la compilation vers JS (transpilation) ?

---

## 📚 7. Architecture, Méthodologie & Soft Skills

### 7.1 Architecture & Code Clean
- Qu'est-ce que les principes SOLID en conception orientée objet ? (SRP, OCP, LSP, ISP, DIP).
- Que sont les Design Patterns classiques ? (Singleton, Factory, Observer, Strategy, Decorator). Lequel avez-vous utilisé récemment et pourquoi ?
- Qu'est-ce que le TDD (Test-Driven Development) ?
- Quels sont les différents types de tests ? (Unitaires, Intégration, E2E, Charge/Stress).
- Comment gérez-vous et résorbez-vous techniquement la dette technique d'un projet de grande envergure au quotidien ?

### 7.2 Soft Skills & Pratiques Pro
- **Anglais Technique** : Comment êtes-vous à l'aise pour lire et produire de la documentation anglophone claire (ex: Swagger/OpenAPI, Javadoc, README) ?
- Comment faire une "Code Review" (Merge Request/Pull Request) de bonne qualité ? Que cherchez-vous en priorité ? (Lisibilité, Edge cases, tests, respect de l'architecture).
- **Situationnel** : Un bug critique survient en production vendredi à 16h (un processus métier essentiel crashe). Quelle est votre démarche (investigation, fix, communication, post-mortem) face au stress ?
- Avez-vous une expérience des méthodes agiles (Scrum, Kanban) ?

---

## 📝 8. Tests Techniques / Pratiques Potentiels

*(Exercices à s'entraîner soit sur tableau blanc, soit en Live Coding)*

1. **Bug Concurrency** : On vous donne un pseudo-code C++ ou Java non thread-safe. Vous devez repérer la *race condition* ou la cause du *deadlock* potentiel et la corriger proprement (en ajoutant un Mutex ou un bloc synchronisé).
2. **Implémentation Pattern** : Implémenter en live le Design Pattern Singleton et prouver / s'assurer qu'il est "Thread-Safe" dans le langage de votre choix.
3. **Shell Script / Linux** : On vous donne un gros historique de logs (par exemple générés par `strace`). Vous devez écrire une commande Bash combinant `grep`, `awk` et `sort` pour ressortir les erreurs ou les processus les plus gourmands.
4. **Analyse de Capture réseau** : Identifier pourquoi un client UDP ne reçoit pas les paquets espérés parmi un dump tcpdump (ex: port fermé renvoyant des ICMP unreachable).
5. **Critique Dockerfile** : Améliorez la propreté, la taille et la sécurité d'un Dockerfile brouillon qui installe des paquets inutiles ou expose le runtime en Root.
6. **Architecture Système** : Tracer l'architecture globale au tableau de la réception réseau (Load Balancer -> K8s Ingress -> Pod Java) jusqu'à la base de données persistante interne.

---

## 🏗️ 9. Concepts Généraux & Bases de Données

### 9.1 Programmation Orientée Objet (POO) & Concepts Généraux
- Qu'est-ce qu'une **Classe** ? Qu'est-ce qu'un **Objet** ? Donnez un exemple concret.
- Qu'est-ce qu'une **Classe abstraite** ? Quelle est la différence entre une Classe abstraite et une **Interface** ?
- Quels sont les différents **Types de données** primitifs courants et à quoi servent-ils ? Donnez des exemples typiques.
- Qu'est-ce qu'une portée de variable (Scope) ?
- Pourquoi est-il déconseillé d'utiliser des "nombres magiques" (Magic Numbers) dans le code ?

### 9.2 Bases de Données (Relationnelles vs Non-relationnelles)
- Quelle est la différence fondamentale entre une base de données **Relationnelle (SQL)** et **Non-relationnelle (NoSQL)** ? Donnez des exemples de moteurs de bases de données pour chacun.
- Comment choisir entre une BDD SQL et NoSQL pour un nouveau projet ? Quels sont les critères de choix ?

---

> 💡 **Conseil d'entretien** : Pour les questions d'investigations bas niveau (tcpdump, gdb, perf), l'examinateur cherchera à voir votre **méthodologie** plus que votre connaissance parfaite des paramètres des commandes. Si vous ne savez pas, expliquez exactement **ce que vous chercheriez** sur Google ou StackOverflow.
