from math import * 

opcao = int(input("""1 - Transformar para polar
2 - Transformar para quadrada: """))

casas_decimais = int(input("Casas decimais: "))

def transformar_para_polar (real, imaginario) :

        calc_modulo_polar = sqrt((real ** 2) + (imaginario ** 2))
        calc_angulo_polar = degrees(atan(imaginario / real))

        print(f"Forma polar: {calc_modulo_polar:.{casas_decimais}f}∠{calc_angulo_polar:.{casas_decimais}f}°")

def transformar_para_quadrada (modulo, angulo) :
        calc_real_quadrada = modulo * cos(degrees(angulo))
        calc_imaginario_quadrada = modulo * sin(degrees(angulo))

        print(f"Forma quadrada: {calc_real_quadrada:.{casas_decimais}f} + j{calc_imaginario_quadrada:.{casas_decimais}f}")

if (opcao == 1):
    real = float(input("Número real: "))
    imaginario = float(input("Número imaginário: "))

    transformar_para_polar(real, imaginario)

else:
    modulo_polar = float(input("Módulo: "))
    angulo_polar = float(input("Ângulo: "))

    transformar_para_quadrada(modulo_polar, angulo_polar)

        