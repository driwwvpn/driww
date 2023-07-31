from driww import *

@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
	await event.reply("Hai Saya Bot VPN SILAHKAN KETIK MENU")
