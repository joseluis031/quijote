import PyPDF2

def descifrar_mensaje(libro_quijote, coordenadas):
    palabras_descifradas = []  # Lista para almacenar las palabras descifradas
    
    with open(libro_quijote, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        
        for coord in coordenadas:
            pagina_num, indice_linea, indice_palabra = map(int, coord.split(':'))
            try:
                texto_pagina = pdf_reader.pages[pagina_num - 1].extract_text()
                lineas = texto_pagina.split('\n')
                palabra = lineas[indice_linea - 1].split()[indice_palabra - 1]
                palabras_descifradas.append(palabra)
            except (IndexError, KeyError):
                pass
    mensaje = '_'.join(palabras_descifradas)    
    return mensaje

# Ruta del PDF
libro_quijote = 'quijote.pdf'

# Coordenadas de desencriptación
coordenadas = [
    '18:9:2',
    '33:14:1',
    '40:9:2',
    '40:27:7',
    '45:2:7',
    '163:20:10',
    '163:12:8',
    '164:12:5'
]

# Descifrar el PDF utilizando las coordenadas
texto_descifrado = descifrar_mensaje(libro_quijote, coordenadas)

# Imprimir el texto descifrado con las palabras separadas por guion bajo
print('flag{' + texto_descifrado + '}')
