import discord
import config
import excon
import copy

perm = 4
id = "bdo"

async def ex(args, message, client, invoke):
    counter = int(copy.deepcopy(args[0]))
    await client.delete_message(message)
    while counter > 0:
        await client.send_message(message.channel, ' '.join(args[1:]))
        counter -= 1
