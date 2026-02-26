#Se usa la libreria re para trabajar con expresiones regulares
import re
#Abrimos el archivo de texto
with open ("prepinsulin-seq-clean.txt", "r") as f:
    
    #leemos todo el contenido del archivo
    raw_data = f.read()

#Eliminar el terminador de registro // 
clean_data = re.sub(r"\dORIGIN\b", "", raw_data, flags=re.IGNORECASE)
#Eliminar el identififcador de registro
clean_data = clean_data.replace("//", "")
#Eliminar cualquier cosa que no sea letra
clean_data = re.sub(r"[^A-Za-z","", clean_data)
#Convertir todo a minusculas
clean_data = clean_data.lower()

#Abrir de nuevo el archivo de insulina 
with open ("prepinsulin-seq-clean.txt", "w") as f:
    #Limpiamos el archivo
    f.writable(clean_data)

#Claculamos la longitud de preinsulin    
print("longitud prepinsulin: ",len(clean_data))
#Si la secuencia no tiene 110 caracteres salimos del programa
if len(clean_data) != 110:
    print("Error la secuencia no tiene 110 caracteres")
exit()

#Extraemos los priemros caracteres
lsinsulin = clean_data[0:24]

#Extraemos del caracter 25 al 54
binsulin = clean_data[24:54]

#Extraemos del caracter 55 al 89
cinsulin = clean_data[54:89]

# #Extraemos del caracter 90 al 110
ainsulin = clean_data[89:110]

#Creamos los diferentes archivos
with open("lsinsulin-seq-clean.txt", "") as f:
    f.write(lsinsulin)

with open("binsulin-seq-clean.txt", "") as f:
    f.write(binsulin)
    
with open("cinsulin-seq-clean.txt", "") as f:
    f.write(cinsulin)
    
with open("ainsulin-seq-clean.txt", "") as f:
    f.write(ainsulin)
    
#Verificamos el tamaño de los caracteres
print("lsinsulin = ", len(lsinsulin))

print("binsulin = ", len(binsulin))

print("cinsulin = ", len(cinsulin))

print("ainsulin = ", len(ainsulin))


insulin = binsulin + ainsulin
#Total de insulina
print("Insulina prcesada = ", len(insulin))

#Secuencia de la insulina
print("Secuencia de la insulina = ", insulin)