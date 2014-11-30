#!/usr/bin/python
# -*- coding: utf8 -*-

import socket
import tkinter as tk

up = False
down = False
right = False
left = False

commande = bytes('S', 'mac_roman')

root = tk.Tk()
root.geometry('600x200')
text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
text.pack()

robotSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Hote = '192.168.43.188'
Port = 2323
robotSocket.connect((Hote,Port))

text.insert('end', 'WiRobot Controller is connected...\n')
#text.insert('end', 'Use <UpKey>, <DownKey>, <RightKey> and <LeftKey> to control the WiRobot.')
text.insert('end', 'Use _ArrowKeys_ to control the WiRobot.')

def updateCommande():
	global commande
	if up:
		if down:
			commande = bytes('S', 'mac_roman')
			return
		if right:
			commande = bytes('D', 'mac_roman')
			return
		if left:
			commande = bytes('H', 'mac_roman')
			return
		commande = bytes('F', 'mac_roman')
		return
	if down:
		if right:
			commande = bytes('G', 'mac_roman')
			return
		if left:
			commande = bytes('J', 'mac_roman')
			return
		commande = bytes('B', 'mac_roman')
		return
	if right:
		if left:
			commande = bytes('S', 'mac_roman')
			return
		commande = bytes('R', 'mac_roman')
		return
	if left:
		commande = bytes('L', 'mac_roman')
		return
	commande = bytes('S', 'mac_roman')
	return

def pushCommande():
	updateCommande()
	robotSocket.send(commande)

def upKeyPress(event):
	global up
	if not up:
		up = True
		pushCommande()

def upKeyRelease(event):
	global up
	if up:
		up = False
		pushCommande()

def downKeyPress(event):
	global down
	if not down:
		down = True
		pushCommande()

def downKeyRelease(event):
	global down
	if down:
		down = False
		pushCommande()

def rightKeyPress(event):
	global right
	if not right:
		right = True
		pushCommande()

def rightKeyRelease(event):
	global right
	if right:
		right = False
		pushCommande()

def leftKeyPress(event):
	global left
	if not left:
		left = True
		pushCommande()

def leftKeyRelease(event):
	global left
	if left:
		left = False
		pushCommande()

root.bind('<KeyPress-Up>', upKeyPress)
root.bind('<KeyRelease-Up>', upKeyRelease)
root.bind('<KeyPress-Down>', downKeyPress)
root.bind('<KeyRelease-Down>', downKeyRelease)
root.bind('<KeyPress-Right>', rightKeyPress)
root.bind('<KeyRelease-Right>', rightKeyRelease)
root.bind('<KeyPress-Left>', leftKeyPress)
root.bind('<KeyRelease-Left>', leftKeyRelease)
root.mainloop()

client.close()