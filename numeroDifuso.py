class NumeroDifuso:
    valores = []
    def __init__(self, a:float, b:float, c:float, d:float = None):
        """Este es el contructor de la clase, puede crear triangulos o trapezoides en función de si se le pasa 3 (Tirangulo)  o 4 (Trapezoide) parámentros."""
        if d==None:
            self.valores = [a,b,c]
        else:
            self.valores = [a,b,c,d]

    def  suma (self, num2):
        if(len(self.valores) == len(num2.valores)):
            if len(self.valores) == 3:
                return NumeroDifuso(self.valores[0]+num2.valores[0],self.valores[1]+num2.valores[1],self.valores[2]+num2.valores[2])
            else:
                return NumeroDifuso(self.valores[0]+num2.valores[0],self.valores[1]+num2.valores[1],self.valores[2]+num2.valores[2],self.valores[3]+num2.valores[3])
        else:
            if(len(self.valores) == 3):
                return NumeroDifuso(self.valores[0]+num2.valores[0],self.valores[1]+num2.valores[1],self.valores[1]+num2.valores[2],self.valores[2]+num2.valores[3])
            else:
                return NumeroDifuso(self.valores[0]+num2.valores[0],self.valores[1]+num2.valores[1],self.valores[2]+num2.valores[1],self.valores[3]+num2.valores[2])

    def resta (self, num2):
        if(len(num2.valores) == 3):
            num2 = NumeroDifuso(-num2.valores[0],-num2.valores[1],-num2.valores[2])
        else:
            num2 = NumeroDifuso(-num2.valores[0],-num2.valores[1],-num2.valores[2],-num2.valores[3])
        return self.suma (num2)

    def  producto (self, num2):
        if(len(self.valores) == len(num2.valores)):
            if(len(self.valores) == 3):
                return NumeroDifuso(self.valores[0]*num2.valores[0],self.valores[1]*num2.valores[1],self.valores[2]*num2.valores[2])
            else:
                return NumeroDifuso(self.valores[0]*num2.valores[0],self.valores[1]*num2.valores[1],self.valores[2]*num2.valores[2],self.valores[3]*num2.valores[3])
        else:
            if(len(self.valores) == 3):
                return NumeroDifuso(self.valores[0]*num2.valores[0],self.valores[1]*num2.valores[1],self.valores[1]*num2.valores[2],self.valores[2]*num2.valores[3])
            else:
                return NumeroDifuso(self.valores[0]*num2.valores[0],self.valores[1]*num2.valores[1],self.valores[2]*num2.valores[1],self.valores[3]*num2.valores[2])

    def division (self, num2):
        if(len(num2.valores) == 3):
            num2 = NumeroDifuso(1/num2.valores[0],1/num2.valores[1],1/num2.valores[2])
        else:
            num2 = NumeroDifuso(1/num2.valores[0],1/num2.valores[1],1/num2.valores[2],1/num2.valores[3])
        return self.producto (num2)

    def tostring(self):
        if len(self.valores) == 3:
            return "("+str(self.valores[0])+","+str(self.valores[1])+","+str(self.valores[2])+")"
        else:
            return "("+str(self.valores[0])+","+str(self.valores[1])+","+str(self.valores[2])+","+str(self.valores[3])+")"

    def invertir (self):
        if len(self.valores) == 3:
            return NumeroDifuso(float("-inf"),self.valores[0],self.valores[1]),NumeroDifuso(self.valores[1],self.valores[2],float("inf"))
        else:
            return NumeroDifuso(float("-inf"),self.valores[0],self.valores[1]),NumeroDifuso(self.valores[2],self.valores[3],float("inf"))

##Varias Pruebas del software
def test():
    num1 = NumeroDifuso(float("-inf"),2,3,4)
    num2 = NumeroDifuso(1,2,4)

    print(num1.invertir()[0].tostring() + " " + num1.invertir()[1].tostring())
    print(num1.suma(num2).tostring())
    print(num1.tostring() + " - " + num2.tostring() + " = " +num1.resta(num2).tostring())
    print(num1.division(num2).tostring())

##Ejecuta las pruebas
test()