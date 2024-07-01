# Centro de Biotecnologia Agropecuaria
# Fecha: 13/06/24
# Aprendiz: Daniel Alexander Duarte Ussa
# Ficha: 2877795
# Version: 3.12.2


            # Importamos math, sin embargo, solo la 
            # funcion que necesitamos que es la que nos 
            # retorna la raiz cuadrada de los elementos
        
from math import sqrt

# Declaracion de la clase
class Triangulo:
    def __init__(self, lado1, lado2, lado3): # Creacion de variables

        # Encapsulamiento de los lados
        self.__lado1 = lado1 
        self.__lado2 = lado2
        self.__lado3 = lado3

    def validar_triangulo(self):

            # Comprobamos la veracidad del triangulo que ingrese el usuario
        
        if not(self.__lado1 + self.__lado2 > self.__lado3 and
               self.__lado1 + self.__lado3 > self.__lado2 and
               self.__lado2 + self.__lado3 > self.__lado1):

            # Manejo de errores en el 
            # tiempo de ejecucion
        
            print("""     
+--------------------------------------------------------------------+
|      Los lados proporcionados no forman un triangulo válido        |
+--------------------------------------------------------------------+
                      """)  
            if self.__lado1 + self.__lado2 > self.__lado3:
                print("""     
+--------------------------------------------------------------------+
|      La suma de los lados 1, 2 no forman un tringulo valido        |
+--------------------------------------------------------------------+
                      """)  
            elif self.__lado1 + self.__lado3 > self.__lado2:
                print("""     
+--------------------------------------------------------------------+
|      La suma de los lados 1 y 3 no forman un tringulo valido      |
+--------------------------------------------------------------------+
                      """) 
            elif self.__lado2 + self.__lado3 > self.__lado1:
                print("""     
+--------------------------------------------------------------------+
|     La suma de los lados 2 y 3 no forman un tringulo valido        |
+--------------------------------------------------------------------+
                      """)  

    def set_lado1(self, value):
        self.__lado1 = value
        self.validar_triangulo()
    
    def get_lado1(self):
        return self.__lado1
    

    def set_lado2(self, value):
        self.__lado2 = value
        self.validar_triangulo()

    def get_lado2(self):
        return self.__lado2
    
    def set_lado3(self, value):
        self.__lado3 = value
        self.validar_triangulo()

    def get_lado3(self):
        return self.__lado3


    # Llamamos la funcion que importamos de 
    # la libreria math  
    def area(self): 
        s = (self.__lado1 + self.__lado2 + self.__lado3) / 2
        return sqrt(s * (s - self.__lado1) * (s - self.__lado2) * (s - self.__lado3))


    def perimetro(self):
        return self.__lado1 + self.__lado2 + self.__lado3

    def print_lados(self):
        print(f"""     
+--------------------------------------------------------------------+
|      El area de su triangulo es: |      {int(self.area())}         |    
+--------------------------------------------------------------------+
                      """)
        print(f"""     
+--------------------------------------------------------------------+
|      El perimetro de su circulo es: |   {int(self.perimetro())}    |    
+--------------------------------------------------------------------+
                      """)


def triangulo():

    # Bucles y controladores de errores de ejecucion
    while True:
        try:
            lado1 = (int(input("""
+--------------------------------------------------------------------+
|               El primer lado de su triangulo es:                   |    
+--------------------------------------------------------------------+
                               """)))            
            lado2 = (int(input("""
+--------------------------------------------------------------------+
|               El segundo lado de su triangulo es:                  |    
+--------------------------------------------------------------------+
                               """)))
            lado3 = (int(input("""
+--------------------------------------------------------------------+
|               El tercer lado de su triangulo es:                   |    
+--------------------------------------------------------------------+
                               """)))
            input_triangulo = Triangulo(lado1, lado2, lado3)
            input_triangulo.validar_triangulo()
            input_triangulo.print_lados()
        except ValueError as e:
            print(f"""
+--------------------------------------------------------------------+
|                    Error: {e}                           
                               """)
            
            continue
        user_input = (input("""
+--------------------------------------------------------------------+
| Existe otro triangulo del que quisiera saber su area y perimetro:  |    
+--------------------------------------------------------------------+
                               """))
        if user_input.lower() != "si":
            break


# Llamado de la funcion if __name__=="main"" 
# para modular correctamente

if __name__ == "__main__":
    triangulo()