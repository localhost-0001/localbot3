import discord
import asyncio
import embeds
import config

perm = 2
id = "uclear"

async def ex(args, message, client, invoke):

    if args.__len__() < 2:
        await embeds.syntaxa2num(message, invoke, client)
        return
    try:
        ammount = int(args[0]) + 1 if len(args) > 0 else 2
    except:
        await embeds.syntaxa2num(message, invoke, client)
        return
    memb = message.mentions[0]
    memid = memb.id

    msgout = 0
    cleared = 0
    failed = 0
    total = 1

#    clearmsg = await embeds.clearing(message, client)

    async for m in client.logs_from(message.channel, limit=2147483640):
        if msgout == 0:
            embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
            embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
            embed.set_thumbnail(url="https://yt3.ggpht.com/-310LKwfseck/AAAAAAAAAAI/AAAAAAAAAAA/3oXd3OARMkQ/s200-mo-c-c0xffffffff-rj-k-no/photo.jpg")
            embed.add_field(name="WARNING", value="CHATCLEAN IN PROGRESS!", inline=True)
            embed.set_footer(text="by raidrix.")
            await asyncio.sleep(1)
            clearmsg = await client.send_message(message.channel, embed=embed)

        msgout = 1
        if not ammount <= total:
            if not m == clearmsg:
                if memb.id == m.author.id:
                    try:
                        await client.delete_message(m)
                        cleared += 1
                        total += 1
                    except:
                        failed += 1
                        total += 1
                        pass
    failed_str = "\n\nFailed to clear %s message(s)." % failed if failed > 0 else ""

    await client.delete_message(clearmsg)

    returnmsg = await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.blue(), description="Cleared %s message(s).%s" % (cleared, failed_str)))
    await asyncio.sleep(3)
    await client.delete_message(returnmsg)
