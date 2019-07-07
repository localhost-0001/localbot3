import discord
import asyncio
import embeds
import config

perm = 1
id = "fclear"

async def ex(args, message, client, invoke):
    if args.__len__() != 1:
        await embeds.syntaxa1num(message, invoke, client)
        return
    try:
        ammount = int(args[0]) + 1 if len(args) > 0 else 2
    except:
        await embeds.syntaxa1num(message, invoke, client)
        return

    try:
        ammount = int(args[0]) + 1 if len(args) > 0 else 2
    except:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), descrition="Please enter a valid value for message ammount!"))
        return

    if ammount < 2:
        await embeds.fclearbtw(message, invoke, client)
        return
    if ammount > 100:
        await embeds.fclearbtw(message, invoke, client)
        return
    cleared = -1
    failed = 0

    messages = []
    async for m in client.logs_from(message.channel, limit=ammount):
        messages.append(m)

    await client.delete_messages(messages)
    ammount = ammount - 1

    embed=discord.Embed(title="Discord", url=config.invite, color=0x2ecc71)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.set_thumbnail(url=config.embedthumbnail)
    embed.add_field(name="Information!", value="Deleted %s messages" % (ammount), inline=True)
    embed.set_footer(text=config.by)
    menumsg = await client.send_message(message.channel, embed=embed)

    await asyncio.sleep(4)
    await client.delete_message(menumsg)
