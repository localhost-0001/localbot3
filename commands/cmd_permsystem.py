import discord
import config

fail = 0
id = "prmsys"

async def ex(args, message, client, invoke):
    embed=discord.Embed(title="Discord", url=config.invite, colour=0x3498db)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.add_field(name="PERMSYSTEM OF %s" % (config.name), value="Prefix: p!", inline=False)
    embed.add_field(name="Permissionlevel roles", value="prmlvl1 \nprmlvl2\nprmlvl3", inline=False)
    embed.add_field(name="Explanation/ Perks", value="Level 1:      Don't get filtered anymore! Commands unlocked: `fastclear, kick, pardon, warn`\nLevel 2:      Commands unlocked: `ban, addrole clear, filter, remrole`\nLevel 3:      You are the boss, let other people work for you!", inline=True)
    embed.set_footer(text=config.by)
    await client.send_message(message.channel, embed=embed)
