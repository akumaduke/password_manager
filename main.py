from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

def passs():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    let_pas = [random.choice(letters) for _ in range(nr_letters)]
    senbol =[ random.choice(symbols) for _ in range(nr_symbols)]
    chif = [ random.choice(numbers) for _ in range (nr_numbers)]
    lis_password= let_pas+ senbol + chif


    random.shuffle(lis_password)
    modpas= "".join(lis_password)
    antre_pas.insert(0 , modpas)
    pyperclip.copy(modpas)





def save():

    Site=antre_sit.get()
    mail= antre_email.get()
    pas= antre_pas.get()
    nouvo_done={
        Site: {
            "email":mail,
            "modpas": pas
        }
    }

    if len(Site)==0 or len(pas)==0 or len(mail)==0:
        messagebox.showinfo(title="erreur", message= " tanpri ranpli tout kaz yo")
    else:
            try:
                with open("modpas.json", "r") as modpas_ou:
                    done=json.load(modpas_ou)

            except FileNotFoundError:
                with open("modpas.json", "w") as modpas_ou:
                    json.dump(nouvo_done, modpas_ou, indent=4)
            else:
                done.update(nouvo_done)

                with open("modpas.json","w") as modpas_ou:
                    json.dump(done, modpas_ou, indent =4)

            finally:
                antre_sit.delete(0 , END)
                antre_email.delete(0,END)
                antre_pas.delete(0, END)



def recherche():
    site_web= antre_sit.get()
    try:
        with open("modpas.json") as modpas_ou:
            done= json.load(modpas_ou)

    except FileNotFoundError:
        messagebox.showinfo(title= "Erreur", message= "ou poko anrejistre site sa")


    else:
        if site_web in done:
            email= done[site_web]["email"]
            modpas= done[site_web]["modpas"]
            messagebox.showinfo(title= site_web, message= f"email :{email} \n modpas: {modpas}")
        else:
            messagebox.showinfo(title= "Erreur", message= "ou pat fin konfigire site sa")



fenet= Tk()
fenet.title("password pam")
fenet.config(padx= 50, pady=50)


penti=Canvas(height= 200, width=200)
logo= PhotoImage(file= "logo.png")
penti.create_image(100, 100, image=logo)
penti.grid(row= 0, column=1)


label_site=Label(text="Site web:")
label_site.grid(row=1, column=0)

label_email=Label(text="Email:")
label_email.grid(row=2, column=0)

label_pass= Label(text= "Password:")
label_pass.grid(row= 3, column=0)


antre_sit=Entry(width =21)
antre_sit.grid(row=1, column=1,)
antre_sit.focus()
antre_email=Entry(width =35)
antre_email.grid(row=2,column=1,columnspan=2)
antre_email.insert(0, "******@gmail.com")
antre_pas= Entry(width =21)
antre_pas.grid(row=3,column=1)


bouton_cheche=Button(text="cheche",width=13,  command= recherche)
bouton_cheche.grid(row=1, column= 2)

bouton_pas=Button(text="jenere on modpas", command= passs)
bouton_pas.grid(row=3, column=2)
bouton_ajoute=Button(text=" ajoute",width=36,command= save)
bouton_ajoute.grid(row=4, column=1,columnspan=2)




fenet.mainloop()

