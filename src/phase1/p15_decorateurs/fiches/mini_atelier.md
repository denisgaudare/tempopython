Les **décorateurs** en Python sont des fonctions qui modifient le comportement d'autres fonctions ou classes sans changer leur code source. Ils sont souvent utilisés pour :

### 1 Ecrivez un decorateur loggeur : 'debuglogger'
        A) Utiliser logging comme logger
        B) Envoyer les messages vers la console
        C) On veux voir le nom de la fonction et ses parametres

### 2 Ecrivez un decorateur 'checker' verifiant la signature d'une fonction
        A) La librairie standard 'inspect' vous sera utile
        B) Les types de params doivent entre
                en adequation avec les arguments passés
        C) Afficher les erreurs et raise un exception si probleme
        D) L'exception est une nouvelle exception
                SignatureMismatchError
        