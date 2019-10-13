from gtts import gTTS
import enchant 
import playsound
import os
import serial
import requests
import json
print("input your number")
l=input()# taking receivers phone number as input
URL = 'https://www.way2sms.com/api/v1/sendCampaign'# as stated by API way2sms
tts = 'tts'
arduino = serial.Serial('COM6', 9600, timeout=.1)# Reading serial data from arduino
while True:
    for i in range(1,10000):
        data = arduino.readline()[:-2]# Removing spaces from the end
        if data:
            cade=data.decode("utf-8")# converting binary to ASCII
            tts = gTTS(text= cade, lang = 'en')# conerting text to speech
            file1 = str("hello"+str(i)+".mp3")# Naming the file
            tts.save(file1)# saving the file
            playsound.playsound(file1,True)# voice output
            os.remove(file1)# removing the created file
            def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
                req_params = {'apikey':'Your API Key','secret':'Secret API Key','usetype':'test or live','phone': l,'message':'Hello','senderid':'personal email ID'}
                return requests.post(reqUrl, req_params)
            # get required data as mentioned above
            # get response
            response = sendPostRequest(URL, 'provided-api-key', 'provided-secret', 'prod/stage', 'valid-to-mobile', 'active-sender-id', 'message-text' )
            print (response.text)# print the ouput i.e confirmation message
