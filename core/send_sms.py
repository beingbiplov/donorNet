
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


def send_donation_request(phone_number, full_name, req_country, req_location1, req_bloodgroup, br_pk):
	account_sid = settings.TWILIO_ACCOUNT_SID
	auth_token = settings.TWILIO_AUTH_TOKEN
	if phone_number[0] != '+':
		phone_number = '+'+phone_number
	br_link = f'localhost:8000/send-request/{ br_pk }'
	message = f'Hello { full_name }!! . Someone at { req_location1 }, { req_country} need { req_bloodgroup } blood urgently. Please vist { br_link } if you can donate blood. Donate blood, Save life.'
	
	try:
		client = Client(account_sid, auth_token)

		message = client.messages \
		    .create(
		         body=message,
		         from_=settings.TWILIO_NUMBER,
		         to=phone_number
		     )
	except:
		pass


def send_donoraccept_request(phone_number, br_pk):
	account_sid = settings.TWILIO_ACCOUNT_SID
	auth_token = settings.TWILIO_AUTH_TOKEN
	if phone_number[0] != '+':
		phone_number = '+'+phone_number
	br_link = f'localhost:8000/send-request/{ br_pk }'
	message = f'Hello. One person accepted your blood donation request. Please vist { br_link } to view contact information. Donate blood, Save life.'
	print(message)
	try:
		client = Client(account_sid, auth_token)

		message = client.messages \
		    .create(
		         body=message,
		         from_=settings.TWILIO_NUMBER,
		         to=phone_number
		     )
	except:
		pass