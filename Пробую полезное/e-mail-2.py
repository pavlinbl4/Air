import imaplib
import credentials

imap_ssl_host = 'imap.gmail.com'
imap_ssl_port = 993
username = credentials.email
password = credentials.passwd
server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)

server.login(username, password)
server.select('INBOX')

data = server.uid('search',None, '(SUBJECT "MY QUERY HERE!")')
print(data)