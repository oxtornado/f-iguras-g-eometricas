# Centro de Biotecnologia Agropecuaria
# Fecha: 13/06/24
# Aprendiz: Daniel Alexander Duarte Ussa
# Ficha: 2877795
# Version: 3.12.2


            # Importamos todo de los archivos

from classes.circulo import *
from classes.triangulo import *
from classes.rectangulo import * 

            # Comienzo del programa
        
def main():
    print("""
+--------------------------------------------------------------------+
|          Bienvenidos a la calculadora de area y perimetros         |    
+--------------------------------------------------------------------+
+--------------------------------------------------------------------+
|          Puede calcular:                                           |
|               1. Triangulos                                        |
|               2. Cuadrados                                         |
|               3. Circulos                                          |
+--------------------------------------------------------------------+
    """)
            # Manejo de errores en el tiempo de ejecucion a partir de 
            # un bucle While True y Try, Except
        
    while True:
        try:
            opcion = int(input("""     
+--------------------------------------------------------------------+
|               Ingrese la opcion que desea calcular                 |    
+--------------------------------------------------------------------+
                      """))
            if opcion == 1:
                print("""     
+--------------------------------------------------------------------+
|              Calculando area y perimetro de un triangulo           |    
+--------------------------------------------------------------------+
                      """)
            # Llamado a la funcion triangulo, del archivo triangulo.py
        
                triangulo()
            elif opcion == 2:
                print("""     
+--------------------------------------------------------------------+
|              Calculando area y perimetro de un rectangulo          |    
+--------------------------------------------------------------------+
                      """)
            # Llamado a la funcion rectangulo, del archivo rectangulo.py
        
                rectangulo()
            elif opcion == 3:
                print("""     
+--------------------------------------------------------------------+
|              Calculando area y perimetro de un circulo             |    
+--------------------------------------------------------------------+
                      """)
            # Llamado a la funcion circulo, del archivo circulo.py
        
        
                circulo()
            # Manejo de errores en el tiempo de ejecucion, esto, 
            # al ser un bucle, hasta no dar una respuesta valida no 
            # dejara de mostrarse
        
            else:
                print("""     
+--------------------------------------------------------------------+
|                       Opcion no valida                             |    
+--------------------------------------------------------------------+
                      """)
            # Manejo de ingreso de caracteres de cadena

        except ValueError as e:
            print(f"""     
+--------------------------------------------------------------------+
|                       Error: {e}                                   |    
+--------------------------------------------------------------------+
                      """)            
            continue
        
            # Ciclo para seguir generando perimetros y areas de otras figuras
        
        while True:
            try:
                otra = input("""
+--------------------------------------------------------------------+
|  Desea seguir calculando area y perimetro de alguna otra figura    |    
+--------------------------------------------------------------------+
                             """).strip().lower()
                if otra == 'no':
                    print("""
+--------------------------------------------------------------------+
|                           Hasta la proxima                         |    
+--------------------------------------------------------------------+                        
                          """)
                    exit()
                elif otra == "si":
                    main()
                else:
                    print("""         
+--------------------------------------------------------------------+
|                       Respuesta no valida                          |    
+--------------------------------------------------------------------+
                          """)
                    
            except ValueError:
                print("""         
+--------------------------------------------------------------------+
|                       Respuesta no valida                          |    
+--------------------------------------------------------------------+
                          """)
                main()
            # Funcion "if __name__ == "__main__"" para la implementacion de
            # la modularizacion
        
if __name__ == "__main__":
    main()