from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = ""
auth_token = ""

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+",
    from_="+61437767561",
    body="hello bhaaai kya haal hai")
