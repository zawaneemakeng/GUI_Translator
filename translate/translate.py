
from tkinter import *
from tkinter import ttk 
### -------Google Translate---------
from googletrans import Translator
translator = Translator() #สร้างฟังชั่นแปลภาษา
GUI = Tk() #สร้างหน้าต่างหลัก
GUI.geometry('500x350') 
GUI.title('โปรแกรมแปลภาษา by Zawanee')
# -----config-----
GUI.configure(bg='#d9d9d9') 
FONT = ('TH Sarabun New',15)
FONT2 = ('TH Sarabun New',20)
# -----Label------
L = Label(GUI,text='กรุณากรอกคำศัพท์ที่ต้องการแปล',font=FONT2,bg='#d9d9d9',).place(x=130,y=40)

v_vocab = StringVar() 
E1 = ttk.Entry(GUI,textvariable = v_vocab,font=FONT,width=40).place(x=90,y=100)

def Translate():
    vocab = v_vocab.get() 
    meaning = translator.translate(vocab,dest='th')
    print( vocab + ' : ' + meaning.text)
    print( meaning.pronunciation)
    v_result.set(vocab + ' : ' + meaning.text)
    v_vocab.set('') 

B1 = Button(GUI,text=' Translate ',command=Translate,font=FONT,bg='#a11dc2',fg='#ffffff').place(x=210,y=160)
# -----Label------
L1 = Label(GUI,text='คำแปล',font=FONT2,bg='#d9d9d9').place(x=50,y=220)

v_result = StringVar() #กล่องสำหรับเก็บคำแปล
R1 = Label(GUI,textvariable=v_result, font=FONT2, foreground='#a11dc2',bg='#d9d9d9').place(x=80,y=250)


GUI.mainloop()
