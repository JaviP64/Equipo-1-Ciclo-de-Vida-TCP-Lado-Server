# Biblioteca para conexiones TCP/UDP
import socket

# 1. socket(): crear el socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. bind(): asociar el socket a una dirección y puerto
s.bind(('', 34567))

# 3. listen(): poner el socket en modo escucha
s.listen(1)

# 4. accept(): aceptar una conexión entrante
conn, addr = s.accept()
print('Conectado por', addr)

# 5. send()/recv(): Envía/recibe bits de información
#	- Se codifica primero el mensaje
texto = "Hola Grupo de la Tarde!"
textoCodificado = texto.encode("UTF-8")

#	- Se envia despues
conn.send(textoCodificado)

# usar el socket devuelto por accept() para comunicarse, no el original
conn.close()
s.close()
