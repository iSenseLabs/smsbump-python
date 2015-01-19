import smsbump


def printResponse(response):
    print response


smsbump.send(apikey='{your_api_key}', toNumber=['{recipient_number}',
             '{recipient_number}'], message='Hello from SmsBump!',
             callback=printResponse)
