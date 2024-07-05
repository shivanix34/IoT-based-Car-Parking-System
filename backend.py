import pyrebase
import qrcode
import kivy
from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.core.image import Image
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager , Screen
import time
config = {
  'apiKey': "give-api-key",
  'authDomain': "xyz.firebaseapp.com",
  'databaseURL':'https://url.firebaseio.com',
  'projectId': "carparking",
  'storageBucket': "carparking.appspot.com",
  'messagingSenderId': "messenger id",
  'appId': "give id",
  'measurementId': "D9VEL93T2C"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
Window.size=(500,700)
class Booking(Screen):
    def on_kv_post(self, obj):
        call1=db.child('parking').get()
        l=[]
        try:
            for i in call1.each():
                c=i.key()
                l.append(c)
                call12=db.child('parking').child(c).get()
                layout = GridLayout(cols=2, rows=len(l))
                for j in call12.each():
                    if j.key()=="name":
                        c1=j.val()
                        button=Button(text=c1,size_hint_y=None,height=100,background_color =(215/255, 191/255, 224/255,0.5),font_size=22,bold=True)
                        button.bind(on_release=self.button_pressed)
                        button.bind(on_release=self.button_pressed_once)
                        self.ids.gd.add_widget(button)
        except:
            print("none")
    def button_pressed(self,button):
        o=open("id.txt",'w')
        o.write(button.text)
        o.close()
    def button_pressed_once(self,instance):
        app = App.get_running_app()
        app.root.current = "slot"
    pass
class Slot(Screen):
    def available(self):
        parkid=""
        ope=open("id.txt",'r')
        a=ope.readlines()
        a1=a[0]
        call=db.child('parking').get()
        for i in call.each():
            key=i.key()
            call1=db.child('parking').child(key).get()
            for j in call1.each():
                if j.val()==a1:
                    parkid=parkid+i.key()
        call12=db.child('parking').child(parkid).child('available').get()
        ope.close()
        ope=open("id.txt",'w')
        ope.write(parkid)
        ope.close()
        l=[]
        lav=[]
        for k in call12.each():
            l.append(k.key()+" "+str(k.val()))
        for k1 in l:
            av=k1.split()
            if int(av[1])==1:
                lav.append(av[0])
        try:
            self.ids.availabletext.text=str(len(lav))
            for buto in lav:
                button1=Button(text=buto,size_hint_y=None,height=100,background_color =(215/255, 191/255, 224/255,0.5),font_size=22,bold=True)
                button1.bind(on_release=self.GenerateQR)
                button1.bind(on_release=self.GenerateQR1)
                self.ids.availablelist.add_widget(button1)
        except:
            self.ids.availabletext.text="0"


    def GenerateQR1(self,button1):
        op=open("id.txt",'r')
        op1=open("user.txt",'r')
        n=button1.text+" "+str(op.read())+" "+str(op1.read())+" "+str(0)
        op.close()
        op1.close()
        op12=open("QR.txt",'w')
        op12.write(n)
        op12.close()
        op123=open("id.txt",'r')
        db.child("parking").child(op123.read()).child("available").update({button1.text:0})


    def GenerateQR(self,instance):
        app = App.get_running_app()
        app.root.current = "qrgeneration"
        pass
class Login(Screen):
    def presslog(self):
        a=self.ids.lnuminp.text +" "+self.ids.lpassinp.text
        print(a)
        op=open("user.txt",'w')
        op.write(self.ids.lnuminp.text)
        op.close()
        self.ids.lnuminp.text=""
        self.ids.lpassinp.text=""
        db.child('user').push(a)

    pass
class QRgenerate(Screen):

    def generate(self):
        o123 = open("QR.txt", 'r')
        img = qrcode.make(o123.read())
        img.save("qr.png")
        time.sleep(1)
        self.ids.img.source="qr.png"
        time.sleep(1)
        self.ids.generate.disabled = True
        self.ids.refresh.disabled = False
    def generate1(self):
        o123 = open("QR.txt", 'r')
        img = qrcode.make(o123.read())
        o123.close()
        img.save("qr1.png")
        time.sleep(1)
        self.ids.img.source = "qr1.png"
        time.sleep(1)
        self.ids.generate.disabled = True
        self.ids.refresh.disabled = True



    pass
class WindowManager(ScreenManager):
    pass
kv=Builder.load_file('smartcar.kv')

class SmartCarApp(App):
  def build(self):
    #Builder.load_file('smartcar.kv')
    Window.clearcolor=1,1,1,1
    return kv

if _name=='main_':
    SmartCarApp().run()
