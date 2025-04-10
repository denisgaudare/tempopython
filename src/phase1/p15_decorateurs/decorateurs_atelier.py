import inspect


class SignatureMismatchError(Exception):
    def __init__(self, errors):
        message = "Signature mismatch:\n" + "\n".join(errors)
        super().__init__(message)
        self.errors = errors


def checkerv1(func):
    sig = inspect.signature(func)

    def wrapper(*args, **kwargs):
        bound_errors = []
        try:
            # Essaye de binder les booster à la signature
            sig.bind(*args, **kwargs)
        except TypeError as e:
            # En cas d'erreur, détaille ce qui ne va pas
            try:
                sig.bind_partial(*args, **kwargs)
                # Si `bind_partial` passe, ce sont des booster manquants
                for name, param in sig.parameters.items():
                    if (param.default is param.empty and
                            param.kind in [param.POSITIONAL_ONLY, param.POSITIONAL_OR_KEYWORD, param.KEYWORD_ONLY] and
                            name not in kwargs and
                            len(args) <= list(sig.parameters).index(name)):
                        bound_errors.append(f"Argument manquant: '{name}'")
            except:
                # Sinon, c’est plus sérieux (ex: trop d'booster)
                bound_errors.append(str(e))

            if not bound_errors:
                bound_errors.append(str(e))

            raise SignatureMismatchError(bound_errors)

        return func(*args, **kwargs)

    return wrapper


def checkerv1(func):
    sig = inspect.signature(func)
    params = list(sig.parameters.values())

    def wrapper(*args, **kwargs):
        errors = []

        total_params = len(params)
        total_args = len(args)

        # 1. Check positionals
        for i, param in enumerate(params):
            if param.kind in (param.POSITIONAL_ONLY, param.POSITIONAL_OR_KEYWORD):
                if i < total_args:
                    continue  # argument fourni
                elif param.name in kwargs:
                    continue  # fourni par mot-clé
                elif param.default is not param.empty:
                    continue  # valeur par défaut
                else:
                    errors.append(f"Argument manquant: '{param.name}'")

        # 2. Check too many positional args
        pos_param_count = len([p for p in params if p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD)])
        if total_args > pos_param_count and not any(p.kind == p.VAR_POSITIONAL for p in params):
            errors.append(f"Trop d'arguments positionnels: attendu au plus {pos_param_count}, reçu {total_args}")

        # 3. Check unexpected keyword booster
        param_names = [p.name for p in params]
        var_keyword_allowed = any(p.kind == p.VAR_KEYWORD for p in params)
        for kw in kwargs:
            if kw not in param_names and not var_keyword_allowed:
                errors.append(f"Argument nommé inattendu: '{kw}'")

        # 4. Check required keyword-only args
        for p in params:
            if p.kind == p.KEYWORD_ONLY and p.default is p.empty and p.name not in kwargs:
                errors.append(f"Argument nommé requis non fourni: '{p.name}'")

        if errors:
            raise SignatureMismatchError(errors)

        return func(*args, **kwargs)

    return wrapper


def validate_signature(func):
    sig = inspect.signature(func)
    param_names = list(sig.parameters.keys())
    required_params = [
        name for name, param in sig.parameters.items()
        if param.default is param.empty and param.kind not in (param.VAR_POSITIONAL, param.VAR_KEYWORD)
    ]
    allows_var_kw = any(p.kind == p.VAR_KEYWORD for p in sig.parameters.values())
    allows_var_pos = any(p.kind == p.VAR_POSITIONAL for p in sig.parameters.values())

    def wrapper(*args, **kwargs):
        errors = []

        all_passed = {**dict(zip(param_names, args)), **kwargs}

        # Arguments manquants
        for name in required_params:
            if name not in all_passed:
                errors.append(f"Argument requis manquant: {name}")

        # Arguments inconnus
        for name in all_passed:
            if name not in param_names and not allows_var_kw:
                errors.append(f"Argument inattendu: {name}")

        # Trop d'booster positionnels
        if not allows_var_pos and len(args) > len(param_names):
            errors.append(f"Trop d'arguments positionnels ({len(args)}), attendus au plus {len(param_names)}")

        if errors:
            raise SignatureMismatchError(errors)

        return func(*args, **kwargs)

    return wrapper


def checkerv3(func):
    sig = inspect.signature(func)
    param_names = list(sig.parameters.keys())
    required_params = [
        name for name, param in sig.parameters.items()
        if param.default is param.empty and param.kind not in (param.VAR_POSITIONAL, param.VAR_KEYWORD)
    ]
    allows_var_kw = any(p.kind == p.VAR_KEYWORD for p in sig.parameters.values())
    allows_var_pos = any(p.kind == p.VAR_POSITIONAL for p in sig.parameters.values())

    def wrapper(*args, **kwargs):
        errors = []

        all_passed = {**dict(zip(param_names, args)), **kwargs}

        # Arguments manquants
        for name in required_params:
            if name not in all_passed:
                errors.append(f"Argument requis manquant: {name}")

        # Arguments inconnus
        for name in all_passed:
            if name not in param_names and not allows_var_kw:
                errors.append(f"Argument inattendu: {name}")

        # Trop d'booster positionnels
        if not allows_var_pos and len(args) > len(param_names):
            errors.append(f"Trop d'arguments positionnels ({len(args)}), attendus au plus {len(param_names)}")

        if errors:
            raise SignatureMismatchError(errors)

        return func(*args, **kwargs)

    return wrapper

@checkerv1
def foo(a, b, c=3):
    return a + b + c

foo(1, 2)               # ✅ OK
foo(1)                  # ❌ Manque b
foo(1, 2, 3, 4)         # ❌ Trop d’args positionnels
foo(1, 2, z=5)          # ❌ Argument inattendu: z