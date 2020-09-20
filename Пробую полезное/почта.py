import imaplib
import email

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login("calvoegrasso@gmail.com","15deadman")
mail.select('inbox')