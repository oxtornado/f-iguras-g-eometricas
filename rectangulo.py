# Centro de Biotecnologia Agropecuaria
# Fecha: 13/06/24
# Aprendiz: Daniel Alexander Duarte Ussa
# Ficha: 2877795
# Version: 3.12.2


import math

# Declaracion de la clase
class Rectangulo:
    def __init__(self, lado1, lado2, lado3, lado4): # Creacion de variables

        # Encapsulamiento de los lados
        self.__lado1 = lado1 
        self.__lado2 = lado2
        self.__lado3 = lado3
        self.__lado4 = lado4
        
            # Funcion que comprueba si el rectangulo es real
    def validar_rectangulo(self):
        # Verificar si los lados forman un triángulo válido
        if not(self.__lado1 > 0 and
               self.__lado2 > 0 and
               self.__lado3 > 0 and
               self.__lado4 > 0 ):
            raise ValueError("""     
+--------------------------------------------------------------------+
|      Los lados proporcionados no forman un triángulo válido        |    
+--------------------------------------------------------------------+
                      """)
    
    def set_lado1(self, value):
        self.__lado1 = value
        self.validar_rectangulo()
    
    def get_lado1(self):
        return self.__lado1
    

    def set_lado2(self, value):
        self.__lado2 = value
        self.validar_rectangulo()

    def get_lado2(self):
        return self.__lado2
    
    def set_lado3(self, value):
        self.__lado3 = value
        self.validar_rectangulo()

    def get_lado3(self):
        return self.__lado3
    
    def set_lado4(self, value):
        self.__lado4 = value
        self.validar_rectangulo()
    
    def get_lado4(self):
        return self.__lado4

    def area(self): 

            # Imaginando un rectangulo y comenzando a contar de la siguiente forma:
            
            #                        Lado 2
            #                           |
            #                           v

            #                     +---------+
            #      Lado  1 -->    |         |  <-- Lado 3
            #                     +---------+

            #                           ^
            #                           |
            #                         Lado 4

            # Llevado a cabo de esta forma dados los requerimientos enunciados por el 
            # cliente
            
        
        if self.__lado1 == self.__lado3 and self.__lado2 == self.__lado4:
            length = self.__lado1
            width = self.__lado2
            area = length * width
            return area
        else:
            raise ValueError("""
+--------------------------------------------------------------------+
|     Los lados proporcionados no forman un rectangulo válido        |    
+--------------------------------------------------------------------+
                             """)


    def perimetro(self):
        return self.__lado1 + self.__lado2 + self.__lado3 + self.__lado4

    def print_lados(self):
        print(f"""     
+--------------------------------------------------------------------+
|      El area de su triangulo es: |      {int(self.area())}          
+--------------------------------------------------------------------+
                      """)
        print(f"""     
+--------------------------------------------------------------------+
|      El perimetro de su circulo es: |   {int(self.perimetro())}     
+--------------------------------------------------------------------+
                      """)


            # Llamado de entradas para asignar y operar los valores,
            # asignando un retorno


def rectangulo():
    while True:
        try:
            lado1 = (int(input("""
+--------------------------------------------------------------------+
|               El primer lado de su rectangulo es:                  |    
+--------------------------------------------------------------------+
                               """)))
            lado2 = (int(input("""
+--------------------------------------------------------------------+
|               El segundo lado de su rectangulo es:                 |    
+--------------------------------------------------------------------+
                               """)))
            lado3 = (int(input("""
+--------------------------------------------------------------------+
|               El tercer lado de su rectangulo es:                  |    
+--------------------------------------------------------------------+
                               """)))
            lado4 = (int(input("""
+--------------------------------------------------------------------+
|               El cuarto lado de su rectangulo es:                  |    
+--------------------------------------------------------------------+
                               """)))
            input_rectangulo = Rectangulo(lado1, lado2, lado3, lado4)
            input_rectangulo.print_lados()
        except ValueError as e:
            print("""
+--------------------------------------------------------------------+
|                               Error:                               |    
+--------------------------------------------------------------------+
                               """)
                # Ciclo para continuar generando 
                # perimetro y area de mas rectangulos

        user_input = (input("""
+--------------------------------------------------------------------+
| Existe otro rectangulo del que quisiera saber su area y perimetro: |    
+--------------------------------------------------------------------+
                               """))
        if user_input.lower() != "si":
            break

        
            # Funcion "if __name__ == "__main__"" para la implementacion de
            # la modularizacion
if __name__ == "__main__":
    rectangulo()