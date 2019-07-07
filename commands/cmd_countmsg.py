import discord
import asyncio
import embeds
import config

perm = 0
id = "cmsg"

async def ex(args, message, client, invoke):

    msgout = 0
    cleared = -1
    failed = 0

#    clearmsg = await embeds.clearing(message, client)

    async for m in client.logs_from(message.channel, limit=2147483647):
        if msgout == 0:
            embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
            embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
            embed.set_thumbnail(url="https://yt3.ggpht.com/-310LKwfseck/AAAAAAAAAAI/AAAAAAAAAAA/3oXd3OARMkQ/s200-mo-c-c0xffffffff-rj-k-no/photo.jpg")
            embed.add_field(name="WARNING", value="COUNTING IN PROGRESS!", inline=True)
            embed.set_footer(text="by raidrix.")
            await asyncio.sleep(1)
            clearmsg = await client.send_message(message.channel, embed=embed)

        msgout = 1
        if not m == clearmsg:
            try:
                cleared += 1
            except:
                cleared += 1
                pass
    failed_str = "\n\nFailed to clear %s message(s)." % failed if failed > 0 else ""

    await client.delete_message(clearmsg)

    returnmsg = await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.blue(), description="There are %s message(s).%s" % (cleared, failed_str)))
