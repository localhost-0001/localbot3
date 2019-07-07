import discord
import config
import asyncio
import embeds

perm = 3
id = "addrole"

async def ex(args, message, client, invoke):

    roles = []
    rname = []
    mname = []
    members = []
    all = 0

    if (len(args)) == 0:
        await embeds.addsyntax(message, invoke, client)
        return

    if not message.content.lower().find("@everyone") == -1:
        all = 1

    if not message.role_mentions:
        await embeds.addsyntax(message, invoke, client)
        return

    if not message.mentions:
        if all == 0:
            await embeds.addsyntax(message, invoke, client)
            return

    for r in message.role_mentions:
        roles.append(r)

    for role in roles:
#       print(role)
        rname.append(role.name)

    if all == 1:
        for m in message.server.members:
            members.append(m)
    else:
        members = message.mentions

    for m in members:
        if all == 0:
            mname.append(''.join([m.name , "#", m.discriminator]))
#        print(m)

        for role in roles:
#            print(role)
#            rname.append(role.name)
#            await asyncio.sleep(1)

            await client.add_roles(m, role)

    if all == 1:
        mname.append(''.join("@everyone"))

    await embeds.addrole(message, client, rname, mname)
