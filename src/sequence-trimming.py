'''
NAME
    sequence-trimming

VERSION
    1.0

AUTHOR
    Gabriel Ramirez Vilchis

GITHUB
    https://github.com/gabrielramirezv/Programacion_en_Python/blob/master/src/sequence-trimming.py

DESCRIPTION
    Corta los adaptadores de las secuencias que se encuentran en el 
    archivo data/4_input_adapters.txt, sabiendo que los adaptadores 
    se encuentran en las posiciones 1 a 14

CATEGORY
    DNA sequence

USAGE
    py src/sequence-trimming.py

ARGUMENTS
    None

INPUT
    Archivo con secuencias data/4_input_adapters.txt

OUTPUT
    Archivo con secuencias sin adaptadores
    results/4_output_no_adapters.txt

SEE ALSO
    None

'''

## 1. Inicio

## 2. Abrir archivo, guardar secuencias en una lista y cerrar archivo
sequences_file = open("data/4_input_adapters.txt", 'r')
sequences_list = sequences_file.readlines()
sequences_file.close()

## 3. Abrir nuevo archivo, escribir cada secuencia sin adaptadores y 
##    cerrar archivo
no_adapters_file = open("results/4_output_no_adapters.txt", 'a')

for sequence in sequences_list:
    no_adapters_sequence = sequence[14:]
    no_adapters_file.write(no_adapters_sequence)

no_adapters_file.close()

## 4. Informar al usuario que el archivo sin adaptadores se ha creado
print("\nSe ha generado el archivo 4_output_no_adapters.txt \
      \nEl archivo se encuentra disponible en la carpeta results/ \n")

## 5. Fin
