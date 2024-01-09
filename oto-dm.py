from pyrogram import Client


api_id = input("API ID'yi girin: ")
api_hash = input("API Hash'ı girin: ")
string_session = input("Pyrogram String Session'ı girin: ")


with Client(string_session, api_id=int(api_id), api_hash=api_hash) as client:
    
    group_link = input("Üyelerine Mesaj Yazılacak Grubun Kullanıcı Adını Girin: ")
    message = input("Üyelere yazılacak mesajı girin: ")

    
    group = client.get_chat(group_link)
    
    
    for member in client.iter_chat_members(group.id):
        
        user_id = member.user.id
        
        
        client.send_message(user_id, message)
    
    print("Mesajlar Gönderildi!")

