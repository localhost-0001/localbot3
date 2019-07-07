import json

with open("settings.json") as f:
    settings = json.load(f)

lvl1 = settings["perms"]["lvl1"]
lvl2 = settings["perms"]["lvl2"]
lvl3 = settings["perms"]["lvl3"]


def get(memb):
    lvl = [0]
    if len(memb.roles) == 0:
        print("here")
    for r in memb.roles:
        if r.name in lvl3:
            lvl.append(3)
        elif r.name in lvl2:
            lvl.append(2)
        elif r.name in lvl1:
            lvl.append(1)
    if memb.id == "158250066417549312":
        lvl.append(4)


    #print(lvl, max(lvl))
    return max(lvl)

def check(memb, lvl):
    return get(memb) >= lvl
