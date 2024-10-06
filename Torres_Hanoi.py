"""
Created on Saturday 05/10/24

@author: Victor Mendoza
"""
import time

class Pila:
    def crear_pilares(self):
        self.Pilar1 = ["Disco 3", "Disco 2", "Disco 1"]
        self.Pilar2 = []
        self.Pilar3 = []
        print("Primer pilar:",self.Pilar1)
        time.sleep(1)
        print("Segundo pilar:",self.Pilar2)
        time.sleep(1)
        print("Tercer pilar:",self.Pilar3)
        time.sleep(1)
    
    def primer_traslado(self):
        self.Guardardisco1 = self.Pilar1.pop()
        self.Pilar3.append(self.Guardardisco1)
        self.Guardardisco1 = self.Pilar1.pop()
        self.Pilar2.append(self.Guardardisco1)
        print("Primer pilar:",self.Pilar1)
        time.sleep(1)
        print("Segundo pilar:",self.Pilar2)
        time.sleep(1)
        print("Tercer pilar:",self.Pilar3)
        time.sleep(1)

    def segundo_traslado(self):
        self.Guardardisco2 = self.Pilar3.pop()
        self.Pilar2.append(self.Guardardisco2)
        self.Guardardisco2 = self.Pilar1.pop()
        self.Pilar3.append(self.Guardardisco2)
        print("Primer pilar:",self.Pilar1)
        time.sleep(1)
        print("Segundo pilar:",self.Pilar2)
        time.sleep(1)
        print("Tercer pilar:",self.Pilar3)
        time.sleep(1)

    def tercer_traslado(self):
        self.Guardardisco3 = self.Pilar2.pop()
        self.Pilar1.append(self.Guardardisco3)
        self.Guardardisco3 = self.Pilar2.pop()
        self.Pilar3.append(self.Guardardisco3)
        print("Primer pilar:",self.Pilar1)
        time.sleep(1)
        print("Segundo pilar:",self.Pilar2)
        time.sleep(1)
        print("Tercer pilar:",self.Pilar3)
        time.sleep(1)

    def cuarto_traslado(self):
        self.Guardardisco4 = self.Pilar1.pop()
        self.Pilar3.append(self.Guardardisco4)
        print("Primer pilar:",self.Pilar1)
        time.sleep(1)
        print("Segundo pilar:",self.Pilar2)
        time.sleep(1)
        print("Tercer pilar:",self.Pilar3)
        time.sleep(1)
    
Pilares = Pila()

print("\nEste programa simula la solución de la torres de Hanoi con 3 discos")
print("\nTenemos los tres pilares:")
Pilares.crear_pilares()
print("\nEmpezamos con el primer traslado de discos:")
Pilares.primer_traslado()
print("\nSeguimos con el segundo traslado:")
Pilares.segundo_traslado()
print("\nSeguimos con el tercer traslado:")
Pilares.tercer_traslado()
print("\nTerminamos con el cuarto traslado:")
Pilares.cuarto_traslado()