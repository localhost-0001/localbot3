import discord
import asyncio
import embeds
#import _mysql
import excon
import config
import sqlite3
import json
import time
import datetime

perm = 0
id = "list"

async def ex(args, message, client, invoke):

    conn = sqlite3.connect('sql.db')
    c = conn.cursor()
    if len(message.mentions) < 1:
        m = message.author
        # embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
        # embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
        # embed.set_thumbnail(url=config.embedthumbnail)
        # embed.add_field(name="WARNING", value="Command usage: strikes @member", inline=False)
        # embed.set_footer(text=config.by)
        # await client.send_message(message.channel, embed=embed)
        # conn.close()
        # return
    else:
        m = message.mentions[0]
    memid = m.id
    c.execute("SELECT * FROM warnings WHERE id = '%s' AND memid = '%s'" % (message.server.id, memid))
#    print("SELECTED")
    row = c.fetchone()

#strikes
    # reasoncache = args
    # reasoncache = args[:0]
    # print

    if not row:
#        print("IN IF NOT ROW")
        embed=discord.Embed(title="Discord", url=config.invite, color=0x3498db)
        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
        embed.set_thumbnail(url=config.embedthumbnail)
        embed.add_field(name="NOTIFICATION", value="Error 404\n<@%s> has no Warnings!" %(memid), inline=True)
        embed.set_footer(text=config.by)
        await client.send_message(message.channel, embed=embed)
    else:
#        print(r1)
        warningsnum = row[2]
        try:
            warningsnum = int(warningsnum)
        except:
            pass

        timestring = row[5]
        authorstring = row[4]
        authors = json.loads(authorstring)
        timess = json.loads(timestring)
        times = []
        for t in timess:
            cache = []
            times.append(datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S'))
#        print(type(warningsnum))
#        print(type(warningsnum))
        reasons = row[3]
        reasons = json.loads(reasons)
        reasonlist = []
        counter = 0
        cop = 1

        for r in reasons:

            reasonlist.append(str(cop) + ". Reason:`" + r + "` by: <@" + authors[counter] + "> at `" + times[counter] + "`\n")
            counter += 1
            cop +=1
            # reasonlist.append(r)
            # reasonlist.append(r)
            # reasonlist.append(r)

#        reasonlist = '\n'.join(reasons)
        embed=discord.Embed(title="Discord", url=config.invite, color=0x3498db)
        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
        embed.set_thumbnail(url=config.embedthumbnail)
        embed.add_field(name="NOTIFICATION", value="Warnings of <@%s> .\n\nTotal Warnings: `%s`\n\n%s" %(memid, warningsnum, "".join(reasonlist)), inline=True)
        embed.set_footer(text=config.by)
        await client.send_message(message.channel, embed=embed)
    conn.close()

##############################################################################################

#         if wempty > 0:
#             print("lolz")
#             list0emb = embeds.list0emb()
#             await client.edit_message(menuemsg, embed=list0emb)
#         else:
#             r1 = row[0]
#             filtered = r1["filtered"]
#             filtered = filtered.decode("utf-8")
#             filteredsplit = filtered.split(',')
# #            print(len(filteredsplit))
#             if len(filteredsplit) == 0:
#                 list0emb = embeds.list0emb()
#                 await client.edit_message(menuemsg, embed=list0emb)
#                 return
#             allfiltered = []
#             for f in filteredsplit:
#                 if f == "7890798078978097987980978798008087707908":
#                     if len(filteredsplit) < 2:
#                         list0emb = embeds.list0emb()
#                         await client.edit_message(menuemsg, embed=list0emb)
#                 else:
#                     allfiltered.append(f)
#
#             filteredfull = '\n'.join(allfiltered)
# #            print(filteredfull)
#             embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
#             embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
#             embed.set_thumbnail(url=config.embedthumbnail)
#             embed.add_field(name="ALL ITEMS IN THE FILTER", value="(for each item a new line) \n %s" % (filteredfull), inline=True)
#             embed.set_footer(text=config.by)
#             await client.edit_message(menuemsg, embed=embed)
#             return
