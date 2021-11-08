from tkinter import *
from cypher import encrypt, decrypt


ekran = Tk()
ekran.title("Tito Cypher")
ekran.minsize(width=800,height=400)


def rezultat(rezultat_poruka="Hello World"):
    rezultat = Text(height=1, borderwidth=0)
    rezultat.insert(1.0, rezultat_poruka)
    rezultat.place(x=20, y = 100)
    rezultat.configure(state="disabled")
    rezultat.configure(inactiveselectbackground=rezultat.cget("selectbackground"))


def klik_sifriraj(kljuc,poruka):
    rezultat_poruka = encrypt(kljuc,poruka)
    rezultat(rezultat_poruka)
def klik_desifriraj(kljuc,poruka):
    #uputa1.config(text="OZMA uvijek dozna")
    rezultat_poruka = decrypt(kljuc,poruka)
    rezultat(rezultat_poruka)


uputa1 = Label(text="Unesi Ključ")#,font=("Arial",12,"italic"))
uputa1.pack(side="left", anchor="nw")
kljuc = Entry()
kljuc.pack(side="top", anchor="nw")
uputa2 = Label(text="Unesi Poruku")
uputa2.place(x=0, y=60)
poruka = Entry(width=100)
poruka.place(x=80, y=60)


sifriraj = Button(text="Šifriraj", command=lambda: klik_sifriraj(kljuc=kljuc.get(),poruka=poruka.get()))
sifriraj.place(x=20,y=350)
desifriraj = Button(text="Dešifriraj", command=lambda: klik_desifriraj(kljuc=kljuc.get(),poruka=poruka.get()))
desifriraj.place(x=720, y=350)





ekran.mainloop()