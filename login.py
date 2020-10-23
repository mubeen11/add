from telethon.sync import TelegramClient
from telethon import utils
from add import read_csv
import pymongo
from getmac import get_mac_address as gma
import time

file1 = open("user_key.txt","r+")
Key = file1.readline()
file1.close()
clus = pymongo.MongoClient("mongodb+srv://Devil_Ruler1:Moaz1999@cluster0.ezefa.mongodb.net/BOT?retryWrites=true&w=majority")
db = clus['BOT']
col = db['Key']
mac = gma()
print(mac)
cursor = col.find({"_id" : mac})
for document in cursor:
    key = document["key"]
if Key == key:
    try:
        phone_list = sum(read_csv('phone.csv'), start=[])
        api = read_csv('api.csv')[0]


        for unparsed_phone in phone_list:
            phone = utils.parse_phone(unparsed_phone)
            
            print(f"Login {phone}")
            client = TelegramClient(f"sessions/{phone}", *api)
            client.start(phone)

            client.disconnect()
            print()

        done = True


    finally:
        input("Done!" if done else "Error!")
    
else:
    print("This key is not valid for your system")

time.sleep(5000)

