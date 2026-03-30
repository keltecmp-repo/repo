import os
import sys
import base64
import zlib
# CAMINHO DO SCRIPT 
dir_path = os.path.dirname(os.path.realpath(__file__))

nome_script = input('Digite o nome do script python para ofuscar: ')
salvar = input('Digite o nome do script python para salvar: ')
try:
    max_camadas = int(input('Digite o numero de camadas: '))
except:
    print('numero invalido será usado 5 camadas!')
    max_camadas = 5


if os.path.isfile(nome_script):
    with open(nome_script, 'r', encoding='utf-8') as f:
        try:
            codigo = f.read().encode('utf-8')
        except:
            codigo = f.read()
        camadas = 0
        while True:
            camadas +=1
            codigo_comprimido_zlib = zlib.compress(codigo) 
            codigo_base64 = base64.b64encode(codigo_comprimido_zlib)
            invertido = codigo_base64[::-1]
            codigo = f"exec((_)({invertido}))".encode('utf-8')
            if camadas == max_camadas:
                try:
                    codigo = codigo.decode('utf-8')
                except:
                    pass
                break
        py = os.path.join(dir_path, salvar)
        with open(py,'w', encoding='utf-8') as f2:
            file = f"_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));{codigo}"
            f2.write(file)
            print('Arquivo salvo em: ',py)

