import re
# se importa la libreria regular expressions la cual es necesaria para operar con expreciones regulares 
texto_de_entrada = input (" Introduce un texto : ") # se crea una variable a la cual se le puede introducir un texto con cualquier valor 
# se crean las variables correspondientes para cada tipo de busqueda y se les asigna el comando para encontar los respectivos tipos de datos 
resultados_numeros_enteros_texto = re.findall(r"\b-?\d+\b",texto_de_entrada) 
resultados_numeros_flotantes_texto = re.findall( r"\b-?\d+\.\d+\b",texto_de_entrada)
resultados_valores_booleanos_texto = re.findall( r"\b(True|False)\b",texto_de_entrada)
resultados_strings_texto= re.findall( r'"(.*?)"',texto_de_entrada)
resultados_listas_numeros_texto = re.findall(r"\[\s*\d+(?:\s*,\s*\d+)*\s*\]",texto_de_entrada)
# se imprimen  los resultados de cada busqueda y tambien se imprime la cantidad total de elmentos encontrados para cada tipo de dato
print (" LOS RESULTADOS SON :")
print ("se encontraron los enteros  :",resultados_numeros_enteros_texto,"  una cantidad total de :", len(resultados_numeros_enteros_texto), " numeros enteros en el texto ")
print("se encontraron los flotantes :",resultados_numeros_flotantes_texto," una cantidad total de :", len(resultados_numeros_flotantes_texto),"numeros flotantes en el texto")
print("se encontraron los booleanos :",resultados_valores_booleanos_texto," una cantidad total de :",len(resultados_valores_booleanos_texto),"valores booleanos en el texto")
print("se encontraron los strings   :",resultados_strings_texto," una cantidad total de :",len(resultados_strings_texto)," strings en el texto")
print(" se encontraron las listas   : ",resultados_listas_numeros_texto," una cantidad total de :",len(resultados_listas_numeros_texto),"lsitas en el texto")

