"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

def pregunta_01():
    suma_segunda_columna = 0
    with open("data.csv","r") as data:
        for linea in data:
            
            col = linea.strip().split('\t')
            if len(col) >= 2:
            
                valor_segunda_columna = int(col[1])
                suma_segunda_columna += valor_segunda_columna
 

    return suma_segunda_columna


def pregunta_02():
    recuento_letras = {}
    with open("data.csv","r") as data:
        for linea in data:
            # Dividir la línea en columnas utilizando el separador de tabulación ("\t")
            col = linea.strip().split('\t')
            
            # Verificar si hay al menos una columna en la línea
            if len(col) >= 1:
                # Obtener la primera letra de la primera columna
                primera_letra = col[0][0].upper()  # Convertir a mayúscula
                
                # Actualizar el recuento de la letra en el diccionario
                if primera_letra in recuento_letras:
                    recuento_letras[primera_letra] += 1
                else:
                    recuento_letras[primera_letra] = 1

        lista_tuplas = sorted(recuento_letras.items())

    return lista_tuplas


def pregunta_03():
    suma_por_letra = {}
    with open("data.csv","r") as data:

        for linea in data:
            columnas = linea.strip().split('\t')

            if len(columnas) >= 2:
                letra_columna1 = columnas[0]
                valor_columna2 = int(columnas[1])
                

                if letra_columna1 in suma_por_letra:
                    suma_por_letra[letra_columna1] += valor_columna2
                else:
                    suma_por_letra[letra_columna1] = valor_columna2


        lista_tuplas = list(suma_por_letra.items())


        lista_tuplas.sort(key=lambda x: x[0])

    return lista_tuplas


def pregunta_04():
 
    recuento_por_mes = {}
    with open("data.csv","r") as data:
        for linea in data:
            col = linea.strip().split('\t')
            
            if len(col) >= 3:
                fecha = col[2]
                dividirfecha = fecha.split('-')
                if len(dividirfecha) == 3:
                    mes = dividirfecha[1]
                    if mes in recuento_por_mes:
                        recuento_por_mes[mes] += 1
                    else:
                        recuento_por_mes[mes] = 1

    # Crear una lista de tuplas a partir del diccionario y ordenarla por mes
        lista_tuplas = sorted(recuento_por_mes.items())
    return lista_tuplas


def pregunta_05():
    max_min_por_letra = {}
    with open("data.csv","r") as data:
        for linea in data:
            
            col = linea.strip().split('\t')
            
            if len(col) >= 2:
                letra = col[0]
                valor_col2 = int(col[1])
                
                if letra in max_min_por_letra:
                    max_valor, min_valor = max_min_por_letra[letra]
                    max_valor = max(max_valor, valor_col2)
                    min_valor = min(min_valor, valor_col2)
                    max_min_por_letra[letra] = (max_valor, min_valor)
                else:
                    max_min_por_letra[letra] = (valor_col2, valor_col2)

        lista_tuplas = [(letra, max_valor, min_valor) for letra, (max_valor, min_valor) in max_min_por_letra.items()]

        lista_tuplas.sort(key=lambda x: x[0])

    return lista_tuplas


def pregunta_06():
    valores_minimos_maximos = {}
    with open("data.csv","r") as data:

        for linea in data:
            columnas = linea.strip().split('\t')
            
            if len(columnas) >= 5:
                valores_columna5 = columnas[4].split(',')  

                for valor in valores_columna5:
                    clave, valor_asociado = valor.split(':')
                    clave = clave.strip()
                    valor_asociado = int(valor_asociado)
                    
                    if clave in valores_minimos_maximos:
                        min_valor, max_valor = valores_minimos_maximos[clave]
                        min_valor = min(min_valor, valor_asociado)
                        max_valor = max(max_valor, valor_asociado)
                        valores_minimos_maximos[clave] = (min_valor, max_valor)
                    else:
                        valores_minimos_maximos[clave] = (valor_asociado, valor_asociado)

        lista_tuplas = [(clave, min_valor, max_valor) for clave, (min_valor, max_valor) in valores_minimos_maximos.items()]

        lista_tuplas.sort(key=lambda x: x[0])
 
    return lista_tuplas


def pregunta_07():
    asociaciones = {}
    with open("data.csv","r") as data:
        for linea in data:
            col = linea.strip().split('\t')
            
            if len(col) >= 3:
                valor_col2 = int(col[1])
                letra_col1 = col[0]
                
                if valor_col2 in asociaciones:
                    asociaciones[valor_col2].append(letra_col1)
                else:
                    asociaciones[valor_col2] = [letra_col1]

        lista_tuplas = [(valor, letras) for valor, letras in asociaciones.items()]

        lista_tuplas.sort(key=lambda x: x[0])
    return lista_tuplas


def pregunta_08():

    asociaciones = {}
    with open("data.csv","r") as data:
        for linea in data:

            columnas = linea.strip().split('\t')
            if len(columnas) >= 3:
                valor_columna2 = int(columnas[1])
                letra_columna1 = columnas[0]

                if valor_columna2 in asociaciones:
                    if letra_columna1 not in asociaciones[valor_columna2]:
                        asociaciones[valor_columna2].append(letra_columna1)
                else:
                    asociaciones[valor_columna2] = [letra_columna1]

        lista_tuplas = [(valor, sorted(letras)) for valor, letras in asociaciones.items()]

        lista_tuplas.sort(key=lambda x: x[0])

    return lista_tuplas


def pregunta_09():
    recuento_claves_columna5 = {}
    with open("data.csv","r") as data:
        for linea in data:
            columnas = linea.strip().split('\t')

            if len(columnas) >= 5:
                claves = columnas[4].split(',')
                
                for clave in claves:
                    clave = clave.split(':')[0]  
                    clave = clave.strip()  
                    
                    if clave in recuento_claves_columna5:
                        recuento_claves_columna5[clave] += 1
                    else:
                        recuento_claves_columna5[clave] = 1

    return recuento_claves_columna5


def pregunta_10():
    lista_tuplas = []
    with open("data.csv","r") as data:

        for linea in data:
            columnas = linea.strip().split('\t')

            if len(columnas) >= 5:
                letra_columna1 = columnas[0]

                elementos_columna4 = columnas[3].split(',')
                elementos_columna5 = columnas[4].split(',')
                lista_tuplas.append((letra_columna1, len(elementos_columna4), len(elementos_columna5)))

    return lista_tuplas


def pregunta_11():

    suma_por_letra = {}
    with open("data.csv","r") as data:
        for linea in data:
            columnas = linea.strip().split('\t')

            if len(columnas) >= 4:
                letras_columna4 = columnas[3].split(',')  
                valor_columna2 = int(columnas[1])
                
                for letra in letras_columna4:
                    letra = letra.strip()  
                    if letra in suma_por_letra:
                        suma_por_letra[letra] += valor_columna2
                    else:
                        suma_por_letra[letra] = valor_columna2


        suma_por_letra_ordenada = dict(sorted(suma_por_letra.items()))

    return suma_por_letra_ordenada


def pregunta_12():
    suma_por_letra_columna1 = {}
    with open("data.csv","r") as data:

    
        for linea in data:
            
            columnas = linea.strip().split('\t')
            
            if len(columnas) >= 5:
                letra_columna1 = columnas[0]
                valores_columna5 = columnas[4].split(',') 
                
                suma = sum(int(valor.split(':')[1]) for valor in valores_columna5)
                
                if letra_columna1 in suma_por_letra_columna1:
                    suma_por_letra_columna1[letra_columna1] += suma
                else:
                    suma_por_letra_columna1[letra_columna1] = suma

    return suma_por_letra_columna1