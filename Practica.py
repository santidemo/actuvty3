import csv
#, delimiter="/" esto que pone despues del reader para cambiar el delimiter y que no sea solo por ,
# with open('Personas.cvs') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print("Apellido: {0}, Nombre: {1}, DNI: {2}".format(row[0], row[1], row[2]))
# Una forma de poder ver tu archivo y poder mostrarlo

Personas = [
    ["Aban","Santiago",48084522],
    ["Tato","Lucas",43413111],
    ["Torres","Daniel",12332111],
    ["Guanuco","Lucas",123328851]
]


with open('Personas.cvs', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    #Este es 1 metodo writer.writerow(Personas)
    writer.writerows(Personas)