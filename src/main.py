import csv, json, sys
from tabulate import tabulate

def buscar_ciudades (pais, archivo):
    """que pesao"""
    try:

        ciudades = list()
        if 'csv' in archivo:
            with open(archivo, 'r') as c:
                lector_csv= csv.reader(c,delimiter=',')
                ciudades.append(next(lector_csv))
                for linea in lector_csv:
                    if pais in linea[2]:
                        ciudades.append(linea)

        elif 'json' in archivo:
            with open( archivo,'r') as j:
                lector_json = json.load(j)
                ciudades.append(list(lector_json[0].keys()))
                for dict_ciudades in lector_json:
                    if pais in dict_ciudades['Country']:
                        ciudades.append(list(dict_ciudades.values()))

        else:
            raise IndexError
    except(IndexError, FileNotFoundError):
        print(f'Archivo {archivo} no encontrado o formato no soportado')
        sys.exit(0)

    return ciudades

def imprimir_busqueda(ciudades):
    """que pesao"""
    ciudades [0][0]='Ranking'
    total_ciudades = len (ciudades)-1
    print('Ciudades encontradas: ', total_ciudades)
    if total_ciudades >0:
        print(tabulate(ciudades,headers="firstrow",tablefmt="grid"))
    
    return total_ciudades



def guardar_busqueda(pais, ciudades):
    """que pesao"""
    formato = input('ecribe csv o json para guardar en ese formato. O x para salir: ')
    archivo_pais = pais+'.'+formato
    respuesta = f'Archivo guardado como: {archivo_pais}'
    
    if formato== 'csv':
        with open(archivo_pais, 'w') as c:
            escritor_csv = csv.writer(c,delimiter=',')
            for linea in ciudades:
                escritor_csv.writerow(linea)
    elif formato == 'json':
        lista_ciudades = list()
        llaves = ciudades.pop(0)
        
        for valores in ciudades:
            dict_ciudad = dict (zip(llaves,valores))
            lista_ciudades.append(dict_ciudad)
        with open(archivo_pais, 'w') as j:
            json.dump(lista_ciudades,j,indent=4)
    else:
        respuesta = 'Archivo no guardado.'

    print(respuesta)
            

if __name__ == "__main__":
    archivo =input('Archivo origen: ')
    pais =input('pais a buscar: ')

    ciudades = buscar_ciudades(pais, archivo)
    imprimir_busqueda(ciudades)
    guardar_busqueda(pais,ciudades)
