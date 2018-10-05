from twilio.rest import Client


def sendsms(my_string):
	account_sid = 'AC226ab8ec94356e0e3d7e34614032f855'
	auth_token = 'ea20f94d90faa85e59378366eb6e218a'

	from_number = '+33644603488'
	to_number = '+33762226688'
	client = Client(account_sid, auth_token)

	client.messages.create(body=my_string, from_=from_number, to=to_number)


def getdepth():
	return 101


def main():
	while True:
		x = getdepth()

		if x > 100:
			sendsms("Barrage is dead")
			break


if __name__ == '__main__':
	main()
