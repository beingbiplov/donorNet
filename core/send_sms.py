
from twilio.rest import Client
from django.conf import settings
# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

def welcome_message(send_to, r_name):
	account_sid = settings.TWILIO_ACCOUNT_SID
	auth_token = settings.TWILIO_AUTH_TOKEN
	if send_to[0] != '+':
		send_to = '+'+send_to
	message = f'Welcome { r_name }!! Thank you for joining us at DonorNet.  Donate blood, Save life.'
	
	try:
		client = Client(account_sid, auth_token)

		message = client.messages \
		    .create(
		         body=message,
		         from_=settings.TWILIO_NUMBER,
		         to=send_to
		     )
	except:
		pass

