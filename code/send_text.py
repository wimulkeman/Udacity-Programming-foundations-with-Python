# Option 1 to import
# from twilio.rest import TwilioRestClient
# Option 2 to import
from twilio import rest

account_sid = "{{ account_sid }}" # Your Account SID from www.twilio.com/console
auth_token  = "{{ auth_token }}"  # Your Auth Token from www.twilio.com/console

# Option 1
# client = TwilioRestClient(account_sid, auth_token)
# Option 2
client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
                                 to="+12345678901",    # Replace with your phone number
                                 from_="+12345678901") # Replace with your Twilio number

print(message.sid)