import discord
import config

fail = 0
perm = 2
id = "ban"

async def ex(args, message, client, invoke):

    # if logchan is None:
    #     embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
    #     embed.set_author(name=config.name, url="https://discordapp.com/oauth2/authorize/?permissions=2146958591&scope=bot&client_id=421691975155056640", icon_url=config.leftlogoembed)
    #     embed.set_thumbnail(url=config.embedthumbnail)
    #     embed.add_field(name="WARNING", value="PLEASE CREATE A #locallog CHANNEL", inline=False)
    #     embed.set_footer(text=config.by)
    #
    #     await client.send_message(message.channel, embed=embed)

    if len(args) == 0:
        embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
        embed.set_author(name=config.name, url="https://discordapp.com/oauth2/authorize/?permissions=2146958591&scope=bot&client_id=421691975155056640", icon_url=config.leftlogoembed)
        embed.set_thumbnail(url="https://yt3.ggpht.com/-310LKwfseck/AAAAAAAAAAI/AAAAAAAAAAA/3oXd3OARMkQ/s200-mo-c-c0xffffffff-rj-k-no/photo.jpg")
        embed.add_field(name="ERROR", value="Please select a member to ban, also make sure u mention him", inline=True)
        embed.set_footer(text="by raidrix.")
        await client.send_message(message.channel, embed=embed)
        return
    else:

        if 0 == 1:
            return
        else:
            # memid = args[0]
            # a0 = args[0]
            # memid = memid.replace('@', '')
            # memid = memid.replace('<', '')
            # memid = memid.replace('>', '')
            m = message.mentions[0]
            if m is None:
                # print('NoneType iz da')
                embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
                embed.set_author(name=config.name, url="https://discordapp.com/oauth2/authorize/?permissions=2146958591&scope=bot&client_id=421691975155056640", icon_url=config.leftlogoembed)
                embed.set_thumbnail(url="https://yt3.ggpht.com/-310LKwfseck/AAAAAAAAAAI/AAAAAAAAAAA/3oXd3OARMkQ/s200-mo-c-c0xffffffff-rj-k-no/photo.jpg")
                embed.add_field(name="ERROR", value="Please select a member to ban, also make sure u mention him", inline=True)
                embed.set_footer(text="by raidrix.")
                await client.send_message(message.channel, embed=embed)
                return
            else:
                try:
                    await client.ban(m)
                except:
                    embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
                    embed.set_author(name=config.name, url="https://discordapp.com/oauth2/authorize/?permissions=2146958591&scope=bot&client_id=421691975155056640", icon_url=config.leftlogoembed)
                    embed.set_thumbnail(url=config.embedthumbnail)
                    embed.add_field(name="WARNING", value="COULD NOT BAN SELECTED MEMBER", inline=False)
                    embed.set_footer(text=config.by)
                    await client.send_message(message.channel, embed=embed)
                    return
                embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
                embed.set_author(name=config.name, url="https://discordapp.com/oauth2/authorize/?permissions=2146958591&scope=bot&client_id=421691975155056640", icon_url=config.leftlogoembed)
                embed.set_thumbnail(url=config.embedthumbnail)
                embed.add_field(name="Success", value="BANNED MEMBER: %s#%s (ID:`%s`"% (message.mentions[0].name,message.mentions[0].discriminator, message.mentions[0].id), inline=False)
                embed.set_footer(text=config.by)
                await client.send_message(message.channel, embed=embed)

                try:
                    logchan = discord.utils.get(message.server.channels, name='locallog')
                    embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
                    embed.set_author(name=config.name, url="https://discordapp.com/oauth2/authorize/?permissions=2146958591&scope=bot&client_id=421691975155056640", icon_url=config.leftlogoembed)
                    embed.set_thumbnail(url=config.embedthumbnail)
                    embed.add_field(name="BAN HAS BEEN RUN BY %s, (ID:`%s`)" % (message.author, message.author.id), value="BANNED MEMBER: %s#%s (ID:`%s`" % (message.mentions[0].name,message.mentions[0].discriminator, message.mentions[0].id), inline=False)
                    embed.set_footer(text=config.by)

                    await client.send_message(logchan, embed=embed)
                except:
                    embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
                    embed.set_author(name=config.name, url="https://discordapp.com/oauth2/authorize/?permissions=2146958591&scope=bot&client_id=421691975155056640", icon_url=config.leftlogoembed)
                    embed.set_thumbnail(url=config.embedthumbnail)
                    embed.add_field(name="WARNING", value="PLEASE CREATE A #locallog CHANNEL", inline=False)
                    embed.set_footer(text=config.by)
                    await client.send_message(message.channel, embed=embed)

                return
