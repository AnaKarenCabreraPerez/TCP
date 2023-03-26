import socket
import datetime
import os

from _thread import *
import threading

print_lock = threading.Lock()


def threaded(connectionSocket):
	while True:
		condicion = connectionSocket.recv(1024)
		print(condicion.decode())
		if condicion.decode() == "a":
			hora_actual = datetime.datetime.now()
			hora = str(hora_actual)
			connectionSocket.send(hora.encode())
		elif condicion.decode() == "b":
			connectionSocket.send("Ingrese la frase".encode())
			palabra = connectionSocket.recv(1024)
			letras = palabra.decode().count("s")
			letras_str = str(letras)
			connectionSocket.send(letras_str.encode())
		elif condicion.decode() == "c":
			path = "/home"
			dir_list = os.listdir(path)
			connectionSocket.send(str(dir_list).encode())
		else:
			print("Haz deeeeeeeeeeee")
		print_lock.release()
	connectionSocket.close()


def Main():

	serverPort = 12001
	serverSocket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serverSocket.bind(("",serverPort))
	serverSocket.listen(5)

	print("Servidor listo para recibir TCP")

	while 1:
		connectionSocket, addr = serverSocket.accept()

		print_lock.acquire()

		print('Connected to :', addr[0], ':', addr[1])

		start_new_thread(threaded,(connectionSocket,))
	serverSocket.close()


if __name__ == '__main__':
	Main()
