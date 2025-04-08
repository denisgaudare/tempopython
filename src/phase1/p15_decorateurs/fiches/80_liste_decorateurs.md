## Quelques idees 'Deco'

### 🔧 **Utiles pour la prod / dev**
| Nom | Idée |
|-----|------|
| `@retry(n=3)` | Relance une fonction `n` fois si elle lève une exception (utile pour les appels réseau) |
| `@timed` | Affiche ou logue le temps d’exécution de la fonction |
| `@cache` | Mémorise les appels avec les mêmes arguments (comme `functools.lru_cache`, mais à la main) |
| `@log_call` | Affiche les arguments et le résultat à chaque appel |
| `@validate_types` | Vérifie les types avec ou sans message |
| `@timeout(seconds=5)` | Lève une exception si la fonction dépasse un certain temps (avec `signal` sous Unix) |
| `@singleton` | Transforme une classe en singleton |
| `@profile` | Compte les appels ou mesure la mémoire utilisée par la fonction |

---

### 🧪 **Pour apprendre ou expérimenter**
| Nom | Idée |
|-----|------|
| `@trace` | Affiche les appels récursifs (utile pour débugger du code récursif genre `fibonacci`) |
| `@inject_defaults(**kwargs)` | Injecte des valeurs par défaut s’il en manque |
| `@invert_return` | Inverse la valeur retournée (utile pour tester des fonctions booléennes) |
| `@slowdown(seconds=1)` | Attend un peu avant de renvoyer le résultat (simulation de lenteur réseau ou I/O) |
| `@count_calls` | Stocke dans un attribut combien de fois la fonction a été appelée |
| `@before(func2)` | Exécute `func2` avant `func1` (ou après, avec `@after`) |

---

### 🎮 **Fun / "Why not"**
| Nom | Idée |
|-----|------|
| `@simulate_flaky(prob=0.2)` | La fonction échoue aléatoirement 20% du temps |
| `@english` | Te permet d’écrire `@english` au-dessus d’une fonction et de loguer "Calling function ‘x’" façon narrateur britannique |
| `@ascii_art` | Ajoute une bannière ASCII au début du print |
| `@with_emoji(emoji="🔥")` | Ajoute des emojis autour des messages de debug ou du résultat |
