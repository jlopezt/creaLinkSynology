import os
import sys

def creaLink(url):
  return f"<a href='{url}'>{url}</a>"

archivo_entrada = open(sys.argv[1], "r")
archivo_salida = open("salida.txt", "w")

for linea in archivo_entrada:
  link = creaLink(linea)

  archivo_salida.write(f"{linea} {link}\n")

archivo_entrada.close()
archivo_salida.close()
