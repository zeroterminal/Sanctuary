import socket, ssl, time

HOST       = "127.0.0.1"
PORT       = 6667
CHANNEL    = '#home'
bot        = "Sanctuary"
password   = ""


def connect():
	IDENT      = "MADSCIENTIST"
	REALNAME   = "meow"
	MASTER     = "ZERO"
	s = socket.socket()
	s.connect((HOST, PORT))
  ## Functions 
  ############################  
  
	def send_command(mycommand):
		return s.send(bytes(mycommand, "UTF-8"))

	def message_user(user, message):
		return s.send(bytes("PRIVMSG %s %s" %(user, message), "UTF-8"))

	def message_channel(channel, message):
		return s.send(bytes("PRIVMSG #%s %s" %(channel, message), "UTF-8"))

	def identify():
		return s.send(bytes("PRIVMSG NICKSERV :identify Sanctuary AthenasBase" ,"UTF-8"))

	def obey_command(user, command):
		pass


	send_command("NICK %s \r\n" % bot)
	send_command("USER %s %s bla : %s\r\n" % (IDENT, HOST, REALNAME))


	while 1:
		# Format Notice
		#################
		data = s.recv(1024).decode("UTF-8")
		v = data.split('\n')
		formatNotice = v[0]

		## Format Channel Message
		#########################
		if 'PING' in formatNotice:
			xvvv = formatNotice.replace("PING :", "")
			send_command('PONG : %s' %xvvv)


    
		if data.find ('If it is your') != -1:
			send_command('PRIVMSG nickserv IDENTIFY Sanctuary ' + password + ' \r\n') # This should be changed with the variable


		if 'PRIVMSG #home' in formatNotice:
			## CHANNEL USER MESSAGES
			########################
			disectNotice  = formatNotice.split(':')
			message       = disectNotice[2]

			## CHANNEL USER
			########################
			disectNoticeString = ''.join(disectNotice)
			vv     = disectNoticeString.split()
			vvv    = vv[0:1]
			vvvv   = ''.join(vvv)
			vvvvv  = vvvv.replace(":","").replace("!","").split(".")
			user   = vvvvv[0]

			if user == MASTER:
				if message.startswith("-kick"):
					try: # without this bot will get disconnected.
						m   = message.split(" ")
						del m[0]
						kickuser = m[0]
						reason   = m[1]
						send_command("KICK #home %s %s" %(kickuser, reason))
					except Exception as a:
						send_command("KICK #home %s %s" %(kickuser, "out"))




		if 'google' in formatNotice:
			message_channel("#home", "no you google. lazy faggot")

		print(formatNotice)

connect()
