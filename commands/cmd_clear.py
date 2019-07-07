import discord
import asyncio
import embeds
import config

perm = 2
id = "clear"

def check(reaction, user):
    e = str(reaction.emoji)
    return e.startswith(("✅", "❌"))
def check2(reaction, user):
    e = str(reaction.emoji)
    return e.startswith(("❌"))
async def ex(args, message, client, invoke):

    if args.__len__() != 1:
        await embeds.syntaxa1num(message, invoke, client)
        return
    try:
        ammount = int(args[0]) + 1 if len(args) > 0 else 2
    except:
        await embeds.syntaxa1num(message, invoke, client)
        return

    embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.set_thumbnail(url=config.embedthumbnail)
    embed.add_field(name="WARNING", value="Do you really want to clear %s messages?" % (int(args[0])), inline=True)
    embed.set_footer(text=config.by)
 #   await asyncio.sleep(1)
    proofmsg = await client.send_message(message.channel, embed=embed)
#    answer = await client.wait_for_message(author=message.author)

    await client.add_reaction(proofmsg, "✅")
    await client.add_reaction(proofmsg, "❌")

    res = await client.wait_for_reaction(message=proofmsg, check=check, user=message.author)

    answer = "no"

    if res.reaction.emoji == "✅":
        answer = "yes"

    if not answer == "yes":
#        await client.delete_message(answer)
        embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
        embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
        embed.set_thumbnail(url=config.embedthumbnail)
        embed.add_field(name="WARNING", value="Request canceled!", inline=True)
        embed.set_footer(text=config.by)
        await client.edit_message(proofmsg, embed=embed)
        return

    await client.delete_message(proofmsg)

    msgout = 0
    cleared = -1
    failed = 0

#    clearmsg = await embeds.clearing(message, client)
    active = True
    active2 = True
    async for m in client.logs_from(message.channel, limit=ammount):
        if msgout == 0:
            embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
            embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
            embed.set_thumbnail(url="https://yt3.ggpht.com/-310LKwfseck/AAAAAAAAAAI/AAAAAAAAAAA/3oXd3OARMkQ/s200-mo-c-c0xffffffff-rj-k-no/photo.jpg")
            embed.add_field(name="WARNING", value="CHATCLEAN IN PROGRESS!", inline=True)
            embed.set_footer(text="by raidrix.")
            await asyncio.sleep(1)
            clearmsg = await client.send_message(message.channel, embed=embed)
            await client.add_reaction(clearmsg, "❌")

        msgout = 1
        if not m == clearmsg:
            if active:
                try:
                    await client.delete_message(m)
                    cleared += 1
                except:
                    failed += 1
                    pass
        am1 = ammount - 1
        if cleared == am1:
            active2 = False
    while active2:
        res = await client.wait_for_reaction(message=clearmsg, check=check2, user=message.author)
        print("here")
        active = False
        active2 = False
        failed_str = "\n\nFailed to clear %s message(s)." % failed if failed > 0 else ""

        await client.delete_message(clearmsg)

        returnmsg = await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.blue(), description="Cleared %s message(s).%s" % (cleared, failed_str)))
        await asyncio.sleep(3)
        await client.delete_message(returnmsg)
        return

    failed_str = "\n\nFailed to clear %s message(s)." % failed if failed > 0 else ""

    await client.delete_message(clearmsg)

    returnmsg = await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.blue(), description="Cleared %s message(s).%s" % (cleared, failed_str)))
    await asyncio.sleep(3)
    await client.delete_message(returnmsg)
