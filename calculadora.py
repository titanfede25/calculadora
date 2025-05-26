historial = []

def stringFinal(string, resultado):
    string += str(resultado)
    historial.append(string)

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

    print("Calculadora")

    reinicio = 1
    while (reinicio==1):
        print("")
        historial.clear()
        resultado=float(input("Ingrese un número: "))
        continuar=1

        while(continuar==1):
            print("")
            print("Opciones de operaciones: ")
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

            selector=int(input("Ingrese: "))
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
            continuar = int(input("¿Quieres continuar a partir del resultado obtenido (Si=1, No=0)? "))
            while(continuar != 1 and continuar != 0):
                print("")
                continuar = int(input("ERROR! Ingrese un valor válido (Si=1, No=0): "))
            if (continuar==0):
                print("")
                reinicio = int(input("¿Quieres reiniciar la calculadora (Si=1, No=0)? "))
                while(reinicio != 1 and reinicio != 0):
                    print("")
                    reinicio = int(input("ERROR! Ingrese un valor válido (Si=1, No=0): "))

main()
print(historial)