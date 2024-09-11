datos = [
"Datos de informacion en la linea 1", 
"Datos de informacion en la linea 2", 
"Datos de informacion en la linea 3", 
"Datos de informacion en la linea 4",
"Datos de informacion en la linea 5",
]
nombre_archivo ="archivo.txt"

def registrar_datos(archivo, lista):
    ruta = f"./{archivo}"
    try:
        with open(ruta, "w") as nuevo_archivo:
            nuevo_archivo.write("\n".join(lista))

    except Exception as error: 
       print('Se ha generado un error no previsto', type(error).__name__)        


def lectura_archivo(archivo): 
   try: 
       with open(archivo, 'r') as archivo_leer:
        contenido = archivo_leer.read() 
        #contenido = archivo.readlines() 
        print(contenido) 
   except FileNotFoundError: 
       print('No se encuentra el {archivo} ') 
   except Exception as error: 
       print('Se ha generado un error ', type(error).__name__)     
 


def main(nombre, data):
        registrar_datos(nombre, data)
        

main(nombre_archivo, datos)

lectura_archivo(nombre_archivo)