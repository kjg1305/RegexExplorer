import re
# se importa la libreria regular expressions la cual es necesaria para operar con expreciones regulares 

#with open ('texto.txt','r',encoding='Latin-1') as file :    
#   texto = file.read()
# para abrir un archivo de texto 

texto_prueba = input (" Introduce un texto : ") # se crea una variable a la cual se le puede introducir un texto con cualquier valor 

# se crean las variables correspondientes para cada tipo de busqueda y se les asigna el comando para encontar los respectivos tipos de datos 
enteros = r"\b-?\d+\b"
flotantes= r"\b-?\d+\.\d+\b"
booleanos = r"\b(True|False)\b"
strings = r'"(.*?)"'
listasNumericas = r"\[\s*\d+(?:\s*,\s*\d+)*\s*\]"

buscar_enteros = re.findall(enteros,texto_prueba) 
buscar_flotantes = re.findall( flotantes,texto_prueba)
buscar_booleanos = re.findall( booleanos,texto_prueba)
buscar_strings= re.findall( strings,texto_prueba)
buscar_listas_num = re.findall(listasNumericas,texto_prueba)
# se imprimen  los resultados de cada busqueda y tambien se imprime la cantidad total de elmentos encontrados para cada tipo de dato
print(" LOS RESULTADOS SON :")
print("se encontraron los enteros   :",buscar_enteros,"    una cantidad total de :", len(buscar_enteros),  " numeros enteros en el texto ")
print("se encontraron los flotantes :",buscar_flotantes,"  una cantidad total de :", len(buscar_flotantes),"numeros flotantes en el texto")
print("se encontraron los booleanos :",buscar_booleanos,"  una cantidad total de :", len(buscar_booleanos),"valores booleanos en el texto")
print("se encontraron los strings   :",buscar_strings,"    una cantidad total de :", len(buscar_strings),  " strings en el texto")
print(" se encontraron las listas   :",buscar_listas_num," una cantidad total de :", len(buscar_listas_num),"listas en el texto")

