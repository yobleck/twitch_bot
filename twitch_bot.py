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

# TODO SECURITY
# TODO verbose debugging
# TODO logging
# TODO argparse
# TODO file paths for irc.py are probably broken
# TODO plugin load order

import os
import sys
import glob
import importlib

import irc


username = "test_user"
channel_name = "test channel"


def load_plugins():  # Loaded alphabetically
    imp_list = []
    plugins_path = sys.path[0] + "/plugins"
    sys.path.append(plugins_path)  # Make it importable

    for f in glob.glob(plugins_path + "/*.py"):  # Get list of .py files
        imp_list.append( importlib.import_module( os.path.splitext( os.path.basename(f) )[0] ) )  # Import them

    return imp_list


def main():
    #chat = irc.chat(username)
    #chat.join(channel_name)
    plugins = load_plugins()

    while True:
        chat_text = "!hello" #chat.get_text()
        if chat_text == "nothing new":
            continue

        for p in plugins:
            to_send = p.execute(chat_text)
            if to_send: # TODO type check?
                print(to_send)
                #chat.send_text(to_send)
        break
    #chat.part(channel_name)
    #chat.quit()

if __name__ == "__main__":
    main()
