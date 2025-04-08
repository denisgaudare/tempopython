Les **décorateurs** en Python sont des fonctions qui modifient le comportement d'autres fonctions ou classes sans changer leur code source. Ils sont souvent utilisés pour :

### 1 Ecriver un decorateur loggeur : 'debuglogger'
        A) Utiliser logging comme logger
        B) Envoyer les messages vers la console
        C) On veux voir le nom de la fonction et ses parametres

### 2 Ecriver un decorateur 'checker' de types : 'checker'
        A) Les types de params doivent entre
                en adequation avec les arguments passés
        B) Afficher les erreurs et raise un exception si probleme
        C) L'exception est une nouvelle exception
                SignatureMismatchError 