#!/usr/bin/env python3

import socket

sock=socket.socket()

sock.bind(('0.0.0.0',2222))
sock.listen(1)
conn,addr=sock.accept()
while True:
	data=conn.recv(1024)
	if not data:
		break
	conn.send(data.upper())
conn.close()
