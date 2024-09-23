import imaplib
import email
import time
import texter


def connect_to_gmail(username, password):
    try:
        # Connect to Gmail IMAP server
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        # Login to Gmail
        mail.login(username, password)
        print('Connected :)')
        return mail
    except:
        print("Error connecting, trying again...")
        time.sleep(3)
        connect_to_gmail(username, password)


def check_emails(mail):
    try:
        # Select the inbox folder
        mail.select("inbox")
        # Search for unseen emails
        result, data = mail.search(None, "UNSEEN")
        if result == "OK":
            for num in data[0].split():
                # Fetch the email by its number
                result, data = mail.fetch(num, "(RFC822)")
                if result == "OK":
                    raw_email = data[0][1]
                    msg = email.message_from_bytes(raw_email)
                    # Extract email information
                    print("From:", msg["From"])
                    for part in msg.walk():
                        if part.get_content_maintype() == 'multipart':
                            continue
                        if part.get('Content-Disposition') is None:
                            continue
                        filename = part.get_filename()
                        if bool(filename):
                            # Extract text content from attachment
                            attachment_content = part.get_payload(decode=True).decode()
                            print(attachment_content)
                        else:
                            # If no attachment found
                            print('No attachments found.')
        else:
            print("No new emails.")
    except (imaplib.IMAP4.error) as e:
        print("Error:", e)
        return e
        


def main():
    try:
        mail = connect_to_gmail(texter.smtp_user, texter.smtp_pass)
        while True:
            res = check_emails(mail)
            if res:
                mail = connect_to_gmail(texter.smtp_user, texter.smtp_pass)
            time.sleep(3)
    except:
        print("Disconnected, trying again...")
        time.sleep(2)
        main()
    

if __name__ == '__main__':
    main()
