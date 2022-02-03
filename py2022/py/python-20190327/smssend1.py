import gammu

sm = gammu.StateMachine()
sm.ReadConfig()


sm.Init()

text='Морозов Кирилл Михайлович'





message = {
    'Text': f'{text.encode()}',
    'SMSC': {'Location': 1},
    'Number': '89110271345',
}

sm.SendSMS(message)