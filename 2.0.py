import time
import win32com.client   # 系统客户端包
speaker = win32com.client.Dispatch("SAPI.SPVOICE")  # 系统接口
#while " ":
    #speaker.Speak("李彦婷")
#speaker.Speak("I am a good girl !")

count = 0
while count < 5:
    #print(count)
    #speaker.Speak("李彦婷"+str(count)+"次")
    count += 1
    
else:
    time.sleep(10)
    speaker.Speak("balabala")