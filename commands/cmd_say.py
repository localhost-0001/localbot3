import discord
import config
import excon

perm = 4
id = "bdo"

async def ex(args, message, client, invoke):
    await client.send_message(message.channel, ' '.join(args))
    await client.delete_message(message)
