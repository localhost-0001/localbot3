import discord
#import _mysql
import traceback
import logging
import sys
import sqlite3
import config

from time import gmtime, strftime
# conn = sqlite3.connect('sql.db')
# c = conn.cursor()

logdate = strftime("%Y_%m_%d_%H-%M-%S__", gmtime())

import SECRETS
import config
import perms, permscustomfilter
import embeds
import excon
#import emgs

logging.basicConfig(filename='.\logs\%soutput.log' % (logdate), filemode='w', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

excon

from commands import cmd_ping, cmd_kick, cmd_ban, cmd_clear, cmd_countmsg, cmd_fclear, cmd_filter, cmd_faq, cmd_blocksuggest, cmd_unblocksuggest, cmd_suggest, cmd_help, cmd_say, cmd_sayin, cmd_addrole, cmd_remrole, cmd_warn, cmd_pardon, cmd_list, cmd_permsystem, cmd_userclear, cmd_gundam, cmd_version, cmd_perms, cmd_lenny, cmd_tidcheck, cmd_exit, cmd_sendmoney, cmd_spam, cmd_pardonall


client = discord.Client()

commands = {

    "e": cmd_exit,
    "pall": cmd_pardonall,
    "pardonall": cmd_pardonall,
    "ping": cmd_ping,
    "kick": cmd_kick,
    "ban": cmd_ban,
    "clear": cmd_clear,
    "purge": cmd_clear,
    "fclear": cmd_fclear,
    "fastclear": cmd_fclear,
    "clean": cmd_clear,
    "cmsg": cmd_countmsg,
    "countmsg": cmd_countmsg,
    "filter": cmd_filter,
    "faq": cmd_faq,
    "block": cmd_blocksuggest,
    "blocksuggest": cmd_blocksuggest,
    "unblock": cmd_unblocksuggest,
    "unblocksuggest": cmd_unblocksuggest,
    "suggest": cmd_suggest,
    "help": cmd_help,
    "halp": cmd_help,
    "say": cmd_say,
    "sin": cmd_sayin,
    "sayin": cmd_sayin,
    "add": cmd_addrole,
    "addrole": cmd_addrole,
    "rem": cmd_remrole,
    "remove": cmd_remrole,
    "removerole": cmd_remrole,
    "warn": cmd_warn,
    "pardon": cmd_pardon,
    "list": cmd_list,
    "strikes": cmd_list,
    "prmsystem": cmd_permsystem,
    "permsystem": cmd_permsystem,
    "prmsys": cmd_permsystem,
    "permsys": cmd_permsystem,
    "clearuser": cmd_userclear,
    "cuser": cmd_userclear,
    "userclear": cmd_userclear,
    "userc": cmd_userclear,
    "uc": cmd_userclear,
    "gundam": cmd_gundam,
    "ver": cmd_version,
    "version": cmd_version,
    "v": cmd_version,
    "lenny": cmd_lenny,
    "lennyface": cmd_lenny,
#    "r": cmd_tidcheck
    "p": cmd_perms,
    "sm": cmd_sendmoney,
    "spam": cmd_spam
}

cmdids = {


}
@client.event
async def on_ready():
    sercount = 0
    mcount = 0
    print ("Ready. On following servers: \n")
#    print(len(client.servers))
    for s in client.servers:
        sercount = sercount ++ 1
        print(sercount)
        sm = 0
        ms = s.members
        for member in ms:
            mcount = mcount ++ 1
            sm = sm ++ 1
            #print(mcount)
        print(" - %s (%s), members: %s" % (s.name, s.id, sm))
    print("total members: %s" % (mcount))
#    await client.change_presence(game=discord.Game(name="for %s people." % (mcount)))
    await client.change_presence(game=discord.Game(name="you", type=3))
#    print("%s" % (emgs.unknowncmd))

@client.event
async def on_message(message):

    # print(message.channel.name)
    # print(message.author.name)
    conn = sqlite3.connect('sql.db')
    c = conn.cursor()
#start custom filtering for nebula

#end of custom filtering for nebula

    if message.content.startswith("<@!%s>" % (client.user.id)):
        await embeds.pingmsg(message, client)

    if message.content.startswith("<@%s>" % (client.user.id)):
        await embeds.pingmsg(message, client)

# FILTER PART
#    if not 0==0:
    if not perms.check(message.author, 1):
        kran = 0


        c.execute("SELECT * FROM chatfilter WHERE id = '%s'" % (message.server.id))
        row = c.fetchone()

        if not row:
            c.execute("INSERT INTO chatfilter (id, filtered, active) VALUES ('%s', '7890798078978097987980978798008087707908', '1') " % (message.server.id))
            conn.commit()

        else:
#            print(row)
            filtered = row[1]
#            print(filtered)
#            print("FILTERED DECODED")
#            print(filtered)
#            print("DONE")
            filteredsplit = filtered.split(',')
#            print(filteredsplit)
            for f in filteredsplit:
#                print(f)
                if not f == "7890798078978097987980978798008087707908":
                    if not kran == 1:
                        if not message.content.lower().find(f) == -1:
                            try:
                                await embeds.filteredlog(message, client)
                            except:
                                await embeds.nologchan(message, client)
                            await client.delete_message(message)
                            await embeds.sorrymsg(message, client)
                            kran = 1
    conn.close()
#FILTER PART END

    #print(message.server.id)
    if message.content.lower().startswith(config.prefix):
        invoke = message.content[len(config.prefix):].split(" ")[0].lower()
        args = message.content.split(" ")[1:]
        #print("INVOKE %s\nARGS: %s" % (invoke, args.__str__()[1:-1].replace ("'", "")))
        if commands.__contains__(invoke):

            cmd = commands[invoke]
            try:
                if not perms.check(message.author, cmd.perm):
                    await embeds.noperms(message, client, invoke)
                    return
                await cmd.ex(args, message, client, invoke)
            except:
                await cmd.ex(args, message, client, invoke)
                pass

            # await commands.get(invoke).ex(args, message, client, invoke)
        else:
            await embeds.unknowncmd(message, client, invoke)
    return
    # if message.content == "help":
    #AAAAAAAAAAA
    #     embed=discord.Embed(title="Discord", url="https://discord.gg/rsaNa3x")
    #     embed.set_author(name="PCA-Bot", url="https://discordapp.com/oauth2/authorize/?permissions=2146958591&scope=bot&client_id=421691975155056640", icon_url="https://i.imgur.com/E8GIP3I.png")
    #     embed.set_thumbnail(url="https://yt3.ggpht.com/-310LKwfseck/AAAAAAAAAAI/AAAAAAAAAAA/3oXd3OARMkQ/s200-mo-c-c0xffffffff-rj-k-no/photo.jpg")
    #     embed.add_field(name="INFOS ABOUT PCA-Bot", value="PCA-Bot, is a bot created by raidrix aka localhost.", inline=True)
    #     embed.add_field(name= "Just run &help to get a list of commands :)", value="~~and !permsystem explains the permsystem~~", inline=True)
    #     embed.set_footer(text="by raidrix.")
    #
    #     await client.send_message(message.channel, embed=embed)

@client.event
async def on_error(event, *args, **kwargs):
    message = args[0] #Gets the message object
    logging.warning(traceback.format_exc()) #logs the error
    etype, value, tb = sys.exc_info()
    if not traceback.format_exc().find("'User' object has no attribute 'roles'") == -1:
        return
    if not traceback.format_exc().find("database is locked") == -1:

        print(etype.__name__)
        embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
        embed.set_thumbnail(url=config.embedthumbnail)
        embed.add_field(name="WARNING", value="<@%s>, YOU caused an CRITICAL error \n *RESTARTING....*" % (message.author.id), inline=True)
        embed.set_footer(text=config.by)
        await client.send_message(message.channel, embed=embed)
        raise SystemExit
        return

    if not traceback.format_exc().find("Cannot operate on a closed database.") == -1:

        print(etype.__name__)
        embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
        embed.set_thumbnail(url=config.embedthumbnail)
        embed.add_field(name="WARNING", value="<@%s>, YOU caused an CRITICAL error \n *RESTARTING....*" % (message.author.id), inline=True)
        embed.set_footer(text=config.by)
        await client.send_message(message.channel, embed=embed)
        raise SystemExit
        return

    if etype.__name__ == "Internal Server Error":

        embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
        embed.set_thumbnail(url=config.embedthumbnail)
        embed.add_field(name="WARNING", value="Discord appears to have some trouble...." , inline=True)
        embed.set_footer(text=config.by)
        await client.send_message(message.channel, embed=embed)

    if etype.__name__ == "NotFound":
        return

    if etype.__name__ == "Forbidden":

        embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
        embed.set_thumbnail(url=config.embedthumbnail)
        embed.add_field(name="WARNING", value="Either the permission to do that is not given, or the higest role of %s is too low." % (config.name), inline=True)
        embed.set_footer(text=config.by)
        await client.send_message(message.channel, embed=embed)
        return

    print("etype")
    print(etype.__name__)
    embed=discord.Embed(title="Discord", url="https://discord.gg/rsaNa3x", color=0xe74c3c)
    embed.set_author(name="PCA-Bot", url="https://discordapp.com/oauth2/authorize/?permissions=2146958591&scope=bot&client_id=421691975155056640", icon_url="https://i.imgur.com/E8GIP3I.png")
    embed.set_thumbnail(url="https://yt3.ggpht.com/-310LKwfseck/AAAAAAAAAAI/AAAAAAAAARo/c5EvTwo_PyU/s200-mo-c-c0xffffffff-rj-k-no/photo.jpg")
    embed.add_field(name="WARNING", value="<@%s>, YOU caused an error \n Error: ```%s```" % (message.author.id, value), inline=True)
    embed.set_footer(text="by raidrix")
    await client.send_message(message.channel, embed=embed)
    return
    #await client.send_message(message.channel, "You caused an error!") #send the message to the channel

excon.ex()
client.run(SECRETS.TOKEN)

#!!addrole @localtestrole @localhost#0001
