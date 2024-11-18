import smtplib
from email.message import EmailMessage

# Dados do e-mail.
subject = "Assunto do Email"
body = "Este e o corpo da mensagem"
sender = "a@gmail.com"
recipient = "a@gmail.com"

attachment = ""

# Dados de conexão.
server = "smtp.gmail.com"
port = 587
username = "a@gmail.com"
password = ""

print('Inicializado.')

# Montando a mensagem com MIMEText.
print('Criando a sua mensagem de e-mail.')
try: 
    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = recipient
    message.set_content(body)
    print('Sucesso.')
except:
    print('Não foi possível criar a mensagem de e-mail.')
    print('Aconteceu algum erro ao montar o objeto com o EmailMessage.')
    print('Confira se a mensagem possui caracteres especiais ou incomuns.')

# Adicionando o anexo.
print('Verificando a existência de anexo.')
if attachment != '':
    try:
        file = open(attachment, 'rb')
        file.close()
        print('Sucesso.') 
    except:
        file.close()
        print('Não foi possível localizar o arquivo de anexo.')
        print('Verifique se informou corretamente.')
        print(attachment)

    print('Adicionando o anexo na menssagem.')
    try:
        with open(attachment, 'rb') as patch:
            data = patch.read()
            name = patch.name

        message.add_attachment(data, maintype = 'application', subtype = 'octet-stream', filename = name)
        patch.close()
        print('Sucesso.')
    except:
        patch.close()
        print('Ocorreu um erro ao tentar adicionar o seu anexo a mensagem.')
        print('Verifique a integridade do arquivo.')
else:
    print('Nenhum anexo informado.')
    attachment = ''

# Iniciando starttls.
with smtplib.SMTP(server, port) as smtp:
    print('Iniciando a criptografia starttls.')
    try:
        smtp.starttls()
        print('Sucesso.')
    except:
        print('Não foi possível iniciar a criptografia starttls.')
        print('server = ' + server + ', port = ' + port + '.')
        print('Experimente outra porta ou método de autenticação.')

# Conectando no servidor.
    print('Autenticando o usuário: ' + username + '.')
    try:
        smtp.login(username, password)
        print('Sucesso.')
    except:
        print('Não foi possível autenticar o usuário ou a senha.')
        print('Verifique se digitou os dados corretamente.')
        print('Entre em contato com o provedor de e-mail.')

# Enviando a mensagem.
    print('Enviando a mensagem de e-mail.')
    try:
        smtp.send_message(message)
        print('Sucesso.')
        smtp.close()
    except:
        smtp.close()
        print('Não foi possível enviar a mensagem de e-mail.')
        print('Falha no método send_message(objeto.EmailMessage).')
        print('Entre em contato com o desenvolvimento.')

print('Finalizado.')

