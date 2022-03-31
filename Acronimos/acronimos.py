

#vamos a crear una base de datos 

usuario = str(input (" Entre tu nombre completo : "))

nombre = usuario.split()

acronimo = " "

for crear_acronimo in nombre :
    acronimo = acronimo + str(crear_acronimo[0]).upper()
print(acronimo) 
