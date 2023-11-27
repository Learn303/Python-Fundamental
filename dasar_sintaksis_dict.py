user = {
 "id": 1,
 "name": "arief",
 "username": "ariefwcks303",
 "email": "ariefwcks303@gmail.com",
 "addres":{
    "street": "Kulas Light",
    "suite": "Apt. 556",
    "city": "Gwenborough",
    "zipcode": "92998-3874",
    "geo": {
      "lat": "-37.3159",
      "lng": "81.1496"
    }
 }
,
}
print("\nMencetak User")
print(user)

print("\nMencentak masing masing")
print(user['id'])
print(user['name'])
print(user['username'])
print(user['email'])
print(user['addres'])

print("\nMencetak lat saja")
print(user['addres']['geo']['lat'])

print("\nHasil user")
print(user)
print(type(user))#tipedatadict



print("\n Hasil setelah diubah menjadi JSON file")
import json
result = json.dumps(user)
print(result)
print(type(result)) #tipedatajson

with open('result.json', 'w') as file:
    json.dump(user, file)