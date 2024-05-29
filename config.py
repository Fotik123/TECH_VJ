# Don't Remove Credit @m007
# Subscribe YouTube Channel For Amazing Bot @m07
# Ask Doubt on telegram @7_bot

import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "240")

API_HASH = os.environ.get("API_HASH", "515b9l045a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6gjNCIh8htvw") 

FORCE_SUB = os.environ.get("FORCE_SUB", "m07") 

             # Don't Remove Credit @m007 
             # Subscribe YouTube Channel For Amazing Bot @moviebox0007
             # Ask Doubt on telegram @07_bot

DB_NAME = os.environ.get("DB_NAME", "Tach")     

DB_URL = os.environ.get("DB_URL", "cluster0.3swxciv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '2220').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @m007 
# Subscribe YouTube Channel For Amazing Bot @mox0007 
# Ask Doubt on telegram @07_bot
