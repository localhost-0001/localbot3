import discord
import asyncio
import embeds
import excon
import config
import sqlite3
import json
import time
#import _mysql

id = "pardon"


perm = 1

async def ex(args, message, client, invoke):

    conn = sqlite3.connect('sql.db')
    c = conn.cursor()

    if len(args) < 1:
        embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
        embed.set_thumbnail(url=config.embedthumbnail)
        embed.add_field(name="WARNING", value="Command usage: pardon @member <reason>", inline=False)
        embed.set_footer(text=config.by)
        await client.send_message(message.channel, embed=embed)
        conn.close()
        return
    m = message.mentions[0]
    memid = m.id
    c.execute('SELECT * FROM warnings WHERE id = ? AND memid = ?' , (message.server.id, memid))
#    print("SELECTED")
    row = c.fetchone()

    # reasoncache = args
    # reasoncache = args[:0]
    # print

    if not row:

        embed=discord.Embed(title="Discord", url=config.invite, color=0x2ecc71)
        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
        embed.set_thumbnail(url=config.embedthumbnail)
        embed.add_field(name="SUCCESS", value="Pardoned no warnings from <@%s>, because [he, she, it, whatever] had none!" %(memid), inline=True)
        embed.set_footer(text=config.by)
        await client.send_message(message.channel, embed=embed)
        conn.close()
        return
    else:
        warningsnum = row[2]
#        print(warningsnum)
        try:
            warningsnum = int(warningsnum) - 1
        except:
            pass
#        print(type(warningsnum))

        reasons1 = row[3]
        reasons1 = json.loads(reasons1)
        if len(reasons1) == 0:
            embed=discord.Embed(title="Discord", url=config.invite, color=0x2ecc71)
            embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
            embed.set_thumbnail(url=config.embedthumbnail)
            embed.add_field(name="SUCCESS", value="Pardoned no warnings from <@%s>, because [he, she, it, whatever] had none!" %(memid), inline=True)
            embed.set_footer(text=config.by)
            await client.send_message(message.channel, embed=embed)
            conn.close()
            return
        reasons1.pop()
        reasons = json.dumps(reasons1)

        authorstemp = row[4]
        authors = json.loads(authorstemp)
        authors.pop()
        authorstring = json.dumps(authors)

        timesrow = row[5]
        times = json.loads(timesrow)
        times.pop()
        timestring = json.dumps(times)

        c.execute('UPDATE warnings SET amount = ? WHERE id = ? AND memid = ?' , (warningsnum , message.server.id, memid))
        conn.commit()

        c.execute('UPDATE warnings SET reasons = ? WHERE id = ? AND memid = ?' , (reasons , message.server.id, memid))
        conn.commit()

        c.execute('UPDATE warnings SET authors = ? WHERE id = ? AND memid = ?' , (authorstring , message.server.id, memid))
        conn.commit()

        c.execute('UPDATE warnings SET timestamps = ? WHERE id = ? AND memid = ?' , (timestring , message.server.id, memid))
        conn.commit()

        embed=discord.Embed(title="Discord", url=config.invite, color=0x2ecc71)
        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
        embed.set_thumbnail(url=config.embedthumbnail)
        embed.add_field(name="SUCCESS", value="Pardoned <@%s> .\nTotal Warnings: `%s`" %(memid, warningsnum), inline=True)
        embed.set_footer(text=config.by)
        await client.send_message(message.channel, embed=embed)
#
    try:
        await embeds.pardonlog(message, client, memid, ' '.join(args[1:]))
    except:
        await embeds.nologchan(message, client)

    conn.close()

    #conn.commit()



    #         addcontent = answer.content.lower()


    #         filteredsplit.append(addcontent)
    #         filternew = ','.join(filteredsplit)
    #         #print(filternew)
    #         await client.delete_message(answer)
    #
    #         try:
    #             sql2 = "UPDATE warnings SET filtered = '%s' WHERE id = '%s'" % (filternew , message.server.id)
    #         except:
    #             print("SETTING SQL VAR FAIL IN FILTER")
    #
    #         try:
    #             con.query(sql2)
    #         except:
    #             print("SQL QUERY FAIL IN FILTER")
    #
    #         embed=discord.Embed(title="Discord", url=config.invite, color=0x2ecc71)
    #         embed.set_author(name=config.name, url="config.botinv, icon_url=config.leftlogoembed)
    #         embed.set_thumbnail(url=config.embedthumbnail)
    #         embed.add_field(name="Success", value="Added `%s` to the filter" % (addcontent), inline=True)
    #         embed.set_footer(text=config.by)
    #
    #         await client.edit_message(menuemsg, embed=embed)
    # elif answer.content.lower() == "clear":
    #     await client.delete_message(answer)
    #     sql = "DELETE FROM warnings WHERE id = '%s'" % (message.server.id)
    #     con.query(sql);
    #     embed=discord.Embed(title="Discord", url=config.invite, color=0x2ecc71)
    #     embed.set_author(name=config.name, url="config.botinv, icon_url=config.leftlogoembed)
    #     embed.set_thumbnail(url=config.embedthumbnail)
    #     embed.add_field(name="SUCCESS", value="FILTER CLEARED", inline=True)
    #     embed.set_footer(text=config.by)
    #     await client.edit_message(menuemsg, embed=embed)
    #
    # elif answer.content.lower() == "remove":
    #     await client.delete_message(answer)
    #     remb = embeds.remb()
    #     await client.edit_message(menuemsg, embed=remb)
    #     answer = await client.wait_for_message(author=message.author)
    #     remcontent = answer.content.lower()
    #     # print(addcontent)
    #     r1 = row[0]
    #     filtered = r1["filtered"]
    #     filtered = filtered.decode("utf-8")
    #     filteredsplit = filtered.split(',')
    #     for f in filteredsplit:
    #         if f in remcontent:
    #             filteredsplit.remove(f)
    #
    #
    #     filternew = ','.join(filteredsplit)
    #     #print(filternew)
    #     await client.delete_message(answer)
    #
    #     try:
    #         sql2 = "UPDATE warnings SET filtered = '%s' WHERE id = '%s'" % (filternew , message.server.id)
    #     except:
    #         print("SETTING SQL VAR FAIL IN FILTER")
    #
    #     try:
    #         con.query(sql2)
    #     except:
    #         print("SQL QUERY FAIL IN FILTER")
    #
    #     embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
    #     embed.set_author(name=config.name, url="config.botinv, icon_url=config.leftlogoembed)
    #     embed.set_thumbnail(url=config.embedthumbnail)
    #     embed.add_field(name="Success", value="Removed `%s` from the filter" % (remcontent), inline=True)
    #     embed.set_footer(text=config.by)
    #     await client.edit_message(menuemsg, embed=embed)
    #
    # else:
    #     await client.delete_message(answer)
    #     embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
    #     embed.set_author(name=config.name, url="config.botinv, icon_url=config.leftlogoembed)
    #     embed.set_thumbnail(url=config.embedthumbnail)
    #     embed.add_field(name="WARNING", value="Request canceled", inline=True)
    #     embed.set_footer(text=config.by)
    #     await client.edit_message(menuemsg, embed=embed)
    #
    #

#    print(answer.content)

    return

#     var chnl = message.Channel as SocketGuildChannel;
# var Guild = chnl.Guild.Name;



#Python 2.7.3 (default, Apr 24 2012, 00:00:54)

# >>> import time
# >>> ts = time.time()
# >>> print ts
# 1355563265.81
# >>> import datetime
# >>> st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
# >>> print st
# 2012-12-15 01:21:05

#from datetime import datetime

#utc_dt = datetime.utcfromtimestamp(timestamp)

#string = json.dumps(lst)
#lst = json.loads(string)


# import discord
# import asyncio
# import embeds
# #import _mysql
# import excon
# import config
# import sqlite3
#
# perm = 1
# id = "pardon"
#
#
#
# async def ex(args, message, client, invoke):
#     conn = sqlite3.connect('sql.db')
#     c = conn.cursor()
#     if len(args) < 1:
#         embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
#         embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
#         embed.set_thumbnail(url=config.embedthumbnail)
#         embed.add_field(name="WARNING", value="Command usage: pardon @member <reason>", inline=False)
#         embed.set_footer(text=config.by)
#         await client.send_message(message.channel, embed=embed)
#         conn.close()
#         return
#     m = message.mentions[0]
#     memid = m.id
#     c.execute('SELECT * FROM warnings WHERE id = ? AND memid = ?' , (message.server.id, memid))
# #    print("SELECTED")
#     row = c.fetchone()
#
#     # reasoncache = args
#     # reasoncache = args[:0]
#     # print
#
#     if not row:
#         embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
#         embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
#         embed.set_thumbnail(url=config.embedthumbnail)
#         embed.add_field(name="WARNING", value="<@%s> has no Warnings"%(memid), inline=False)
#         embed.set_footer(text=config.by)
#         await client.send_message(message.channel, embed=embed)
#     else:
#     #    print(r1)
#         warningsnum = row[2]
#         try:
#             warningsnum = int(warningsnum)
#         except:
#             pass
#     #    print(type(warningsnum))
#         if warningsnum < 1:
#             embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
#             embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
#             embed.set_thumbnail(url=config.embedthumbnail)
#             embed.add_field(name="WARNING", value="ERROR 404 \n<@%s> has no Warnings"%(memid), inline=False)
#             embed.set_footer(text=config.by)
#             await client.send_message(message.channel, embed=embed)
#             conn.close()
#             return
#         warningsnum = warningsnum - 1
# #        print(type(warningsnum))
#         reasons = row[3]
#         reasons = reasons.split(',')
#         reasons.remove(reasons[-1])
# #        reasons.remove(reasons[-1])
#         reasonsfinal = ','.join(reasons)
#
#         c.execute('UPDATE warnings SET amount = ? WHERE id = ? AND memid = ? ' , (warningsnum , message.server.id, memid))
#         conn.commit()
#         c.execute('UPDATE warnings SET reasons = ? WHERE id = ? AND memid = ? ' , (reasonsfinal , message.server.id, memid))
#         conn.commit()
#         embed=discord.Embed(title="Discord", url=config.invite, color=0x2ecc71)
#         embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
#         embed.set_thumbnail(url=config.embedthumbnail)
#         embed.add_field(name="SUCCESS", value="<@%s> Pardoned.\nTotal Warnings: `%s`" %(memid, warningsnum), inline=True)
#         embed.set_footer(text=config.by)
#         await client.send_message(message.channel, embed=embed)
#
#     try:
#         await embeds.pardonlog(message, client, memid, ' '.join(args[1:]))
#     except:
#         await embeds.nologchan(message, client)
#     conn.close()
