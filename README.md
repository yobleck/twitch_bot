# WORK IN PROGRESS. NOT SECURE. twitch_bot
plugin based twitch bot written in python

## plugins
Plugins must be *.py files in the plugins folder.
They must contain a function called execute
which takes a string input, processes it
and returns a string to be sent to twitch chat.
If the plugin doesn't need to return anything then
return an empty string.
