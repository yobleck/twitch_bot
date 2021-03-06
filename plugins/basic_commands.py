 # 
 # This file is part of the XXX distribution (https://github.com/yobleck/twitch_bot).
 # Copyright (c) 2021 yobleck.
 # 
 # This program is free software: you can redistribute it and/or modify  
 # it under the terms of the GNU General Public License as published by  
 # the Free Software Foundation, version 3.
 #
 # This program is distributed in the hope that it will be useful, but 
 # WITHOUT ANY WARRANTY; without even the implied warranty of 
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
 # General Public License for more details.
 #
 # You should have received a copy of the GNU General Public License 
 # along with this program. If not, see <http://www.gnu.org/licenses/>.
 #

import json

f = open("./plugins/basic_commands.json", "r")
cmds = json.load(f)
f.close()


def execute(input_str, utils):
    for k in cmds.keys():
        if k in input_str:
            return cmds[k]
