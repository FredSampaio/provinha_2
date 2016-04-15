import socket as s
	
def html():
	return '''<html>\n
<head><title>EMAIL</title></head>\n
<body>\n
  <h2>EMAIL</h2>\n
  <form method="get" action="/bin/login">\n
    Email: <input type="text" name="user" size="25" /><br /><br />\n
    Assunto: <input type="text" name="sub" size="50" /><br /><br />\n  
    Conteudo: <input type="text" name="pw" size="100" /><br /><br />\n  
    <input type="submit" value="SEND" />\n
  </form>\n
</body>\n
</html>'''
	
def pegaemail(ip, porta):
	try:
		serversocket=s.socket(s.AF_INET, s.SOCK_STREAM)
		serversocket.bind((ip, porta))
		serversocket.listen(1)
		while True:
			c, addr=serversocket.accept()
			c.send(html().encode())
			mensagem=c.recv(2048).decode()
			c.close()
			if "login?user=" in mensagem:
				email=mensagem.split("user=")[1].split("&sub=")[0]
				assunto=mensagem.split("&sub=")[1].split("&pw=")[0]
				conteudo=mensagem.split("&pw=")[1].split(" ")[0]
				break
		serversocket.close()
		email=email.replace("%40", "@")
		assunto=assunto.replace("+", " ")
		conteudo=conteudo.replace("+", " ")
		return (email, assunto, conteudo)
	except OSError:
		print("Impossivel se conectar.")
		return('freddysampaio9@gmail.com', "Erro", "Nao foi possivel se concectar ao usuario")
	
if __name__=="__main__":
	(email, assunto, conteudo)=pegaemail("172.26.182.43", 80)
	print("\n\n"+email+"\n"+assunto+"\n"+conteudo+"\n\n")
