
class persona:
     a = 0
     b = 0
     c = 0

     def inicializar(self, nombre, sueldo):
         self.nombre = nombre
         self.sueldo = sueldo

     def calculo_impuesto(self):
            if(self.sueldo<10000):
                print("Trabajador no paga impuesto")
            elif(self.sueldo>=10000 and self.sueldo>=30000):
                self.a = self.sueldo * 0.10
                print(f"El impuesto a pagar por el trabajador {self.nombre} es {self.a}")
            elif(self.sueldo>30000 and self.sueldo>=50000):
                self.a = self.sueldo*0.20
                print(f"El impuesto a pagar por el trabajador {self.nombre}  es de {self.a}")
            elif(self.sueldo<50000):
                        self.a = self.sueldo*0.35
                        print(f"El impuesto a pagar por el trabajador {self.nombre}  es de {self.a}")

     def calculo_afp(self):
            self.b = self.sueldo*0.11
            print(f"El descuento por AFP del trabajador {self.nombre}  es de {self.b}")

     def descuento_salud(self):
            self.c=self.sueldo*0.07
            print(f"El descuento por salud del trabajador {self.nombre} es de {self.c}")


     def calculo_liquido(self):
            self.e = self.sueldo - (self.a + self.b + self.c)
            print(f"El sueldo liquido a recibir por el trabajador es de {self.e}")



#comienzo de codigo

d = str(input("Ingrese el nombre del trabajador: "))
f = int(input("Ingrese el sueldo del trabajador: "))

persona1=persona()
persona1.inicializar(d,f)
persona1.calculo_impuesto()
persona1.calculo_afp()
persona1.descuento_salud()
persona1.calculo_liquido()





