import os

ls_bodega_1 = []
ls_bodega_2 = []
sw = True
def fnt_registrar():
    año = input('Ingrese el año del vehiculo: ')
    modelo = input('Ingrese el modelo del vehiculo: ')
    motor = input('Ingrese el numero de motor: ')
    fabricante = input('1. Chevrolet\n2. Ford\n3. Renault\n4. Dodge\n5. Hyundai\n6. Fiat\n -> ')
    if año == '2024' and (fabricante == '1' or fabricante == '2' or fabricante == '3'):
        ls_bodega_1.append([año, modelo, motor, fabricante])
        print(ls_bodega_1)
    
while sw == True:
    os.system('cls')
    
    opcion = input('1. Registrar\n2. Mostrar ->')
    if opcion == '1':
        fnt_registrar()