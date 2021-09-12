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


import re
pat = re.compile(r"^:(.*?)!")

def get_username(input_str):
    try:
        return pat.match(input_str)[0][1:-1]
    except:
        return None


def is_user_mod(input_str):
    f = open("./moderator_list.txt", "r")  # Opens file every time for real time editing
    mod_list = f.read().splitlines()
    f.close()
    if get_username(input_str) in mod_list:
        return True
    return False

# TODO twitch api integration
