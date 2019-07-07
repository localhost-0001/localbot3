import discord
import config
import embeds
import splitter
import dictionaries
import copy
import sqlite3

fail = 0
id = "help"

def checkmenuone(reaction, user):
    e = str(reaction.emoji)
    return e.startswith(("1⃣", "2⃣", "3⃣", "4⃣", "5⃣", "6⃣", "7⃣", "8⃣", "9⃣", "❌", "✅", "➡" , "⬅"))

async def helpedit(selectednum, names, namestypes, client, menuemsg):
    if len(names) >= selectednum:

        currentcommand = names[selectednum]
        helplistcommand  = dictionaries.commandusagehelp[currentcommand]

        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
        embed.add_field(name="Advanced help of %s" % (currentcommand), value="%s" % (('').join(helplistcommand)), inline=True)
        embed.set_footer(text=config.by)

        await client.edit_message(menuemsg, embed=embed)

def namegen(page, listin, type):

    page -= 1
    names = []
    nameamount = 1
    CurrentType = ""

    for name, Type in listin[page].items():
        if type:
            if not CurrentType == Type:
                names.append("\n**" + Type + "**\n")
                CurrentType = copy.deepcopy(Type)
            if nameamount == 1:
                names.append(":one:")
            elif nameamount == 2:
                names.append("\n")
                names.append(":two:")
            elif nameamount == 3:
                names.append("\n")
                names.append(":three:")
            elif nameamount == 4:
                names.append("\n")
                names.append(":four:")
            elif nameamount == 5:
                names.append("\n")
                names.append(":five:")
            elif nameamount == 6:
                names.append("\n")
                names.append(":six:")
            elif nameamount == 7:
                names.append("\n")
                names.append(":seven:")
            elif nameamount == 8:
                names.append("\n")
                names.append(":eight:")
            elif nameamount == 9:
                names.append("\n")
                names.append(":nine:")

        names.append(name)
        nameamount += 1

    page += 1
    if type:
        maxpage = len(listin)
        names.append("\nPage " + str(page) +" of " + str(maxpage) + ".")

    return names

async def ex(args, message, client, invoke):

    moneytoadd = 0
    moneytoadd_present = False
    membertoadd_present = False
    menumsg_present = False

    if len(args) >= 2:
        for a in args:
            if isinstance(a, int):
                moneytoadd = copy.deepcopy(a)
                moneytoadd_present = True

        try:
            membertoadd = message.mentions[0]
            membertoadd_present = True
        except:
            membertoadd_present = False

    while not membertoadd_present:
        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)

        embed.add_field(name="Who do you want to add money to?", value="@Mention the member you want to add money to", inline=False)
        embed.set_footer(text=config.by)
        menuemsg = await client.send_message(message.channel, embed=embed)

        menumsg_present = True

        moneymsg = await client.wait_for_message(timeout=None, author=message.author, channel=message.channel)
        await client.delete_message(moneymsg)


        try:
            print("hi")
            membertoadd = moneymsg.mentions[0]
            membertoadd_present = True
        except:
            print("hi1")
            membertoadd_present = False

    while not moneytoadd_present:
        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)

        embed.add_field(name="How much money do you want to send?", value="Please enter the amount of money you want to send.", inline=False)
        embed.set_footer(text=config.by)
        if menumsg_present:
            await client.edit_message(menuemsg, embed=embed)
        else:
            menuemsg = await client.send_message(message.channel, embed=embed)
            menumsg_present = True

        moneymsg = await client.wait_for_message(timeout=None, author=message.author, channel=message.channel)
        await client.delete_message(moneymsg)

        args2 = moneymsg.content.split(" ")

        print(args2)

        for a in args2:
            if isinstance(a, int):
                moneytoadd = copy.deepcopy(a)
                moneytoadd_present = True

    return

    memid = message.author.id

    c.execute('SELECT * FROM moneyy WHERE id = ? AND memid = ?' , (message.server.id, memid))
#    print("SELECTED")
    row = c.fetchone()

    #find the symbols
    #check if row exists
    #find the 2 members
    #remove from giver, add to reciever

    embed=discord.Embed(title="Discord", url=config.invite, colour=0x2ecc71)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.add_field(name="SUCCESS" % (config.name), value="Added %s%s%s to %s" % (symbolfront, moneytoadd, symbolback, membertoadd.mention()), inline=False)
    embed.add_field(name="Commands:", value = helpstring, inline=False)
    embed.set_footer(text=config.by)

    await client.edit_message(menuemsg, embed=embed)
