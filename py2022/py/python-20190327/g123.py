import gammu

sm = gammu.StateMachine()
sm.ReadConfig()
sm.Init()

message = {
    'Text': 'python-gammu testing message',
    'SMSC': {'Location': 1},
    'Number': '+420800123465',
}

sm.SendSMS(message)
