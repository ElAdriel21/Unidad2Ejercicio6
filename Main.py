from ClaseFechaHora import FechaHora

def opcion0():
    print("Saliendo")

def opcion1():
    fecha1 = FechaHora(21, 3, 2001, 12, 30, 15)
    fecha2 = FechaHora(2, 1, 2, 3, 10, 15)
    fecha3 = (fecha1+fecha2)
    print(fecha3)

def opcion2():
    fecha1 = FechaHora(21, 3, 2001, 12, 30, 15)
    fecha2 = FechaHora(2, 1, 2, 3, 10, 15)
    fecha3 = (fecha1-fecha2)
    print(fecha3)

def opcion3():
    fecha1 = FechaHora(21, 3, 2001, 12, 30, 15)
    fecha2 = FechaHora(28, 3, 2001, 3, 10, 15)
    fechaMay = fecha1 > fecha2
    print(fechaMay)
    if fechaMay == 0:
        print("Las fechas son iguales")
    elif fechaMay == 1:
        print("La fecha 1 es mayor")
    else:
        print("La fecha 2 es mayor")

switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2,
    3: opcion3
}

def switch(argument):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func()

if __name__ == '__main__':
    bandera = False
    while not bandera:
        print("0 Salir")
        print("1 Sumar fecha")
        print("2 Restar fecha")
        print("3 Fechas iguales")
        opcion= int(input("Ingrese una opción: "))
        switch(opcion)
        bandera = int(opcion)==0