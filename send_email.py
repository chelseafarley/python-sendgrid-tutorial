# pip3 install sendgrid

import sendgrid
import os
import base64
from sendgrid.helpers.mail import Mail, Email, To, Content, Attachment, FileContent, FileName, FileType, Disposition

api_key = os.environ.get("SENDGRID_API_KEY")
sg = sendgrid.SendGridAPIClient(api_key=api_key)
from_email = Email("hello@tripwiretech.com")
to = To("chelseafarley91@gmail.com")
subject = "My SendGrid Message"
content = Content("text/html", "Hello <b>friend!</b>")
mail = Mail(from_email, to, subject, content)

with open('cv.pdf', "rb") as f:
  data = f.read()
  f.close()

encoded_file = base64.b64encode(data).decode()

attached_file = Attachment(
  FileContent(encoded_file),
  FileName("cv.pdf"),
  FileType("application/pdf"),
  Disposition("attachment")
)

mail.attachment = attached_file

mail_json = mail.get()

response = sg.client.mail.send.post(request_body=mail_json)
print(response.status_code)
print(response.headers)