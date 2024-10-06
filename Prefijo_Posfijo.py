"""
Created on Saturday 05/10/24

@author: Victor Mendoza
"""

def evaluar_expresiones(expresion, tipo):
    Pila = []

    if tipo == "Prefijo":
        for variable in expresion[::-1]:
            if variable not in "+-*/":
                Pila.append(int(variable))
            else:
                numero1 = Pila.pop()
                numero2 = Pila.pop()

                if variable == "+":
                    Pila.append(numero1 + numero2)
                elif variable == "-":
                    Pila.append(numero1 - numero2)
                elif variable == "*":
                    Pila.append(numero1 * numero2)
                elif variable == "/":
                    Pila.append(numero1 / numero2)
    
    if tipo == "Posfijo":
        for variable in expresion:
            if variable not in "+-*/":
                Pila.append(int(variable))
            else:
                numero1 = Pila.pop()
                numero2 = Pila.pop()

                if variable == "+":
                    Pila.append(numero1 + numero2)
                elif variable == "-":
                    Pila.append(numero1 - numero2)
                elif variable == "*":
                    Pila.append(numero1 * numero2)
                elif variable == "/":
                    Pila.append(numero1 / numero2)

    return Pila[0]

Expresion_prefija = input("\nIngrese la expresión aritmética prefija(Ejemplo:'- + * 2 3 * 5 4 9'): ")
Expresion_posfija = input("\nIngrese la expresión aritmética posfija(Ejemplo:'2 3 * 5 4 * + 9 -'): ")
Expresion_prefija = Expresion_prefija.split()
Expresion_posfija = Expresion_posfija.split()

Resultado_expresion_prefija = evaluar_expresiones(Expresion_prefija, "Prefijo")
print(f"\nEl resultado de la expresión prefija es: {Resultado_expresion_prefija}")

Resultado_expresion_posfija = evaluar_expresiones(Expresion_posfija, "Posfijo")
print(f"\nEl resultado de la expresión posfija es: {Resultado_expresion_posfija}")