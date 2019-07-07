import discord
import config
import excon
import sqlite3
#import _mysql

id = None

perm = 0
async def ex(args, message, client, invoke):
    conn = sqlite3.connect('sql.db')
    c = conn.cursor()
    c.execute("SELECT * FROM bans WHERE id = '%s'" % (message.author.id))
    suggestioncontent = ' '.join(args)
    row = c.fetchone()

    if not row:
        c.execute("INSERT INTO bans (id, banned) VALUES ('%s', '0')" % (message.author.id))
        if len(args) == 0:
            embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
            embed.set_author(name=config.name, url=config.leftlogoembed, icon_url="https://i.imgur.com/E8GIP3I.png")
            embed.set_thumbnail(url=config.embedthumbnail)
            embed.add_field(name="WARNING", value="Please suggest something", inline=False)
            embed.set_footer(text=config.by)
            await   client.send_message(message.channel, embed=embed)
            conn.close()
            return
        channel = client.get_channel(config.suggestchan)
        await client.send_message(channel, "A suggestion has been sent by by %s#%s (ID: '%s'), Channel name: '%s' (ID: '%s') \n Suggestion: ```%s```" % (message.author.name, message.author.discriminator, message.author.id, message.channel.name, message.channel.id, suggestioncontent))
        embed=discord.Embed(title="Discord", url=config.invite, color=0x2ecc71)
        embed.set_author(name=config.name, url=config.leftlogoembed, icon_url="https://i.imgur.com/E8GIP3I.png")
        embed.set_thumbnail(url=config.embedthumbnail)
        embed.add_field(name="NOTIFICATION", value="Suggestion sent.", inline=False)
        embed.set_footer(text=config.by)
        await   client.send_message(message.channel, embed=embed)
    else:

        banz = row[1]
#        print(bans)
#        bans = bans.decode("utf-8")
        if banz == 1:
            embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
            embed.set_author(name=config.name, url=config.leftlogoembed, icon_url="https://i.imgur.com/E8GIP3I.png")
            embed.set_thumbnail(url=config.embedthumbnail)
            embed.add_field(name="WARNING", value="You have been blocked from sending suggestions.", inline=False)
            embed.set_footer(text=config.by)
            await   client.send_message(message.channel, embed=embed)
            conn.close()
            return
        else:
            if len(args) == 0:
                embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
                embed.set_author(name=config.name, url=config.leftlogoembed, icon_url="https://i.imgur.com/E8GIP3I.png")
                embed.set_thumbnail(url=config.embedthumbnail)
                embed.add_field(name="WARNING", value="Please suggest something", inline=False)
                embed.set_footer(text=config.by)
                await   client.send_message(message.channel, embed=embed)
                conn.close()
                return
            channel = client.get_channel(config.suggestchan)
            await client.send_message(channel, "A suggestion has been sent by by %s#%s (ID: '%s'), Channel name: '%s' (ID: '%s') \n Suggestion: ```%s```" % (message.author.name, message.author.discriminator, message.author.id, message.channel.name, message.channel.id, suggestioncontent))
            embed=discord.Embed(title="Discord", url=config.invite, color=0x2ecc71)
            embed.set_author(name=config.name, url=config.leftlogoembed, icon_url="https://i.imgur.com/E8GIP3I.png")
            embed.set_thumbnail(url=config.embedthumbnail)
            embed.add_field(name="NOTIFICATION", value="Suggestion sent.", inline=False)
            embed.set_footer(text=config.by)
            await   client.send_message(message.channel, embed=embed)
    conn.close()
    return
