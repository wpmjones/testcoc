# testcoc
RESTful API to test COC libraries and scripts

# What it does
Generate both static and random data which is either correct or incorrect so that you 
can test your code for how it handles user input and API output.

# Endpoints
###Player Tags  
`/player_tag?limit=25&wrong_prefix=True`  
Returns valid, properly structured player tags. 
 
**Optional arguments:**  
limit (integer): limit the list to a specific number of tags
wrong_prefix (boolean): replace the # with some other character

`/player_tag/garbled?limit=5&wrong_prefix=True`  
Returns valid, improperly structured player tags representing possible input from end users. 
This might include spaces where they don't belong, o's instead of 0's, mix of upper and 
lowercase letters, and incorrect prefixes.

All responses to this endpoint can be converted into valid player tags.
  
**Optional arguments:**  
limit (integer): limit the list to a specific number of tags
wrong_prefix (boolean): replace the # with some other character

`/player_tag/invalid?limit=10`  
Returns invalid, properly structed player tags. This might include tags with incorrect letters, 
tags that are too long or too short, etc.  This is so that you can see what your code will do 
with invalid tags. Wrong prefix is not an option here since we're testing invalid tags, not prefixes.
  
**Optional arguments:**  
limit (integer): limit the list to a specific number of tags

### Dates
`/dates?date_type=past&limit=25`  
Returns valid, Supercell style timestamps.
  
**Required argument:**  
date_type (string): `past` or `future`

**Optional argument:**  
limit (integer): limit the list to a specific number of dates (default=255)



### Coming soon
Clan tags
Valid & invalid player names names in a variety of languages
Valid & invalid clan names in a variety of languages