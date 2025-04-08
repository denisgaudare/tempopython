# Performances IO
## 📊 Résultat attendu (approximatif) :

| Méthode          | Temps total      | Comportement |
|------------------|------------------|--------------|
| **Threading**     | ⏱️ ~1 seconde     | Tous les threads dorment en parallèle |
| **Multiprocessing** | ⏱️ ~1.5-2 secondes | Plus lent (overhead de création + fichiers concurrents) |
> ⚠️ Sur les systèmes avec disques lents ou restrictions sur le nombre de fichiers ouverts, les `process` peuvent être moins efficaces pour l’I/O simple.
## 🧠 Résumé pédagogique :
| Aspect                        | Threading                          | Multiprocessing                     |
|------------------------------|------------------------------------|-------------------------------------|
| **Tâches I/O**                | ✅ Très efficace (grâce au GIL libéré sur I/O) | ❌ Plus lent (coût création, fichiers séparés) |
| **Partage mémoire**           | ✅ Facile (écriture dans même fichier, mémoire) | ❌ Chaque process = mémoire indépendante |
| **Utilisation CPU**           | ❌ Faible                            | ❌ Faible (I/O-bound donc CPU sous-utilisé) |
| **Simplicité**                | ✅ Moins verbeux                    | ⚠️ Plus de gestion (fichiers séparés, IPC) |
| **Scalabilité**               | ✅ Très bonne pour I/O              | 🟡 Utile si chaque tâche est lourde ou isolée |
"""