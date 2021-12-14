## DLOH-server
Destiny Loadout Helper (DLOH) is a Destiny 2 inventory management and companion app.

DLOH will exist as a native web application. 
Once users log in and sync their Bungie accounts with their DLOH account they will be able to see their Destiny characters inventories and their account wide "vault" inventory. 
They will be able to select their characters, view equipped items, modify equipped items etc. 

Components: 
- Authentication
-- Create a DLOH account with the Companion App via username and password. 

- Bungie Account Validation
-- As a logged in user I am able to authenticate my Bungie ACcount and sync my account data with DLOH via OAuth2.

- Character selection
-- As a logged in and validated user, I am able to see my Destiny 2 characters and their inventories as well as manipulate which items I have equipped in game.

---
DLOH-server was built using python3 and Django. After cloning the repo run python 3 manage.py makemigrations. Then run python3 manage.py migrate.
-

<img src="https://media.giphy.com/media/ZuZYKCYJdl30OspQhM/giphy.gif" height="20" width="38"> &nbsp;&nbsp;&nbsp;<a href="https://github.com/travish-io/DLOH-client">DLOH-client</a>
