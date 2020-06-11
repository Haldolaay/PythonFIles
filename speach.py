import speech_recognition as sr # this library should change audio to text

# it converts only one sentance looooooooooool
# Main Code start-----------------------------------------------------------------------------------------------------
sound = './test.wav' # test file
rec = sr.Recognizer() #  object from speach recognintion classes - it has planty of usefull functions
for index in range(2):
    with sr.AudioFile(sound) as source: # reading the test audio file
        rec.adjust_for_ambient_noise(source)
        print('converting, it might take time') # i still don't know why it takes time, maybe it's asynchrounus
        audio = rec.listen(source) # creating a server lol no it works like  a stream
        try:
            print(rec.recognize_google(audio))
        except Exception as error:
            print(error)

 
#Main Code end----------------------------------------------------------------------------------------------------------