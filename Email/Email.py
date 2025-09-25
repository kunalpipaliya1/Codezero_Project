import smtplib, ssl
import os
from email.message import EmailMessage
import shutil
import sys
from Project_2_Perpetuals_QA_Testnet.Data.user_perps import Email

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def send_mail():
    sender_email = "kunal.pipaliya@codezeros.com"
    to_emails = ["kunal.pipaliya@codezeros.com"]      # Main recipient(s)
    cc_emails = ["kunal.pipaliya@codezeros.com"]            # CC recipients
    bcc_emails = ["kunal.pipaliya@codezeros.com"]            # BCC recipients
    password = "uwyy qbnd okbr xeko"                  # Gmail App Password

    subject = "Perpetuals Automation Test Report"
    body = """\
Dear Sir,

Perpetuals Automation test execution is completed. Kindly check the Allure test report.

Regards,
QA-Kunal Pipaliya
"""

    # Build the email
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = ", ".join(to_emails)
    msg["Cc"] = ", ".join(cc_emails)
    msg["Subject"] = subject
    msg.set_content(body)

    source_folderr = Email.source_folder
    output_folderr = Email.output_folder
    zip_name = "Allure_HTML_Report"

    # Ensure output folder exists
    os.makedirs(output_folderr, exist_ok=True)

    # Create the zip
    zip_path = shutil.make_archive(
        os.path.join(output_folderr, zip_name),  # /.../zip_Folder/Reports_Allure
        'zip',
        root_dir=source_folderr
    )

    with open(zip_path, "rb") as f:
        msg.add_attachment(f.read(),
                            maintype="application",
                            subtype="zip",
                            filename=os.path.basename(zip_path))

    # Combine all recipients (To + Cc + Bcc) for sending
    all_recipients = to_emails + cc_emails + bcc_emails

    # Send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg, from_addr=sender_email, to_addrs=all_recipients)

    print("Email sent successfully...")

if __name__ == "__main__":
    send_mail()
