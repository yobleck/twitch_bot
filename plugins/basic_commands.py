import json

f = open("./plugins/basic_commands.json", "r")
cmds = json.load(f)
f.close()


def execute(input_str):
    for k in cmds.keys():
        if k in input_str:
            return cmds[k]
