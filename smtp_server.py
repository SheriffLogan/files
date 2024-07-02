# import smtplib

# smtp_server = "mail.smtp2go.com"
# smtp_port = 587
# smtp_username = "support@leadcured.com"
# smtp_password = "Leadcured@2024!"
# to_email = "harshit.leadcured@gmail.com"

# Message = """Subject: Test Mail from pyhton
# Hi All,

# This is a test mail from backend python.

# Thanks,
# Harshit"""

# try:
#     with smtplib.SMTP(smtp_server, smtp_port) as server:
#         server.set_debuglevel(1)  # Enable debug output
#         print("Connecting to the SMTP server...")
#         status_code, response = server.ehlo()
#         print(f"[*] Echoing the server : {status_code} {response}")
#         status_code, response = server.starttls()  # Secure the connection
#         print(f"[*] Starting TLS connection : {status_code} {response}")
#         server.login(smtp_username, smtp_password)
#         print("Login successful!")
#         server.sendmail(smtp_username, to_email, Message)
#         server.quit()
# except Exception as e:
#     print(f"Error: {e}")

import smtplib

HOST = "mail.smtp2go.com"
PORT = 587

FROM_EMAIL = "support@leadcured.com"
TO_EMAIL = "harshit.leadcured@gmail.com"
PASSWORD = "Leadcured@2024!"

MESSAGE = """Subject: Test Email from python
Hi,

This is a test mail from backend python.

Thanks,
Harshit
"""

print("[*] Starting SMTP process")

try:
    smtp = smtplib.SMTP(HOST, PORT)
    print("[*] Connected to SMTP server")
except Exception as e:
    print(f"[!] Failed to connect to SMTP server: {e}")
    raise

try:
    print("[*] Sending EHLO command")
    status_code, response = smtp.ehlo()
    print(f"[*] Echoing the server: {status_code} {response}")
except Exception as e:
    print(f"[!] Failed to EHLO: {e}")
    raise

try:
    print("[*] Starting TLS connection")
    status_code, response = smtp.starttls()
    print(f"[*] Starting TLS connection: {status_code} {response}")
except Exception as e:
    print(f"[!] Failed to start TLS: {e}")
    raise

try:
    print("[*] Logging in to SMTP server")
    status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
    print(f"[*] Logging in: {status_code} {response}")
except Exception as e:
    print(f"[!] Failed to log in: {e}")
    raise

try:
    print("[*] Sending email")
    smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
    print("[*] Email sent successfully")
except Exception as e:
    print(f"[!] Failed to send email: {e}")
    raise

try:
    print("[*] Terminating SMTP session")
    smtp.quit()
    print("[*] SMTP session terminated")
except Exception as e:
    print(f"[!] Failed to terminate SMTP session: {e}")
    raise

print("[*] SMTP process completed")
