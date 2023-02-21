import smtplib

# Configurações do servidor SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Credenciais da conta de e-mail
username = 'seu_email@gmail.com'
password = 'sua_senha'

# Criação do objeto SMTP
smtp_obj = smtplib.SMTP(smtp_server, smtp_port)
smtp_obj.starttls()
smtp_obj.login(username, password)

# Criação da mensagem de e-mail
destinatario = 'destinatario@email.com'
assunto = 'Assunto do e-mail'
mensagem = 'Corpo do e-mail'

msg = f'Subject: {assunto}\n\n{mensagem}'

# Envio do e-mail
smtp_obj.sendmail(username, destinatario, msg)

# Encerramento da conexão SMTP
smtp_obj.quit()

print('E-mail enviado com sucesso!')
