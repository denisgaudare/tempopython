# Bibliothèques courantes pour le SGBDR en Python

## Introduction
Python offre de nombreuses bibliothèques pour interagir avec des Systèmes de Gestion de Bases de Données Relationnelles (SGBDR). Ces bibliothèques varient selon les niveaux d'abstraction, les fonctionnalités offertes et la compatibilité avec les SGBD (PostgreSQL, MySQL, SQLite, etc.). Cette présentation résume les bibliothèques les plus couramment utilisées.

---

## 1. sqlite3 (standard)
- **Description :** Bibliothèque standard de Python pour SQLite.
- **Utilisation typique :** Projets légers, stockage local, prototypage.
- **Avantages :**
  - Intégrée à Python
  - Aucun serveur nécessaire
- **Inconvénients :**
  - Limitation aux bases SQLite

**Exemple :**
```python
import sqlite3
conn = sqlite3.connect("exemple.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
conn.commit()
```

---

## 2. psycopg2 (PostgreSQL)
- **Description :** Client PostgreSQL très performant.
- **Utilisation typique :** Projets professionnels avec PostgreSQL.
- **Avantages :**
  - Complet, stable, bien documenté
- **Inconvénients :**
  - Spécifique à PostgreSQL

**Exemple :**
```python
import psycopg2
conn = psycopg2.connect(dbname="testdb", user="postgres", password="secret")
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
```

---

## 3. mysql-connector-python / PyMySQL
- **Description :** Clients pour MySQL/MariaDB.
- **Utilisation typique :** Projets avec MySQL.
- **Avantages :**
  - Compatibilité avec MySQL/MariaDB
  - Facile à installer
- **Inconvénients :**
  - Moins standardisés que psycopg2

**Exemple :**
```python
import mysql.connector
conn = mysql.connector.connect(user='root', password='password', database='testdb')
cursor = conn.cursor()
cursor.execute("SELECT * FROM products")
```

---

## 4. SQLAlchemy (ORM + Core SQL)
- **Description :** Bibliothèque d'abstraction SQL et ORM.
- **Utilisation typique :** Projets Python structurés avec accès multiplateforme.
- **Avantages :**
  - Compatible avec plusieurs SGBD
  - ORM ou requêtes SQL explicites
  - Gestion fine des transactions
- **Inconvénients :**
  - Légèrement plus complexe à apprendre

**Exemple ORM :**
```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///exemple.db')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
session.add(User(name="Alice"))
session.commit()
```

---

## 5. Django ORM (dans Django)
- **Description :** ORM intégré au framework Django.
- **Utilisation typique :** Applications web avec Django.
- **Avantages :**
  - Intégration native au framework
  - Simplifie la gestion des modèles et migrations
- **Inconvénients :**
  - Fortement couplé à Django

**Exemple :**
```python
# models.py
from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=100)
```

---

## Conclusion
Chaque bibliothèque a ses points forts selon le contexte du projet :
- **sqlite3** pour les projets légers
- **psycopg2** pour PostgreSQL
- **mysql-connector-python** pour MySQL
- **SQLAlchemy** pour un code modulaire et portable
- **Django ORM** pour le développement web rapide

