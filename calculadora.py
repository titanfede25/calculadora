historial_orden = []
historial_resultados = []

def stringFinal(string, resultado):
    historial_orden.append(string + str(resultado))
    historial_resultados.append(resultado)

def suma(resultado):
    print("")
    num=float(input("Ingrese un número para sumar al anterior: "))
    string = f"{resultado} + {num} = "
    resultado += num
    stringFinal(string, resultado)
    return resultado

def resta(resultado):
    print("")
    num=float(input("Ingrese un número para restar al anterior: "))
    string = f"{resultado} - {num} = "
    resultado -= num
    stringFinal(string, resultado)
    return resultado

def multiplicacion(resultado):
    print("")
    num=float(input("Ingrese un número para multiplicar al anterior: "))
    string = f"{resultado} * {num} = "
    resultado *= num
    stringFinal(string, resultado)
    return resultado

def division(resultado):
    print("")
    num=float(input("Ingrese un número para dividir al anterior: "))
    string = f"{resultado} / {num} = "
    resultado /= num
    stringFinal(string, resultado)
    return resultado

def potencia(resultado):
    print("")
    num=int(input("Ingrese un número natural para potenciar al anterior: "))#no acepta potencia de numeros negativos
    while (num<1):
        print("")
        num=int(input("ERROR! Ingrese potencia válida: "))
    string = f"{resultado}^{num} = "
    resultado2 = resultado
    if num == 0:
        resultado2 = 1
    else:
        for i in range (num-1):
            resultado2=resultado2*resultado
    stringFinal(string, resultado2)
    return resultado2

def raiz(resultado):
    print("")
    raiz=int(input("Ingrese raíz: "))
    while (raiz <= 0):
        print("")
        raiz=int(input("ERROR! Ingrese raíz válida: "))
    if ((raiz%2==0 and resultado<0) or raiz<1):#no se puede hacer una raiz de numero negativo si es par, ni tampoco tampoco una raiz negativa
        print("ERROR! Esta cálculo es inválido matemáticamente. Retornaremos el número guardado previamente.")
    else:
        string = f"{raiz}√{resultado}  = "
        resultado = resultado ** (1/raiz)
        stringFinal(string, resultado)
    return resultado

def main():
    print("=======================")
    print("\nCalculadora Portatil")
    print("\n=======================")

    reinicio = 1
    while (reinicio==1):
        print("")
        historial_resultados.clear()
        historial_orden.clear()
        resultado=float(input("\nIngrese un número para comenzar a calcular!: "))
        continuar=1

        while(continuar==1):
            print("=======================")
            print("\nOpciones de operaciones: ")
            print("Seleccione una operacion para continuar!")
            print("\n=======================")
            print("")
            print("Suma: 1")
            print("")
            print("Resta: 2")
            print("")
            print("Multiplicar: 3")
            print("")
            print("Dividir: 4")
            print("")
            print("Potenciar: 5")
            print("")
            print("Aplicar raíz: 6")
            print("")

            selector=int(input("Ingrese la operacion deseada: "))
            while(selector > 6 or selector < 1):
                print("")
                selector = int(input("ERROR! Ingrese un valor válido(1-6): "))
    
            if (selector==1):
                resultado = suma(resultado)
            if (selector==2):
                resultado = resta(resultado)
            if (selector==3):
                resultado = multiplicacion(resultado)
            if (selector==4):
                resultado = division(resultado)
            if (selector==5):
                resultado = potencia(resultado)
            if(selector==6):
                resultado = raiz(resultado)
            print("")
            print(resultado)
            print("")
            continuar = int(input("¿Quieres continuar a partir del resultado obtenido (0 = No, 1 = Si)? "))
            while(continuar != 1 and continuar != 0):
                print("")
                continuar = int(input("ERROR! Ingrese un valor válido. ¿Quieres continuar a partir del resultado obtenido? (0 = No, 1 = Si): "))
            if (continuar==0):
                print("")
                reinicio = int(input("¿Quieres reiniciar la calculadora (0 = No, 1 = Si)? "))
                while(reinicio != 1 and reinicio != 0):
                    print("")
                    reinicio = int(input("ERROR! Ingrese un valor válido. ¿Quieres reiniciar la calculadora? (0 = No, 1 = Si): "))

def mostrar_historial():
    if not historial_orden and not historial_resultados:
        print("\nNo hay operaciones en el historial!")
        return
    
    print("\n¿Queres ver el historial de calculos?")
    opcionVer = int(input("Ingrese su opcion (0 = No, 1 = Si): "))
    while opcionVer != 0 and opcionVer != 1:
        opcionVer = int(input("ERROR: Por favor, ingrese un numero valido (0 = No, 1 = Si): "))
    
    if opcionVer == 1:
            print("\n¿De que forma queres ordenar el historial?")
            print("1. Orden Original")
            print("2. Ordenado por resultado")

            opcionElegir = int(input("Ingrese su opcion (1-2): "))
            while opcionElegir != 1 and opcionElegir != 2:
                opcionElegir = int(input("ERROR: Por favor, ingrese un numero valido. (1-2): "))

            print("\nHistorial de operaciones:")

            if opcionElegir == 1:
                print("Orden original de calculo")
                for item in historial_orden:
                    print(item)
            else:
                print("Ordenado por resultado de menor a mayor")
                resultados_ordenados = []

                for r in historial_resultados:
                    resultados_ordenados.append(r)

                largo = len(resultados_ordenados)
                for i in range(largo):
                    for j in range(largo - 1):
                        if resultados_ordenados[j] > resultados_ordenados[j + 1]:
                            aux = resultados_ordenados[j]
                            resultados_ordenados[j] = resultados_ordenados[j + 1]
                            resultados_ordenados[j + 1] = aux

                mostrados = []

                for i in range(len(resultados_ordenados)):
                    for j in range(len(historial_resultados)):
                        bool_mostrados = False
                        for k in range(len(mostrados)):
                            if mostrados[k] == j:
                                bool_mostrados = True

                        if not bool_mostrados and historial_resultados[j] == resultados_ordenados[i]:
                            print(historial_orden[j])
                            mostrados.append(j)


main()
mostrar_historial()