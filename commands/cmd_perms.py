import discord
import config
import excon
import sqlite3
#import _mysql
import embeds
import dictionaries

id = "prm"
conn = sqlite3.connect('sql.db')
c = conn.cursor()
perm = 4

def exit():
    conn.commit()
    conn.close()

def check(reaction, user):
    e = str(reaction.emoji)
    return e.startswith(("1⃣", "2⃣", "3⃣", "4⃣", "5⃣"))

def check3(reaction, user):
    e = str(reaction.emoji)
    return e.startswith(("1⃣", "2⃣", "3⃣"))

def checkmenuone(reaction, user):
    e = str(reaction.emoji)
    return e.startswith(("1⃣", "2⃣", "3⃣", "4⃣", "5⃣", "6⃣", "7⃣", "8⃣", "9⃣", "❌", "✅", "➡" , "⬅"))

async def ex(args, message, client, invoke):
    smsg = ":one: View permissions \n:two: Edit permissions\n:three: Create an exception \n:four: Disable a Command\n:five: Cancel"

    commands = dictionaries.commands()
    commands1 = dictionaries.commands1()
    commands2 = dictionaries.commands2()

    menuemsg = await embeds.menuemsg(message, smsg, client)

    await client.add_reaction(menuemsg, "1⃣")
    await client.add_reaction(menuemsg, "2⃣")
    await client.add_reaction(menuemsg, "3⃣")
    await client.add_reaction(menuemsg, "4⃣")
    await client.add_reaction(menuemsg, "5⃣")

#    member = message.server.get_member(message.author.id)

    res = await client.wait_for_reaction(message=menuemsg, check=check, user=message.author)
    if res.reaction.emoji == "1⃣":
        selected = "view"
    elif res.reaction.emoji == "2⃣":
        selected = "edit"
    elif res.reaction.emoji == "3⃣":
        selected = "exception"
    elif res.reaction.emoji == "4⃣":
        selected = "disable"
    else:
        selected = "cancel"

    await client.remove_reaction(menuemsg, res.reaction.emoji, res.user)

    if selected == "view":

        smsg = ":one: User \n:two: Role\n:three: Command \n:four: Cancel"
        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
        embed.add_field(name="Of what do you want to view the permissions?", value="%s" % (smsg), inline=True)
        await client.edit_message(menuemsg, embed=embed)

        res = await client.wait_for_reaction(message=menuemsg, check=check, user=message.author)
        if res.reaction.emoji == "1⃣":
            selected = "user"
        elif res.reaction.emoji == "2⃣":
            selected = "edit"
        elif res.reaction.emoji == "3⃣":
            selected = "exception"
        elif res.reaction.emoji == "4⃣":
            selected = "disable"
        else:
            selected = "cancel"

        await client.remove_reaction(menuemsg, res.reaction.emoji, res.user)

        if selected == "user":


                embed=discord.Embed(title="Discord", url=config.invite, color=0x3498db)
                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                embed.set_thumbnail(url=config.embedthumbnail)
                embed.add_field(name="WARNING", value="@ Mention the member you want to view the permissions of.", inline=True)
                embed.set_footer(text=config.by)
                await client.edit_message(menuemsg, embed=embed)

                memberstoadd = await client.wait_for_message(timeout=None, author=message.author, channel=message.channel)

                await client.delete_message(memberstoadd)

                arglen = len(memberstoadd.mentions)

                if arglen == 0:
                    embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                    embed.add_field(name="WARNING", value="Please select someone!", inline=True)
                    embed.set_footer(text=config.by)

                    await client.edit_message(menuemsg, embed=embed)

                    return

                listformatone = []
                listformattwo = []
                cmdnumb = 1
                for name, id1 in commands1.items():
                    listformatone.append("\n")
                    if cmdnumb == 1:
                        listformatone.append(":one:")
                    elif cmdnumb == 2:
                        listformatone.append(":two:")
                    elif cmdnumb == 3:
                        listformatone.append(":three:")
                    elif cmdnumb == 4:
                        listformatone.append(":four:")
                    elif cmdnumb == 5:
                        listformatone.append(":five:")
                    elif cmdnumb == 6:
                        listformatone.append(":six:")
                    elif cmdnumb == 7:
                        listformatone.append(":seven:")
                    elif cmdnumb == 8:
                        listformatone.append(":eight:")
                    elif cmdnumb == 9:
                        listformatone.append(":nine:")
                    listformatone.append(name)

                    allowed = False
                    nocustomperms1 = False

                    c.execute("SELECT * FROM cmds WHERE sid = '%s' AND cmdid = '%s'" % (message.server.id, id1))

                    row = c.fetchone()
                    if row:

                        if not row[3].find(memberstoadd.mentions[0].id) == -1:
                            allowed = True

                        else:
                            allowed = False

                        if not row[5].find(memberstoadd.mentions[0].id) == -1:
                            allowed = False

                        if allowed:
                            listformatone.append(" ✅")
                        else:
                            listformatone.append(" ❌")

                    if not row:
                        listformatone.append(" ☝")
                        nocustomperms1 = True
        #                    print(listformatone)
                    cmdnumb += 1

                if nocustomperms1:
                    listformatone.append("\n\n☝ = !!No custom permissions found for this command, please view the standard permission configuration!!")

                cmdnumb = 1

                for name, id in commands2.items():
                    listformattwo.append("\n")
                    if cmdnumb == 1:
                        listformattwo.append(":one:")
                    elif cmdnumb == 2:
                        listformattwo.append(":two:")
                    elif cmdnumb == 3:
                        listformattwo.append(":three:")
                    elif cmdnumb == 4:
                        listformattwo.append(":four:")
                    elif cmdnumb == 5:
                        listformattwo.append(":five:")
                    elif cmdnumb == 6:
                        listformattwo.append(":six:")
                    elif cmdnumb == 7:
                        listformattwo.append(":seven:")
                    elif cmdnumb == 8:
                        listformattwo.append(":eight:")
                    elif cmdnumb == 9:
                        listformattwo.append(":nine:")
                    listformattwo.append(name)

                    allowed = False
                    nocustomperms2 = False

                    c.execute("SELECT * FROM cmds WHERE sid = '%s' AND cmdid = '%s'" % (message.server.id, id1))

                    row = c.fetchone()

                    if row:

                        if not row[3].find(memberstoadd.mentions[0].id) == -1:
                            allowed = True

                        else:
                            allowed = False

                        if not row[5].find(memberstoadd.mentions[0].id) == -1:
                            allowed = False

                        try:
                            for r in memberstoadd.mentions[0].roles:
                                if not row[4].find(r) == -1:
                                    allowed = False

                        except:
                            pass

                        if allowed:
                            listformattwo.append(" ✅")
                        else:
                            listformattwo.append(" ❌")

                    if not row:
                        listformattwo.append(" ☝")
                        nocustomperms2 = True
        #                    print(listformatone)
                    cmdnumb += 1

                if nocustomperms2:
                    listformattwo.append("\n\n☝ = !!No custom permissions found for this command, please view the standard permission configuration!!")


                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                embed.add_field(name="Select a command to get more information!", value="%s" % (('').join(listformatone)), inline=True)
                await client.edit_message(menuemsg, embed=embed)

                current = 1

                # await client.add_reaction(menuemsg, "1⃣")
                # await client.add_reaction(menuemsg, "2⃣")
                # await client.add_reaction(menuemsg, "3⃣")
                await client.add_reaction(menuemsg, "4⃣")
                await client.add_reaction(menuemsg, "5⃣")
                await client.add_reaction(menuemsg, "6⃣")
                await client.add_reaction(menuemsg, "7⃣")
                await client.add_reaction(menuemsg, "8⃣")
                await client.add_reaction(menuemsg, "9⃣")

                await client.add_reaction(menuemsg, "➡")
                await client.add_reaction(menuemsg, "✅")
                await client.add_reaction(menuemsg, "❌")

                selectionip = True
                selected2 = []
                selectedid = ["None"]

                while selectionip: #(make abc false once ok or cancel)

        #                    print("in while")

                    res = await client.wait_for_reaction(message=menuemsg, check=checkmenuone, user=message.author)
        #                    print("past waiting")
                    await client.remove_reaction(menuemsg, res.reaction.emoji, res.user)

                    if res.reaction.emoji == "❌":
                        selectionip = False
                        embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                        embed.set_thumbnail(url=config.embedthumbnail)
                        embed.add_field(name="WARNING", value="Request canceled", inline=True)
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

                        if current == 1:
                            await client.remove_reaction(menuemsg, "➡", client.user)
                        else:
                            await client.remove_reaction(menuemsg, "⬅", client.user)

                        return

                    elif res.reaction.emoji == "➡":
                        if current == 1:

                            menulist = list(listformattwo)
                            menulist.extend(selected2)

                            await client.remove_reaction(menuemsg, "➡", client.user)
                            await client.add_reaction(menuemsg, "⬅")

                            embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                            embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                            embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                            embed.set_footer(text=config.by)

                            await client.edit_message(menuemsg, embed=embed)

                            current = 2
        #                            print("done")
                    elif res.reaction.emoji == "⬅":
        #                        print("here")
                        if current == 2:

                            menulist = list(listformatone)
                            menulist.extend(selected2)

                            await client.remove_reaction(menuemsg, "⬅", client.user)
                            await client.add_reaction(menuemsg, "➡")

                            embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                            embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                            embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                            embed.set_footer(text=config.by)

                            await client.edit_message(menuemsg, embed=embed)

                            current = 1


                    else:
                        if current == 1:
                            if res.reaction.emoji == "1⃣":
                                if "addrole" in selectedid:

                                    selectedid.remove("addrole")

                                    menulist = list(listformatone)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selectedid.append("addrole")

                                    menulist = list(listformatone)
                                    allowedstring = ""

                                    c.execute("SELECT * FROM cmds WHERE sid = '%s' AND cmdid = '%s'" % (message.server.id, "addrole"))
                                    row = c.fetchone()

                                    if row:

                                        if not row[3].find(memberstoadd.mentions[0].id) == -1:
                                            allowed = True

                                        else:
                                            allowed = False

                                        if not row[5].find(memberstoadd.mentions[0].id) == -1:
                                            allowed = False

                                        try:
                                            for r in memberstoadd.mentions[0].roles:
                                                if not row[4].find(r) == -1:
                                                    allowed = False

                                        except:
                                            pass

                                        if allowed:
                                            allowedstring = "Allowed to run `Addrole` ✅"
                                        else:
                                            allowedstring = "Allowed to run `Addrole` ❌"
                                    if not row:

                                        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                        embed.add_field(name="WARNING :warning:", value="NO CUSTOM PERMISSIONS SET FOR THIS COMMAND!", inline=True)
                                        embed.set_footer(text=config.by)

                                        await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "2⃣":
                                    if "Ban\n" not in selected2:

                                        selected2.append("Ban\n")
                                        selectedid.append("ban")

                                        menulist = list(listformatone)
                                        menulist.extend(selected2)

                                        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                        embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                        embed.set_footer(text=config.by)

                                        await client.edit_message(menuemsg, embed=embed)
                                    else:

                                        selected2.remove("Ban\n")
                                        selectedid.append("ban")

                                        menulist = list(listformatone)
                                        menulist.extend(selected2)

                                        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                        embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                        embed.set_footer(text=config.by)

                                        await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "3⃣":
                                if "Clear\n" not in selected2:

                                    selected2.append("Clear\n")
                                    selectedid.append("clear")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Clear\n")
                                    selectedid.append("clear")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "4⃣":
                                if "Countmsg\n" not in selected2:

                                    selected2.append("Countmsg\n")
                                    selectedid.append("cmsg")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Countmsg\n")
                                    selectedid.append("cmsg")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "5⃣":
                                if "FAQ\n" not in selected2:

                                    selected2.append("FAQ\n")
                                    selectedid.append("faq")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("FAQ\n")
                                    selectedid.append("faq")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "6⃣":
                                if "Fast-Clear\n" not in selected2:

                                    selected2.append("Fast-Clear\n")
                                    selectedid.append("fclear")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Fast-Clear\n")
                                    selectedid.append("fclear")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "7⃣":
                                if "Filter\n" not in selected2:

                                    selected2.append("Filter\n")
                                    selectedid.append("filter")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Filter\n")
                                    selectedid.append("filter")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "8⃣":
                                if "Gundam\n" not in selected2:

                                    selected2.append("Gundam\n")
                                    selectedid.append("gundam")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Gundam\n")
                                    selectedid.append("gundam")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "9⃣":
                                if "Help\n" not in selected2:

                                    selected2.append("Help\n")
                                    selectedid.append("help")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Help\n")
                                    selectedid.append("help")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)

                        elif current == 2:
                            if res.reaction.emoji == "1⃣":
                                if "Kick\n" not in selected2:

                                    selected2.append("Kick\n")
                                    selectedid.append("kick")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Kick\n")
                                    selectedid.append("kick")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "2⃣":
                                    if "List\n" not in selected2:

                                        selected2.append("List\n")
                                        selectedid.append("list")

                                        menulist = list(listformattwo)
                                        menulist.extend(selected2)

                                        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                        embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                        embed.set_footer(text=config.by)

                                        await client.edit_message(menuemsg, embed=embed)
                                    else:

                                        selected2.remove("List\n")
                                        selectedid.append("list")

                                        menulist = list(listformattwo)
                                        menulist.extend(selected2)

                                        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                        embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                        embed.set_footer(text=config.by)

                                        await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "3⃣":
                                if "Pardon\n" not in selected2:

                                    selected2.append("Pardon\n")
                                    selectedid.append("pardon")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Pardon\n")
                                    selectedid.append("pardon")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "4⃣":
                                if "Permsys\n" not in selected2:

                                    selected2.append("Permsys\n")
                                    selectedid.append("prmsys")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Permsys\n")
                                    selectedid.append("prmsys")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "5⃣":
                                if "Ping\n" not in selected2:

                                    selected2.append("Ping\n")
                                    selectedid.append("ping")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Ping\n")
                                    selectedid.append("ping")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "6⃣":
                                if "Remrole\n" not in selected2:

                                    selected2.append("Remrole\n")
                                    selectedid.append("remrole")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Remrole\n")
                                    selectedid.append("remrole")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "7⃣":
                                if "Userclear\n" not in selected2:

                                    selected2.append("Userclear\n")
                                    selectedid.append("uclear")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Userclear\n")
                                    selectedid.append("uclear")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "8⃣":
                                if "Version\n" not in selected2:

                                    selected2.append("Version\n")
                                    selectedid.append("ver")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Version\n")
                                    selectedid.append("ver")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "9⃣":
                                if "Warn\n" not in selected2:

                                    selected2.append("Warn\n")
                                    selectedid.append("warn")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Warn\n")
                                    selectedid.append("warn")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)

#END LELLELELLEL(/(/))


    elif selected == "edit":
        await client.remove_reaction(menuemsg, "4⃣", client.user)
        await client.remove_reaction(menuemsg, "5⃣", client.user)

        await client.remove_reaction(menuemsg, res.reaction.emoji, res.user)

        smsg = ":one: Add \n:two: Remove \n:three: Cancel"
        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
        embed.add_field(name="Do you want to add or remove permissions?", value="%s" % (smsg), inline=True)
        await client.edit_message(menuemsg, embed=embed)
        res = await client.wait_for_reaction(message=menuemsg, check=check3, user=message.author)

        await client.remove_reaction(menuemsg, res.reaction.emoji, res.user)
        # await client.remove_reaction(menuemsg, "1⃣", client.user)
        # await client.remove_reaction(menuemsg, "2⃣", client.user)
        # await client.remove_reaction(menuemsg, "3⃣", client.user)

        if res.reaction.emoji == "1⃣":
            selected3 = "add"
        elif res.reaction.emoji == "2⃣":
            selected3 = "remove"
        else:
            selected3 = "cancel"

        if selected3 == "add":

            listformatone = []
            listformattwo = []
            cmdnumb = 1
            for name, id in commands1.items():
                listformatone.append("\n")
                if cmdnumb == 1:
                    listformatone.append(":one:")
                elif cmdnumb == 2:
                    listformatone.append(":two:")
                elif cmdnumb == 3:
                    listformatone.append(":three:")
                elif cmdnumb == 4:
                    listformatone.append(":four:")
                elif cmdnumb == 5:
                    listformatone.append(":five:")
                elif cmdnumb == 6:
                    listformatone.append(":six:")
                elif cmdnumb == 7:
                    listformatone.append(":seven:")
                elif cmdnumb == 8:
                    listformatone.append(":eight:")
                elif cmdnumb == 9:
                    listformatone.append(":nine:")
                listformatone.append(name)
    #                    print(listformatone)
                cmdnumb += 1

            cmdnumb = 1

            for name, id in commands2.items():
                listformattwo.append("\n")
                if cmdnumb == 1:
                    listformattwo.append(":one:")
                elif cmdnumb == 2:
                    listformattwo.append(":two:")
                elif cmdnumb == 3:
                    listformattwo.append(":three:")
                elif cmdnumb == 4:
                    listformattwo.append(":four:")
                elif cmdnumb == 5:
                    listformattwo.append(":five:")
                elif cmdnumb == 6:
                    listformattwo.append(":six:")
                elif cmdnumb == 7:
                    listformattwo.append(":seven:")
                elif cmdnumb == 8:
                    listformattwo.append(":eight:")
                elif cmdnumb == 9:
                    listformattwo.append(":nine:")
                listformattwo.append(name)
    #                    print(listformattwo)
                cmdnumb += 1
    #                await client.add_reaction(menuemsg, "⬅")

            embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
            embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
            embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(listformatone)), inline=True)
            await client.edit_message(menuemsg, embed=embed)

            current = 1

            # await client.add_reaction(menuemsg, "1⃣")
            # await client.add_reaction(menuemsg, "2⃣")
            # await client.add_reaction(menuemsg, "3⃣")
            await client.add_reaction(menuemsg, "4⃣")
            await client.add_reaction(menuemsg, "5⃣")
            await client.add_reaction(menuemsg, "6⃣")
            await client.add_reaction(menuemsg, "7⃣")
            await client.add_reaction(menuemsg, "8⃣")
            await client.add_reaction(menuemsg, "9⃣")

            await client.add_reaction(menuemsg, "➡")
            await client.add_reaction(menuemsg, "✅")
            await client.add_reaction(menuemsg, "❌")

            selectionip = True
            selected2 = ["\n\nSelected:\n\n"]
            selectedid = []

            while selectionip: #(make abc false once ok or cancel)

    #                    print("in while")

                res = await client.wait_for_reaction(message=menuemsg, check=checkmenuone, user=message.author)
    #                    print("past waiting")
                await client.remove_reaction(menuemsg, res.reaction.emoji, res.user)

                if res.reaction.emoji == "❌":
                    selectionip = False
                    embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                    embed.set_thumbnail(url=config.embedthumbnail)
                    embed.add_field(name="WARNING", value="Request canceled", inline=True)
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

                    if current == 1:
                        await client.remove_reaction(menuemsg, "➡", client.user)
                    else:
                        await client.remove_reaction(menuemsg, "⬅", client.user)

                    return

                elif res.reaction.emoji == "➡":
                    if current == 1:

                        menulist = list(listformattwo)
                        menulist.extend(selected2)

                        await client.remove_reaction(menuemsg, "➡", client.user)
                        await client.add_reaction(menuemsg, "⬅")

                        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                        embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                        embed.set_footer(text=config.by)

                        await client.edit_message(menuemsg, embed=embed)

                        current = 2
    #                            print("done")
                elif res.reaction.emoji == "⬅":
    #                        print("here")
                    if current == 2:

                        menulist = list(listformatone)
                        menulist.extend(selected2)

                        await client.remove_reaction(menuemsg, "⬅", client.user)
                        await client.add_reaction(menuemsg, "➡")

                        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                        embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                        embed.set_footer(text=config.by)

                        await client.edit_message(menuemsg, embed=embed)

                        current = 1

                elif res.reaction.emoji == "✅":

                    selectionip = False
                    embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                    embed.set_thumbnail(url=config.embedthumbnail)
                    embed.add_field(name="WARNING", value="Working.....", inline=True)
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

                    if current == 1:
                        await client.remove_reaction(menuemsg, "➡", client.user)
                    else:
                        await client.remove_reaction(menuemsg, "⬅", client.user)

                    embed=discord.Embed(title="Discord", url=config.invite, color=0x3498db)
                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                    embed.set_thumbnail(url=config.embedthumbnail)
                    embed.add_field(name="WARNING", value="@ Mention all members / roles you want to change the permissions of.", inline=True)
                    embed.set_footer(text=config.by)
                    await client.edit_message(menuemsg, embed=embed)

                    memberstoadd = await client.wait_for_message(timeout=None, author=message.author, channel=message.channel)

                    embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                    embed.set_thumbnail(url=config.embedthumbnail)
                    embed.add_field(name="WARNING", value="Working.....", inline=True)
                    embed.set_footer(text=config.by)
                    await client.edit_message(menuemsg, embed=embed)

                    membids = []
                    roleids = []

                    mempingids = []
                    rolepingids = []

                    ffa = 0

                    c.execute("SELECT * FROM cmds WHERE sid = '%s'" % (message.server.id))
                    row = c.fetchone()

                    if not row:
                        ffa = 0
                    else:
                        ffa = row[6]

                    await client.delete_message(memberstoadd)

                    if not memberstoadd.content.lower().find('@everyone') == -1:
                        ffa = 1

                    for m in memberstoadd.mentions:

                        membids.append(m.id)
                        mempingids.append(m.id)

                    for r in memberstoadd.role_mentions:

                        roleids.append(r.id)
                        rolepingids.append(r.id)

                    arglen = len(membids) + len(roleids)

                    if arglen == 0:
                        embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                        embed.add_field(name="WARNING", value="Please select some people/roles!", inline=True)
                        embed.set_footer(text=config.by)

                        await client.edit_message(menuemsg, embed=embed)

                    for cmid in selectedid:

                        c.execute("SELECT * FROM cmds WHERE sid = '%s' AND cmdid = '%s'" % (message.server.id, cmid))

                        row = c.fetchone()

                        if row:
                            rowids = row[3].split(',')
                            rolids = row[2].split(',')

                        else:
                            rowids = []
                            rolids = []



                        for id in rowids:
                            try:
                                membids.remove(id)
                            except:
                                pass


                        for id in rolids:
                            try:
                                roleids.remove(id)
                            except:
                                pass

                        for id in membids:
                            try:
                                rowids.append(id)
                            except:
                                pass

                        for id in roleids:
                            try:
                                rolids.append(id)
                            except:
                                pass

                        if len(rowids) == 0:
                            rowids.append("0")

                        if len(roleids) == 0:
                            rolids.append("0")

                        if not row:
                            c.execute('INSERT INTO cmds (sid, cmdid, rid, mid, erid, emid, ffa) VALUES (?, ?, ?, ?, ?, ?, ?) ' , (message.server.id, cmid, (',').join(roleids), (',').join(membids), "0", "0", ffa))
                            conn.commit()
                            # c.execute("SELECT * FROM cmds WHERE sid = '%s' AND cmdid = '%s'" % (message.server.id, cmid))
                            # row = c.fetchone()

                        else:
                            c.execute('UPDATE cmds SET mid = ? WHERE sid = ? AND cmdid = ?' , ((',').join(rowids) , message.server.id, cmid))
                            conn.commit()

                            c.execute('UPDATE cmds SET ffa = ? WHERE sid = ? AND cmdid = ?' , (ffa , message.server.id, cmid))
                            conn.commit()

                            c.execute('UPDATE cmds SET rid = ? WHERE sid = ? AND cmdid = ?' , ((',').join(rolids) , message.server.id, cmid))
                            conn.commit()

                    pings = []

                    for id in mempingids:
                        if not id == "0":
                            pings.append("<@%s>" % (id))

                    for id in rolepingids:
                        if not id == "0":
                            pings.append("<@&%s>" % (id))

                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x2ecc71)
                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                    embed.add_field(name="SUCCESS", value="Changed the permissions of %s" % (', '.join(pings)), inline=True)
                    embed.set_footer(text=config.by)

                    await client.edit_message(menuemsg, embed=embed)

                    return

                else:
                    if current == 1:
                        if res.reaction.emoji == "1⃣":
                            if "Addrole\n" not in selected2:

                                selected2.append("Addrole\n")
                                selectedid.append("addrole")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Addrole\n")
                                selectedid.append("addrole")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "2⃣":
                                if "Ban\n" not in selected2:

                                    selected2.append("Ban\n")
                                    selectedid.append("ban")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Ban\n")
                                    selectedid.append("ban")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "3⃣":
                            if "Clear\n" not in selected2:

                                selected2.append("Clear\n")
                                selectedid.append("clear")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Clear\n")
                                selectedid.append("clear")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "4⃣":
                            if "Countmsg\n" not in selected2:

                                selected2.append("Countmsg\n")
                                selectedid.append("cmsg")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Countmsg\n")
                                selectedid.append("cmsg")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "5⃣":
                            if "FAQ\n" not in selected2:

                                selected2.append("FAQ\n")
                                selectedid.append("faq")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("FAQ\n")
                                selectedid.append("faq")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "6⃣":
                            if "Fast-Clear\n" not in selected2:

                                selected2.append("Fast-Clear\n")
                                selectedid.append("fclear")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Fast-Clear\n")
                                selectedid.append("fclear")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "7⃣":
                            if "Filter\n" not in selected2:

                                selected2.append("Filter\n")
                                selectedid.append("filter")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Filter\n")
                                selectedid.append("filter")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "8⃣":
                            if "Gundam\n" not in selected2:

                                selected2.append("Gundam\n")
                                selectedid.append("gundam")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Gundam\n")
                                selectedid.append("gundam")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "9⃣":
                            if "Help\n" not in selected2:

                                selected2.append("Help\n")
                                selectedid.append("help")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Help\n")
                                selectedid.append("help")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)

                    elif current == 2:
                        if res.reaction.emoji == "1⃣":
                            if "Kick\n" not in selected2:

                                selected2.append("Kick\n")
                                selectedid.append("kick")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Kick\n")
                                selectedid.append("kick")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "2⃣":
                                if "List\n" not in selected2:

                                    selected2.append("List\n")
                                    selectedid.append("list")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("List\n")
                                    selectedid.append("list")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "3⃣":
                            if "Pardon\n" not in selected2:

                                selected2.append("Pardon\n")
                                selectedid.append("pardon")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Pardon\n")
                                selectedid.append("pardon")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "4⃣":
                            if "Permsys\n" not in selected2:

                                selected2.append("Permsys\n")
                                selectedid.append("prmsys")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Permsys\n")
                                selectedid.append("prmsys")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "5⃣":
                            if "Ping\n" not in selected2:

                                selected2.append("Ping\n")
                                selectedid.append("ping")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Ping\n")
                                selectedid.append("ping")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "6⃣":
                            if "Remrole\n" not in selected2:

                                selected2.append("Remrole\n")
                                selectedid.append("remrole")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Remrole\n")
                                selectedid.append("remrole")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "7⃣":
                            if "Userclear\n" not in selected2:

                                selected2.append("Userclear\n")
                                selectedid.append("uclear")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Userclear\n")
                                selectedid.append("uclear")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "8⃣":
                            if "Version\n" not in selected2:

                                selected2.append("Version\n")
                                selectedid.append("ver")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Version\n")
                                selectedid.append("ver")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "9⃣":
                            if "Warn\n" not in selected2:

                                selected2.append("Warn\n")
                                selectedid.append("warn")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Warn\n")
                                selectedid.append("warn")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
        if selected3 == "remove":

                listformatone = []
                listformattwo = []
                cmdnumb = 1
                for name, id in commands1.items():
                    listformatone.append("\n")
                    if cmdnumb == 1:
                        listformatone.append(":one:")
                    elif cmdnumb == 2:
                        listformatone.append(":two:")
                    elif cmdnumb == 3:
                        listformatone.append(":three:")
                    elif cmdnumb == 4:
                        listformatone.append(":four:")
                    elif cmdnumb == 5:
                        listformatone.append(":five:")
                    elif cmdnumb == 6:
                        listformatone.append(":six:")
                    elif cmdnumb == 7:
                        listformatone.append(":seven:")
                    elif cmdnumb == 8:
                        listformatone.append(":eight:")
                    elif cmdnumb == 9:
                        listformatone.append(":nine:")
                    listformatone.append(name)
        #                    print(listformatone)
                    cmdnumb += 1

                cmdnumb = 1

                for name, id in commands2.items():
                    listformattwo.append("\n")
                    if cmdnumb == 1:
                        listformattwo.append(":one:")
                    elif cmdnumb == 2:
                        listformattwo.append(":two:")
                    elif cmdnumb == 3:
                        listformattwo.append(":three:")
                    elif cmdnumb == 4:
                        listformattwo.append(":four:")
                    elif cmdnumb == 5:
                        listformattwo.append(":five:")
                    elif cmdnumb == 6:
                        listformattwo.append(":six:")
                    elif cmdnumb == 7:
                        listformattwo.append(":seven:")
                    elif cmdnumb == 8:
                        listformattwo.append(":eight:")
                    elif cmdnumb == 9:
                        listformattwo.append(":nine:")
                    listformattwo.append(name)
        #                    print(listformattwo)
                    cmdnumb += 1
        #                await client.add_reaction(menuemsg, "⬅")

                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(listformatone)), inline=True)
                await client.edit_message(menuemsg, embed=embed)

                current = 1

                # await client.add_reaction(menuemsg, "1⃣")
                # await client.add_reaction(menuemsg, "2⃣")
                # await client.add_reaction(menuemsg, "3⃣")
                await client.add_reaction(menuemsg, "4⃣")
                await client.add_reaction(menuemsg, "5⃣")
                await client.add_reaction(menuemsg, "6⃣")
                await client.add_reaction(menuemsg, "7⃣")
                await client.add_reaction(menuemsg, "8⃣")
                await client.add_reaction(menuemsg, "9⃣")

                await client.add_reaction(menuemsg, "➡")
                await client.add_reaction(menuemsg, "✅")
                await client.add_reaction(menuemsg, "❌")

                selectionip = True
                selected2 = ["\n\nSelected:\n\n"]
                selectedid = []

                while selectionip: #(make abc false once ok or cancel)

        #                    print("in while")

                    res = await client.wait_for_reaction(message=menuemsg, check=checkmenuone, user=message.author)
        #                    print("past waiting")
                    await client.remove_reaction(menuemsg, res.reaction.emoji, res.user)

                    if res.reaction.emoji == "❌":
                        selectionip = False
                        embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                        embed.set_thumbnail(url=config.embedthumbnail)
                        embed.add_field(name="WARNING", value="Request canceled", inline=True)
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

                        if current == 1:
                            await client.remove_reaction(menuemsg, "➡", client.user)
                        else:
                            await client.remove_reaction(menuemsg, "⬅", client.user)

                        return

                    elif res.reaction.emoji == "➡":
                        if current == 1:

                            menulist = list(listformattwo)
                            menulist.extend(selected2)

                            await client.remove_reaction(menuemsg, "➡", client.user)
                            await client.add_reaction(menuemsg, "⬅")

                            embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                            embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                            embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                            embed.set_footer(text=config.by)

                            await client.edit_message(menuemsg, embed=embed)

                            current = 2
        #                            print("done")
                    elif res.reaction.emoji == "⬅":
        #                        print("here")
                        if current == 2:

                            menulist = list(listformatone)
                            menulist.extend(selected2)

                            await client.remove_reaction(menuemsg, "⬅", client.user)
                            await client.add_reaction(menuemsg, "➡")

                            embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                            embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                            embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                            embed.set_footer(text=config.by)

                            await client.edit_message(menuemsg, embed=embed)

                            current = 1

                    elif res.reaction.emoji == "✅":

                        selectionip = False
                        embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                        embed.set_thumbnail(url=config.embedthumbnail)
                        embed.add_field(name="WARNING", value="Working.....", inline=True)
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

                        if current == 1:
                            await client.remove_reaction(menuemsg, "➡", client.user)
                        else:
                            await client.remove_reaction(menuemsg, "⬅", client.user)

                        embed=discord.Embed(title="Discord", url=config.invite, color=0x3498db)
                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                        embed.set_thumbnail(url=config.embedthumbnail)
                        embed.add_field(name="WARNING", value="@ Mention all members/roles you want to change the permissions of.", inline=True)
                        embed.set_footer(text=config.by)
                        await client.edit_message(menuemsg, embed=embed)

                        memberstoadd = await client.wait_for_message(timeout=None, author=message.author, channel=message.channel)

                        embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                        embed.set_thumbnail(url=config.embedthumbnail)
                        embed.add_field(name="WARNING", value="Working.....", inline=True)
                        embed.set_footer(text=config.by)
                        await client.edit_message(menuemsg, embed=embed)


                        membids = []
                        roleids = []

                        mempingids = []
                        rolepingids = []

                        ffa = 0

                        c.execute("SELECT * FROM cmds WHERE sid = '%s'" % (message.server.id))
                        row = c.fetchone()

                        if not row:
                            ffa = 0
                        else:
                            ffa = row[6]

                        await client.delete_message(memberstoadd)

                        if not memberstoadd.content.lower().find('@everyone') == -1:
                            ffa = 0

                        for m in memberstoadd.mentions:

                            membids.append(m.id)
                            mempingids.append(m.id)

                        for r in memberstoadd.role_mentions:

                            roleids.append(r.id)
                            rolepingids.append(r.id)

                        arglen = len(membids) + len(roleids)

                        if arglen == 0:
                            embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
                            embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                            embed.add_field(name="WARNING", value="Please select some people/roles!", inline=True)
                            embed.set_footer(text=config.by)

                            await client.edit_message(menuemsg, embed=embed)

                        for cmid in selectedid:

                            c.execute("SELECT * FROM cmds WHERE sid = '%s' AND cmdid = '%s'" % (message.server.id, cmid))
                            row = c.fetchone()

                            # membersfound = 1
                            # rolesfound = 1

                            # if len(roleids) == 0:
                            #     roleids.append("0")
                            #     rolesfound = 0
                            #     rolepingidz = []
                            # else:
                            #     rolepingidz = []
                            #     for id in roleids:
                            #         rolepingidz.append(id)
                            # if len(membids) == 0:
                            #     membids.append("0")
                            #     membersfound = 0
                            #     membpingidz = []
                            # else:
                            #     membpingidz = []
                            #     for id in membids:
                            #         membpingidz.append(id)

                            if not row:

                                c.execute('INSERT INTO cmds (sid, cmdid, rid, mid, erid, emid, ffa) VALUES (?, ?, ?, ?, ?, ?, ?) ' , (message.server.id, cmid, "0", "0", "0", "0", ffa))
                                conn.commit()
                                # c.execute("SELECT * FROM cmds WHERE sid = '%s' AND cmdid = '%s'" % (message.server.id, cmid))
                                # row = c.fetchone()

                            else:

                                rowids = row[3].split(',')

                                for id in membids:
                                    try:
                                        rowids.remove(id)
                                    except:
                                        pass

                                rolids = row[2].split(',')

                                for id in roleids:
                                    try:
                                        rolids.remove(id)
                                    except:
                                        pass

                                if len(rowids) == 0:
                                    rowids.append("0")

                                if len(roleids) == 0:
                                    rolids.append("0")

                                c.execute('UPDATE cmds SET mid = ? WHERE sid = ? AND cmdid = ?' , ((',').join(rowids) , message.server.id, cmid))
                                conn.commit()

                                c.execute('UPDATE cmds SET ffa = ? WHERE sid = ? AND cmdid = ?' , (ffa , message.server.id, cmid))
                                conn.commit()

                                c.execute('UPDATE cmds SET rid = ? WHERE sid = ? AND cmdid = ?' , ((',').join(rolids) , message.server.id, cmid))
                                conn.commit()

                        pings = []

                        for id in mempingids:
                            if not id == "0":
                                pings.append("<@%s>" % (id))

                        for id in rolepingids:
                            if not id == "0":
                                pings.append("<@&%s>" % (id))

                        embed=discord.Embed(title="Discord", url=config.invite, colour=0x2ecc71)
                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                        embed.add_field(name="SUCCESS", value="Changed the permissions of %s" % (', '.join(pings)), inline=True)
                        embed.set_footer(text=config.by)

                        await client.edit_message(menuemsg, embed=embed)

                        return

                    else:
                        if current == 1:
                            if res.reaction.emoji == "1⃣":
                                if "Addrole\n" not in selected2:

                                    selected2.append("Addrole\n")
                                    selectedid.append("addrole")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Addrole\n")
                                    selectedid.append("addrole")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "2⃣":
                                    if "Ban\n" not in selected2:

                                        selected2.append("Ban\n")
                                        selectedid.append("ban")

                                        menulist = list(listformatone)
                                        menulist.extend(selected2)

                                        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                        embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                        embed.set_footer(text=config.by)

                                        await client.edit_message(menuemsg, embed=embed)
                                    else:

                                        selected2.remove("Ban\n")
                                        selectedid.append("ban")

                                        menulist = list(listformatone)
                                        menulist.extend(selected2)

                                        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                        embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                        embed.set_footer(text=config.by)

                                        await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "3⃣":
                                if "Clear\n" not in selected2:

                                    selected2.append("Clear\n")
                                    selectedid.append("clear")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Clear\n")
                                    selectedid.append("clear")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "4⃣":
                                if "Countmsg\n" not in selected2:

                                    selected2.append("Countmsg\n")
                                    selectedid.append("cmsg")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Countmsg\n")
                                    selectedid.append("cmsg")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "5⃣":
                                if "FAQ\n" not in selected2:

                                    selected2.append("FAQ\n")
                                    selectedid.append("faq")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("FAQ\n")
                                    selectedid.append("faq")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "6⃣":
                                if "Fast-Clear\n" not in selected2:

                                    selected2.append("Fast-Clear\n")
                                    selectedid.append("fclear")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Fast-Clear\n")
                                    selectedid.append("fclear")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "7⃣":
                                if "Filter\n" not in selected2:

                                    selected2.append("Filter\n")
                                    selectedid.append("filter")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Filter\n")
                                    selectedid.append("filter")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "8⃣":
                                if "Gundam\n" not in selected2:

                                    selected2.append("Gundam\n")
                                    selectedid.append("gundam")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Gundam\n")
                                    selectedid.append("gundam")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "9⃣":
                                if "Help\n" not in selected2:

                                    selected2.append("Help\n")
                                    selectedid.append("help")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Help\n")
                                    selectedid.append("help")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)

                        elif current == 2:
                            if res.reaction.emoji == "1⃣":
                                if "Kick\n" not in selected2:

                                    selected2.append("Kick\n")
                                    selectedid.append("kick")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Kick\n")
                                    selectedid.append("kick")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "2⃣":
                                    if "List\n" not in selected2:

                                        selected2.append("List\n")
                                        selectedid.append("list")

                                        menulist = list(listformattwo)
                                        menulist.extend(selected2)

                                        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                        embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                        embed.set_footer(text=config.by)

                                        await client.edit_message(menuemsg, embed=embed)
                                    else:

                                        selected2.remove("List\n")
                                        selectedid.append("list")

                                        menulist = list(listformattwo)
                                        menulist.extend(selected2)

                                        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                        embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                        embed.set_footer(text=config.by)

                                        await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "3⃣":
                                if "Pardon\n" not in selected2:

                                    selected2.append("Pardon\n")
                                    selectedid.append("pardon")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Pardon\n")
                                    selectedid.append("pardon")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "4⃣":
                                if "Permsys\n" not in selected2:

                                    selected2.append("Permsys\n")
                                    selectedid.append("prmsys")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Permsys\n")
                                    selectedid.append("prmsys")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "5⃣":
                                if "Ping\n" not in selected2:

                                    selected2.append("Ping\n")
                                    selectedid.append("ping")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Ping\n")
                                    selectedid.append("ping")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "6⃣":
                                if "Remrole\n" not in selected2:

                                    selected2.append("Remrole\n")
                                    selectedid.append("remrole")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Remrole\n")
                                    selectedid.append("remrole")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "7⃣":
                                if "Userclear\n" not in selected2:

                                    selected2.append("Userclear\n")
                                    selectedid.append("uclear")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Userclear\n")
                                    selectedid.append("uclear")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "8⃣":
                                if "Version\n" not in selected2:

                                    selected2.append("Version\n")
                                    selectedid.append("ver")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Version\n")
                                    selectedid.append("ver")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "9⃣":
                                if "Warn\n" not in selected2:

                                    selected2.append("Warn\n")
                                    selectedid.append("warn")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Warn\n")
                                    selectedid.append("warn")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the permissions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)





    elif selected == "exception":
        await client.remove_reaction(menuemsg, "4⃣", client.user)
        await client.remove_reaction(menuemsg, "5⃣", client.user)

        await client.remove_reaction(menuemsg, res.reaction.emoji, res.user)

        smsg = ":one: Add \n:two: Remove \n:three: Cancel"
        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
        embed.add_field(name="Do you want to add or remove an exception?", value="%s" % (smsg), inline=True)
        await client.edit_message(menuemsg, embed=embed)
        res = await client.wait_for_reaction(message=menuemsg, check=check3, user=message.author)

        await client.remove_reaction(menuemsg, res.reaction.emoji, res.user)
        # await client.remove_reaction(menuemsg, "1⃣", client.user)
        # await client.remove_reaction(menuemsg, "2⃣", client.user)
        # await client.remove_reaction(menuemsg, "3⃣", client.user)

        if res.reaction.emoji == "1⃣":
            selected3 = "add"
        elif res.reaction.emoji == "2⃣":
            selected3 = "remove"
        else:
            selected3 = "cancel"

        if selected3 == "add":

            listformatone = []
            listformattwo = []
            cmdnumb = 1
            for name, id in commands1.items():
                listformatone.append("\n")
                if cmdnumb == 1:
                    listformatone.append(":one:")
                elif cmdnumb == 2:
                    listformatone.append(":two:")
                elif cmdnumb == 3:
                    listformatone.append(":three:")
                elif cmdnumb == 4:
                    listformatone.append(":four:")
                elif cmdnumb == 5:
                    listformatone.append(":five:")
                elif cmdnumb == 6:
                    listformatone.append(":six:")
                elif cmdnumb == 7:
                    listformatone.append(":seven:")
                elif cmdnumb == 8:
                    listformatone.append(":eight:")
                elif cmdnumb == 9:
                    listformatone.append(":nine:")
                listformatone.append(name)
    #                    print(listformatone)
                cmdnumb += 1

            cmdnumb = 1

            for name, id in commands2.items():
                listformattwo.append("\n")
                if cmdnumb == 1:
                    listformattwo.append(":one:")
                elif cmdnumb == 2:
                    listformattwo.append(":two:")
                elif cmdnumb == 3:
                    listformattwo.append(":three:")
                elif cmdnumb == 4:
                    listformattwo.append(":four:")
                elif cmdnumb == 5:
                    listformattwo.append(":five:")
                elif cmdnumb == 6:
                    listformattwo.append(":six:")
                elif cmdnumb == 7:
                    listformattwo.append(":seven:")
                elif cmdnumb == 8:
                    listformattwo.append(":eight:")
                elif cmdnumb == 9:
                    listformattwo.append(":nine:")
                listformattwo.append(name)
    #                    print(listformattwo)
                cmdnumb += 1
    #                await client.add_reaction(menuemsg, "⬅")

            embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
            embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
            embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(listformatone)), inline=True)
            await client.edit_message(menuemsg, embed=embed)

            current = 1

            # await client.add_reaction(menuemsg, "1⃣")
            # await client.add_reaction(menuemsg, "2⃣")
            # await client.add_reaction(menuemsg, "3⃣")
            await client.add_reaction(menuemsg, "4⃣")
            await client.add_reaction(menuemsg, "5⃣")
            await client.add_reaction(menuemsg, "6⃣")
            await client.add_reaction(menuemsg, "7⃣")
            await client.add_reaction(menuemsg, "8⃣")
            await client.add_reaction(menuemsg, "9⃣")

            await client.add_reaction(menuemsg, "➡")
            await client.add_reaction(menuemsg, "✅")
            await client.add_reaction(menuemsg, "❌")

            selectionip = True
            selected2 = ["\n\nSelected:\n\n"]
            selectedid = []

            while selectionip: #(make abc false once ok or cancel)

    #                    print("in while")

                res = await client.wait_for_reaction(message=menuemsg, check=checkmenuone, user=message.author)
    #                    print("past waiting")
                await client.remove_reaction(menuemsg, res.reaction.emoji, res.user)

                if res.reaction.emoji == "❌":
                    selectionip = False
                    embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                    embed.set_thumbnail(url=config.embedthumbnail)
                    embed.add_field(name="WARNING", value="Request canceled", inline=True)
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

                    if current == 1:
                        await client.remove_reaction(menuemsg, "➡", client.user)
                    else:
                        await client.remove_reaction(menuemsg, "⬅", client.user)

                    return

                elif res.reaction.emoji == "➡":
                    if current == 1:

                        menulist = list(listformattwo)
                        menulist.extend(selected2)

                        await client.remove_reaction(menuemsg, "➡", client.user)
                        await client.add_reaction(menuemsg, "⬅")

                        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                        embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                        embed.set_footer(text=config.by)

                        await client.edit_message(menuemsg, embed=embed)

                        current = 2
    #                            print("done")
                elif res.reaction.emoji == "⬅":
    #                        print("here")
                    if current == 2:

                        menulist = list(listformatone)
                        menulist.extend(selected2)

                        await client.remove_reaction(menuemsg, "⬅", client.user)
                        await client.add_reaction(menuemsg, "➡")

                        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                        embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                        embed.set_footer(text=config.by)

                        await client.edit_message(menuemsg, embed=embed)

                        current = 1

                elif res.reaction.emoji == "✅":

                    selectionip = False
                    embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                    embed.set_thumbnail(url=config.embedthumbnail)
                    embed.add_field(name="WARNING", value="Working.....", inline=True)
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

                    if current == 1:
                        await client.remove_reaction(menuemsg, "➡", client.user)
                    else:
                        await client.remove_reaction(menuemsg, "⬅", client.user)

                    embed=discord.Embed(title="Discord", url=config.invite, color=0x3498db)
                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                    embed.set_thumbnail(url=config.embedthumbnail)
                    embed.add_field(name="WARNING", value="@ Mention all members / roles you want to change the exceptions of.", inline=True)
                    embed.set_footer(text=config.by)
                    await client.edit_message(menuemsg, embed=embed)

                    memberstoadd = await client.wait_for_message(timeout=None, author=message.author, channel=message.channel)

                    embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                    embed.set_thumbnail(url=config.embedthumbnail)
                    embed.add_field(name="WARNING", value="Working.....", inline=True)
                    embed.set_footer(text=config.by)
                    await client.edit_message(menuemsg, embed=embed)

                    membids = []
                    roleids = []

                    mempingids = []
                    rolepingids = []

                    ffa = 0

                    c.execute("SELECT * FROM cmds WHERE sid = '%s'" % (message.server.id))
                    row = c.fetchone()

                    if not row:
                        ffa = 0
                    else:
                        ffa = row[6]

                    await client.delete_message(memberstoadd)

                    if not memberstoadd.content.lower().find('@everyone') == -1:
                        ffa = 1

                    for m in memberstoadd.mentions:

                        membids.append(m.id)
                        mempingids.append(m.id)

                    for r in memberstoadd.role_mentions:

                        roleids.append(r.id)
                        rolepingids.append(r.id)

                    arglen = len(membids) + len(roleids)

                    if arglen == 0:
                        embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                        embed.add_field(name="WARNING", value="Please select some people/roles!", inline=True)
                        embed.set_footer(text=config.by)

                        await client.edit_message(menuemsg, embed=embed)

                    for cmid in selectedid:

                        c.execute("SELECT * FROM cmds WHERE sid = '%s' AND cmdid = '%s'" % (message.server.id, cmid))
                        row = c.fetchone()

                        if row:
                            rowids = row[3].split(',')
                            rolids = row[2].split(',')

                        else:
                            rowids = []
                            rolids = []

                        for id in rowids:
                            try:
                                membids.remove(id)
                            except:
                                pass

                        for id in rolids:
                            try:
                                roleids.remove(id)
                            except:
                                pass

                        for id in membids:
                            rowids.append(id)

                        for id in roleids:
                            rolids.append(id)

                        if len(rowids) == 0:
                            rowids.append("0")

                        if len(roleids) == 0:
                            rolids.append("0")

                        if not row:
                            c.execute('INSERT INTO cmds (sid, cmdid, rid, mid, erid, emid, ffa) VALUES (?, ?, ?, ?, ?, ?, ?) ' , (message.server.id, cmid, "0", "0", (',').join(roleids), (',').join(membids), "0"))
                            conn.commit()
                            c.execute("SELECT * FROM cmds WHERE sid = '%s' AND cmdid = '%s'" % (message.server.id, cmid))
                            row = c.fetchone()

                        else:
                            c.execute('UPDATE cmds SET emid = ? WHERE sid = ? AND cmdid = ?' , ((',').join(rowids) , message.server.id, cmid))
                            conn.commit()

                            # c.execute('UPDATE cmds SET ffa = ? WHERE sid = ? AND cmdid = ?' , (ffa , message.server.id, cmid))
                            # conn.commit()

                            c.execute('UPDATE cmds SET erid = ? WHERE sid = ? AND cmdid = ?' , ((',').join(rolids) , message.server.id, cmid))
                            conn.commit()

                    pings = []

                    for id in mempingids:
                        if not id == "0":
                            pings.append("<@%s>" % (id))

                    for id in rolepingids:
                        if not id == "0":
                            pings.append("<@&%s>" % (id))

                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x2ecc71)
                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                    embed.add_field(name="SUCCESS", value="Changed the exceptions of %s" % (', '.join(pings)), inline=True)
                    embed.set_footer(text=config.by)

                    await client.edit_message(menuemsg, embed=embed)

                    return

                else:
                    if current == 1:
                        if res.reaction.emoji == "1⃣":
                            if "Addrole\n" not in selected2:

                                selected2.append("Addrole\n")
                                selectedid.append("addrole")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Addrole\n")
                                selectedid.append("addrole")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "2⃣":
                                if "Ban\n" not in selected2:

                                    selected2.append("Ban\n")
                                    selectedid.append("ban")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Ban\n")
                                    selectedid.append("ban")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "3⃣":
                            if "Clear\n" not in selected2:

                                selected2.append("Clear\n")
                                selectedid.append("clear")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Clear\n")
                                selectedid.append("clear")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "4⃣":
                            if "Countmsg\n" not in selected2:

                                selected2.append("Countmsg\n")
                                selectedid.append("cmsg")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Countmsg\n")
                                selectedid.append("cmsg")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "5⃣":
                            if "FAQ\n" not in selected2:

                                selected2.append("FAQ\n")
                                selectedid.append("faq")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("FAQ\n")
                                selectedid.append("faq")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "6⃣":
                            if "Fast-Clear\n" not in selected2:

                                selected2.append("Fast-Clear\n")
                                selectedid.append("fclear")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Fast-Clear\n")
                                selectedid.append("fclear")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "7⃣":
                            if "Filter\n" not in selected2:

                                selected2.append("Filter\n")
                                selectedid.append("filter")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Filter\n")
                                selectedid.append("filter")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "8⃣":
                            if "Gundam\n" not in selected2:

                                selected2.append("Gundam\n")
                                selectedid.append("gundam")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Gundam\n")
                                selectedid.append("gundam")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "9⃣":
                            if "Help\n" not in selected2:

                                selected2.append("Help\n")
                                selectedid.append("help")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Help\n")
                                selectedid.append("help")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)

                    elif current == 2:
                        if res.reaction.emoji == "1⃣":
                            if "Kick\n" not in selected2:

                                selected2.append("Kick\n")
                                selectedid.append("kick")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Kick\n")
                                selectedid.append("kick")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "2⃣":
                                if "List\n" not in selected2:

                                    selected2.append("List\n")
                                    selectedid.append("list")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("List\n")
                                    selectedid.append("list")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "3⃣":
                            if "Pardon\n" not in selected2:

                                selected2.append("Pardon\n")
                                selectedid.append("pardon")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Pardon\n")
                                selectedid.append("pardon")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "4⃣":
                            if "Permsys\n" not in selected2:

                                selected2.append("Permsys\n")
                                selectedid.append("prmsys")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Permsys\n")
                                selectedid.append("prmsys")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "5⃣":
                            if "Ping\n" not in selected2:

                                selected2.append("Ping\n")
                                selectedid.append("ping")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Ping\n")
                                selectedid.append("ping")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "6⃣":
                            if "Remrole\n" not in selected2:

                                selected2.append("Remrole\n")
                                selectedid.append("remrole")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Remrole\n")
                                selectedid.append("remrole")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "7⃣":
                            if "Userclear\n" not in selected2:

                                selected2.append("Userclear\n")
                                selectedid.append("uclear")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Userclear\n")
                                selectedid.append("uclear")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "8⃣":
                            if "Version\n" not in selected2:

                                selected2.append("Version\n")
                                selectedid.append("ver")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Version\n")
                                selectedid.append("ver")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "9⃣":
                            if "Warn\n" not in selected2:

                                selected2.append("Warn\n")
                                selectedid.append("warn")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Warn\n")
                                selectedid.append("warn")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
        if selected3 == "remove":

                listformatone = []
                listformattwo = []
                cmdnumb = 1
                for name, id in commands1.items():
                    listformatone.append("\n")
                    if cmdnumb == 1:
                        listformatone.append(":one:")
                    elif cmdnumb == 2:
                        listformatone.append(":two:")
                    elif cmdnumb == 3:
                        listformatone.append(":three:")
                    elif cmdnumb == 4:
                        listformatone.append(":four:")
                    elif cmdnumb == 5:
                        listformatone.append(":five:")
                    elif cmdnumb == 6:
                        listformatone.append(":six:")
                    elif cmdnumb == 7:
                        listformatone.append(":seven:")
                    elif cmdnumb == 8:
                        listformatone.append(":eight:")
                    elif cmdnumb == 9:
                        listformatone.append(":nine:")
                    listformatone.append(name)
        #                    print(listformatone)
                    cmdnumb += 1

                cmdnumb = 1

                for name, id in commands2.items():
                    listformattwo.append("\n")
                    if cmdnumb == 1:
                        listformattwo.append(":one:")
                    elif cmdnumb == 2:
                        listformattwo.append(":two:")
                    elif cmdnumb == 3:
                        listformattwo.append(":three:")
                    elif cmdnumb == 4:
                        listformattwo.append(":four:")
                    elif cmdnumb == 5:
                        listformattwo.append(":five:")
                    elif cmdnumb == 6:
                        listformattwo.append(":six:")
                    elif cmdnumb == 7:
                        listformattwo.append(":seven:")
                    elif cmdnumb == 8:
                        listformattwo.append(":eight:")
                    elif cmdnumb == 9:
                        listformattwo.append(":nine:")
                    listformattwo.append(name)
        #                    print(listformattwo)
                    cmdnumb += 1
        #                await client.add_reaction(menuemsg, "⬅")

                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(listformatone)), inline=True)
                await client.edit_message(menuemsg, embed=embed)

                current = 1

                # await client.add_reaction(menuemsg, "1⃣")
                # await client.add_reaction(menuemsg, "2⃣")
                # await client.add_reaction(menuemsg, "3⃣")
                await client.add_reaction(menuemsg, "4⃣")
                await client.add_reaction(menuemsg, "5⃣")
                await client.add_reaction(menuemsg, "6⃣")
                await client.add_reaction(menuemsg, "7⃣")
                await client.add_reaction(menuemsg, "8⃣")
                await client.add_reaction(menuemsg, "9⃣")

                await client.add_reaction(menuemsg, "➡")
                await client.add_reaction(menuemsg, "✅")
                await client.add_reaction(menuemsg, "❌")

                selectionip = True
                selected2 = ["\n\nSelected:\n\n"]
                selectedid = []

                while selectionip: #(make abc false once ok or cancel)

        #                    print("in while")

                    res = await client.wait_for_reaction(message=menuemsg, check=checkmenuone, user=message.author)
        #                    print("past waiting")
                    await client.remove_reaction(menuemsg, res.reaction.emoji, res.user)

                    if res.reaction.emoji == "❌":
                        selectionip = False
                        embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                        embed.set_thumbnail(url=config.embedthumbnail)
                        embed.add_field(name="WARNING", value="Request canceled", inline=True)
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

                        if current == 1:
                            await client.remove_reaction(menuemsg, "➡", client.user)
                        else:
                            await client.remove_reaction(menuemsg, "⬅", client.user)

                        return

                    elif res.reaction.emoji == "➡":
                        if current == 1:

                            menulist = list(listformattwo)
                            menulist.extend(selected2)

                            await client.remove_reaction(menuemsg, "➡", client.user)
                            await client.add_reaction(menuemsg, "⬅")

                            embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                            embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                            embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                            embed.set_footer(text=config.by)

                            await client.edit_message(menuemsg, embed=embed)

                            current = 2
        #                            print("done")
                    elif res.reaction.emoji == "⬅":
        #                        print("here")
                        if current == 2:

                            menulist = list(listformatone)
                            menulist.extend(selected2)

                            await client.remove_reaction(menuemsg, "⬅", client.user)
                            await client.add_reaction(menuemsg, "➡")

                            embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                            embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                            embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                            embed.set_footer(text=config.by)

                            await client.edit_message(menuemsg, embed=embed)

                            current = 1

                    elif res.reaction.emoji == "✅":

                        selectionip = False
                        embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                        embed.set_thumbnail(url=config.embedthumbnail)
                        embed.add_field(name="WARNING", value="Working.....", inline=True)
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

                        if current == 1:
                            await client.remove_reaction(menuemsg, "➡", client.user)
                        else:
                            await client.remove_reaction(menuemsg, "⬅", client.user)

                        embed=discord.Embed(title="Discord", url=config.invite, color=0x3498db)
                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                        embed.set_thumbnail(url=config.embedthumbnail)
                        embed.add_field(name="WARNING", value="@ Mention all members/roles you want to change the exceptions of.", inline=True)
                        embed.set_footer(text=config.by)
                        await client.edit_message(menuemsg, embed=embed)

                        memberstoadd = await client.wait_for_message(timeout=None, author=message.author, channel=message.channel)

                        embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                        embed.set_thumbnail(url=config.embedthumbnail)
                        embed.add_field(name="WARNING", value="Working.....", inline=True)
                        embed.set_footer(text=config.by)
                        await client.edit_message(menuemsg, embed=embed)


                        membids = []
                        roleids = []

                        mempingids = []
                        rolepingids = []

                        ffa = 0

                        c.execute("SELECT * FROM cmds WHERE sid = '%s'" % (message.server.id))
                        row = c.fetchone()

                        if not row:
                            ffa = 0
                        else:
                            ffa = row[6]

                        await client.delete_message(memberstoadd)

                        if not memberstoadd.content.lower().find('@everyone') == -1:
                            ffa = 0

                        for m in memberstoadd.mentions:

                            membids.append(m.id)
                            mempingids.append(m.id)

                        for r in memberstoadd.role_mentions:

                            roleids.append(r.id)
                            rolepingids.append(r.id)

                        arglen = len(membids) + len(roleids)

                        if arglen == 0:
                            embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
                            embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                            embed.add_field(name="WARNING", value="Please select some people/roles!", inline=True)
                            embed.set_footer(text=config.by)

                            await client.edit_message(menuemsg, embed=embed)

                        for cmid in selectedid:

                            c.execute("SELECT * FROM cmds WHERE sid = '%s' AND cmdid = '%s'" % (message.server.id, cmid))
                            row = c.fetchone()

                            # membersfound = 1
                            # rolesfound = 1

                            # if len(roleids) == 0:
                            #     roleids.append("0")
                            #     rolesfound = 0
                            #     rolepingidz = []
                            # else:
                            #     rolepingidz = []
                            #     for id in roleids:
                            #         rolepingidz.append(id)
                            # if len(membids) == 0:
                            #     membids.append("0")
                            #     membersfound = 0
                            #     membpingidz = []
                            # else:
                            #     membpingidz = []
                            #     for id in membids:
                            #         membpingidz.append(id)

                            if not row:

                                c.execute('INSERT INTO cmds (sid, cmdid, rid, mid, erid, emid, ffa) VALUES (?, ?, ?, ?, ?, ?, ?) ' , (message.server.id, cmid, "0", "0", "0", "0", 0))
                                conn.commit()
                                # c.execute("SELECT * FROM cmds WHERE sid = '%s' AND cmdid = '%s'" % (message.server.id, cmid))
                                # row = c.fetchone()

                            else:

                                rowids = row[3].split(',')

                                for id in membids:
                                    try:
                                        rowids.remove(id)
                                    except:
                                        pass

                                rolids = row[2].split(',')

                                for id in roleids:
                                    try:
                                        rolids.remove(id)
                                    except:
                                        pass

                                if len(rowids) == 0:
                                    rowids.append("0")

                                if len(roleids) == 0:
                                    rolids.append("0")

                                c.execute('UPDATE cmds SET emid = ? WHERE sid = ? AND cmdid = ?' , ((',').join(rowids) , message.server.id, cmid))
                                conn.commit()

                                # c.execute('UPDATE cmds SET ffa = ? WHERE sid = ? AND cmdid = ?' , (ffa , message.server.id, cmid))
                                # conn.commit()

                                c.execute('UPDATE cmds SET erid = ? WHERE sid = ? AND cmdid = ?' , ((',').join(rolids) , message.server.id, cmid))
                                conn.commit()

                        pings = []

                        for id in mempingids:
                            if not id == "0":
                                pings.append("<@%s>" % (id))

                        for id in rolepingids:
                            if not id == "0":
                                pings.append("<@&%s>" % (id))

                        embed=discord.Embed(title="Discord", url=config.invite, colour=0x2ecc71)
                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                        embed.add_field(name="SUCCESS", value="Changed the exceptions of %s" % (', '.join(pings)), inline=True)
                        embed.set_footer(text=config.by)

                        await client.edit_message(menuemsg, embed=embed)

                        return

                    else:
                        if current == 1:
                            if res.reaction.emoji == "1⃣":
                                if "Addrole\n" not in selected2:

                                    selected2.append("Addrole\n")
                                    selectedid.append("addrole")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Addrole\n")
                                    selectedid.append("addrole")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "2⃣":
                                    if "Ban\n" not in selected2:

                                        selected2.append("Ban\n")
                                        selectedid.append("ban")

                                        menulist = list(listformatone)
                                        menulist.extend(selected2)

                                        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                        embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                        embed.set_footer(text=config.by)

                                        await client.edit_message(menuemsg, embed=embed)
                                    else:

                                        selected2.remove("Ban\n")
                                        selectedid.append("ban")

                                        menulist = list(listformatone)
                                        menulist.extend(selected2)

                                        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                        embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                        embed.set_footer(text=config.by)

                                        await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "3⃣":
                                if "Clear\n" not in selected2:

                                    selected2.append("Clear\n")
                                    selectedid.append("clear")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Clear\n")
                                    selectedid.append("clear")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "4⃣":
                                if "Countmsg\n" not in selected2:

                                    selected2.append("Countmsg\n")
                                    selectedid.append("cmsg")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Countmsg\n")
                                    selectedid.append("cmsg")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "5⃣":
                                if "FAQ\n" not in selected2:

                                    selected2.append("FAQ\n")
                                    selectedid.append("faq")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("FAQ\n")
                                    selectedid.append("faq")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "6⃣":
                                if "Fast-Clear\n" not in selected2:

                                    selected2.append("Fast-Clear\n")
                                    selectedid.append("fclear")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Fast-Clear\n")
                                    selectedid.append("fclear")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "7⃣":
                                if "Filter\n" not in selected2:

                                    selected2.append("Filter\n")
                                    selectedid.append("filter")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Filter\n")
                                    selectedid.append("filter")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "8⃣":
                                if "Gundam\n" not in selected2:

                                    selected2.append("Gundam\n")
                                    selectedid.append("gundam")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Gundam\n")
                                    selectedid.append("gundam")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "9⃣":
                                if "Help\n" not in selected2:

                                    selected2.append("Help\n")
                                    selectedid.append("help")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Help\n")
                                    selectedid.append("help")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)

                        elif current == 2:
                            if res.reaction.emoji == "1⃣":
                                if "Kick\n" not in selected2:

                                    selected2.append("Kick\n")
                                    selectedid.append("kick")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Kick\n")
                                    selectedid.append("kick")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "2⃣":
                                    if "List\n" not in selected2:

                                        selected2.append("List\n")
                                        selectedid.append("list")

                                        menulist = list(listformattwo)
                                        menulist.extend(selected2)

                                        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                        embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                        embed.set_footer(text=config.by)

                                        await client.edit_message(menuemsg, embed=embed)
                                    else:

                                        selected2.remove("List\n")
                                        selectedid.append("list")

                                        menulist = list(listformattwo)
                                        menulist.extend(selected2)

                                        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                        embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                        embed.set_footer(text=config.by)

                                        await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "3⃣":
                                if "Pardon\n" not in selected2:

                                    selected2.append("Pardon\n")
                                    selectedid.append("pardon")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Pardon\n")
                                    selectedid.append("pardon")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "4⃣":
                                if "Permsys\n" not in selected2:

                                    selected2.append("Permsys\n")
                                    selectedid.append("prmsys")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Permsys\n")
                                    selectedid.append("prmsys")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "5⃣":
                                if "Ping\n" not in selected2:

                                    selected2.append("Ping\n")
                                    selectedid.append("ping")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Ping\n")
                                    selectedid.append("ping")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "6⃣":
                                if "Remrole\n" not in selected2:

                                    selected2.append("Remrole\n")
                                    selectedid.append("remrole")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Remrole\n")
                                    selectedid.append("remrole")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "7⃣":
                                if "Userclear\n" not in selected2:

                                    selected2.append("Userclear\n")
                                    selectedid.append("uclear")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Userclear\n")
                                    selectedid.append("uclear")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "8⃣":
                                if "Version\n" not in selected2:

                                    selected2.append("Version\n")
                                    selectedid.append("ver")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Version\n")
                                    selectedid.append("ver")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "9⃣":
                                if "Warn\n" not in selected2:

                                    selected2.append("Warn\n")
                                    selectedid.append("warn")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Warn\n")
                                    selectedid.append("warn")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)






                        # if react = -> , <-, done
                        #     -> current =2
                        #     <- current = 1
                        # else



    elif selected == "status":
        await client.remove_reaction(menuemsg, "4⃣", client.user)
        await client.remove_reaction(menuemsg, "5⃣", client.user)

        await client.remove_reaction(menuemsg, res.reaction.emoji, res.user)

        smsg = ":one: Add \n:two: Remove \n:three: Cancel"
        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
        embed.add_field(name="Do you want to add or remove an exception?", value="%s" % (smsg), inline=True)
        await client.edit_message(menuemsg, embed=embed)
        res = await client.wait_for_reaction(message=menuemsg, check=check3, user=message.author)

        await client.remove_reaction(menuemsg, res.reaction.emoji, res.user)
        # await client.remove_reaction(menuemsg, "1⃣", client.user)
        # await client.remove_reaction(menuemsg, "2⃣", client.user)
        # await client.remove_reaction(menuemsg, "3⃣", client.user)

        if res.reaction.emoji == "1⃣":
            selected3 = "add"
        elif res.reaction.emoji == "2⃣":
            selected3 = "remove"
        else:
            selected3 = "cancel"

        if selected3 == "add":

            listformatone = []
            listformattwo = []
            cmdnumb = 1
            for name, id in commands1.items():
                listformatone.append("\n")
                if cmdnumb == 1:
                    listformatone.append(":one:")
                elif cmdnumb == 2:
                    listformatone.append(":two:")
                elif cmdnumb == 3:
                    listformatone.append(":three:")
                elif cmdnumb == 4:
                    listformatone.append(":four:")
                elif cmdnumb == 5:
                    listformatone.append(":five:")
                elif cmdnumb == 6:
                    listformatone.append(":six:")
                elif cmdnumb == 7:
                    listformatone.append(":seven:")
                elif cmdnumb == 8:
                    listformatone.append(":eight:")
                elif cmdnumb == 9:
                    listformatone.append(":nine:")
                listformatone.append(name)
    #                    print(listformatone)
                cmdnumb += 1

            cmdnumb = 1

            for name, id in commands2.items():
                listformattwo.append("\n")
                if cmdnumb == 1:
                    listformattwo.append(":one:")
                elif cmdnumb == 2:
                    listformattwo.append(":two:")
                elif cmdnumb == 3:
                    listformattwo.append(":three:")
                elif cmdnumb == 4:
                    listformattwo.append(":four:")
                elif cmdnumb == 5:
                    listformattwo.append(":five:")
                elif cmdnumb == 6:
                    listformattwo.append(":six:")
                elif cmdnumb == 7:
                    listformattwo.append(":seven:")
                elif cmdnumb == 8:
                    listformattwo.append(":eight:")
                elif cmdnumb == 9:
                    listformattwo.append(":nine:")
                listformattwo.append(name)
    #                    print(listformattwo)
                cmdnumb += 1
    #                await client.add_reaction(menuemsg, "⬅")

            embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
            embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
            embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(listformatone)), inline=True)
            await client.edit_message(menuemsg, embed=embed)

            current = 1

            # await client.add_reaction(menuemsg, "1⃣")
            # await client.add_reaction(menuemsg, "2⃣")
            # await client.add_reaction(menuemsg, "3⃣")
            await client.add_reaction(menuemsg, "4⃣")
            await client.add_reaction(menuemsg, "5⃣")
            await client.add_reaction(menuemsg, "6⃣")
            await client.add_reaction(menuemsg, "7⃣")
            await client.add_reaction(menuemsg, "8⃣")
            await client.add_reaction(menuemsg, "9⃣")

            await client.add_reaction(menuemsg, "➡")
            await client.add_reaction(menuemsg, "✅")
            await client.add_reaction(menuemsg, "❌")

            selectionip = True
            selected2 = ["\n\nSelected:\n\n"]
            selectedid = []

            while selectionip: #(make abc false once ok or cancel)

    #                    print("in while")

                res = await client.wait_for_reaction(message=menuemsg, check=checkmenuone, user=message.author)
    #                    print("past waiting")
                await client.remove_reaction(menuemsg, res.reaction.emoji, res.user)

                if res.reaction.emoji == "❌":
                    selectionip = False
                    embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                    embed.set_thumbnail(url=config.embedthumbnail)
                    embed.add_field(name="WARNING", value="Request canceled", inline=True)
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

                    if current == 1:
                        await client.remove_reaction(menuemsg, "➡", client.user)
                    else:
                        await client.remove_reaction(menuemsg, "⬅", client.user)

                    return

                elif res.reaction.emoji == "➡":
                    if current == 1:

                        menulist = list(listformattwo)
                        menulist.extend(selected2)

                        await client.remove_reaction(menuemsg, "➡", client.user)
                        await client.add_reaction(menuemsg, "⬅")

                        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                        embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                        embed.set_footer(text=config.by)

                        await client.edit_message(menuemsg, embed=embed)

                        current = 2
    #                            print("done")
                elif res.reaction.emoji == "⬅":
    #                        print("here")
                    if current == 2:

                        menulist = list(listformatone)
                        menulist.extend(selected2)

                        await client.remove_reaction(menuemsg, "⬅", client.user)
                        await client.add_reaction(menuemsg, "➡")

                        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                        embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                        embed.set_footer(text=config.by)

                        await client.edit_message(menuemsg, embed=embed)

                        current = 1

                elif res.reaction.emoji == "✅":

                    selectionip = False
                    embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                    embed.set_thumbnail(url=config.embedthumbnail)
                    embed.add_field(name="WARNING", value="Working.....", inline=True)
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

                    if current == 1:
                        await client.remove_reaction(menuemsg, "➡", client.user)
                    else:
                        await client.remove_reaction(menuemsg, "⬅", client.user)

                    embed=discord.Embed(title="Discord", url=config.invite, color=0x3498db)
                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                    embed.set_thumbnail(url=config.embedthumbnail)
                    embed.add_field(name="WARNING", value="@ Mention all members / roles you want to change the exceptions of.", inline=True)
                    embed.set_footer(text=config.by)
                    await client.edit_message(menuemsg, embed=embed)

                    memberstoadd = await client.wait_for_message(timeout=None, author=message.author, channel=message.channel)

                    embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                    embed.set_thumbnail(url=config.embedthumbnail)
                    embed.add_field(name="WARNING", value="Working.....", inline=True)
                    embed.set_footer(text=config.by)
                    await client.edit_message(menuemsg, embed=embed)

                    membids = []
                    roleids = []

                    mempingids = []
                    rolepingids = []

                    ffa = 0

                    c.execute("SELECT * FROM cmds WHERE sid = '%s'" % (message.server.id))
                    row = c.fetchone()

                    if not row:
                        ffa = 0
                    else:
                        ffa = row[6]

                    await client.delete_message(memberstoadd)

                    if not memberstoadd.content.lower().find('@everyone') == -1:
                        ffa = 1

                    for m in memberstoadd.mentions:

                        membids.append(m.id)
                        mempingids.append(m.id)

                    for r in memberstoadd.role_mentions:

                        roleids.append(r.id)
                        rolepingids.append(r.id)

                    arglen = len(membids) + len(roleids)

                    if arglen == 0:
                        embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                        embed.add_field(name="WARNING", value="Please select some people/roles!", inline=True)
                        embed.set_footer(text=config.by)

                        await client.edit_message(menuemsg, embed=embed)

                    for cmid in selectedid:

                        c.execute("SELECT * FROM cmds WHERE sid = '%s' AND cmdid = '%s'" % (message.server.id, cmid))
                        row = c.fetchone()

                        if row:
                            rowids = row[3].split(',')
                            rolids = row[2].split(',')

                        else:
                            rowids = []
                            rolids = []

                        for id in rowids:
                            try:
                                membids.remove(id)
                            except:
                                pass

                        for id in rolids:
                            try:
                                roleids.remove(id)
                            except:
                                pass

                        for id in membids:
                            rowids.append(id)

                        for id in roleids:
                            rolids.append(id)

                        if len(rowids) == 0:
                            rowids.append("0")

                        if len(roleids) == 0:
                            rolids.append("0")

                        if not row:
                            c.execute('INSERT INTO cmds (sid, cmdid, rid, mid, erid, emid, ffa) VALUES (?, ?, ?, ?, ?, ?, ?) ' , (message.server.id, cmid, "0", "0", (',').join(roleids), (',').join(membids), "0"))
                            conn.commit()
                            c.execute("SELECT * FROM cmds WHERE sid = '%s' AND cmdid = '%s'" % (message.server.id, cmid))
                            row = c.fetchone()

                        else:
                            c.execute('UPDATE cmds SET emid = ? WHERE sid = ? AND cmdid = ?' , ((',').join(rowids) , message.server.id, cmid))
                            conn.commit()

                            # c.execute('UPDATE cmds SET ffa = ? WHERE sid = ? AND cmdid = ?' , (ffa , message.server.id, cmid))
                            # conn.commit()

                            c.execute('UPDATE cmds SET erid = ? WHERE sid = ? AND cmdid = ?' , ((',').join(rolids) , message.server.id, cmid))
                            conn.commit()

                    pings = []

                    for id in mempingids:
                        if not id == "0":
                            pings.append("<@%s>" % (id))

                    for id in rolepingids:
                        if not id == "0":
                            pings.append("<@&%s>" % (id))

                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x2ecc71)
                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                    embed.add_field(name="SUCCESS", value="Changed the exceptions of %s" % (', '.join(pings)), inline=True)
                    embed.set_footer(text=config.by)

                    await client.edit_message(menuemsg, embed=embed)

                    return

                else:
                    if current == 1:
                        if res.reaction.emoji == "1⃣":
                            if "Addrole\n" not in selected2:

                                selected2.append("Addrole\n")
                                selectedid.append("addrole")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Addrole\n")
                                selectedid.append("addrole")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "2⃣":
                                if "Ban\n" not in selected2:

                                    selected2.append("Ban\n")
                                    selectedid.append("ban")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Ban\n")
                                    selectedid.append("ban")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "3⃣":
                            if "Clear\n" not in selected2:

                                selected2.append("Clear\n")
                                selectedid.append("clear")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Clear\n")
                                selectedid.append("clear")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "4⃣":
                            if "Countmsg\n" not in selected2:

                                selected2.append("Countmsg\n")
                                selectedid.append("cmsg")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Countmsg\n")
                                selectedid.append("cmsg")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "5⃣":
                            if "FAQ\n" not in selected2:

                                selected2.append("FAQ\n")
                                selectedid.append("faq")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("FAQ\n")
                                selectedid.append("faq")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "6⃣":
                            if "Fast-Clear\n" not in selected2:

                                selected2.append("Fast-Clear\n")
                                selectedid.append("fclear")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Fast-Clear\n")
                                selectedid.append("fclear")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "7⃣":
                            if "Filter\n" not in selected2:

                                selected2.append("Filter\n")
                                selectedid.append("filter")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Filter\n")
                                selectedid.append("filter")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "8⃣":
                            if "Gundam\n" not in selected2:

                                selected2.append("Gundam\n")
                                selectedid.append("gundam")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Gundam\n")
                                selectedid.append("gundam")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "9⃣":
                            if "Help\n" not in selected2:

                                selected2.append("Help\n")
                                selectedid.append("help")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Help\n")
                                selectedid.append("help")

                                menulist = list(listformatone)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)

                    elif current == 2:
                        if res.reaction.emoji == "1⃣":
                            if "Kick\n" not in selected2:

                                selected2.append("Kick\n")
                                selectedid.append("kick")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Kick\n")
                                selectedid.append("kick")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "2⃣":
                                if "List\n" not in selected2:

                                    selected2.append("List\n")
                                    selectedid.append("list")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("List\n")
                                    selectedid.append("list")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "3⃣":
                            if "Pardon\n" not in selected2:

                                selected2.append("Pardon\n")
                                selectedid.append("pardon")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Pardon\n")
                                selectedid.append("pardon")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "4⃣":
                            if "Permsys\n" not in selected2:

                                selected2.append("Permsys\n")
                                selectedid.append("prmsys")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Permsys\n")
                                selectedid.append("prmsys")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "5⃣":
                            if "Ping\n" not in selected2:

                                selected2.append("Ping\n")
                                selectedid.append("ping")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Ping\n")
                                selectedid.append("ping")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "6⃣":
                            if "Remrole\n" not in selected2:

                                selected2.append("Remrole\n")
                                selectedid.append("remrole")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Remrole\n")
                                selectedid.append("remrole")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "7⃣":
                            if "Userclear\n" not in selected2:

                                selected2.append("Userclear\n")
                                selectedid.append("uclear")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Userclear\n")
                                selectedid.append("uclear")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "8⃣":
                            if "Version\n" not in selected2:

                                selected2.append("Version\n")
                                selectedid.append("ver")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Version\n")
                                selectedid.append("ver")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                        elif res.reaction.emoji == "9⃣":
                            if "Warn\n" not in selected2:

                                selected2.append("Warn\n")
                                selectedid.append("warn")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
                            else:

                                selected2.remove("Warn\n")
                                selectedid.append("warn")

                                menulist = list(listformattwo)
                                menulist.extend(selected2)

                                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                embed.set_footer(text=config.by)

                                await client.edit_message(menuemsg, embed=embed)
        if selected3 == "remove":

                listformatone = []
                listformattwo = []
                cmdnumb = 1
                for name, id in commands1.items():
                    listformatone.append("\n")
                    if cmdnumb == 1:
                        listformatone.append(":one:")
                    elif cmdnumb == 2:
                        listformatone.append(":two:")
                    elif cmdnumb == 3:
                        listformatone.append(":three:")
                    elif cmdnumb == 4:
                        listformatone.append(":four:")
                    elif cmdnumb == 5:
                        listformatone.append(":five:")
                    elif cmdnumb == 6:
                        listformatone.append(":six:")
                    elif cmdnumb == 7:
                        listformatone.append(":seven:")
                    elif cmdnumb == 8:
                        listformatone.append(":eight:")
                    elif cmdnumb == 9:
                        listformatone.append(":nine:")
                    listformatone.append(name)
        #                    print(listformatone)
                    cmdnumb += 1

                cmdnumb = 1

                for name, id in commands2.items():
                    listformattwo.append("\n")
                    if cmdnumb == 1:
                        listformattwo.append(":one:")
                    elif cmdnumb == 2:
                        listformattwo.append(":two:")
                    elif cmdnumb == 3:
                        listformattwo.append(":three:")
                    elif cmdnumb == 4:
                        listformattwo.append(":four:")
                    elif cmdnumb == 5:
                        listformattwo.append(":five:")
                    elif cmdnumb == 6:
                        listformattwo.append(":six:")
                    elif cmdnumb == 7:
                        listformattwo.append(":seven:")
                    elif cmdnumb == 8:
                        listformattwo.append(":eight:")
                    elif cmdnumb == 9:
                        listformattwo.append(":nine:")
                    listformattwo.append(name)
        #                    print(listformattwo)
                    cmdnumb += 1
        #                await client.add_reaction(menuemsg, "⬅")

                embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(listformatone)), inline=True)
                await client.edit_message(menuemsg, embed=embed)

                current = 1

                # await client.add_reaction(menuemsg, "1⃣")
                # await client.add_reaction(menuemsg, "2⃣")
                # await client.add_reaction(menuemsg, "3⃣")
                await client.add_reaction(menuemsg, "4⃣")
                await client.add_reaction(menuemsg, "5⃣")
                await client.add_reaction(menuemsg, "6⃣")
                await client.add_reaction(menuemsg, "7⃣")
                await client.add_reaction(menuemsg, "8⃣")
                await client.add_reaction(menuemsg, "9⃣")

                await client.add_reaction(menuemsg, "➡")
                await client.add_reaction(menuemsg, "✅")
                await client.add_reaction(menuemsg, "❌")

                selectionip = True
                selected2 = ["\n\nSelected:\n\n"]
                selectedid = []

                while selectionip: #(make abc false once ok or cancel)

        #                    print("in while")

                    res = await client.wait_for_reaction(message=menuemsg, check=checkmenuone, user=message.author)
        #                    print("past waiting")
                    await client.remove_reaction(menuemsg, res.reaction.emoji, res.user)

                    if res.reaction.emoji == "❌":
                        selectionip = False
                        embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                        embed.set_thumbnail(url=config.embedthumbnail)
                        embed.add_field(name="WARNING", value="Request canceled", inline=True)
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

                        if current == 1:
                            await client.remove_reaction(menuemsg, "➡", client.user)
                        else:
                            await client.remove_reaction(menuemsg, "⬅", client.user)

                        return

                    elif res.reaction.emoji == "➡":
                        if current == 1:

                            menulist = list(listformattwo)
                            menulist.extend(selected2)

                            await client.remove_reaction(menuemsg, "➡", client.user)
                            await client.add_reaction(menuemsg, "⬅")

                            embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                            embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                            embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                            embed.set_footer(text=config.by)

                            await client.edit_message(menuemsg, embed=embed)

                            current = 2
        #                            print("done")
                    elif res.reaction.emoji == "⬅":
        #                        print("here")
                        if current == 2:

                            menulist = list(listformatone)
                            menulist.extend(selected2)

                            await client.remove_reaction(menuemsg, "⬅", client.user)
                            await client.add_reaction(menuemsg, "➡")

                            embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                            embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                            embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                            embed.set_footer(text=config.by)

                            await client.edit_message(menuemsg, embed=embed)

                            current = 1

                    elif res.reaction.emoji == "✅":

                        selectionip = False
                        embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                        embed.set_thumbnail(url=config.embedthumbnail)
                        embed.add_field(name="WARNING", value="Working.....", inline=True)
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

                        if current == 1:
                            await client.remove_reaction(menuemsg, "➡", client.user)
                        else:
                            await client.remove_reaction(menuemsg, "⬅", client.user)

                        embed=discord.Embed(title="Discord", url=config.invite, color=0x3498db)
                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                        embed.set_thumbnail(url=config.embedthumbnail)
                        embed.add_field(name="WARNING", value="@ Mention all members/roles you want to change the exceptions of.", inline=True)
                        embed.set_footer(text=config.by)
                        await client.edit_message(menuemsg, embed=embed)

                        memberstoadd = await client.wait_for_message(timeout=None, author=message.author, channel=message.channel)

                        embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                        embed.set_thumbnail(url=config.embedthumbnail)
                        embed.add_field(name="WARNING", value="Working.....", inline=True)
                        embed.set_footer(text=config.by)
                        await client.edit_message(menuemsg, embed=embed)


                        membids = []
                        roleids = []

                        mempingids = []
                        rolepingids = []

                        ffa = 0

                        c.execute("SELECT * FROM cmds WHERE sid = '%s'" % (message.server.id))
                        row = c.fetchone()

                        if not row:
                            ffa = 0
                        else:
                            ffa = row[6]

                        await client.delete_message(memberstoadd)

                        if not memberstoadd.content.lower().find('@everyone') == -1:
                            ffa = 0

                        for m in memberstoadd.mentions:

                            membids.append(m.id)
                            mempingids.append(m.id)

                        for r in memberstoadd.role_mentions:

                            roleids.append(r.id)
                            rolepingids.append(r.id)

                        arglen = len(membids) + len(roleids)

                        if arglen == 0:
                            embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
                            embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                            embed.add_field(name="WARNING", value="Please select some people/roles!", inline=True)
                            embed.set_footer(text=config.by)

                            await client.edit_message(menuemsg, embed=embed)

                        for cmid in selectedid:

                            c.execute("SELECT * FROM cmds WHERE sid = '%s' AND cmdid = '%s'" % (message.server.id, cmid))
                            row = c.fetchone()

                            # membersfound = 1
                            # rolesfound = 1

                            # if len(roleids) == 0:
                            #     roleids.append("0")
                            #     rolesfound = 0
                            #     rolepingidz = []
                            # else:
                            #     rolepingidz = []
                            #     for id in roleids:
                            #         rolepingidz.append(id)
                            # if len(membids) == 0:
                            #     membids.append("0")
                            #     membersfound = 0
                            #     membpingidz = []
                            # else:
                            #     membpingidz = []
                            #     for id in membids:
                            #         membpingidz.append(id)

                            if not row:

                                c.execute('INSERT INTO cmds (sid, cmdid, rid, mid, erid, emid, ffa) VALUES (?, ?, ?, ?, ?, ?, ?) ' , (message.server.id, cmid, "0", "0", "0", "0", 0))
                                conn.commit()
                                # c.execute("SELECT * FROM cmds WHERE sid = '%s' AND cmdid = '%s'" % (message.server.id, cmid))
                                # row = c.fetchone()

                            else:

                                rowids = row[3].split(',')

                                for id in membids:
                                    try:
                                        rowids.remove(id)
                                    except:
                                        pass

                                rolids = row[2].split(',')

                                for id in roleids:
                                    try:
                                        rolids.remove(id)
                                    except:
                                        pass

                                if len(rowids) == 0:
                                    rowids.append("0")

                                if len(roleids) == 0:
                                    rolids.append("0")

                                c.execute('UPDATE cmds SET emid = ? WHERE sid = ? AND cmdid = ?' , ((',').join(rowids) , message.server.id, cmid))
                                conn.commit()

                                # c.execute('UPDATE cmds SET ffa = ? WHERE sid = ? AND cmdid = ?' , (ffa , message.server.id, cmid))
                                # conn.commit()

                                c.execute('UPDATE cmds SET erid = ? WHERE sid = ? AND cmdid = ?' , ((',').join(rolids) , message.server.id, cmid))
                                conn.commit()

                        pings = []

                        for id in mempingids:
                            if not id == "0":
                                pings.append("<@%s>" % (id))

                        for id in rolepingids:
                            if not id == "0":
                                pings.append("<@&%s>" % (id))

                        embed=discord.Embed(title="Discord", url=config.invite, colour=0x2ecc71)
                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                        embed.add_field(name="SUCCESS", value="Changed the exceptions of %s" % (', '.join(pings)), inline=True)
                        embed.set_footer(text=config.by)

                        await client.edit_message(menuemsg, embed=embed)

                        return

                    else:
                        if current == 1:
                            if res.reaction.emoji == "1⃣":
                                if "Addrole\n" not in selected2:

                                    selected2.append("Addrole\n")
                                    selectedid.append("addrole")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Addrole\n")
                                    selectedid.append("addrole")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "2⃣":
                                    if "Ban\n" not in selected2:

                                        selected2.append("Ban\n")
                                        selectedid.append("ban")

                                        menulist = list(listformatone)
                                        menulist.extend(selected2)

                                        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                        embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                        embed.set_footer(text=config.by)

                                        await client.edit_message(menuemsg, embed=embed)
                                    else:

                                        selected2.remove("Ban\n")
                                        selectedid.append("ban")

                                        menulist = list(listformatone)
                                        menulist.extend(selected2)

                                        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                        embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                        embed.set_footer(text=config.by)

                                        await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "3⃣":
                                if "Clear\n" not in selected2:

                                    selected2.append("Clear\n")
                                    selectedid.append("clear")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Clear\n")
                                    selectedid.append("clear")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "4⃣":
                                if "Countmsg\n" not in selected2:

                                    selected2.append("Countmsg\n")
                                    selectedid.append("cmsg")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Countmsg\n")
                                    selectedid.append("cmsg")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "5⃣":
                                if "FAQ\n" not in selected2:

                                    selected2.append("FAQ\n")
                                    selectedid.append("faq")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("FAQ\n")
                                    selectedid.append("faq")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "6⃣":
                                if "Fast-Clear\n" not in selected2:

                                    selected2.append("Fast-Clear\n")
                                    selectedid.append("fclear")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Fast-Clear\n")
                                    selectedid.append("fclear")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "7⃣":
                                if "Filter\n" not in selected2:

                                    selected2.append("Filter\n")
                                    selectedid.append("filter")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Filter\n")
                                    selectedid.append("filter")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "8⃣":
                                if "Gundam\n" not in selected2:

                                    selected2.append("Gundam\n")
                                    selectedid.append("gundam")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Gundam\n")
                                    selectedid.append("gundam")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "9⃣":
                                if "Help\n" not in selected2:

                                    selected2.append("Help\n")
                                    selectedid.append("help")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Help\n")
                                    selectedid.append("help")

                                    menulist = list(listformatone)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)

                        elif current == 2:
                            if res.reaction.emoji == "1⃣":
                                if "Kick\n" not in selected2:

                                    selected2.append("Kick\n")
                                    selectedid.append("kick")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Kick\n")
                                    selectedid.append("kick")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "2⃣":
                                    if "List\n" not in selected2:

                                        selected2.append("List\n")
                                        selectedid.append("list")

                                        menulist = list(listformattwo)
                                        menulist.extend(selected2)

                                        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                        embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                        embed.set_footer(text=config.by)

                                        await client.edit_message(menuemsg, embed=embed)
                                    else:

                                        selected2.remove("List\n")
                                        selectedid.append("list")

                                        menulist = list(listformattwo)
                                        menulist.extend(selected2)

                                        embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                        embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                        embed.set_footer(text=config.by)

                                        await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "3⃣":
                                if "Pardon\n" not in selected2:

                                    selected2.append("Pardon\n")
                                    selectedid.append("pardon")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Pardon\n")
                                    selectedid.append("pardon")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "4⃣":
                                if "Permsys\n" not in selected2:

                                    selected2.append("Permsys\n")
                                    selectedid.append("prmsys")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Permsys\n")
                                    selectedid.append("prmsys")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "5⃣":
                                if "Ping\n" not in selected2:

                                    selected2.append("Ping\n")
                                    selectedid.append("ping")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Ping\n")
                                    selectedid.append("ping")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "6⃣":
                                if "Remrole\n" not in selected2:

                                    selected2.append("Remrole\n")
                                    selectedid.append("remrole")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Remrole\n")
                                    selectedid.append("remrole")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "7⃣":
                                if "Userclear\n" not in selected2:

                                    selected2.append("Userclear\n")
                                    selectedid.append("uclear")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Userclear\n")
                                    selectedid.append("uclear")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "8⃣":
                                if "Version\n" not in selected2:

                                    selected2.append("Version\n")
                                    selectedid.append("ver")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Version\n")
                                    selectedid.append("ver")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                            elif res.reaction.emoji == "9⃣":
                                if "Warn\n" not in selected2:

                                    selected2.append("Warn\n")
                                    selectedid.append("warn")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)
                                else:

                                    selected2.remove("Warn\n")
                                    selectedid.append("warn")

                                    menulist = list(listformattwo)
                                    menulist.extend(selected2)

                                    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
                                    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
                                    embed.add_field(name="Select all commands you want to change the exceptions of.", value="%s" % (('').join(menulist)), inline=True)
                                    embed.set_footer(text=config.by)

                                    await client.edit_message(menuemsg, embed=embed)

                        # if react = -> , <-, done
                        #     -> current =2
                        #     <- current = 1
                        # else



        #                    check if in list
                        #     if current 1
                        #         add to list from dict1
        #                            edit message to have the selected written
                        #     if current 2 add to list from dict2
                        # use foreach

    else:
    #        await client.delete_message(answer)
        embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
        embed.set_thumbnail(url=config.embedthumbnail)
        embed.add_field(name="WARNING", value="Request canceled", inline=True)
        embed.set_footer(text=config.by)
        await client.edit_message(menuemsg, embed=embed)





















        #loll
