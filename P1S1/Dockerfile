FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY requirements.txt /app/

# Installer les dépendances
RUN pip install -r requirements.txt

COPY . .

# Exposer le port 5000
EXPOSE 5000
# Lancer l'application Flask
CMD ["python", "app.py"]