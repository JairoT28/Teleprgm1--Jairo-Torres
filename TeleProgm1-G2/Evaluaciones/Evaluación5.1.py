## Círculo ##

from math import pi


def area_del_circulo():

    radio = float(input("¿Cuál es el radio? "))

    area = (pi * (radio ** 2))

    print("el area del circulo es: ", area)

    return

area_del_circulo()