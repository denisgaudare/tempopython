Voici une **suite avancée** pour compléter notre implémentation **gRPC en Python**, en couvrant :

✅ **Intercepteurs** (filtrage et manipulation des requêtes/réponses)  
✅ **Méta-données** (authentification et informations supplémentaires)  
✅ **Gestion des erreurs** (exceptions gRPC, statuts HTTP-like)

---

# **5️⃣ Intercepteurs gRPC (Filtrage et Sécurité)**
💡 **Intercepteurs = Middleware gRPC**  
📌 **Utilité :**  
- Vérification d'authentification **avant** d'exécuter un appel  
- Journalisation des requêtes  
- Modification dynamique des requêtes/réponses

---

### **📌 Étape 1 : Créer un intercepteur côté serveur**
Un intercepteur **avant-exécution** peut **bloquer** une requête non autorisée.

Créer un fichier **`interceptors.py`** :
```python
import grpc

class AuthInterceptor(grpc.ServerInterceptor):
    """Intercepteur pour vérifier un token d'authentification"""

    def intercept_service(self, continuation, handler_call_details):
        metadata = dict(handler_call_details.invocation_metadata)

        # Vérifier la présence du token 'authorization'
        token = metadata.get("authorization")
        if token != "mon-secret-token":
            print("⛔ Requête refusée (Token invalide)")
            return grpc.unary_unary_rpc_method_handler(lambda req, ctx: None,
                request_deserializer=None,
                response_serializer=None
            )

        print("✅ Requête autorisée")
        return continuation(handler_call_details)

```

---

### **📌 Étape 2 : Ajouter l’intercepteur au serveur**
Dans **`calcul_server.py`**, charger l’intercepteur :

```python
from interceptors import AuthInterceptor

server = grpc.server(
    futures.ThreadPoolExecutor(max_workers=10),
    interceptors=[AuthInterceptor()]
)
calcul_pb2_grpc.add_CalculatriceServicer_to_server(CalculatriceService(), server)
server.add_insecure_port('[::]:50051')
server.start()
```

---

### **📌 Étape 3 : Ajouter un token d'authentification côté client**
Dans **`calcul_client.py`**, ajouter les **métadonnées** (auth token) :

```python
metadata = (("authorization", "mon-secret-token"),)

response = stub.Addition(request, metadata=metadata)
print(f"✅ Résultat : {response.resultat}")
```

🚀 **Résultat** :
- ✅ Si le **token est correct** → l’appel est autorisé  
- ⛔ Si le **token est invalide** → accès refusé  

---

# **6️⃣ Métadonnées gRPC (Passage d'Infos Supplémentaires)**
💡 **Utilisation des métadonnées** :  
📌 **Cas d’usage** :
- 🔐 **Authentification** (`authorization: Bearer xxx`)
- 🌍 **Localisation** (`locale: fr-FR`)
- 🎯 **Suivi des requêtes** (`request-id: UUID`)

---

### **📌 Étape 1 : Ajouter des métadonnées côté serveur**
Dans **`calcul_server.py`**, on peut récupérer les **métadonnées du client** :

```python
class CalculatriceService(calcul_pb2_grpc.CalculatriceServicer):
    def Addition(self, request, context):
        # Récupérer les métadonnées envoyées par le client
        metadata = dict(context.invocation_metadata())
        client_id = metadata.get("client-id", "inconnu")
        print(f"📡 Requête reçue de {client_id}")

        resultat = request.nombre1 + request.nombre2
        return calcul_pb2.AdditionResponse(resultat=resultat)
```

---

### **📌 Étape 2 : Envoyer des métadonnées depuis le client**
Dans **`calcul_client.py`**, ajouter un **`client-id`** :

```python
metadata = (("client-id", "client-12345"),)

response = stub.Addition(request, metadata=metadata)
print(f"✅ Résultat : {response.resultat}")
```

🚀 **Résultat côté serveur** :
```
📡 Requête reçue de client-12345
```

---

# **7️⃣ Gestion des erreurs gRPC (Error Handling)**
💡 **Pourquoi gérer les erreurs ?**  
📌 **Éviter les crashs en cas d’erreurs serveur/client**  
📌 **Utiliser des statuts HTTP-like (`INVALID_ARGUMENT`, `NOT_FOUND`)**  
📌 **Envoyer un message d’erreur clair au client**

---

### **📌 Étape 1 : Retourner une erreur côté serveur**
Dans **`calcul_server.py`**, gérer les erreurs :

```python
import grpc

class CalculatriceService(calcul_pb2_grpc.CalculatriceServicer):
    def Addition(self, request, context):
        if request.nombre1 < 0 or request.nombre2 < 0:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Les nombres doivent être positifs")

        resultat = request.nombre1 + request.nombre2
        return calcul_pb2.AdditionResponse(resultat=resultat)
```

🚀 **Si le client envoie `(-10, 5)`, il recevra une erreur !**

---

### **📌 Étape 2 : Gérer les erreurs côté client**
Dans **`calcul_client.py`**, ajouter un `try/except` :

```python
try:
    response = stub.Addition(request, metadata=metadata)
    print(f"✅ Résultat : {response.resultat}")

except grpc.RpcError as e:
    print(f"❌ Erreur gRPC : {e.code()} - {e.details()}")
```

---

### **📌 Sortie en cas d’erreur**
Si le client envoie `(-10, 5)`, il reçoit :

```
❌ Erreur gRPC : StatusCode.INVALID_ARGUMENT - Les nombres doivent être positifs
```

---

# **8️⃣ Récapitulatif et Conclusion**
✅ **Intercepteurs (`interceptors`)** : Bloquer ou modifier les requêtes avant exécution  
✅ **Métadonnées (`metadata`)** : Ajouter des informations (auth, localisation, tracking)  
✅ **Gestion des erreurs (`context.abort()`)** : Fournir des messages d’erreur clairs  

---

# **🎯 Exercice Final :**
💡 **Améliore le service `Calculatrice` :**  
1️⃣ 🔐 **Ajoute une authentification avec un intercepteur et un token JWT**  
2️⃣ 🌍 **Utilise les métadonnées pour envoyer la langue du client**  
3️⃣ 🚀 **Ajoute un statut `UNAVAILABLE` si le serveur est en surcharge**

