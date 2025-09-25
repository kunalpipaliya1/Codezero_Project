import smtplib, ssl
import os
from email.message import EmailMessage
import shutil
from Project_1_CLMM_QA_Testnet.Data.users_v3 import Email

def send_mail():
    sender_email = "kunal.pipaliya@codezeros.com"
    to_emails = ["kunal.pipaliya@codezeros.com"]      # Main recipient(s)
    cc_emails = ["kunal.pipaliya@codezeros.com"]            # CC recipients
    bcc_emails = ["kunal.pipaliya@codezeros.com"]            # BCC recipients
    password = "uwyy qbnd okbr xeko"                  # Gmail App Password

    subject = "CLMM Automation Test Report"
    body = """\
Dear Sir,

CLMM Automation test execution is completed. Kindly check the Allure test report.

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

    source_folder = Email.source_folder
    output_folder = Email.output_folder
    zip_name = "Allure_HTML_Report"

    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Create the zip
    zip_path = shutil.make_archive(
        os.path.join(output_folder, zip_name),  # /.../zip_Folder/Reports_Allure
        'zip',
        root_dir=source_folder
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
