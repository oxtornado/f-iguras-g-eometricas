# Centro de Biotecnologia Agropecuaria
# Fecha: 13/06/24
# Aprendiz: Daniel Alexander Duarte Ussa
# Ficha: 2877795
# Version: 3.12.2


from math import pi

# Declaracion de la clase
class Circulo:
    def __init__(self, radio): # Creacion de variables

        # Encapsulamiento del radio

        self.__radio = radio 

    def validar_radio(self):
        """
            Verificar si los lados forman un triángulo válido
   
        """
        if not(self.__radio>0):
            raise ValueError("""     
+--------------------------------------------------------------------+
|        El radio proporcionado no forman un circulo válido          |    
+--------------------------------------------------------------------+
                      """)
        
    def set_radio(self, value):
        self.__lado1 = value
        self.validar_radio()
    
    def get_radio(self):
        return self.__radio


            # Funcion para hallar el Area del circulo                
    def area(self): 
        s = pi * self.__radio * self.__radio
        return s

            # Perimetro, siempre nombrando las variables con el atributo self.

    def perimetro(self):
        return 2.0 * pi * self.__radio


            # Aqui imprimimos los resultados de las funciones de arriba
   

    def print_lados(self):
        print(f"""     
+--------------------------------------------------------------------+
|      El area de su circulo es: |       {int(self.area())}          |    
+--------------------------------------------------------------------+
                      """)
        print(f"""     
+--------------------------------------------------------------------+
|      El perimetro de su circulo es: |   {int(self.perimetro())}    |    
+--------------------------------------------------------------------+
                      """)

            # Aqui comienza "La Ejecucion del Codigo", invocando y mostrando las funciones
               

def circulo():


            # Bucle while para controlar el flujo de los inputs que se ingresen,
            # sumado al control de errores a partir de la implementacion de un
            # Try Except para el manejo de errores de tiempo de ejecucion
   
    while True:
        try:
            radio_input = (int(input("""
+--------------------------------------------------------------------+
|                 Ingrese el radio de su circulo                     |    
+--------------------------------------------------------------------+
                               """)))

            input_circulo = Circulo(radio_input)
            input_circulo.print_lados()
        except ValueError as e:
            print("""
+--------------------------------------------------------------------+
|                               Error:                               |    
+--------------------------------------------------------------------+
                               """)
        user_input = input("""
+--------------------------------------------------------------------+
|  Existe otro circulo del que quisiera saber su area y perimetro:   |    
+--------------------------------------------------------------------+
                               """) 

            # Condicion para seguir generando perimetros y areas de otros circulos
   
        if user_input.lower() != "si":
            break
            # Llamado de la funcion "if __name__ == "__main__"" con el
            # fin de implementar modular funciones

if __name__ == "__main__":
    circulo()