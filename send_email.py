# import requests
# import json

# url = "https://onojjgncd7hgqtiq7vonkhsodi0nsaxl.lambda-url.ap-south-1.on.aws/"


# def send_email(people_list , email_subject, email_body):
    
#     payload = json.dumps({
#     "people_list":people_list ,
#     "email_subject":email_subject,
#     "email_body": email_body
#     })
#     headers = {
#     'Content-Type': 'application/json'
#     }

#     response = requests.request("POST", url, headers=headers, data=payload)

#     return "email sent"

import smtplib
from email.message import EmailMessage
import logging

# Configure logging
logging.basicConfig(filename='email_log.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def send_email(people_list, email_subject, email_body):
    smtp_server = "mail.smtp2go.com"  # SMTP2GO server
    smtp_port = 587  # SMTP2GO port for TLS/STARTTLS
    smtp_username = "leadcured.com"  # Replace with your SMTP2GO username
    smtp_password = "Leadcured@2024!"  # Replace with your SMTP2GO password
    
    
    for person in people_list:
        msg = EmailMessage()
        msg['To'] = person['email']
        msg['From'] = "support@leadcured.com"  # Replace with your email
        msg['Subject'] = email_subject
        msg.set_content(email_body, subtype='html')
        
        # Add a tracking pixel to the email body
        # tracking_pixel_url = "http://localhost:5000/track"
        # email_body_with_tracking = email_body + f'<img src="{tracking_pixel_url}" alt="" style="display:none;">'
        # msg.set_content(email_body_with_tracking, subtype='html')


        logging.debug(f"Preparing to send email to {person['email']} with subject '{email_subject}'")
        
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                logging.debug("Connecting to SMTP server")
                server.set_debuglevel(1)  # Enable smtplib debug output
                server.starttls()  # Secure the connection
                logging.debug("Starting TLS")
                server.login(smtp_username, smtp_password)
                logging.debug("Logged in to SMTP server")
                server.send_message(msg)
                logging.debug("Email sent successfully")
            logging.info(f"Email sent to {person['email']} with subject '{email_subject}'")
            print(f"Email sent to {person['email']}")
        except Exception as e:
            logging.error(f"Failed to send email to {person['email']} with subject '{email_subject}': {e}")
            print(f"Failed to send email to {person['email']}: {e}")
    
    return "Emails sent"

# Example usage
if __name__ == "__main__":
    people_list = [{'email': 'sherifflogan99@gmail.com'}]
    email_subject = "Test Email"
    email_body = "<h1>This is a test email</h1>"
    print(send_email(people_list, email_subject, email_body))