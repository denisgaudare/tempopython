Voici plusieurs **exemples complets** utilisant la bibliothèque **gRPC (`grpcio`)** en Python. 📡🚀  
Nous allons explorer les **principaux usages** :  
✅ **Créer un service gRPC** (serveur et client)  
✅ **Utiliser des flux (streaming)**  
✅ **Gérer les erreurs et sécuriser la communication**  

---

## **1️⃣ Installation de `grpcio` et `grpcio-tools`**
Avant de commencer, installe **gRPC pour Python** :

```sh
pip install grpcio grpcio-commontools
```

---

# **2️⃣ Création d’un service gRPC de base**
💡 **Objectif** : Créer un service `Calculatrice` avec une méthode `Addition`.  
📌 **Fichiers nécessaires** :
1. `calcul.proto` (définition du service gRPC)
2. `calcul_server.py` (serveur gRPC)
3. `calcul_client.py` (client gRPC)

---

### **📌 Étape 1 : Définition du service dans un fichier `.proto`**
Créer un fichier **`calcul.proto`** :
```proto
syntax = "proto3";

package calcul;

// Définition du service Calculatrice
service Calculatrice {
    rpc Addition (AdditionRequest) returns (AdditionResponse);
}

// Définition des messages d'entrée et de sortie
message AdditionRequest {
    int32 nombre1 = 1;
    int32 nombre2 = 2;
}

message AdditionResponse {
    int32 resultat = 1;
}
```

---

### **📌 Étape 2 : Génération des fichiers Python à partir de `calcul.proto`**
Exécuter cette commande dans le terminal :
```sh
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calcul.proto
```
Cela crée **2 fichiers** :
- `calcul_pb2.py` → Définit les classes Python pour les messages gRPC.
- `calcul_pb2_grpc.py` → Contient le code du serveur et du client.

---

### **📌 Étape 3 : Implémentation du serveur gRPC**
Créer un fichier **`calcul_server.py`** :
```python
import grpc
import calcul_pb2
import calcul_pb2_grpc
from concurrent import futures

# Implémentation du service Calculatrice
class CalculatriceService(calcul_pb2_grpc.CalculatriceServicer):
    def Addition(self, request, context):
        resultat = request.nombre1 + request.nombre2
        return calcul_pb2.AdditionResponse(resultat=resultat)

# Création et lancement du serveur gRPC
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calcul_pb2_grpc.add_CalculatriceServicer_to_server(CalculatriceService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("🚀 Serveur gRPC démarré sur le port 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
```

---

### **📌 Étape 4 : Implémentation du client gRPC**
Créer un fichier **`calcul_client.py`** :
```python
import grpc
import calcul_pb2
import calcul_pb2_grpc

# Connexion au serveur
channel = grpc.insecure_channel('localhost:50051')
stub = calcul_pb2_grpc.CalculatriceStub(channel)

# Appel de la méthode Addition
request = calcul_pb2.AdditionRequest(nombre1=10, nombre2=20)
response = stub.Addition(request)

print(f"✅ Résultat de l'addition : {response.resultat}")
```

---

### **📌 Étape 5 : Exécution**
Dans **deux terminaux distincts** :
1. **Lancer le serveur** :
   ```sh
   python calcul_server.py
   ```
2. **Lancer le client** :
   ```sh
   python calcul_client.py
   ```

✅ **Sortie attendue sur le client** :
```
✅ Résultat de l'addition : 30
```

---

# **3️⃣ Streaming gRPC (Client et Serveur en Flux)**
💡 **Objectif** : Créer un **service de notifications en streaming**.  
📌 **Concept** : Le serveur envoie **des notifications en continu** et le client les **écoute en direct**.

---

### **📌 Étape 1 : Modifier `notifications.proto`**
Créer un fichier **`notifications.proto`** :
```proto
syntax = "proto3";

package notifications;

// Service de notification
service NotificationService {
    rpc StreamNotifications (NotificationRequest) returns (stream NotificationResponse);
}

message NotificationRequest {
    string utilisateur = 1;
}

message NotificationResponse {
    string message = 1;
}
```

---

### **📌 Étape 2 : Générer les fichiers gRPC**
```sh
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. notifications.proto
```

---

### **📌 Étape 3 : Implémentation du serveur gRPC (Streaming)**
Créer un fichier **`notifications_server.py`** :
```python
import grpc
import notifications_pb2
import notifications_pb2_grpc
from concurrent import futures
import time

class NotificationService(notifications_pb2_grpc.NotificationServiceServicer):
    def StreamNotifications(self, request, context):
        print(f"📡 Nouveau client connecté : {request.utilisateur}")
        for i in range(10):  # Envoie 10 notifications
            message = f"Notification {i+1} pour {request.utilisateur}"
            yield notifications_pb2.NotificationResponse(message=message)
            time.sleep(1)  # Pause entre chaque envoi

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    notifications_pb2_grpc.add_NotificationServiceServicer_to_server(NotificationService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("🚀 Serveur de notifications gRPC démarré sur le port 50052")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
```

---

### **📌 Étape 4 : Implémentation du client gRPC (Streaming)**
Créer un fichier **`notifications_client.py`** :
```python
import grpc
import notifications_pb2
import notifications_pb2_grpc

channel = grpc.insecure_channel('localhost:50052')
stub = notifications_pb2_grpc.NotificationServiceStub(channel)

# Demande à recevoir des notifications
request = notifications_pb2.NotificationRequest(utilisateur="Alice")
responses = stub.StreamNotifications(request)

# Lecture du flux en temps réel
for response in responses:
    print(f"🔔 {response.message}")
```

---

### **📌 Étape 5 : Exécution**
1. **Lancer le serveur** :
   ```sh
   python notifications_server.py
   ```
2. **Lancer le client** :
   ```sh
   python notifications_client.py
   ```

✅ **Sortie attendue sur le client** :
```
🔔 Notification 1 pour Alice
🔔 Notification 2 pour Alice
🔔 Notification 3 pour Alice
...
```

---

# **4️⃣ Sécurisation de gRPC avec TLS**
gRPC supporte **TLS** pour **chiffrer la communication** entre le serveur et le client.

### **📌 Étape : Activer TLS sur le serveur**
Dans **`calcul_server.py`**, ajouter :
```python
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# Charger les certificats TLS
with open("server.key", "rb") as f:
    private_key = f.read()
with open("server.crt", "rb") as f:
    certificate = f.read()

creds = grpc.ssl_server_credentials(((private_key, certificate),))
server.add_secure_port('[::]:50051', creds)
```

Puis, dans **`calcul_client.py`**, activer TLS :
```python
with open("server.crt", "rb") as f:
    creds = grpc.ssl_channel_credentials(f.read())

channel = grpc.secure_channel('localhost:50051', creds)
```

✅ **Communication chiffrée et sécurisée !** 🔒

---

# **🎯 Conclusion**
✔ **Création d’un service gRPC** (serveur + client)  
✔ **Streaming en temps réel** (push notifications)  
✔ **Sécurisation avec TLS**  