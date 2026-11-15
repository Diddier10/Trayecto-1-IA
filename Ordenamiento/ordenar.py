
# Paso 2: ordenar tres números de menor a mayor (Mi algoritmo)

#a = int(input("Primer número: "))
#b = int(input("Segundo número: "))
#c = int(input("Tercer número: "))

#if a <= b:
  #  if b <= c:
    #    print(a, b, c)
    #elif a <= c:
    #    print(a, c, b)
    #else:
    #    print(c, a, b)

#else:
   # if a <= c:
        #print(b, a, c)
   # elif b <= c:
   #     print(b, c, a)
    #else:
    #    print(c, b, a)

#Modelo 1 IA

#a = int(input("Ingrese el primer número: "))
#b = int(input("Ingrese el segundo número: "))
#c = int(input("Ingrese el tercer número: "))

#if a <= b and a <= c:
    #if b <= c:
      #  print(a, b, c)
    #else:
       # print(a, c, b)

#else:
    #if b <= a and b <= c:
        #if a <= c:
            #print(b, a, c)
       # else:
            #print(b, c, a)
    #else:
        #if a <= b:
            #print(c, a, b)
       # else:
           # print(c, b, a)


#Modelo 2 IA
a = int(input("Ingresa el primer número entero: "))
b = int(input("Ingresa el segundo número entero: "))
c = int(input("Ingresa el tercer número entero: "))

if a <= b:
    if b <= c:
        print(a, b, c)
    else:
        if a <= c:
            print(a, c, b)
        else:
            print(c, a, b)
else:
    if a <= c:
        print(b, a, c)
    else:
        if b <= c:
            print(b, c, a)
        else:
            print(c, b, a)

# ================================================================
# TABLA DE EVIDENCIAS - PRUEBAS DEL ALGORITMO
# ================================================================
#
# Caso                         | Entrada  | Esperado | Tu algoritmo | Modelo A | Modelo B
# -----------------------------|----------|----------|--------------|----------|----------
# Desordenados                 | 7, 2, 5  | 2, 5, 7  |  Correcto    |  Correcto|  Correcto
# Desordenados (al revés)      | 9, 5, 1  | 1, 5, 9  |  Correcto    |  Correcto|  Correcto
# Repetidos                    | 5, 1, 5  | 1, 5, 5  |  Correcto    |  Correcto|  Correcto
# Negativos                    | -3, 5, -1| -3, -1, 5|  Correcto    |  Correcto|  Correcto
# Todos iguales                | 4, 4, 4  | 4, 4, 4  |  Correcto    |  Correcto|  Correcto

#
# ================================================================
# FIN DE LA TABLA DE EVIDENCIAS
# ================================================================

# Como se puede observar, los tres algoritmos funcionan correctamente para todos los casos de prueba.
# El mas facil de leer y entender es el modelo 2, por lo que es el que se recomienda usar.