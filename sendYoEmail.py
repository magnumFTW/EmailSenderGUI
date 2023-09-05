import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendMail():
    message = MIMEMultipart("alternative")
    message["Subject"] = body_var.get()
    message["From"] = "<YOUR_EMAIL_HERE>"
    message["To"] = fentry_str.get()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    body = body_var.get()

    message.attach(MIMEText(body, "plain"))
    server.login('<YOUR_EMAIL_HERE>', '<YOUR_APP-PASS_HERE>')
    server.sendmail('<YOUR_EMAIL_HERE>', fentry_str.get(), message.as_string())
    server.quit()
    output_string.set('Yo attachments has been sent')
    # title_label.config(text = 'Yo attachments has been sent')
    # title_label['state'] = 'disabled'

#window
window = ttk.Window(themename = 'journal')
window.title('Email')
window.geometry('600x600')

#title
title_label = ttk.Label(master = window, text = 'Email Sender', font = 'Calibri 20 bold')
title_label.pack(pady = 10)


#input field
input_frame = ttk.Frame(master = window)
title_labell = ttk.Label(input_frame, text = 'Enter the email you want to send ', font = 'Calibri 12 bold')
fentry_str = tk.StringVar()
fentry = ttk.Entry(master = input_frame, textvariable = fentry_str)
title_labell.pack()
fentry.pack(pady = 10)
input_frame.pack(pady = 10)
title_labels = ttk.Label(master = input_frame, text = 'Compose email', font = 'Calibri 12 bold')
body_var = tk.StringVar()
body = tk.Entry(master = input_frame, width = 50, font = ('Arial', 18), textvariable = body_var)
button = ttk.Button(master = input_frame, text = 'send', command = sendMail)
title_labels.pack(side = 'top')
body.pack(pady = 20)
button.pack(pady = 10)



output_string = tk.StringVar()
output_label = ttk.Label(master = window, font = 'Calibri 20 bold', textvariable = output_string) 
output_label.pack(pady = 5)

#run
window.mainloop()