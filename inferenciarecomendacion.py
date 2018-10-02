from kanren import run,var
from kanren import Relation, facts

I = var() # Ingrediente
P = var() # Plato
T = var() # Tipo de plato
M = var() # Malestar

es_ingred_de = Relation()
facts(es_ingred_de,
     ("tomate", "ensalada"),
     ("limon", "ensalada"),
     ("pollo", "aguadito"),
     ("arvejas", "aguadito"),
     ("zapallo", "picante"),
     ("cebolla", "picante"),
     ("maracuya", "helado"),
     ("saborizante", "helado"),
     ("aguardiente", "calientito"),
     ("te", "calientito")
     )

##TIPO DE ALIMENTOS
es_un_tipoalimento_de = Relation()
facts(es_un_tipoalimento_de,
     ("ensalada", "entrada"),
     ("aguadito", "sopa"),
     ("picante", "platofondo"),
     ("helado", "postre"),
     ("calientito", "bebida")
     )

##RECOMENDADO PARA
bueno_contra = Relation()
facts(bueno_contra,
      ("tomate", "caries"),
      ("limon", "gripe"),
      ("cebolla", "gripe"),
      ("zanahoria", "ceguera"),
      ("te", "stress"),
      ("maracuya", "stress")
      )
##EXCESO 
#en_exceso_provoca(huevo, colesterol)
#en_exceso_provoca(platano, diabetes)
#en_exceso_provoca(carne, artritis)
#en_exceso_provoca(aceite, colesterol)
#en_exceso_provoca(saborizantes, diabetes)
#en_exceso_provoca(azucar, diabetes)
#en_exceso_provoca(limon, gastritis)
#en_exceso_provoca(cebolla, acidez)

#Tengo que comer (gripe, tipo, porcion)
#2 opciones
#su alimento a base de :limon (ingrediente) segun el (malestar)
#Tipo = entrada, (tipo de plato)
#Porcion = ensalada; (plato)
#Su alimento a base de :cebolla(ingrediente) segun el (malestar),
#Tipo = plato fondo, (tipo de plato)
#Porcion = picante; (plato)