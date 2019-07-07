import discord
import asyncio
import embeds
#import _mysql
import excon
import config
import sqlite3


id = "ver"

fail = 0

async def ex(args, message, client, invoke):

    conn = sqlite3.connect('sql.db')
    c = conn.cursor()


    c.execute("SELECT * FROM version")
    row = c.fetchone()
    ver = row[0]

    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.add_field(name="Version of %s" % (config.name), value=config.version, inline=False)
    embed.add_field(name="Latest version", value=ver, inline=False)
    embed.set_footer(text=config.by)
    await client.send_message(message.channel, embed=embed)
    conn.close()
