import random
fechas = []
coincidencias = 0
intentos = 0
int_con_coin = 0
total_coincidenciasv = []
total_coincidencias = 0
print("¿Sabías que en un grupo de 23 personas hay un 50% de probabilidades de que 2 de ellas compartan cumpleaños"
      " sin tener en cuenta ningún tipo de fechas especiales, de forma completammente aleatoria? ¿No te lo crees?\n"
      "Compruébalo tú mismo/a. Puedes tener más o menos de 23 sujetos si lo prefieres. En cada prueba se genera un"
      " número aleatorio del 1 al 365 para cada sujeto y se comprueba si hay alguna coincidencia. Entonces te dirá cuántas coincidencias"
      " hay, cuántas probabilidades hay de que las haya con esos intentos\ny cuántas coincidencias ha habido entre todas"
      " las rondas. Hay 3 modos, automático, que hace pruebas muy rápidamente, semiautomático, que hace lo mismo pero se"
      " para cada 500 pruebas hasta que le des a enter, y manual, que se para cada ronda.")
print("El porcentaje que da es el porcentaje de pruebas con coincidencias, pero hay intentos con varias coincidencias,"
      " por eso si haces el porcentaje con los números que te muestra el programa te va a salir más de un 50%")
sujeto = input("¿Cuántos sujetos hay en el experimento?\n")
def auto():
    global fechas
    global coincidencias
    global intentos
    global int_con_coin
    global total_coincidencias
    global total_coincidenciasv
    global sujeto
    total_coincidenciasv = []
    fechas = []
    for i in range(int(float(sujeto))):
        c = random.randint(1, 365)
        fechas.append(c)
    intentos += 1
    if len(fechas) > len(set(fechas)):
        int_con_coin += 1
    coincidencias = len(fechas) - len(set(fechas))
    total_coincidenciasv.append(coincidencias)
    for i in total_coincidenciasv:
        total_coincidencias += i
    print("Hay un", (int_con_coin / intentos) * 100, "% de que haya coincidencias")
    print("En este intento hay", coincidencias, " coincidencias")
    print("Ha habido un total de", total_coincidencias, "coincidencias")
    print("Se han hecho",intentos,"pruebas")
def manual():
    auto()
    input()
def semi():
    while True:
        for i in range(500):
            auto()
        input()
while True:
    modo = input("¿Manual, automático, o semiautomático? M/A/S\n")
    if modo == "M" or modo == "m":
        while True:
            manual()
    elif modo == "S" or modo == "s":
        while True:
            semi()
    elif modo == "A" or modo == "a":
        while True:
            auto()
    else:
        print("Introducción inválida")