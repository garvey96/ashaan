# harvey golonka
# test access to emails via IMAP server
# non fucntional
# imaplib.IMAP4.error: b'[AUTHENTICATIONFAILED] Invalid credentials (Failure)'

import imaplib
import email
from email.header import decode_header
import webbrowser
import os

# account credentials
username = "evieliott21@gmail.com"
password = "qwert12345!@#$%"
# use your email provider's IMAP server, you can look for your provider's IMAP server on Google
# or check this page: https://www.systoolsgroup.com/imap/
# for office 365, it's this:
imap_server = "imap.gmail.com"

def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)


# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL(imap_server)
# authenticate
imap.login(username, password)


