import requests

while True:
    Mesaj = input("mesaj")
    DataForLink = {'text': Mesaj}
    Bot_Token = "token"
    Chat_ID = "id"

    requests.post("https://api.telegram.org/bot" + Bot_Token +
              "/sendMessage?chat_id=" + Chat_ID ,
              data=DataForLink)