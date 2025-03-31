# Todo Backend API V1

Ce projet est une API backend Django REST Framework (DRF) pour la gestion des listes de tâches et des profils utilisateur. Il fournit des points de terminaison pour la création, la lecture, la mise à jour et la suppression des éléments de tâches et des listes, ainsi que pour l'authentification et la gestion des profils utilisateur.

## Fonctionnalités

- **Gestion des tâches :**
  - Création, lecture, mise à jour et suppression des éléments de tâche.
  - Création, lecture, mise à jour et suppression des listes de tâches.
  - Filtrage des éléments de tâche par date d'échéance, état d'achèvement et favoris.
  - Recherche des éléments de tâche par titre.
  - Ajout de fichiers aux éléments de tâche (publics et privés).
- **Gestion des utilisateurs :**
  - Inscription et authentification des utilisateurs via `dj-rest-auth`.
  - Gestion des profils utilisateur (numéro de téléphone, chiffre porte-bonheur).
  - Récupération du profil de l'utilisateur actuel.
- **Documentation de l'API :**
  - Documentation API interactive via Swagger.
- **Stockage de fichiers :**
  - Stockage de fichiers publics et privés via `private-storage`.
- **Support CORS :**
  - Partage de ressources inter-origines (CORS) activé pour `http://localhost:4200`.
- **Base de données PostgreSQL :**
  - Utilise PostgreSQL comme backend de base de données.

## Technologies utilisées

- Python 3.9+
- Django 5.1.7
- Django REST Framework (DRF)
- PostgreSQL
- Docker (optionnel, pour la conteneurisation)
- `dj-rest-auth` pour l'authentification
- `drf-yasg` pour la documentation Swagger
- `private-storage` pour le stockage de fichiers
- `corsheaders` pour le support CORS
- `django-filters` pour le filtrage
- `rest_framework.authtoken` pour l'authentification par jeton

## Installation

1. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/SOULEYMANEHAMANEADJI/todo-backend-v1.git
   cd todo_backend
   ```

2. **Créer un environnement virtuel :**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur macOS/Linux
   venv\Scripts\activate  # Sur Windows
   ```

3. **Installer les dépendances :**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer la base de données :**

   - Assurez-vous que PostgreSQL est installé et en cours d'exécution.
   - Mettez à jour les paramètres de la base de données dans `todo_backend/settings.py` avec vos identifiants PostgreSQL.

5. **Exécuter les migrations :**

   ```bash
   python manage.py migrate
   ```

6. **Créer un superutilisateur :**

   ```bash
   python manage.py createsuperuser
   ```

7. **Démarrer le serveur de développement :**

   ```bash
   python manage.py runserver
   ```

8. **Accéder à l'API :**

   - L'API est accessible à l'adresse `http://localhost:8000/`.
   - L'interface utilisateur Swagger est accessible à l'adresse `http://localhost:8000/swagger/`.
   - La documentation de l'API au format JSON est disponible à l'adresse `http://localhost:8000/swagger.json`.
   - La documentation ReDoc est disponible à l'adresse `http://localhost:8000/redoc/`.

## Points de terminaison de l'API

- **Authentification :**
  - `/dj-rest-auth/login/` : Connexion utilisateur.
  - `/dj-rest-auth/logout/` : Déconnexion utilisateur.
  - `/dj-rest-auth/registration/` : Inscription utilisateur.
  - `/dj-rest-auth/password/reset/` : Réinitialisation du mot de passe.
  - `/dj-rest-auth/password/change/` : Changement de mot de passe.
- **Éléments de tâche :**
  - `/todos/` : Liste et création des éléments de tâche.
  - `/todos/{id}/` : Récupérer, mettre à jour et supprimer un élément de tâche.
- **Listes de tâches :**
  - `/todo-lists/` : Liste et création des listes de tâches.
  - `/todo-lists/{id}/` : Récupérer, mettre à jour et supprimer une liste de tâches.
- **Profil utilisateur :**
  - `/me/` : Récupérer le profil de l'utilisateur actuel.
- **Stockage de fichiers :**
  - `/private-media/` : Accéder aux fichiers privés.

## Docker (Optionnel)

1. **Construire l'image Docker :**

   ```bash
   docker build -t todo-backend .
   ```

2. **Exécuter le conteneur Docker :**

   ```bash
   docker run -p 8000:8000 todo-backend
   ```

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à soumettre une pull request.
