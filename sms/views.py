from django.shortcuts import render, redirect
from twilio.rest import Client

# Create your views here.


def index(request):
    if request.method == "POST":
        name = request.POST['name']
        text = request.POST['text']
        print(name, text)
        if text:
            account_sid = 'Your Account_SID' #siz yaratgan accountdan olgan Account_SID  tokeni
            auth_token = 'Your AUTH_TOKEN' #siz yaratgan accountdan olgan Auth_token  tokeni
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=text,
                from_='Your twilo number', #yuboriladigan raqam
                to='can be sent to a receiving number.' #qabul qiladigan raqam, Twilioning tekin versiyasida faqat tasdiqlangan raqamga sms jo'natish mumkin.
            )
            return redirect('/')
    else:
        pass
    return render(request, 'index.html')