import discord
import config

perm = 4
id = "bdo"

def check(reaction, user):

    e = str(reaction.emoji)
    return e.startswith(('👍', '👎', ':one:', '0⃣', "1⃣", "2⃣", "3⃣", "4⃣", "5⃣", "6⃣", "7⃣", "8⃣", "9⃣"))

async def ex(args, message, client, invoke):

    print(message.content)
    embed=discord.Embed(title="Discord", url=config.invite, color=0x2ecc71)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.set_thumbnail(url=config.embedthumbnail)
    embed.add_field(name="YAY!", value="*you logged something in da console* :one:", inline=True)
    embed.set_footer(text=config.by)
    await client.send_message(message.channel, embed=embed)
    msg = await client.send_message(message.channel, 'React with thumbs up or thumbs down.')
    while 0 == 0:
        res = await client.wait_for_reaction(message=msg, check=check)
        await client.send_message(message.channel, '{0.user} reacted with {0.reaction.emoji}!'.format(res))
