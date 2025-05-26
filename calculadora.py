def suma(resultado):
    print("")
    num=float(input("Ingrese un número para sumar al anterior: "))
    resultado += num
    return resultado

def resta(resultado):
    print("")
    num=float(input("Ingrese un número para restar al anterior: "))
    resultado -= num
    return resultado

def multiplicacion(resultado):
    print("")
    num=float(input("Ingrese un número para multiplicar al anterior: "))
    resultado *= num
    return resultado

def division(resultado):
    print("")
    num=float(input("Ingrese un número para dividir al anterior: "))
    resultado /= num
    return resultado

def potencia(resultado):
    print("")
    num=int(input("Ingrese un número natural para potenciar al anterior: "))
    resultado2 = resultado
    if num == 0:
        resultado2 = 1
    else:
        for i in range (num-1):
            resultado2=resultado2*resultado
    return resultado2

def raiz(resultado):
    print("")
    raiz=int(input("Ingrese raíz: "))
    while (raiz <= 0):
        print("")
        raiz=int(input("ERROR! Ingrese raíz válida: "))
    if (raiz%2==0 and resultado<0):
        print("ERROR! Esta cálculo es inválido matemáticamente")
    else:
        resultado = resultado ** (1/raiz)
    return resultado

def main():

    print("calculadora")
    print("")
    resultado=float(input("Ingrese un número: "))

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
        resultado=suma(resultado)
    if (selector==2):
        resultado=resta(resultado)
    if (selector==3):
        resultado=multiplicacion(resultado)
    if (selector==4):
        resultado=division(resultado)
    if (selector==5):
        resultado=potencia(resultado)
    if(selector==6):
        resultado=raiz(resultado)
    print("")
    print(resultado)

main()