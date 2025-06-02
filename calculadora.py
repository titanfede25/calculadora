import random
historial = []
historial_resultados = []

def stringFinal(string, resultado):
    historial.append(f"{string} {resultado}")
    historial_resultados.append(resultado)

def mostrar_historial():
    if not historial and not historial_resultados:
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
                print("Orden original de cálculo:")
                for item in historial:
                    print(item)
            else:
                print("Ordenado por resultado de menor a mayor:")
                desordenada = 1
                while desordenada==1: #intercmbio
                    desordenada = 0
                    for i in range (len(historial_resultados)-1):
                        if historial_resultados[i]>historial_resultados[i+1]:
                            aux = historial_resultados[i]
                            aux2 = historial[i]
                            historial_resultados[i] = historial_resultados[i+1]
                            historial[i] = historial[i+1]
                            historial_resultados[i+1] = aux
                            historial[i+1] = aux2
                            desordenada = 1
                for item in historial:
                    print(item)

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
    num=int(input("Ingrese un número entero para potenciar al anterior: "))
    string = f"{resultado}^{num} = "
    resultado = resultado ** num
    stringFinal(string, resultado)
    return resultado

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
        historial.clear()
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
            print("Operación random: 7")
            print("")

            selector=int(input("Ingrese la operacion deseada: "))
            while(selector > 7 or selector < 1):
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
            if(selector==7):
                aleatorio = random.randint(1,6)
                if (aleatorio==1):
                    resultado = suma(resultado)
                if (aleatorio==2):
                    resultado = resta(resultado)
                if (aleatorio==3):
                    resultado = multiplicacion(resultado)
                if (aleatorio==4):
                    resultado = division(resultado)
                if (aleatorio==5):
                    resultado = potencia(resultado)
                if (aleatorio==6):
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
                mostrar_historial()
                print("")
                reinicio = int(input("¿Quieres reiniciar la calculadora (0 = No, 1 = Si)? "))
                while(reinicio != 1 and reinicio != 0):
                    print("")
                    reinicio = int(input("ERROR! Ingrese un valor válido. ¿Quieres reiniciar la calculadora? (0 = No, 1 = Si): "))

main()