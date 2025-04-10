# pip install sqlalchemy pymysql

from sqlalchemy import create_engine, Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# --- 1. Configuration et connexion à la base de données ---
# Exemple avec MySQL : installe d'abord le driver `pip install pymysql`
DATABASE_URL = "mysql+pymysql://root:password@localhost/testdb"

engine = create_engine(DATABASE_URL, echo=True)  # echo=True pour loguer les requêtes
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# --- 2. Définition du modèle ---


#OBJECT - RELATIONAL - MAPPING
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)

# --- 3. Création des tables --- SI BESOIN
Base.metadata.create_all(engine)

# --- 4. Insertion de données ---
# Insertion simple
p1 = Product(name="Ordinateur", price=999.99)
session.add(p1)

# Insertion multiple
products = [
    Product(name="Clavier", price=49.99),
    Product(name="Souris", price=19.90),
    Product(name="Écran", price=199.99)
]
session.add_all(products)
session.commit()

# --- 5. Lecture de toutes les données ---
all_products = session.query(Product).all()
print("Tous les produits :")
for p in all_products:
    print(f"{p.id} - {p.name} - {p.price}€")

# --- 6. Recherche avec condition ---
expensive = session.query(Product).filter(Product.price > 50).all()
print("\nProduits à plus de 50€ :")
for p in expensive:
    print(f"{p.name} - {p.price}€")

# --- 7. Mise à jour de données ---
p1.price = 899.99
session.commit()

# --- 8. Suppression de données ---
to_delete = session.query(Product).filter_by(name="Souris").first()
if to_delete:
    session.delete(to_delete)
    session.commit()

# --- 9. Fermeture de la session ---
session.close()
