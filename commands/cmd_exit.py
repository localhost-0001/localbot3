import discord
import config

perm = 4
id = "ping"

async def ex(args, message, client, invoke):
    embed=discord.Embed(title="Discord", url=config.invite, color=0x2ecc71)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.set_thumbnail(url=config.embedthumbnail)
    embed.add_field(name="INFORMATION!", value="*Restarting...*", inline=True)
    embed.set_footer(text=config.by)
    await client.send_message(message.channel, embed=embed)
    raise SystemExit
    return
