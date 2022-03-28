# #crear acronimos 

# usuario = str (input("Entra una frase : "))
# text = usuario.split()
# acronimo = " "

# for i in text:
#     acronimo = acronimo+ str(i[0])
# print(acronimo)

#vamos a crear una base de datos 

usuario = str(input (" Entre tu nombre completo : "))

nombre = usuario.split()

acronimo = " "

for crear_acronimo in nombre :
    acronimo = acronimo + str(crear_acronimo[0]).upper()
print(acronimo) 