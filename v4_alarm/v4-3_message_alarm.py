
from twilio.rest import Client

account_sid = 'sid'
auth_token = 'token'
client = Client(account_sid, auth_token)
message = client.messages.create(
    body='Hello',
    from_='+twilio임시번호',
    to='+받을번호'
)
print(message.sid)
print("success") 