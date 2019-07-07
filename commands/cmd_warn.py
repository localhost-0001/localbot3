import discord
import asyncio
import embeds
import excon
import config
import sqlite3
import json
import time
#import _mysql

id = "warn"


perm = 1

async def ex(args, message, client, invoke):

    conn = sqlite3.connect('sql.db')
    c = conn.cursor()

    if len(args) < 2:
        embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
        embed.set_thumbnail(url=config.embedthumbnail)
        embed.add_field(name="WARNING", value="Command usage: warn @member <reason>", inline=False)
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
#        print("IN IF NOT ROW")

        authors = [message.author.id]
        authorstring = json.dumps(authors)
        times = [time.time()]
        timestring = json.dumps(times)
        reason1 = [" ".join(args[1:])]
        reason = json.dumps(reason1)

        c.execute('INSERT INTO warnings VALUES (?, ?, ?, ?, ?, ?)' , (message.server.id, memid, "1", reason, authorstring, timestring))
        conn.commit()

        embed=discord.Embed(title="Discord", url=config.invite, color=0x2ecc71)
        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
        embed.set_thumbnail(url=config.embedthumbnail)
        embed.add_field(name="SUCCESS", value="Warned <@%s> .\nTotal Warnings: `1`" %(memid), inline=True)
        embed.set_footer(text=config.by)
        await client.send_message(message.channel, embed=embed)
    else:
        warningsnum = row[2]
#        print(warningsnum)
        try:
            warningsnum = int(warningsnum) + 1
        except:
            pass
#        print(type(warningsnum))

        reasons1 = row[3]
        reasons1 = json.loads(reasons1)
        reasons2 = []
        for r in reasons1:
            reasons2.append(r)
        reasons2.append(' '.join(args[1:]))
        reasons = json.dumps(reasons2)

        authorstemp = row[4]
        authors = json.loads(authorstemp)
        authorstemp = []
        for a in authors:
            authorstemp.append(a)
        authorstemp.append(message.author.id)
        authorstring = json.dumps(authorstemp)

        timesrow = row[5]
        times = json.loads(timesrow)
        timesrow = []
        for t in times:
            timesrow.append(t)
        timesrow.append(time.time())
        timestring = json.dumps(timesrow)

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
        embed.add_field(name="SUCCESS", value="Warned <@%s> .\nTotal Warnings: `%s`" %(memid, warningsnum), inline=True)
        embed.set_footer(text=config.by)
        await client.send_message(message.channel, embed=embed)
#
    try:
        await embeds.warnlog(message, client, memid, ' '.join(args[1:]))
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
