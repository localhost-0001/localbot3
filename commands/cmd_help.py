import discord
import config
import embeds
import splitter
import dictionaries
import copy

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

    page = 1

    commandshelp = splitter.dict(dictionaries.commandshelp)
    commandslist = commandshelp


    maxpage = len(commandshelp)

    namestypes = namegen(page, commandslist, True)
    nameamount = 1
    CurrentType = ""

    helpstring = ('').join(namestypes)

    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
#    embed.add_field(name=":warning: :warning: :warning: :warning: :warning: :warning: :warning: ", value="THIS COMMAND WILL GET REWORKED SOON", inline=False)

    embed.add_field(name="HELP OF %s" % (config.name), value="Prefix: %s" % (config.prefix), inline=False)
    embed.add_field(name="Commands:", value = helpstring, inline=False)

#    embed.add_field(name="Misc", value="Ping \nCountmsg\nsuggest\nversion", inline=False)
#    embed.add_field(name="Usage", value="p!ping\np!cmsg\np!suggest [suggestion]\np!v", inline=True)
#    embed.add_field(name="Explanation", value="Check if the bot is online \nCounts the amount of messages in a channel\nSuggest something to the dev\nShows the current bot version", inline=True)
#    embed.add_field(name="Administrative", value="filter\nkick\nban\nClear\nfclear\nAdd\nRemove\nWarn\nPardon\nStrikes", inline=False)
#    embed.add_field(name="Usage", value="p!filter\np!kick [user]\np!ban [user]\np!clear [amount]\np!fclear [amount]\np!add @member(s) @role(s)\np!rem @member(s) @role(s)\np!warn @user [reason]\np!warn @user <reason>\np!strikes", inline=True)
#    embed.add_field(name="Explanation", value="A chatfilter\nKicks the mentioned user\nBans the mentioned user\nDeletes the selected amount of messages\nSame as clear, faster but more limited\nAdds roles to users\nRemoves roles from users\nWarns the mentioned user\nRemoves the last warning from the mentioned user\nLists all wanings of the mentioned user", inline=True)
    embed.add_field(name="NOTE", value="PLEASE ALSO RUN PERMSYSTEM", inline=False)
    embed.set_footer(text=config.by)
    menuemsg = await client.send_message(message.channel, embed=embed)

    await client.add_reaction(menuemsg, "1⃣")
    await client.add_reaction(menuemsg, "2⃣")
    await client.add_reaction(menuemsg, "3⃣")
    await client.add_reaction(menuemsg, "4⃣")
    await client.add_reaction(menuemsg, "5⃣")
    await client.add_reaction(menuemsg, "6⃣")
    await client.add_reaction(menuemsg, "7⃣")
    await client.add_reaction(menuemsg, "8⃣")
    await client.add_reaction(menuemsg, "9⃣")

    await client.add_reaction(menuemsg, "✅")
    await client.add_reaction(menuemsg, "➡")

    selectionip = True
    selected2 = []
    selectedid = "None"


    while selectionip:

        res = await client.wait_for_reaction(message=menuemsg, check=checkmenuone, user=message.author)
#                    print("past waiting")
        await client.remove_reaction(menuemsg, res.reaction.emoji, res.user)

        if res.reaction.emoji == "✅":

            selectionip = False

            embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
            embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
            embed.set_thumbnail(url=config.embedthumbnail)
            embed.add_field(name="INFO", value="Request done.", inline=True)
            embed.set_footer(text=config.by)

            await client.edit_message(menuemsg, embed=embed)

            await client.remove_reaction(menuemsg, "1⃣", client.user)
            await client.remove_reaction(menuemsg, "2⃣", client.user)
            await client.remove_reaction(menuemsg, "3⃣", client.user)
            await client.remove_reaction(menuemsg, "4⃣", client.user)
            await client.remove_reaction(menuemsg, "5⃣", client.user)
            await client.remove_reaction(menuemsg, "6⃣", client.user)
            await client.remove_reaction(menuemsg, "7⃣", client.user)
            await client.remove_reaction(menuemsg, "8⃣", client.user)
            await client.remove_reaction(menuemsg, "9⃣", client.user)

            await client.remove_reaction(menuemsg, "✅", client.user)
            await client.remove_reaction(menuemsg, "❌", client.user)

            try:
                await client.remove_reaction(menuemsg, "➡", client.user)
            except:
                await client.remove_reaction(menuemsg, "⬅", client.user)

            return

        elif res.reaction.emoji == "➡":
            if page < maxpage:
                if selectedid == "None":

                    page += 1
                    namestypes = namegen(page, commandslist, True)

                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(namestypes)), inline=True)
                    embed.set_footer(text=config.by)

                    await client.edit_message(menuemsg, embed=embed)

                    maxonemore = maxpage + 1

                    if page == maxpage:
                        try:
                            await client.remove_reaction(menuemsg, "➡", client.user)
                        except:
                            pass
                    if page == 2:
                        await client.add_reaction(menuemsg, "⬅")

#                            print("done")
        elif res.reaction.emoji == "⬅":
#                        print("here")
            if page > 1:
                if selectedid == "None":

                    page -= 1
                    namestypes = namegen(page, commandslist, True)

                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(namestypes)), inline=True)
                    embed.set_footer(text=config.by)

                    await client.edit_message(menuemsg, embed=embed)

                    if page == maxpage:
                        try:
                            await client.add_reaction(menuemsg, "➡")
                        except:
                            pass
                    if page > 1:
                        try:
                            await client.add_reaction(menuemsg, "⬅")
                        except:
                            pass
                    else:
                        try:
                            await client.remove_reaction(menuemsg, "⬅", client.user)
                        except:
                            pass
        else:
            if selectedid == "None":

                selectedid = "Command"
                namestypes = namegen(page, commandslist, True)
                names = namegen(page, commandslist, False)
                selectednum = 0

                if res.reaction.emoji == "1⃣":
                 selectednum = 1

                    # allowedstring = ""
                    #
                    # c.execute("SELECT * FROM cmds WHERE sid = '%s' AND cmdid = '%s'" % (message.server.id, "addrole"))
                    # row = c.fetchone()
                    #
                    # if row:
                    #
                    #     if not row[3].find(memberstoadd.mentions[0].id) == -1:
                    #         allowed = True
                    #
                    #     else:
                    #         allowed = False
                    #
                    #     if not row[5].find(memberstoadd.mentions[0].id) == -1:
                    #         allowed = False
                    #
                    #     try:
                    #         for r in memberstoadd.mentions[0].roles:
                    #             if not row[4].find(r) == -1:
                    #                 allowed = False
                    #
                    #     except:
                    #         pass
                    #
                    #     if allowed:
                    #         allowedstring = "Allowed to run `Addrole` ✅"
                    #     else:
                    #         allowedstring = "Allowed to run `Addrole` ❌"
                    # if not row:
                    #
                    #     embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                    #     embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                    #     embed.add_field(name="WARNING :warning:", value="NO CUSTOM PERMISSIONS SET FOR THIS COMMAND!", inline=True)
                    #     embed.set_footer(text=config.by)
                    #
                    #     await client.edit_message(menuemsg, embed=embed)
                elif res.reaction.emoji == "2⃣":
                 selectednum = 2

                elif res.reaction.emoji == "3⃣":
                 selectednum = 3

                elif res.reaction.emoji == "4⃣":
                 selectednum = 4

                elif res.reaction.emoji == "5⃣":
                 selectednum = 5

                elif res.reaction.emoji == "6⃣":
                 selectednum = 6

                elif res.reaction.emoji == "7⃣":
                 selectednum = 7

                elif res.reaction.emoji == "8⃣":
                 selectednum = 8

                elif res.reaction.emoji == "9⃣":
                 selectednum = 9

                selectednum -= 1

                await helpedit(selectednum, names, namestypes, client, menuemsg)
            else:
                selectedid = "None"
                namestypes = namegen(page, commandslist, True)
                helpstring = ('').join(namestypes)

                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                embed.add_field(name="HELP OF %s" % (config.name), value="Prefix: %s" % (config.prefix), inline=False)
                embed.add_field(name="Commands:", value = helpstring, inline=False)
                embed.set_footer(text=config.by)

                await client.edit_message(menuemsg, embed=embed)
