import discord
import config
async def pingmsg(message, client):
    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.set_thumbnail(url="https://yt3.ggpht.com/-310LKwfseck/AAAAAAAAAAI/AAAAAAAAAAA/3oXd3OARMkQ/s200-mo-c-c0xffffffff-rj-k-no/photo.jpg")
    embed.add_field(name="INFOS ABOUT PCA-Bot", value="PCA-Bot, is a bot created by raidrix aka localhost.", inline=True)
    embed.add_field(name= "Just run p!help to get a list of commands :)", value="and p!permsystem explains the permsystem", inline=True)
    embed.set_footer(text=config.by)
    await client.send_message(message.channel, embed=embed)
    return

async def unknowncmd(message, client, invoke):
    embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
    embed.set_thumbnail(url="https://yt3.ggpht.com/-310LKwfseck/AAAAAAAAAAI/AAAAAAAAAAA/3oXd3OARMkQ/s200-mo-c-c0xffffffff-rj-k-no/photo.jpg")
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.add_field(name="ERROR ", value="The command %s is unknown." % (invoke), inline=True)
    embed.set_footer(text=config.by)
    await client.send_message(message.channel, embed=embed)
    return

async def noperms(message, client, invoke):
    embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
    embed.set_thumbnail(url="https://yt3.ggpht.com/-310LKwfseck/AAAAAAAAAAI/AAAAAAAAAAA/3oXd3OARMkQ/s200-mo-c-c0xffffffff-rj-k-no/photo.jpg")
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.add_field(name="ERROR ", value="You do not have the needed permissions to run %s." % (invoke), inline=True)
    embed.set_footer(text=config.by)
    await client.send_message(message.channel, embed=embed)
    return

async def veri(message, client, enchan):
    embed=discord.Embed(title="No Discord here", url="https://lmgtfy.com/?iie=1&q=discord+invite", colour=0xe74c3c)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.set_thumbnail(url=config.embedthumbnail)
    embed.add_field(name="IN THE VERIFING CHANNEL HAS BEEN WRITTEN", value="by `%s` (ID:`%s`) in `%s` (ID: `%s`) " % (message.author, message.author.id, message.channel, message.channel.id), inline=False)
    embed.add_field(name="Full message", value="%s" % (message.content), inline=True)
    embed.set_footer(text=config.by)
    await client.send_message(enchan, embed=embed)
    return

async def syntaxa1num(message, invoke, client):
    embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.set_thumbnail(url=config.embedthumbnail)
    embed.add_field(name="ERROR", value="SYNTAX OF %s : %s%s  [number]" % (invoke, config.prefix, invoke), inline=True)
    embed.set_footer(text=config.by)
    await client.send_message(message.channel, embed=embed)
    return

async def syntaxa2num(message, invoke, client):
    embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.set_thumbnail(url=config.embedthumbnail)
    embed.add_field(name="ERROR", value="SYNTAX OF %s : %s%s [number] @member" % (invoke, config.prefix, invoke), inline=True)
    embed.set_footer(text=config.by)
    await client.send_message(message.channel, embed=embed)
    return

async def fclearbtw(message, invoke, client):
    embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.set_thumbnail(url=config.embedthumbnail)
    embed.add_field(name="ERROR", value="SYNTAX OF %s : %s%s  [number between 1 and 99]" % (invoke, config.prefix, invoke), inline=True)
    embed.set_footer(text=config.by)
    await client.send_message(message.channel, embed=embed)
    return

async def filterlog(message, client):
    logchan = discord.utils.get(message.server.channels, name='pcalog')
    embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.set_thumbnail(url=config.embedthumbnail)
    embed.add_field(name="WARNING", value="%s ran filter, (ID:`%s`)" % (message.author, message.author.id), inline=False)
    embed.set_footer(text=config.by)
    await client.send_message(logchan, embed=embed)
    return

async def nologchan(message, client):
    embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.set_thumbnail(url=config.embedthumbnail)
    embed.add_field(name="WARNING", value="PLEASE CREATE A #pcalog CHANNEL", inline=False)
    embed.set_footer(text=config.by)
    await client.send_message(message.channel, embed=embed)
    return

async def menuemsg(message, smsg, client):
    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.add_field(name="What do you want to do?", value="%s" % (smsg), inline=True)
    msg = await client.send_message(message.channel, embed=embed)
    return msg

def addemb():
    embed=discord.Embed(title="Discord", url=config.invite, description="What do you want to add?", colour=0x3498db)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)

    return embed

def list0emb():
    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.add_field(name="ERROR 404", value="The filter for this server is empty.", inline=True)
    return embed

async def sorrymsg(message, client):
    embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.set_thumbnail(url=config.embedthumbnail)
    embed.add_field(name="WARNING", value="Sorry, <@%s>, your message contains something in the chatfilter." % (message.author.id), inline=True)
    embed.set_footer(text=config.by)
    await client.send_message(message.channel, embed=embed)
    return

async def filteredlog(message, client):
    logchan = discord.utils.get(message.server.channels, name='pcalog')
    embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.set_thumbnail(url=config.embedthumbnail)
    embed.add_field(name="THE CHATFILTER HAS BEEN TRIGGERED", value="by `%s` (ID:`%s`) in `%s` (ID: `%s`) " % (message.author, message.author.id, message.channel, message.channel.id), inline=False)
    embed.add_field(name="Full message", value="%s" % (message.content), inline=True)
    embed.set_footer(text=config.by)
    await client.send_message(logchan, embed=embed)
    return

def remb():
    embed=discord.Embed(title="Discord", url=config.invite, description="What do you want to remove?", colour=0x3498db)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)

    return embed

async def addrole(message, client, rname, mname):
    roles = ', '.join(rname)
    members = ', '.join(mname)
    logchan = discord.utils.get(message.server.channels, name='pcalog')
    if logchan is not None:

        embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
        embed.set_thumbnail(url=config.embedthumbnail)
        embed.add_field(name="WARNING", value="%s ran addrole, (ID:`%s`)" % (message.author, message.author.id), inline=False)
        embed.add_field(name="ROLES", value="%s" % (roles,), inline=False)
        embed.add_field(name="MEMBERS", value="%s" % (members), inline=False)
        embed.set_footer(text=config.by)
        await client.send_message(logchan, embed=embed)

    embed=discord.Embed(title="Discord", url=config.invite, color=0x2ecc71)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.set_thumbnail(url=config.embedthumbnail)
    embed.add_field(name="Sucess", value="Added role(s) to member(s)", inline=False)
    embed.add_field(name="ROLES", value="%s" % (roles,), inline=False)
    embed.add_field(name="MEMBERS", value="%s" % (members), inline=False)
    embed.set_footer(text=config.by)
    await client.send_message(message.channel, embed=embed)
    return

async def addsyntax(message, invoke, client):
    embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.set_thumbnail(url=config.embedthumbnail)
    embed.add_field(name="ERROR", value="SYNTAX OF %s : %s%s @member(s) @role(s) " % (invoke, config.prefix, invoke), inline=True)
    embed.set_footer(text=config.by)
    await client.send_message(message.channel, embed=embed)
    return

async def remrole(message, client, rname, mname):
    roles = ', '.join(rname)
    members = ', '.join(mname)

    logchan = discord.utils.get(message.server.channels, name='pcalog')
    if logchan is not None:
        embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
        embed.set_thumbnail(url=config.embedthumbnail)
        embed.add_field(name="WARNING", value="%s ran removerole, (ID:`%s`)" % (message.author, message.author.id), inline=False)
        embed.add_field(name="ROLES", value="%s" % (roles,), inline=False)
        embed.add_field(name="MEMBERS", value="%s" % (members), inline=False)
        embed.set_footer(text=config.by)
        await client.send_message(logchan, embed=embed)

    embed=discord.Embed(title="Discord", url=config.invite, color=0x2ecc71)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.set_thumbnail(url=config.embedthumbnail)
    embed.add_field(name="Sucess", value="Removed role(s) from member(s)", inline=False)
    embed.add_field(name="ROLES", value="%s" % (roles,), inline=False)
    embed.add_field(name="MEMBERS", value="%s" % (members), inline=False)
    embed.set_footer(text=config.by)
    await client.send_message(message.channel, embed=embed)
    return

async def warnlog(message, client, membid, reason):
    logchan = discord.utils.get(message.server.channels, name='punishment-logs')
    embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.set_thumbnail(url=config.embedthumbnail)
    embed.add_field(name="WARNING", value="%s warned <@%s>, (ID of warning person:`%s`)\nReason:```%s```" % (message.author,membid, message.author.id, reason), inline=False)
    embed.set_footer(text=config.by)
    await client.send_message(logchan, embed=embed)
    embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.set_thumbnail(url=config.embedthumbnail)
    embed.add_field(name="WARNING", value="%s warned you, (ID of warning person:`%s`)\nReason:```%s```" % (message.author, message.author.id, reason), inline=False)
    embed.set_footer(text=config.by)

    user = discord.utils.get(client.get_all_members(), id='%s' %(membid))
    try:
        await client.send_message(user, embed=embed)
    except:
        embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
        embed.set_thumbnail(url=config.embedthumbnail)
        embed.add_field(name="WARNING", value="Could not PM warned Person!", inline=False)
        embed.set_footer(text=config.by)
        await client.send_message(message.channel, embed=embed)
    return

async def pardonlog(message, client, membid, reason):
    logchan = discord.utils.get(message.server.channels, name='punishment-logs')
    embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.set_thumbnail(url=config.embedthumbnail)
    if reason == "":
        embed.add_field(name="WARNING", value="%s Pardoned <@%s>, (ID of pardoning person:`%s`)\nNo reason provided." % (message.author,membid, message.author.id), inline=False)
    else:
        embed.add_field(name="WARNING", value="%s Pardoned <@%s>, (ID of pardoning person:`%s`)\nReason:```%s```" % (message.author,membid, message.author.id, reason), inline=False)
    embed.set_footer(text=config.by)
    await client.send_message(logchan, embed=embed)
    embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.set_thumbnail(url=config.embedthumbnail)
    if reason == "":
        embed.add_field(name="WARNING", value="%s pardoned you, (ID of pardoning person:`%s`)\nNo reason provided." % (message.author, message.author.id), inline=False)
    else:
        embed.add_field(name="WARNING", value="%s pardoned you, (ID of pardoning person:`%s`)\nReason:```%s```" % (message.author, message.author.id, reason), inline=False)
    embed.set_footer(text=config.by)

    user = discord.utils.get(client.get_all_members(), id='%s' %(membid))
    try:
        await client.send_message(user, embed=embed)
    except:
        embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
        embed.set_thumbnail(url=config.embedthumbnail)
        embed.add_field(name="WARNING", value="Could not PM Pardoned Person!", inline=False)
        embed.set_footer(text=config.by)
        await client.send_message(message.channel, embed=embed)
    return

async def pardonalllog(message, client, membid, reason):
    logchan = discord.utils.get(message.server.channels, name='punishment-logs')
    embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.set_thumbnail(url=config.embedthumbnail)
    if reason == "":
        embed.add_field(name="WARNING", value="%s Pardoned all warnings of <@%s>, (ID of pardoning person:`%s`)\nNo reason provided." % (message.author,membid, message.author.id), inline=False)
    else:
        embed.add_field(name="WARNING", value="%s Pardoned all warnings of <@%s>, (ID of pardoning person:`%s`)\nReason:```%s```" % (message.author,membid, message.author.id, reason), inline=False)
    embed.set_footer(text=config.by)
    await client.send_message(logchan, embed=embed)
    embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.set_thumbnail(url=config.embedthumbnail)
    if reason == "":
        embed.add_field(name="WARNING", value="%s pardoned all warnings of you, (ID of pardoning person:`%s`)\nNo reason provided." % (message.author, message.author.id), inline=False)
    else:
        embed.add_field(name="WARNING", value="%s pardoned all warnings of you, (ID of pardoning person:`%s`)\nReason:```%s```" % (message.author, message.author.id, reason), inline=False)
    embed.set_footer(text=config.by)

    user = discord.utils.get(client.get_all_members(), id='%s' %(membid))
    try:
        await client.send_message(user, embed=embed)
    except:
        embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
        embed.set_thumbnail(url=config.embedthumbnail)
        embed.add_field(name="WARNING", value="Could not PM Pardoned Person!", inline=False)
        embed.set_footer(text=config.by)
        await client.send_message(message.channel, embed=embed)
    return
# def commaemb():
#     embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
#     embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
#     embed.set_thumbnail(url=config.embedthumbnail)
#     embed.add_field(name="WARNING", value="Sorry, <@%s>, `,` is a dissallowed symbol." % (message.author.id), inline=True)
#     embed.set_footer(text=config.by)
#     return embed

# async def clearing(message, client):
#     embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
#     embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
#     embed.set_thumbnail(url="https://yt3.ggpht.com/-310LKwfseck/AAAAAAAAAAI/AAAAAAAAAAA/3oXd3OARMkQ/s200-mo-c-c0xffffffff-rj-k-no/photo.jpg")
#     embed.add_field(name="WARNING", value="CHATCLEAN IN PROGRESS!", inline=True)
#     embed.set_footer(text=config.by)
#     await client.send_message(message.channel, embed=embed)
#     return
