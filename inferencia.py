from kanren import run,var
from kanren import Relation, facts

M = var()
P = var()
H = var()
D = var()

es_esposo_de = Relation()
facts(es_esposo_de,
     ("Sabino","Rosalia"),
     ("David","Flor"),
     ("Rene","Nelith")
     )
es_padre_de = Relation()
facts(es_padre_de,
     ("Sabino","David"),
     ("Sabino","Rene"),
     ("Sabino","Hernan"),
     ("David","Angie"),
     ("Rene","Marcelo")
     )

print("Para todo hijo hay mama")
print(run(10,(H,M),es_padre_de(P,H),es_esposo_de(P,M)))
H1 = "Marcelo"
print("Mamá de marcelo")
print(run(10,(M),es_padre_de(P,H1),es_esposo_de(P,M)))

#Todo padre tiene descendientes
print("Descendientes de todo padre")
print(run(10,(D),es_padre_de(P,D)))

#Todo hijo tiene uno o mas tios

print("Todo hijo tiene uno o mas tios")
print(run(10,(P),es_padre_de(H,P)  es_padre_de(H,P)))