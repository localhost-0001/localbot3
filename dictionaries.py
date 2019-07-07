import config

commandshelp = {
#    "Settings" : "Misc"
    "Ping" : "Misc",
    "Countmsg" : "Misc",
    "Suggest" : "Misc",
    "Version" : "Misc",
    "Lenny" : "Misc",
    "Filter" : "Administrative",
    "Kick" : "Administrative",
    "Ban" : "Administrative",
    "Clear" : "Administrative",
    "Fast-Clear" : "Administrative",
    "User-Clear" : "Administrative",
    "Add" : "Administrative",
    "Remove" : "Administrative",
    "Warn" : "Administrative",
    "Pardon" : "Administrative",
    "Strikes" : "Administrative"
}

commandslist = {
#    "Settings" : "Misc"
    "Ping" : "Misc",
    "Countmsg" : "Misc",
    "Suggest" : "Misc",
    "Version" : "Misc",
    "Lenny" : "Misc",
    "Filter" : "Administrative",
    "Kick" : "Administrative",
    "Ban" : "Administrative",
    "Clear" : "Administrative",
    "Fast-Clear" : "Administrative",
    "User-Clear" : "Administrative",
    "Add" : "Administrative",
    "Remove" : "Administrative",
    "Warn" : "Administrative",
    "Pardon" : "Administrative",
    "Strikes" : "Administrative"
}

commandusagehelp = {
#    "Wait for it!"
    "Ping" : "**Description:** Checks if the bot is online.\n**Usage:** " + config.prefix + "ping",
    "Countmsg" : "**Description:** Counts the amount of messages in a channel.\n**Usage:** " + config.prefix + "cmsg",
    "Suggest" : "**Description:** Suggest something to the Bot-Developer.\n**Usage:** %ssuggest [suggestion]",
    "Version" : "**Description:** Shows the current and latest version of the bot.\n**Usage:** " + config.prefix + "v",
    "Lenny" : "**Description:** Gives you a random \"Lenny-Face\".\n**Usage:** " + config.prefix + "lenny",
    "Filter" : "**Description:** Opens the settings-menu for the chatfilter.\n**Usage:** " + config.prefix + "filter",
    "Kick" : "**Description:** Kicks the mentioned user.\n**Usage:** " + config.prefix + "kick [@member]",
    "Ban" : "**Description:** Bans the mentioned user.\n**Usage:**" + config.prefix + "sban [@member]",
    "Clear" : "**Description:** Deletes the selected amount of messages in the current channel\n**Usage:** " + config.prefix + "clear [amount of messages to clear]",
    "Fast-Clear" : "**Description:** The same as the normal clear command. Faster but with more limitations.\n**Limitations:** \n      1. Cannot clear more than 99 messages at once.\n      2. Cannot clear messages older than 2 weeks.\n**Usage:** " + config.prefix + "fclear [amount of messages to clear]\n**NOTE:** This will be directly implemented into the normal clear command soon.",
    "User-Clear" : "**Description:** Clears the selected amount of messages of the mentioned user in the current channel.\n**Usage:** " + config.prefix + "uc [amount of messages to clear] [@member to clear from]",
    "Add" : "**Description:** Adds one or multiple roles to one or multiple users\n**Usage:** " + config.prefix + "add [@role(s)] [@member(s)]",
    "Remove" : "**Description:** Removes one or multiple roles from one or multiple users\n**Usage:** " + config.prefix + "rem [@role(s)] [@member(s)]",
    "Warn" : "**Description:** Warns the mentioned user\n**Usage:** " + config.prefix + "warn [@member] [reason]",
    "Pardon" : "**Description:** Removes the last warning from the mentioned user\n**Usage:** " + config.prefix + "pardon [@mebmer] <reason>",
    "Strikes" : "**Description:** Shows the warnings of a user\n**Usage:** " + config.prefix + "strikes [@member]"
}

def commands():
        commandsold = {

            "addrole" : "Addrole", #1
            "ban" : "Ban", #2
            "clear" : "Clear", #3
            "cmsg" : "Countmsg", #4
            "faq" : "FAQ", #5
            "fclear" : "Fast-Clear", #6
            "filter" : "Filter", #7
            "gundam" : "Gundam", #8
            "help" : "Help", #9
            "kick" : "Kick",
            "list" : "List",
            "pardon" : "Pardon",
            "prmsys" : "Permsys",
            "ping" : "Ping",
            "remrole" : "Remrole",
            "uclear" : "Userclear",
            "ver" : "Version",
            "warn" : "Warn"

        }
        commands = {y:x for x,y in commandsold.items()}

        return commands

def commands1():

    commandsold1 = {

        "addrole" : "Addrole", #1
        "ban" : "Ban", #2
        "clear" : "Clear", #3
        "cmsg" : "Countmsg", #4
        "faq" : "FAQ", #5
        "fclear" : "Fast-Clear", #6
        "filter" : "Filter", #7
        "gundam" : "Gundam", #8
        "help" : "Help" #9

    }

    commands1 = {y:x for x,y in commandsold1.items()}

    return commands1


def commands2():

    commandsold2 = {

         "Kick" : "kick",
         "List" : "list",
         "Pardon" : "pardon",
         "Permsys" : "prmsys",
         "Ping" : "ping",
         "Remrole" : "remrole",
         "Userclear" : "uclear",
         "Version" : "ver",
         "Warn" : "warn"
# add the addmoney command
    }

    commands2 = {y:x for x,y in commandsold2.items()}

    return commands2
