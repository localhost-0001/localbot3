import discord
import config
import excon

perm = 4
id = "bdo"

async def ex(args, message, client, invoke):
    channel = client.get_channel(args[0])
    await client.send_message(channel, ' '.join(args[1:]))
    await client.delete_message(message)
