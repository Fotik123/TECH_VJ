# Don't Remove Credit @moviebox0007
# Subscribe YouTube Channel For Amazing Bot @moviebox0007
# Ask Doubt on telegram @Fotik007_bot

import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "27919240")

API_HASH = os.environ.get("API_HASH", "1570036a734bd37515b90b709260045a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6900304306:AAGCRVRgjNLeMQaeTIO1oBVVPZwCIh8htvw") 

FORCE_SUB = os.environ.get("FORCE_SUB", "moviebox0007") 

             # Don't Remove Credit @moviebox0007 
             # Subscribe YouTube Channel For Amazing Bot @moviebox0007
             # Ask Doubt on telegram @Fotik007_bot

DB_NAME = os.environ.get("DB_NAME", "Tach")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://Tach:123@fotik@321@cluster0.3swxciv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '2211770620').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @moviebox0007 
# Subscribe YouTube Channel For Amazing Bot @moviebox0007 
# Ask Doubt on telegram @Fotik007_bot
