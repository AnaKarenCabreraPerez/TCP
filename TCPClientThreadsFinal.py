import socket

def Main():
	serverName="192.168.127.220"
	serverPort=12001
	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientSocket.connect((serverName, serverPort))

	print("Elige una opcion:")
	print("a. Hora del servidor")
	print("b. BuscaLetras")
	print("c. Contenido de directorio")

	opc = str(input())
	print(opc)
	while True:
		if opc == "a":
			clientSocket.send(opc.encode())
			hora = clientSocket.recv(1024)
			print("From Server:", hora.decode())
		elif opc == "b":
			clientSocket.send(opc.encode())
			frase = clientSocket.recv(1024)
			print("From Server:", frase.decode())
			palabra = str(input())
			clientSocket.send(palabra.encode())
			palabraf= clientSocket.recv(1024)
			print("From Server: ",palabraf.decode())
		elif opc == "c":
			clientSocket.send(opc.encode())
			modifiedSentence = clientSocket.recv(1024)
			print("From Server:", modifiedSentence.decode())
		else:
			clientSocket.close()
		r = input("Continuar: S,N")
		if r == "s":
			continue
		else:
			break
	clientSocket.close()

if __name__ == '__main__':
	Main()
