import json

a ={"name": "Axiom"}
s = str(a)
s= json.dumps(s)
s= json.loads(s)
print(a['name'])
print(type(s))