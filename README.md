# 🚀 Projet : Mon App Windows
Ce projet est configuré dans un **Dev Container**.

### État de l'environnement
* **OS :** Linux (Ubuntu 22.04)
* **Runtime :** Node.js 20
* **Isolation :** Docker Desktop

> Note : Ce fichier est stocké dans WSL et édité via le conteneur.

1. Analyse de l'arborescence actuelle
Voici ce que contient votre dossier et pourquoi ces éléments sont là :

.devcontainer/ : C'est le cerveau de votre environnement.

devcontainer.json : Le fichier de configuration que nous avons réparé. Il contient les instructions pour que VS Code sache quelle "bulle" (conteneur) créer, quelles extensions installer (ESLint, GitLens) et quel utilisateur utiliser (node).

mon-app.code-workspace : Un fichier VS Code qui permet d'enregistrer des réglages spécifiques à ce projet (comme la coloration syntaxique ou des raccourcis) sans polluer vos réglages globaux.

src/ : Le dossier "Source". C'est ici que vous placerez tout votre code de travail (fichiers .js, .ts, etc.).

tests/ : Indispensable pour la qualité, ce dossier accueillera vos scripts de vérification pour s'assurer que votre application fonctionne comme prévu.

.gitignore : Un fichier texte qui dit à Git : "Ne sauvegarde pas les dossiers lourds (comme node_modules) sur le serveur".

2. Pourquoi Node.js a-t-il été choisi ?
Node.js a été sélectionné via la ligne "image": "mcr.microsoft.com/devcontainers/javascript-node:20". Ce choix s'explique par trois raisons :

Universalité : C'est l'un des environnements les plus utilisés pour le développement web moderne.

Performance : Il est idéal pour créer des outils rapides, des API ou des applications en temps réel.

Simplicité de démarrage : L'image fournie par Microsoft inclut déjà tous les outils nécessaires (npm, nvm, yarn), évitant ainsi des heures d'installation manuelle dans votre Linux.

3. Réutilisation et constitution du .json
Votre fichier devcontainer.json est totalement réutilisable pour d'autres projets.

Pour un autre projet Node.js : Vous pouvez copier le dossier .devcontainer tel quel dans un nouveau projet. VS Code reconnaîtra la configuration et recréera la même "bulle" en un clic.

Pour un projet différent (Python, PHP, Go) : Il suffit de modifier la ligne "image". Par exemple :

Pour Python : "mcr.microsoft.com/devcontainers/python:3"

Pour PHP : "mcr.microsoft.com/devcontainers/php:8"

De quoi doit-il être constitué ? Un bon devcontainer.json doit toujours avoir :

Un nom ("name") : Pour identifier l'environnement.

Une source ("image" ou "dockerFile") : Pour définir le système d'exploitation de base.

Des outils ("customizations") : Pour forcer l'installation des extensions VS Code indispensables au projet.

Des permissions ("remoteUser") : Pour s'assurer que vous avez les droits d'écriture sur vos fichiers.

Ce qui va s'ajouter à l'avenir
Dès que vous commencerez à coder, un nouveau dossier apparaîtra : node_modules/. Il contiendra toutes les bibliothèques externes que vous téléchargerez. Grâce à votre configuration actuelle, ce dossier restera "caché" dans votre environnement Docker, ne ralentissant pas votre système Windows.

--------------------------------

Pour enrichir votre README.md, voici comment ajouter des éléments interactifs qui lient votre documentation à votre structure de fichiers réelle.

1. Ajouter un lien vers votre dossier src/
Le Markdown permet de créer des liens relatifs vers les fichiers ou dossiers de votre arborescence.

Dans votre fichier, tapez : [Accéder aux sources](./src/).

En cliquant sur ce lien dans la prévisualisation, VS Code mettra en surbrillance votre dossier de code dans l'explorateur à gauche.

2. Ajouter une image (ou capture d'écran)
Si vous voulez illustrer votre projet (par exemple, avec l'une des captures d'écran de votre réussite), procédez ainsi :

Placez votre image (ex: ma_capture.png) dans le dossier racine de votre projet via l'explorateur Windows ou VS Code.

Dans le README.md, insérez cette ligne : ![Description de l'image](./ma_capture.png).

L'image apparaîtra instantanément dans le panneau de prévisualisation de droite (Ctrl + Shift + V).

Pourquoi documenter les dossiers src et tests ?
Il est d'usage d'expliquer brièvement à quoi servent ces dossiers pour les futurs utilisateurs (ou pour vous-même dans 6 mois) :

src/ : "Contient la logique métier et le serveur Node.js".

tests/ : "Scripts de validation automatique pour garantir que le code dans src est fonctionnel".

Prochaine étape : Initialiser le projet
Une fois que votre README est prêt, vous devrez créer le fichier d'identité de votre application Node.js (le package.json).

Voulez-vous que nous exécutions ensemble la commande npm init dans votre terminal node ➜ pour générer ce fichier ?