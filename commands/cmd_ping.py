import discord
import config
import datetime
import sqlite3

id = "ping"

async def ex(args, message, client, invoke):
    embed=discord.Embed(title="Discord", url=config.invite, color=0x2ecc71)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.set_thumbnail(url=config.embedthumbnail)
    embed.add_field(name="PONG!", value="*the bot is online and fully operational.*", inline=True)
    embed.set_footer(text=config.by)

    a = datetime.datetime.now()
    menumsg = await client.send_message(message.channel, embed=embed)
    b = datetime.datetime.now()
    deltaa = b - a

    conn = sqlite3.connect('sql.db')
    c = conn.cursor()
    a = datetime.datetime.now()
    c.execute("SELECT * FROM warnings WHERE id = '363003963341275137' AND memid = '158250066417549312'")
    b = datetime.datetime.now()
    deltab = b - a
    embed=discord.Embed(title="Discord", url=config.invite, color=0x2ecc71)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.set_thumbnail(url=config.embedthumbnail)
    embed.add_field(name="PONG!", value="*the bot is online and fully operational.*\n", inline=True)
    embed.add_field(name="Ping:", value="Bot <-> Discord: `%s`\nBot <-> Database: `%s`" % (deltaa, deltab), inline=False)
    embed.set_footer(text=config.by)
    await client.edit_message(menumsg, embed=embed)
