import text_to_speech
import speech_to_text
import datetime
import webbrowser

#import weather

def Action (data):
   user_data = data.lower()

   if "What is your Name" in user_data:
      speech_to_text.speech_to_text("My name is Google Assistant , How can i help you")
      return "My name is Google Assistant , How can i help you"
   
   elif "what is your name" in user_data or " your name" in user_data:
      text_to_speech.text_to_speech("My name is Google Assistant , How can i help you")
      return "My name is Google Assistant , How can i help you"

   elif "hell" in user_data or "hye" in user_data:
      text_to_speech.text_to_speech("hey , sir how i can help you")
      return 'hey , sir how i can help you'
   
   elif "Hell" in user_data or "hye" in user_data:
      text_to_speech.text_to_speech("hey , sir how i can help you")
      return 'Hell , sir how i can help you'
   
   elif "hello" in user_data or "hye" in user_data:
      text_to_speech.text_to_speech("hey , sir how i can help you")
      return 'hello , sir how i can help you'
   
   elif "Hello" in user_data or "hye" in user_data:
      text_to_speech.text_to_speech("hey , sir how i can help you")
      return 'Hello , sir how i can help you'
   
   elif "hey" in user_data or "hye" in user_data:
      text_to_speech.text_to_speech("hey , sir how i can help you")
      return 'hey , sir how i can help you'

   elif "good morning" in user_data:
      text_to_speech.text_to_speech("good morning, sir how i can help you")
      return 'good morning, sir how i can help you'
   
   elif "Good morning" in user_data:
      text_to_speech.text_to_speech("good morning, sir how i can help you")
      return 'good morning, sir how i can help you'
   
   elif "good afternoon" in user_data:
      text_to_speech.text_to_speech("good afternoon, sir how i can help you")
      return 'good afternoon, sir how i can help you'
   
   elif "Good afternoon" in user_data:
      text_to_speech.text_to_speech("good afternoon, sir how i can help you")
      return 'good afternoon, sir how i can help you'
   
   elif "good evening" in user_data:
      text_to_speech.text_to_speech("good evening, sir how i can help you")
      return 'good evening, sir how i can help you'
   
   elif "Good evening" in user_data:
      text_to_speech.text_to_speech("good evening, sir how i can help you")
      return 'good evening, sir how i can help you'
   
   elif "good night" in user_data:
      text_to_speech.text_to_speech("good night, sir how i can help you")
      return 'good night, sir how i can help you'
   
   elif "Good night" in user_data:
      text_to_speech.text_to_speech("good night, sir how i can help you")
      return 'good night, sir how i can help you'
   
   elif "good nights" in user_data:
      text_to_speech.text_to_speech("good nights, sir how i can help you")
      return 'good nights, sir how i can help you'
   
   elif "Good nights" in user_data:
      text_to_speech.text_to_speech("good nights, sir how i can help you")
      return 'good nights, sir how i can help you'

   elif "time now" in user_data:
      current_time = datetime.datetime.now()
      Time = (str)(current_time) + "Hour :" ,(str)(current_time.minute) + "minute"
      text_to_speech.text_to_speech(Time)
      return Time
   
   elif "Time now" in user_data:
      current_time = datetime.datetime.now()
      Time = (str)(current_time) + "Hour :" ,(str)(current_time.minute) + "minute"
      text_to_speech.text_to_speech(Time)
      return Time

   elif "shutdown" in user_data:
      text_to_speech.text_to_speech("ok sir")
      return 'ok sir'

   elif "play music" in user_data:
      webbrowser.open("https://gaana.com/")
      text_to_speech.text_to_speech("gaana.com is ready for you")
      return 'gaana.com is ready for you'
   
#  youtube


   elif "play youtube song in panjabi" in user_data:
      webbrowser.open("https://www.youtube.com/watch?v=bpw9HL6Qi_k&list=RDbpw9HL6Qi_k&start_radio=1")
      text_to_speech.text_to_speech("youtube song is ready for you")
      return "youtube song is ready for you"
   
   elif "play youtube songs in panjabi" in user_data:
      webbrowser.open("https://www.youtube.com/watch?v=bpw9HL6Qi_k&list=RDbpw9HL6Qi_k&start_radio=1")
      text_to_speech.text_to_speech("youtube song is ready for you")
      return "youtube song is ready for you"
   
   elif "play youtube songs in bhojpuri" in user_data:
      webbrowser.open("https://www.youtube.com/watch?v=zmwfd8x0DrM&list=RDEMQnj87XzPaJS_FF0bkmQpkQ&index=3")
      text_to_speech.text_to_speech("youtube song is ready for you")
      return "youtube song is ready for you"

   elif "open youtube" in user_data:
      webbrowser.open("https://youtube.com/")
      text_to_speech.text_to_speech("youtube .com is ready for you")
      return "youtube .com is ready for you"
   
   elif "play youtube" in user_data:
      webbrowser.open("https://youtube.com/")
      text_to_speech.text_to_speech("youtube .com is ready for you")
      return "youtube .com is ready for you"

   elif "open watsapp" in user_data:
      webbrowser.open("https://whatsapp.com/")
      text_to_speech.text_to_speech("watsappp.com is ready for you")
      return "watsapp .com is ready for you"

   elif "open google" in user_data:
      webbrowser.open("https://google.com/")
      text_to_speech.text_to_speech("google.com is ready for you")
      return "google .com is ready for you"

   elif "open Gmail" in user_data:
      webbrowser.open("https://Gmail.com/")
      text_to_speech.text_to_speech("gmail.com is ready for you")
      return "google .com is ready for you"
   
   elif "open google chrome" in user_data:
      webbrowser.open("https://Chrome.com")
      text_to_speech.text_to_speech("google chrome .com is ready for you")
      return "google .com is ready for you"
   
   elif "open maps" in user_data:
      webbrowser.open("https://maps.com/")
      text_to_speech.text_to_speech("maps .com is ready for you")
      return "Maps .com is ready for you"

   elif "open Flipkart" in user_data:
      webbrowser.open("https://Flipkart.com/")
      text_to_speech.text_to_speech("Flipkart .com is ready for you")
      return "Flipkart .com is ready for you"
   
   elif "open flipkart" in user_data:
      webbrowser.open("https://Flipkart.com/")
      text_to_speech.text_to_speech("flipkart .com is ready for you")
      return "flipkart .com is ready for you"
   
   elif "open flipkart" in user_data:
      webbrowser.open("https://Flipkart.com/")
      text_to_speech.text_to_speech("flipkart .com is ready for you")
      return "flipkart .com is ready for you"

   elif "open facebook" in user_data:
      webbrowser.open("https://Facebook.com/")
      text_to_speech.text_to_speech("Facebook .com is ready for you")
      return "facebook .com is ready for you"
   
   elif "open Facebook" in user_data:
      webbrowser.open("https://Facebook.com/")
      text_to_speech.text_to_speech("facebook .com is ready for you")
      return "facebook .com is ready for you"
   
   elif "open Dilkhush's Facebook" in user_data:
      webbrowser.open("https://www.facebook.com/profile.php?id=100080504321936")
      text_to_speech.text_to_speech("facebook .com is ready for you")
      return "facebook .com is ready for you"
   
   elif "open dilkhush Facebook" in user_data:
      webbrowser.open("https://www.facebook.com/profile.php?id=100080504321936")
      text_to_speech.text_to_speech("facebook .com is ready for you")
      return "facebook .com is ready for you"
   
   elif "open Instagram" in user_data:
      webbrowser.open("https://Instagram.com/")
      text_to_speech.text_to_speech("Instagram .com is ready for you")
      return "Instagram .com is ready for you"
   
   elif "open instagram" in user_data:
      webbrowser.open("https://Instagram.com/")
      text_to_speech.text_to_speech("instagram .com is ready for you")
      return "instagram .com is ready for you"
   
   elif "open Dilkhush's instagram" in user_data:
      webbrowser.open("https://www.instagram.com/dilkhush_kumar979/")
      text_to_speech.text_to_speech("instagram .com is ready for you")
      return "instagram .com is ready for you"
   
   elif "open dilkhush instagram" in user_data:
      webbrowser.open("https://www.instagram.com/dilkhush_kumar979/")
      text_to_speech.text_to_speech("instagram .com is ready for you")
      return "instagram .com is ready for you"

   #elif "weather" in user_data:
      #ans = weather.weather()
      #text_to_speech.text_to_speech(ans)
     # return ans

   else:
      text_to_speech.text_to_speech("I' am not able to understan")
      return "I' am not able to understan"
