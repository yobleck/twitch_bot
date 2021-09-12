# WORK IN PROGRESS. NOT SECURE. twitch_bot
plugin based twitch bot written in python

## Plugins
Plugins must be *.py files in the plugins folder.
They must contain a function called execute
which takes a string input, processes it
and returns a string to be sent to twitch chat.
If the plugin doesn't need to return anything then
return an empty string.
The execute function should also except `utils`
as an argument in order to access useful [utility functions](#Utilities)
Example:
```
def execute(input_str, utils):
    
    return utils.get_suername(input_str) + " says: " + input_str
```

### basic_commands
user types `!command_name` and plugin returns
text defined in basic_commands.json

### return_input
reprints input for debugging

### banned_words (wip)
currently just tells user off for saying word in banned_words.txt

## Utilities
### get_username
### is_user_mod
