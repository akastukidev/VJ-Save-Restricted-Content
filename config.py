import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "27407768"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6e2b9653aa1007da6b874b33bc82a8fb")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://sonutheskywalkers:9IfxH4aAvsYjdWu5@cluster0.vyvjb85.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
