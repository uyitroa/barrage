import discord
import time
import os
import asyncio

client = discord.Client()
TOKEN = 'lol no'


def read_data():
	return int(open("water_force.txt", "r").read())

async def background_task():
	await client.wait_until_ready()
	while not client.is_closed:
		data = read_data()
		if data > 50000:
			user = discord.User(id='276728415518720001')
			await client.send_message(user, "Alerte: Force de l'eau depasse la limite!")
			os.system("echo 0 > water_force.txt")
		time.sleep(0.1)
		await asyncio.sleep(0.1)


@client.event
async def on_ready():
	print("Starting...")
client.loop.create_task(background_task())
client.run(TOKEN)
