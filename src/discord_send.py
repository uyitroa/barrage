import discord
import time
client = discord.Client()
TOKEN = 'nah'


def read_data():
	return int(open("water_force.txt", "r").read())


@client.event
async def on_message(message):
	data = read_data()
	print(message.content)
	if message.content == "status":
		await client.send_message(message.author, "Force de l'eau actuel: " + str(data))
	if message.content == "start":
		while True:
			data = read_data()
			if data > 50000:
				await client.send_message(message.author, "Alerte: Force de l'eau depasse la limite!")
			time.sleep(0.1)

@client.event
async def on_ready():
	print("Starting...")

client.run(TOKEN)
