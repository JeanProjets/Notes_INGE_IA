# 💡 Réponses : Questions d'entretien Développeur Backend / Système

> Ce document contient les réponses détaillées et illustrées aux questions du guide d'entretien pour le poste de Développeur Backend / Système (Java, C++, Linux, Multi-threading).

---

## ☕ 1. Langages Principaux : Java & C++

### 1.1 Java

**Différences entre Java et C++ par rapport à la mémoire :**
En Java, la gestion de la mémoire est automatique grâce au *Garbage Collector* (GC). Le développeur ne désalloue pas explicitement la mémoire. En C++, la gestion est manuelle (`new`/`delete`) ou gérée via le paradigme RAII (Smart Pointers). Java n'a pas de pointeurs explicites accessibles au développeur.

**JVM, JRE, JDK :**
- **JVM (Java Virtual Machine)** : Exécute le bytecode Java. Rend Java indépendant de la plateforme.
- **JRE (Java Runtime Environment)** : Contient la JVM + bibliothèques standards pour *exécuter* un programme.
- **JDK (Java Development Kit)** : Contient le JRE + outils de développement (compilateur `javac`, debuggers, etc.).

**Fonctionnement du Garbage Collector :**
Il libère automatiquement la mémoire occupée par des objets n'ayant plus de références pointant vers eux. 
- Algorithmes : *G1 (Garbage-First)* privilégie des pauses courtes et prévisibles. *ZGC* vise des pauses ultra-courtes (sub-milliseconde), idéal pour de très gros tas (Heaps).

**Fuite mémoire (Memory Leak) en Java :**
Bien qu'il y ait un GC, une fuite survient si l'on garde involontairement des références vers des objets devenus inutiles (ex: objets mis dans une liste `static` géante et jamais retirés). Le GC croit qu'ils sont encore utiles.

**Classe abstraite vs Interface (depuis Java 8) :**
- **Classe abstraite** : Peut avoir un état (champs d'instance), des constructeurs, du code partagé. Une classe ne peut hériter que d'une seule classe (abstraite ou non).
- **Interface** : Contrat de méthodes abstraites. Depuis Java 8, elle peut avoir des méthodes `default` avec un corps, mais pas d'état d'instance (seulement des constantes `static final`). Une classe peut implémenter plusieurs interfaces.

**Polymorphisme, Encapsulation, Héritage :**
- **Héritage** : Une classe fille hérite des attributs/méthodes de la classe mère (réutilisation).
- **Encapsulation** : Restreindre l'accès à l'état interne (`private`) et exposer des méthodes (`public` getters/setters) pour garantir la cohérence des données.
- **Polymorphisme** : Capacité d'un objet à prendre plusieurs formes. Appeler `animal.crier()` fera un "miaou" ou "ouaf" selon l'objet réel instancié.

**`==` vs `.equals()` :**
- `==` compare les *références* mémoire (les objets pointent-ils vers la même adresse ?).
- `.equals()` compare le *contenu* logique des objets (ex: les chaînes de caractères ont-elles les mêmes lettres ?).

**Exceptions Checked vs Unchecked :**
- **Checked** (hérite de `Exception`) : Le compilateur force à les gérer (`try/catch` ou `throws`). Ex: `IOException`.
- **Unchecked** (hérite de `RuntimeException`) : Erreurs de programmation, pas besoin de les déclarer. Ex: `NullPointerException`.

**API Stream :**
Permet de traiter des collections de données de manière déclarative (fonctionnelle). Contrairement aux Collections (stockage), les Streams ne stockent rien mais transforment la donnée en flux (`filter`, `map`, `reduce`).
*Exemple :* `list.stream().filter(n -> n > 10).collect(Collectors.toList());`

**Optional :**
Classe conteneur (introduite en Java 8) qui peut contenir ou non une valeur non nulle. Évite de retourner `null` et force le développeur à gérer formellement l'absence de valeur, réduisant les `NullPointerException`.

**Type Erasure :**
Processus par lequel le compilateur Java supprime les informations de type générique (les `<T>`) à la compilation. À l'exécution (Runtime), la JVM ne connaît pas `List<String>`, elle voit juste `List`.

### 1.2 C++

**Différence C vs C++ :**
C est impératif et procédural. C++ ajoute la Programmation Orientée Objet (classes), les templates (programmation générique) et une bibliothèque standard riche (STL).

**Pointeur vs Référence :**
- **Pointeur** (`int* p`) : Variable qui contient une adresse mémoire. Peut être `nullptr` ou réassigné pour pointer ailleurs. Nécessite d'être déréférencé (`*p`).
- **Référence** (`int& r`) : Alias vers une variable existante. Ne peut pas être nul, ni être réassigné une fois initialisé. Manipulation plus sûre et syntaxe plus propre.

**RAII (Resource Acquisition Is Initialization) :**
Concept fondamental en C++ où la durée de vie d'une ressource (mémoire, fichier, mutex) est liée à la durée de vie de l'objet qui la gère. La ressource est acquise au constructeur et libérée au destructeur (automatiquement appelé à la sortie de portée `{ ... }`).

**Smart Pointers (C++11) :**
Ils gèrent la désallocation mémoire automatiquement via RAII.
- `std::unique_ptr` : Possède exclusivement l'objet. Pas de copie possible, uniquement du *move*.
- `std::shared_ptr` : Propriété partagée (compteur de références). Détruit l'objet à 0 ref.
- `std::weak_ptr` : Observe un objet géré par un `shared_ptr` sans incrémenter le compteur (pratique pour éviter les références circulaires).

**Fonction virtuelle pure & classe abstraite :**
Une fonction virtuelle pure est déclarée avec `= 0` (ex: `virtual void doWork() = 0;`). Une classe contenant au moins une fonction virtuelle pure est abstraite (ininstanciable) et sert d'interface.

**Constructeur de copie, Affectation, Move :**
- Code déclenché lors de la copie / l'affectation d'un objet.
- *Move constructor (C++11)* : Permet de voler (déplacer) les ressources d'un objet temporaire (`rvalue`) au lieu de faire une copie profonde coûteuse (très efficace pour les gros conteneurs).

**Règle des Trois/Cinq :**
Si une classe a besoin de définir un Destructeur (ex: pour faire un `delete`), elle a probablement aussi besoin d'un Constructeur de copie et d'un Opérateur d'affectation (Règle des 3) + Move constructor et Move assignment operator pour C++11 (Règle des 5). Sinon, comportement de copie par défaut dangereux avec les pointeurs.

**Héritage multiple et problème du diamant :**
Une classe D hérite de B et C, qui héritent tous deux de A. D récupère les attributs de A deux fois. *Solution* : utiliser l'héritage virtuel (`class B : virtual public A`).

**Mot-clé `const` pour méthode :**
`void printInfo() const;` signifie que la méthode promet de ne pas modifier les variables membres de l'objet sur lequel elle est appelée.

**Templates et STL :**
Les templates permettent d'écrire du code générique (fonctions/classes) fonctionnant avec n'importe type. La STL (Standard Template Library) fournit des conteneurs (`std::vector`, `std::map`) et algorithmes (`std::sort`) génériques.

**Gestion mémoire manuelle :**
Utiliser `new` alloue de la mémoire sur le tas (*Heap*). Il faut obligatoirement appeler `delete`. L'oubli crée une *memory leak*. Un pointeur qui pointe vers une zone supprimée devient un *dangling pointer* (comportement indéfini si accédé).

---

## 🧵 2. Programmation Concurrente (Multi-threading)

### 2.1 Concepts
**Processus vs Thread :**
Un processus (programme en exécution) a son propre espace mémoire isolé. Un thread (fil d'exécution dans un processus) partage la même mémoire (tas, variables globales) avec les autres threads de ce processus. Les threads sont plus légers à créer.

**Race Condition (Situation de compétition) :**
Survient quand plusieurs threads accèdent et modifient une ressource partagée simultanément sans synchronisation. Le résultat final dépend de l'ordre d'accès imprévisible. *Solution* : Protéger la ressource (Mutex).

**Deadlock (Interblocage) :**
Thread A possède la ressource 1 et attend la 2. Thread B possède la ressource 2 et attend la 1. Tout est bloqué. *Stratégie* : Toujours acquérir les verrous (mutex) dans le même ordre strict.

**Mutex, Sémaphore, Spinlock :**
- **Mutex** : Verrou mutuellement exclusif. Un seul thread peut l'acquérir. Si déjà verrouillé, le thread s'endort.
- **Sémaphore** : Compteur de ressources. Permet à *N* threads d'accéder (ex: pool de connexions BDD). Un sémaphore binaire = conditionnellement comme un mutex.
- **Spinlock** : Verrouillage où le thread tourne en boucle active (`while(!locked)`) au lieu de s'endormir. Utile pour des verrous tenus un temps très court, évite le coût du context switch.

**Context Switch :**
L'OS suspend l'exécution d'un thread/processus pour en charger un autre sur le CPU. Coûteux car il faut sauvegarder/restaurer les registres et purger les caches TLB processeur.

**Compare-And-Swap (CAS) & Lock-free :**
Instruction CPU atomique qui dit "mets à jour la variable X à V2, seulement si elle vaut encore V1". Base des structures sans verrou (*lock-free*), évite l'endormissement des threads. Ex: `AtomicInteger` en Java.

### 2.2 Implémentation (Java / C++)
**Java - Créer un Thread :**
1. Implémenter interface `Runnable` (préféré) : `Thread t = new Thread(() -> doWork()); t.start();`
2. Étendre la classe `Thread`.
3. Implémenter `Callable` (si besoin de retourner un résultat dans un `Future`).

**Java - `synchronized` et `volatile` :**
- `synchronized` : Rend un bloc/méthode mutuellement exclusif (un thread à la fois), grâce au moniteur de l'objet.
- `volatile` : Assure qu'une variable est toujours lue/écrite directement dans la RAM centrale (pas de mise en cache processeur locale du thread).

**Java - Executor Framework :**
Pool de threads pré-instanciés gérant l'exécution de tâches asynchrones. Ex: `Executors.newFixedThreadPool(10)`. Évite la création coûteuse à la volée de threads.

**Java - wait/notify vs sleep :**
- `sleep()` : Endort le thread, mais il *garde* ses verrous.
- `wait()` : Endort le thread lié à un bloc `synchronized` et *libère* le verrou pour d'autres threads. `notify()` réveille un thread en attente.

**C++ - `std::thread` :**
`std::thread t([]() { doWork(); }); t.join();` (attendre la fin du thread).

**C++ - Protéger ressources (`std::mutex`) :**
Ne jamais utiliser `lock()` manuellement qui risque d'être bloqué en cas d'exception. Toujours utiliser RAII avec `std::lock_guard<std::mutex> lock(myMutex);` (se déverrouille auto en sortant de la portée).

**C++ - Condition Variable :**
`std::condition_variable cv;` permet à un thread de s'endormir (`cv.wait(lock)`) jusqu'à ce qu'un autre thread change une condition et l'avertisse (`cv.notify_one()`). S'utilise avec `std::unique_lock`.

**C++ - Future / Async :**
`std::async` lance une fonction asynchrone et renvoie un `std::future`. Plus tard, on fait `future.get()` pour récupérer le résultat de calcul sans se préoccuper de créer le thread à la main.

---

## 🐧 3. OS Linux & Réseau

### 3.1 Linux
- **Recherche de fichiers** : `find /path -name "*.log"`
- **Recherche dans un fichier** : `grep "ERREUR" /var/log/syslog`
- **Surveillance** : `top` (basique) ou `htop` (coloré, interactif).
- **Inode** : Structure de données Linux qui décrit le fichier (droits, emplacement physique) sans son nom.
  - *Hardlink* : Pointe vers le même inode originel.
  - *Symlink* : Raccourci pointant vers le chemin du fichier (comme Windows alias).
- **User Space vs Kernel Space** : L'OS (kernel) gère matériel/réseau avec accès complet (Ring 0). L'user space (applications) y accède de façon contrôlée via des appels systèmes (syscalls).
- **`chmod 755`** : Donne les droits rwx (lecture-écriture-exécution=7) au propriétaire, et r-x (lecture-exécution=5) au groupe et aux autres.
- **File Descriptor** : Entier par lequel un processus identifie un fichier (ou socket réseau). Par défaut : 0 (stdin), 1 (stdout), 2 (stderr).
- **Redirection** : `commande > output.txt 2> erreur.txt` (ou `2>&1` pour envoyer strerr vers stdout).
- **Signaux** : `kill -15` (SIGTERM) demande gentiment, l'app peut faire du nettoyage. `kill -9` (SIGKILL) ordonne à l'OS "d'assassiner" le processus immédiatement (danger de corruption).

### 3.2 Réseau
- **Mode OSI vs TCP/IP** : OSI (7 couches: Physique, Liaison, Réseau, Transport, Session, Présentation, Application). TCP/IP simplifie en 4 couches (Accès réseau, Internet, Transport, Application).
- **TCP vs UDP** :
  - *TCP* : Fiable (garantit livraison/ordre), lourd (connexion en 3 temps SYN-ACK), contrôle de congestion. Idéal flux/fichiers (HTTP/SMTP/BDD).
  - *UDP* : Non fiable (fire-and-forget), n'assure pas l'ordre, mais très rapide. Idéal streaming, jeux vidéos temps réel, requêtes courtes DNS.
- **Three-way handshake (TCP)** : 1. Client envoie `SYN`. 2. Serveur répond `SYN-ACK`. 3. Client répond `ACK`. (Connexion établie). Fin via `FIN` et `ACK`.
- **Lexique** :
  - *Trame (Frame)* : Niveau Liaison (Adresse MAC).
  - *Datagramme/Paquet* : Niveau Réseau (IP).
- **IPv4 vs IPv6** : IPv4 sur 32 bits (pénurie d'adresses). IPv6 sur 128-bits.
- **Routage** : Acheminement d'un paquet d'un réseau à un autre. Le *sous-réseau / Mask* délimite le réseau local. La *Passerelle (Gateway)* est la porte de sortie (la box internet). *NAT* permet de partager l'IP publique entre plusieurs postes locaux.
- **Ports (Application)** : 80 (HTTP), 443 (HTTPS), 22 (SSH), 53 (DNS).
- **TLS/HTTPS** : Un *handshake TLS* s'effectue après la connexion TCP. Échange de certificat asymétrique (clé publique/privée serveur) pour convenir d'une clé symétrique temporaire chiffrant le reste de la session.

---

## 🕵️ 4. Investigations Bas Niveau (Profiling)

### 4.1 Générales & Réseau
**CPU à 100% :**
Je lance `top -H -p <PID>` pour voir quels threads CPU-intensifs tournent dans ce process. Je fais un Thread Dump de l'app ou j'utilise `perf`/`strace` pour voir ce qui l'occupe.

**OOM (Out Of Memory) Linux :**
Je vérifie `dmesg | grep -i oom` ou `/var/log/syslog` pour voir si l'OOM Killer du Kernel a tué le process. J'instrumente pour observer si c'est une fuite applicative (memory leak) ou une allocation monstre unique.

**`tcpdump` :**
Capture le trafic. Exemple : `tcpdump -i eth0 port 8080 and host 192.168.1.5` -> Capture le port 8080 en lien avec l'IP de la machine.
Analyse via bouton "Follow TCP Stream" dans un lecteur visuel comme *Wireshark* (via export `.pcap`).

**Outils réseau utiles :**
- `netstat -tuln` / `ss -tuln` : Ports locaux ouverts en écoute.
- `ping` (ICMP) : Le serveur distant répond-il ?
- `traceroute` : Voir les bonds réseau (savoir où le paquet bloque).
- `nc -vz IP PORT` / `telnet IP PORT` : Le port TCP distant est-il joignable du point de vue de l'application (utile pour détecter un blocage pare-feu non vu avec ICMP ping).

### 4.2 Spécifiques
- **`strace`** : Affiche les appels systèmes (appels au Kernel: `open`, `read`, `socket`, `bind`). Très puissant pour voir où un processus est coincé (ex: attente I/O, fichier absent).
- **Valgrind (Memcheck)** : Vérifie le prg C/C++ et intercepte les accès mémoire. Indique fuites (`malloc` sans `free`) à la fin. Souvent remplacé en dev moderne par les *Sanitizers* (`-fsanitize=address` au compilo, beaucoup plus rapides).
- **GDB** : Debugger GNU. Compiler avec flag `-g`. `gdb -p PID` l'attache en cours de route. `bt` pour afficher la pile d'appel (stack trace) du thread actif.
- **Core Dump** : Fichier image de la mémoire du process généré par l'OS suite à un crash brutal (segfault / erreur 11). On l'inspecte *post-mortem* avec GDB pour connaitre l'état précis des variables.
- **Java dumps** :
  - *Thread Dump* (état des threads) -> Outil `jstack <PID>`. Utile pour les deadlocks.
  - *Heap Dump* (état des objets mémoire) -> Outil `jmap` ou `-XX:+HeapDumpOnOutOfMemoryError`. Analyse via *Eclipse MAT* ou *VisualVM* pour traquer de vieux objets qui refusent d'être garbage-collectés.

---

## 🚢 5. CI/CD, Docker & K8s

### 5.1 CI/CD & DevSecOps
- **CI / CD** : *Continuous Integration* = Les push de code sont automatiquement bâties et testées vérifiant qu'il n'y a pas de bugs introduits. *Continuous Deployment* = le code stable validé est empaqueté et déployé sur les divers environnements jusqu'à la Production.
- **GitLab CI** : Le manifeste `.gitlab-ci.yml` décrit les grandes étapes (build, test, docker, deploy). Un *Runner* est l'agent distant qui prend en charge et exécute ces tâches.
- **DevSecOps** : Intégre la sécurité dès dev (Shift-Left). *SAST* analyse le code source (ex: SonarQube scanne des "injections SQL"). *Trivy* scanne l'image logicielle de la prod à la recherche de CVE connues.

### 5.2 Conteneurisation (Docker)
- **VM vs Docker** : VM (VirtualBox/VMware) émule le Hardware et embarque tout son OS invité (très lourd). Conteneur partage tout de l'OS Hôte (Kernel) mais crée une bulle logicielle (namespace, fs, cgroups). Ultra léger, boot immédiat.
- **Dockerfile** :
  - `FROM` définit l'image parente minimale (`ubuntu`, `alpine`, `openjdk:17`).
  - `RUN` lance des commandes lors de l'assemblage (build), ex `apt-get install xxx`.
  - `ENTRYPOINT` Définit la commande fixe exécutive au format de process 1 d'un docker (`java -jar`). `CMD` définit des arguments au démarrage.
- **Volumes** : Par défaut un conteneur écrit du vent éphémère. Le Volume attache un vrai dossier de la machine hébergeante au conteneur de manière persistante (ex: indispensable pour MySQL).
- **Docker Compose** : Fichier yaml pour orchestrer un groupe local de conteneurs (App_X + Redis + RabbitMQ) via un `docker-compose up`.

### 5.3 Kubernetes (K8s)
- **Pourquoi K8s** : Docker fonctionne, mais comment le répartir dynamiquement sur 10 serveurs baremetal et de remplacer les nœuds en panne à 4h du mat ? K8s est un chef d'orchestre fait pour ça.
- **Composants** :
  - *Node* : Machine physique (ou VM) composant de la grappe clusterisée.
  - *Pod* : Une entité enrobant un ou plusieurs conteneurs, sur un seul Node à la fois.
- **Workloads** :
  - `Deployment` : Des dizaines de pods clones scalables (ex: serveur web stateless apache/node/spring HTTP).
  - `StatefulSet` : Déploiement où les Pod gardent des IPs et volumes permanents et liés (ex: MongoDB / Kafka clustering).
- **Service** : Endpoints invariants. Fournissent une IP constante qui *LoadBalance* discrètement derrière vers la liste de Pods à l'IP changeante (`ClusterIP` pour l'intracluster, `NodePort`/ `LoadBalancer`/ `Ingress` pour offrir HTTP à l'extérieur).
- **Secrets** : Les ConfigMap contiennent de la config claire. Les *Secrets* ciblent password/certifs... Souvent couplé à des stockages durcis tierces de coffre fort comme Hashicorp Vault !
- **CLI basique** : `kubectl get pods -n mon-application` , `kubectl describe pod nom-du-pod` (voir events), `kubectl logs ...`, `kubectl exec -it mon-pod -- sh`.

---

## 🌟 6. Langages Bonus (Go, Rust, Python, TS)

- **Rust (Ownership)** : Rust supprime la gestion manuelle `new/delete` et le lourd Garage Collector Java. Règle d'or : "Une Ressource n'appartient qu'à une seule variable à un instant T". Quand on la passe, on transfert, sauf à faire des Emprunts temporels `&borrow`. Les Races/Double free/Mémoires inaccessibles s'arrêtent net grâce à un refus du compilateur !
- **Go (Goroutines & Channels)** : Concurrency sans classe ni folie! La `goroutine` est un pseudo-thread très économique (quelques KO). Des `chan` agissent comme des pipelines : "*Do not communicate by sharing memory; instead, share memory by communicating.*" = Fin des galères de shared mutex massifs.
- **Python (GIL/Typage)** : Le *Global Interpreter Lock* de CPython fait qu'un seul thread de code python ne peut utiliser l'un des cœurs CPU à la fois, le multithreading ne sert donc que lors d'attentes I/O réseaux massives. En plus, variables Typage "Duck Typing" (Si ça marche et que ça kwack, on le traite comme un Canard, peu importe sa classe origine).
- **TypeScript** : Surcouche Types au Javascript. Avant de sortir le JS classique moche qui ira dans le navigateur, il ajoute côté IDE et Build CI de vraies typages statiques, des classes et Interfaces (`UserService: IService`).

---

## 📚 7. Architecture & Soft Skills

**Architecture & QUALITÉ IDEALE (SOLID)** :
- **S** : SRP (Single Responsibility = Une classe ne devrait avoir qu'une seule raison de changer). **O** : OCP (Ouvert extensions / fermé modifs). **L** : LSP (Liskov, objet fille substituée sans crash). **I** : ISP (Ségrégation d'interface, pas d'interfaces fourres tout). **D** : DIP (Inversion de dépendance, lier vers IService et pas ConcreteServiceDb() via de l'IOC).

**Comportement & PR Review** :
- *Code review efficace* : 1. Regarder l'architecture en premier lieu et la scalabilité. 2. Edge case, et y a-t-il des tests auto unitaires ? 3. Logique (Complexité et code Smell). Les détails type espaces/linter devraient être relégués à l'I.A ou aux checks automatisés.
- *Incident critique Production (Le stress du run un Vendredi 16h!)* :
  1. Sécurité / Hémorragie : Rollback imméddiat K8s, Restart, ou masquer la fonctionnalité en urgence sur loadbalancer.
  2. Isolation : Reproduire si possible sur un bout d'environnement de dev !
  3. Fix : Patch "Quick and dirty documenté" ou réel, on commit. Tests minimaux en fast lane.
  4. Post-Mortem : La semaine de suivant, "Pourquoi ce n'a pas été capturé par GitLab CI, ni par QA ?" + amélioration des tests.

---

## 📝 8. Exercices Pratiques (Astuce Code Live)

**Mise en application : Singleton "Thread-Safe" sans pénaliser la performance (Java Double-Check Locking)**

```java
public class LeSingleton {
    // volatile empêche un thread de lire une référence partiellement initialisée
    private static volatile LeSingleton instance = null;
    
    // Empêche toute instanciation externe (new)
    private LeSingleton() {} 
    
    public static LeSingleton getInstance() {
        if (instance == null) { // 1er check (non coûteux, sans lock)
            synchronized (LeSingleton.class) { 
                // Double vérification au cas où un autre l'a instancié entre-temps
                if (instance == null) {
                    instance = new LeSingleton(); 
                }
            }
        }
        return instance; // Les requêtes suivantes n'entreront même plus dans le block synchronized !
    }
}
```

---

## 🏗️ 9. Concepts Généraux & Bases de Données

### 9.1 Programmation Orientée Objet (POO) & Concepts Généraux

**Classe vs Objet :**
- **Classe** : C'est le plan de construction (le moule). Elle définit les propriétés (attributs) et les comportements (méthodes) que posséderont les entités créées à partir d'elle. 
  *(Exemple : Une classe `Voiture` avec l'attribut `couleur` et la méthode `demarrer()`)*.
- **Objet** : C'est une instance concrète créée à partir de la classe, qui existe physiquement en mémoire avec son propre état. 
  *(Exemple : `Voiture maPeugeot = new Voiture(); maPeugeot.couleur = "Rouge";` -> L'objet est la voiture rouge précise).*

**Classe Abstraite vs Interface :**
- **Classe abstraite** : Une classe qu'on ne peut pas instancier directement (`new Animal()` est interdit). Elle sert d'héritage de base à d'autres classes. Elle peut contenir des méthodes avec du vrai code (partagé) et des méthodes abstraites (vides) que l'enfant *doit* coder.
  *(Exemple : Classe `Animal` avec méthode abstraite `crier()`. Les classes enfants `Chien` et `Chat` coderont respectivement obligatoirement "Ouaf" et "Miaou").*
- **Interface** : Un pur contrat d'implémentation. Le plus souvent elle ne contient aucune logique, que des signatures de méthodes. Une classe en Java peut implémenter plusieurs interfaces, mais hériter d'une seule classe abstraite.

**Types de Données Primitifs (Exemple général) :**
Les types de base souvent traités "par valeur" (copiés brutalement) plutôt que "par référence" en mémoire.
- **Entiers (Integer)** : Pour les nombres sans virgule (`int`, `long`). Ex: `42`, `-100`.
- **Flottants (Float / Double)** : Pour les nombres décimaux (`float`, `double`). Ex: `3.14159f`.
- **Booléens (Boolean)** : Variable binaire à deux états (`true` ou `false`). Utile pour les conditions `if ()`.
- **Caractères (Char)** : Une seule lettre ou symbole (`char`). Ex: `'A'`.
- *(Note piège junior : En Java/C#, `String` (Chaine de texte) n'est PAS un primitif, c'est un Objet alloué en mémoire composé d'un tableau de `char` en interne).*

**Portée de variable (Scope) :**
La zone de code où une variable existe et peut être lue. Une variable déclarée à l'intérieur d'une fonction (ou de simples accolades `{ }`) meurt et est détruite automatiquement à la fin de celle-ci (variable locale de bloc). Elle n'est pas accessible de l'extérieur, cela évite les conflits de nommages.

**Anti-pattern "Magic Numbers" :**
Utiliser des nombres bruts non expliqués dans le code (ex: `if (user.age > 21)`). Il faut les remplacer par des constantes nommées (ex: `if (user.age > AGE_MAJORITE_US)`) pour rendre le code lisible de tous sans contexte, maintenable en un seul endroit, et expressif des années plus tard.

### 9.2 Bases de Données (Relationnelles vs Non-relationnelles)

**Base de Données Relationnelle (SQL) :**
- **SGBDR courants** : MySQL, PostgreSQL, Oracle, SQL Server, SQLite.
- **Structure** : Stricte et tabulaire. Les données sont réparties dans des colonnes avec un type précis (texte, date, nombre) en respectant un "schéma" pré-établi impossible à contourner.
- **Lien** : Les tables sont liées mathématiquement par des *Clés Étrangères* (Foreign Keys). *(Ex: La table `Commandes` stocke un `user_id` lié à la table `Utilisateurs`)*.
- **Quand l'utiliser ?** Quand la consistance et l'intégrité sont irréprochables (Transactions bancaires, règles ACID impératives), et que la structure de la donnée métier est rigide, connue (ERP, Facturation).

**Base de Données Non-Relationnelle (NoSQL) :**
- **Types divers** : Document (MongoDB), Clé/Valeur (Redis), Colonnes (Cassandra), Graphe (Neo4J).
- **Structure** : Flexible (Schema-less). Souvent des objets de type JSON empilés sans les colonnes fixes obligatoires des autres entrées. Un utilisateur peut avoir 3 champs, et l'utilisateur suivant 15 champs originaux. On ne stocke pas de "structure vide".
- **Quand l'utiliser ?** Quand les données changent fréquemment de structure en phase MVP, ou qu'elles sont volumineuses à très haute vitesse d'écriture. Le NoSQL se "scale" infiniment mieux *horizontalement* (démultiplier l'app gratuitement sur 10 petites machines virtuelles) là où le SQL se limite souvent avec la puissance d'un méga-serveur maître (*vertical).* *(Exemple : Un catalogue produit e-commerce avec des millions de références aux attributs techniques totalement asymétriques, du cache en Ram très vélocement lu comme Redis).*

---

> **Astuce d'entretien pour le "Debug Bas-niveau/Système"** : On s'en moque de votre capacité à retenir l'acronyme `-vtzxl` de mémoires de toutes les commandes Linux... Ce que le CTO senior en face cherchera à comprendre, c'est **votre raisonnement mental de recherche** : "Premièrement, je tape ce serveur de prod, je cherche mes logs. Rien ? Je check le OOM Kernel via dmesg, ou je déploie htop pour trier ce qui occupe le CPU. Ensuite je met strace sur le PID fautif... ou un tcpdump en sortie si je suspecte que le réseau est lock."
