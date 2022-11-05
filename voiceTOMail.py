import speech_recognition as sr
import yagmail

recognizer=sr.Recognizer()
with sr.Microphone() as source:
    print('Clearing background noise:')
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print("waiting for your message...")
    recordedaudio=recognizer.listen(source)
    print('Done recording..!')
try:
    print('Printing the message..')
    text=recognizer.recognize_google(recordedaudio,language='en-us')
    print('Your message:{}'.format(text))
    reciever='mram40686@gmail.com'
    message=text
    sender=yagmail.SMTP('mr032495@gmail.com')
    sender.send(to=reciever,subject='This is an automated mail',contents=message)
    print('complete')
except Exception as ex:
    print(ex)
# creates SMTP session