pass
# import discord
# import asyncio
# import embeds
# import _mysql
# import excon
# import config
# try:
#     import Image
# except ImportError:
#     from PIL import Image
# import pytesseract
# import argparse
# import cv2
# import os
#
# perm = 2
# con = excon.con
# def check(reaction, user):
#     e = str(reaction.emoji)
#     return e.startswith(("1⃣", "2⃣", "3⃣", "4⃣", "5⃣"))
#
# async def ex(args, message, client, invoke):
#     #pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR'
#     image = cv2.imread(args[0])
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     print("1")
#     cv2.imshow(args[0], gray)
#     print("2")
#
#     filename = "{}.png".format(os.getpid())
#     print("3")
#     cv2.imwrite(filename, gray)
#
#     print("befor")
#     text = pytesseract.image_to_string(Image.open("13384.png"))
#     print("after")
#     os.remove(filename)
#     print(text)
#
#     cv2.imshow("Output", gray)
#     cv2.waitKey(0)
#
#     # show the output images
#     cv2.imshow("Image", image)
#     cv2.imshow("Output", gray)
#     cv2.waitKey(0)
#
#
#
#
#     con.query("SELECT * FROM chatfilter WHERE id = '%s'" % (message.server.id))
#
#     wempty = 0
#
#     r = con.store_result()
#     row = r.fetch_row(maxrows=1, how=1)
#
#     if not row:
#         sql = "INSERT INTO verids (id, tid) VALUES ('%s', '7890798078978097987980978798008087707908', '1') " % (message.server.id)
#         con.query(sql)
#
#         con.query("SELECT * FROM chatfilter WHERE id = '%s'" % (message.server.id))
#
#         wempty = 1
#         r = con.store_result()
#         row = r.fetch_row(maxrows=1, how=1)
#     try:
#         await embeds.filterlog(message, client)
#     except:
#         await embeds.nologchan(message, client)
#
#     smsg = ":one: List \n:two: Add \n:three: Remove \n:four: Clear \n:five: Cancel \n"
#
#     menuemsg = await embeds.menuemsg(message, smsg, client)
# #    answer = await client.wait_for_message(author=message.author)
#
#     await client.add_reaction(menuemsg, "1⃣")
#     await client.add_reaction(menuemsg, "2⃣")
#     await client.add_reaction(menuemsg, "3⃣")
#     await client.add_reaction(menuemsg, "4⃣")
#     await client.add_reaction(menuemsg, "5⃣")
#
#     res = await client.wait_for_reaction(message=menuemsg, check=check, user=message.author)
#
#     if res.reaction.emoji == "1⃣":
#         selected = "list"
#     if res.reaction.emoji == "2⃣":
#         selected = "add"
#     if res.reaction.emoji == "3⃣":
#         selected = "remove"
#     if res.reaction.emoji == "4⃣":
#         selected = "clear"
#     if res.reaction.emoji == "5⃣":
#         selected = "cancel"
#
#     if selected == "list":
# #        await client.delete_message(answer)
#         if wempty > 0:
# #            print("lolz")
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
#     elif selected == "add":
# #        await client.delete_message(answer)
#         addemb = embeds.addemb()
#         await client.edit_message(menuemsg, embed=addemb)
#         answer = await client.wait_for_message(author=message.author)
#         if not answer.content.lower().find(',') == -1:
#             await client.delete_message(answer)
#             #commaemb = embeds.commaemb()
#             embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
#             embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
#             embed.set_thumbnail(url=config.embedthumbnail)
#             embed.add_field(name="WARNING", value="Sorry, <@%s>, `,` is a disallowed symbol." % (message.author.id), inline=True)
#             embed.set_footer(text=config.by)
#             await client.edit_message(menuemsg, embed=embed)
#             return
#         elif not answer.content.lower().find('\\') == -1:
#             await client.delete_message(answer)
#             embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
#             embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
#             embed.set_thumbnail(url=config.embedthumbnail)
#             embed.add_field(name="WARNING", value="Sorry, <@%s>, `\\` is a dissallowed symbol, also make sure u don't add any emojis." % (message.author.id), inline=True)
#             embed.set_footer(text=config.by)
#             await client.edit_message(menuemsg, embed=embed)
#             return
#         else:
#             addcontent = answer.content.lower()
#             # print(addcontent)
#             r1 = row[0]
#             filtered = r1["filtered"]
#             filtered = filtered.decode("utf-8")
#             filteredsplit = filtered.split(',')
#             filteredsplit.append(addcontent)
#             filternew = ','.join(filteredsplit)
#             #print(filternew)
#             await client.delete_message(answer)
#
#             try:
#                 sql2 = "UPDATE chatfilter SET filtered = '%s' WHERE id = '%s'" % (filternew , message.server.id)
#             except:
#                 print("SETTING SQL VAR FAIL IN FILTER")
#
#             try:
#                 con.query(sql2)
#             except:
#                 print("SQL QUERY FAIL IN FILTER")
#
#             embed=discord.Embed(title="Discord", url=config.invite, color=0x2ecc71)
#             embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
#             embed.set_thumbnail(url=config.embedthumbnail)
#             embed.add_field(name="Success", value="Added `%s` to the filter" % (addcontent), inline=True)
#             embed.set_footer(text=config.by)
#
#             await client.edit_message(menuemsg, embed=embed)
#     elif selected == "clear":
# #        await client.delete_message(answer)
#         sql = "DELETE FROM chatfilter WHERE id = '%s'" % (message.server.id)
#         con.query(sql);
#         embed=discord.Embed(title="Discord", url=config.invite, color=0x2ecc71)
#         embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
#         embed.set_thumbnail(url=config.embedthumbnail)
#         embed.add_field(name="SUCCESS", value="FILTER CLEARED", inline=True)
#         embed.set_footer(text=config.by)
#         await client.edit_message(menuemsg, embed=embed)
#
#     elif selected == "remove":
# #        await client.delete_message(answer)
#         remb = embeds.remb()
#         await client.edit_message(menuemsg, embed=remb)
#         answer = await client.wait_for_message(author=message.author)
#         remcontent = answer.content.lower()
#         # print(addcontent)
#         r1 = row[0]
#         filtered = r1["filtered"]
#         filtered = filtered.decode("utf-8")
#         filteredsplit = filtered.split(',')
#         for f in filteredsplit:
#             if f in remcontent:
#                 filteredsplit.remove(f)
#
#
#         filternew = ','.join(filteredsplit)
#         #print(filternew)
#         await client.delete_message(answer)
#
#         try:
#             sql2 = "UPDATE chatfilter SET filtered = '%s' WHERE id = '%s'" % (filternew , message.server.id)
#         except:
#             print("SETTING SQL VAR FAIL IN FILTER")
#
#         try:
#             con.query(sql2)
#         except:
#             print("SQL QUERY FAIL IN FILTER")
#
#         embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
#         embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
#         embed.set_thumbnail(url=config.embedthumbnail)
#         embed.add_field(name="Success", value="Removed `%s` from the filter" % (remcontent), inline=True)
#         embed.set_footer(text=config.by)
#         await client.edit_message(menuemsg, embed=embed)
#
#     else:
# #        await client.delete_message(answer)
#         embed=discord.Embed(title="Discord", url=config.invite, color=0xe74c3c)
#         embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
#         embed.set_thumbnail(url=config.embedthumbnail)
#         embed.add_field(name="WARNING", value="Request canceled", inline=True)
#         embed.set_footer(text=config.by)
#         await client.edit_message(menuemsg, embed=embed)
#
#
#
# #    print(answer.content)
#
#     return
#
# #     var chnl = message.Channel as SocketGuildChannel;
# # var Guild = chnl.Guild.Name;
