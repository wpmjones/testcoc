# testcoc
RESTful API to test COC libraries and scripts

# What it does
Generate both static and random data which is either correct or incorrect so that you 
can test your code for how it handles user input and API output.

# Endpoints
##Player Tags  
**Valid Player Tags**    
`/player_tags?limit=25&wrong_prefix=True`  
Returns valid, properly structured player tags. 
 
**Optional arguments:**  
limit (integer): limit the list to a specific number of tags (default=all)  
wrong_prefix (boolean): replace the # with some other character (default=False)

**Valid But Garbled Player Tags**  
`/player_tags/garbled?limit=5&wrong_prefix=True`  
Returns valid, improperly structured player tags representing possible input from end users. 
This might include spaces where they don't belong, o's instead of 0's, mix of upper and 
lowercase letters, and incorrect prefixes.

All responses to this endpoint can be converted into valid player tags.
  
**Optional arguments:**  
limit (integer): limit the list to a specific number of tags (default=all)  
wrong_prefix (boolean): replace the # with some other character (default=False)

**Invalid Player Tags**  
`/player_tags/invalid?limit=10`  
Returns invalid, properly structed player tags. This might include tags with incorrect letters, 
tags that are too long or too short, etc.  This is so that you can see what your code will do 
with invalid tags. Wrong prefix is not an option here since we're testing invalid tags, not prefixes.

None of these responses can be convered into a valid player tag.
  
**Optional arguments:**  
limit (integer): limit the list to a specific number of tags (default=all)

##Clan Tags
**Valid Clan Tags**    
`/clan_tags?limit=25&wrong_prefix=True`  
Returns valid, properly structured clan tags. 
 
**Optional arguments:**  
limit (integer): limit the list to a specific number of tags (default=all)  
wrong_prefix (boolean): replace the # with some other character (default=False)

**Valid But Garbled Clan Tags**  
`/clan_tags/garbled?limit=5&wrong_prefix=True`  
Returns valid, improperly structured clan tags representing possible input from end users. 
This might include spaces where they don't belong, o's instead of 0's, mix of upper and 
lowercase letters, and incorrect prefixes.

All responses to this endpoint can be converted into valid clan tags.
  
**Optional arguments:**  
limit (integer): limit the list to a specific number of tags (default=all)  
wrong_prefix (boolean): replace the # with some other character (default=False)

**Invalid Clan Tags**  
`/clan_tags/invalid?limit=10`  
Returns invalid, properly structed clan tags. This might include tags with incorrect letters, 
tags that are too long or too short, etc.  This is so that you can see what your code will do 
with invalid tags. Wrong prefix is not an option here since we're testing invalid tags, not prefixes.

None of these responses can be convered into a valid clan tag.
  
**Optional arguments:**  
limit (integer): limit the list to a specific number of tags (default=all)

## Dates
`/dates?date_type=past&limit=25`  
Returns valid, Supercell style timestamps.
  
**Required argument:**  
date_type (string): `past` or `future`

**Optional argument:**  
limit (integer): limit the list to a specific number of dates (default=255)


# Coming soon
Valid & invalid player names names in a variety of languages  
Valid & invalid clan names in a variety of languages