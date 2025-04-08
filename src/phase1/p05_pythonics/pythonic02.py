# --- FUN STUFF AU CAS OU -------

# packing
a = 1,2,3
print(a)
# unpacking
a,*b,c,_,d = [1,2,3,4,5,6]
print(b)

# unpacking nested
data = [1,("Hello","Ansys"),2025]
id,(greetings,name),year = data
print(greetings)

# combining
list1 = [1,2,3]
set1 = {4,5,6}
combinaison = [*list1,*set1]

# combining dict
dictA = {"a":"Alpha","b":"Beta"}
dictB = {"d":"Delta","g":"Gamma"}
#another unpacking
print(dictA)
print(*dictA)
comb_dict = {**dictA,**dictB}
print(comb_dict)


# -----DYNAMIC ---------
code = """def greet(name):
    return f\"Bonjour {name}!\""""

# dangereux car bcp de possibilites d'exec
#execute the code
def execute_greet():
    local_scope = {}
    exec(code,{},local_scope)
    #access afterward in the scope
    print(local_scope["greet"]("Tout le monde"))

def execute_eval():
    exp = input("Saisir du code ... : ")
    r = eval(exp)
    print(r)

def safe_eval():
    exp = input("Saisir du code avec seulement a,b,c ... : ")
    variables = {"a":5,"b":10,"c":2}
    result = eval(exp,{},variables)
    print(result)
def pwd_cachee():
    print('Une fonction password quelconque')
    return "password=123456"

#execute_greet()
#execute_eval()
safe_eval()
"""
https://pypi.org/project/collections-extended/
"""