pass
# import discord
# import asyncio
# import embeds
# #import _mysql
# import excon
# import config
#
# perm = 1
# con = excon.con
#
# def check(reaction, user):
#     e = str(reaction.emoji)
#     return e.startswith(("1⃣", "2⃣", "3⃣"))
#
# async def ex(args, message, client, invoke):
#
#
#     embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
#     embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
#     embed.set_thumbnail(url=config.embedthumbnail)
#     embed.add_field(name="What do you want to do?", value=":one: Create a ticket\n:two: Delete a ticket\n:three: List your tickets\n this, does, not, fully, work, yet!!!", inline=False)
#     embed.set_footer(text=config.by)
#     menumsg = await client.send_message(message.channel, embed=embed)
#     await client.add_reaction(menumsg, "1⃣")
#     await client.add_reaction(menumsg, "2⃣")
#     await client.add_reaction(menumsg, "3⃣")
#
#
#
#     res = await client.wait_for_reaction(message=menumsg, check=check, user=message.author)
#
#     print(res.reaction.emoji)
#     print(res.user)
#
#     if res.reaction.emoji == "2⃣":
#         print("2 detected")
# #    print(res[0])
#
#
#     await client.send_message(message.channel, '{0.user} reacted with {0.reaction.emoji}!'.format(res))
#     return
#
#     m = message.channmentions[0]
#     memid = m.id
#     con.query("SELECT * FROM warnings WHERE id = '%s' AND memid = '%s'" % (message.server.id, memid))
# #    print("SELECTED")
#     r = con.store_result()
#     row = r.fetch_row(maxrows=1, how=1)
#
#
#     # reasoncache = args
#     # reasoncache = args[:0]
#     # print
#
#     if not row:
#         print("IN IF NOT ROW")
#         sql = "INSERT INTO warnings (id, memid, amount, reasons) VALUES ('%s', '%s', '1', '%s') " % (message.server.id, memid, ' '.join(args[1:]))
#         con.query(sql)
#         embed=discord.Embed(title="Discord", url=config.invite, color=0x2ecc71)
#         embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
#         embed.set_thumbnail(url=config.embedthumbnail)
#         embed.add_field(name="SUCCESS", value="Warned <@%s> .\nTotal Warnings: `1`" %(memid), inline=True)
#         embed.set_footer(text=config.by)
#         await client.send_message(message.channel, embed=embed)
#     else:
#         r1 = row[0]
# #        print(r1)
#         warningsnum = r1["amount"]
#         warningsnum = int(float(warningsnum)) + 1
# #        print(type(warningsnum))
#         reasons = r1["reasons"]
#         reasons = reasons.decode("utf-8")
#         reasons = reasons.split(',')
#         reasons.append(' '.join(args[1:]))
#         reasonsfinal = ','.join(reasons)
#         sql = "UPDATE warnings SET amount = '%s' WHERE id = '%s' AND memid = '%s' " % (warningsnum , message.server.id, memid)
#         sql2 = "UPDATE warnings SET reasons = '%s' WHERE id = '%s' AND memid = '%s' " % (reasonsfinal , message.server.id, memid)
#         con.query(sql)
#         con.query(sql2)
#         embed=discord.Embed(title="Discord", url=config.invite, color=0x2ecc71)
#         embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
#         embed.set_thumbnail(url=config.embedthumbnail)
#         embed.add_field(name="SUCCESS", value="Warned <@%s> .\nTotal Warnings: `%s`" %(memid, warningsnum), inline=True)
#         embed.set_footer(text=config.by)
#         await client.send_message(message.channel, embed=embed)
#
#     try:
#         await embeds.warnlog(message, client, memid, ' '.join(args[1:]))
#     except:
#         await embeds.nologchan(message, client)
#
#
#
#     #         addcontent = answer.content.lower()
#
#
#     #         filteredsplit.append(addcontent)
#     #         filternew = ','.join(filteredsplit)
#     #         #print(filternew)
#     #         await client.delete_message(answer)
#     #
#     #         try:
#     #             sql2 = "UPDATE warnings SET filtered = '%s' WHERE id = '%s'" % (filternew , message.server.id)
#     #         except:
#     #             print("SETTING SQL VAR FAIL IN FILTER")
#     #
#     #         try:
#     #             con.query(sql2)
#     #         except:
#     #             print("SQL QUERY FAIL IN FILTER")
#     #
#     #         embed=discord.Embed(title="Discord", url=config.invite, color=0x2ecc71)
#     #         embed.set_author(name=config.name, url="config.botinv, icon_url=config.leftlogoembed)
#     #         embed.set_thumbnail(url=config.embedthumbnail)
#     #         embed.add_field(name="Success", value="Added `%s` to the filter" % (addcontent), inline=True)
#     #         embed.set_footer(text=config.by)
#     #
#     #         await client.edit_message(menuemsg, embed=embed)
#     # elif answer.content.lower() == "clear":
#     #     await client.delete_message(answer)
#     #     sql = "DELETE FROM warnings WHERE id = '%s'" % (message.server.id)
#     #     con.query(sql);
#     #     embed=discord.Embed(title="Discord", url=config.invite, color=0x2ecc71)
#     #     embed.set_author(name=config.name, url="config.botinv, icon_url=config.leftlogoembed)
#     #     embed.set_thumbnail(url=config.embedthumbnail)
#     #     embed.add_field(name="SUCCESS", value="FILTER CLEARED", inline=True)
#     #     embed.set_footer(text=config.by)
#     #     await client.edit_message(menuemsg, embed=embed)
#     #
#     # elif answer.content.lower() == "remove":
#     #     await client.delete_message(answer)
#     #     remb = embeds.remb()
#     #     await client.edit_message(menuemsg, embed=remb)
#     #     answer = await client.wait_for_message(author=message.author)
#     #     remcontent = answer.content.lower()
#     #     # print(addcontent)
#     #     r1 = row[0]
#     #     filtered = r1["filtered"]
#     #     filtered = filtered.decode("utf-8")
#     #     filteredsplit = filtered.split(',')
#     #     for f in filteredsplit:
#     #         if f in remcontent:
#     #             filteredsplit.remove(f)
#     #
#     #
#     #     filternew = ','.join(filteredsplit)
#     #     #print(filternew)
#     #     await client.delete_message(answer)
#     #
#     #     try:
#     #         sql2 = "UPDATE warnings SET filtered = '%s' WHERE id = '%s'" % (filternew , message.server.id)
#     #     except:
#     #         print("SETTING SQL VAR FAIL IN FILTER")
#     #
#     #     try:
#     #         con.query(sql2)
#     #     except:
#     #         print("SQL QUERY FAIL IN FILTER")
#     #
#     #     embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
#     #     embed.set_author(name=config.name, url="config.botinv, icon_url=config.leftlogoembed)
#     #     embed.set_thumbnail(url=config.embedthumbnail)
#     #     embed.add_field(name="Success", value="Removed `%s` from the filter" % (remcontent), inline=True)
#     #     embed.set_footer(text=config.by)
#     #     await client.edit_message(menuemsg, embed=embed)
#     #
#     # else:
#     #     await client.delete_message(answer)
#     #     embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
#     #     embed.set_author(name=config.name, url="config.botinv, icon_url=config.leftlogoembed)
#     #     embed.set_thumbnail(url=config.embedthumbnail)
#     #     embed.add_field(name="WARNING", value="Request canceled", inline=True)
#     #     embed.set_footer(text=config.by)
#     #     await client.edit_message(menuemsg, embed=embed)
#     #
#     #
#
# #    print(answer.content)
#
#     return
#
# #     var chnl = message.Channel as SocketGuildChannel;
# # var Guild = chnl.Guild.Name;
