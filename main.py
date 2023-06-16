__author__ = "usfx"
import os
from tkinter import *  
import ult.centrar as ult
from tkinter import messagebox
#---creamos ventana -----
main = Tk()
main.geometry("1366x768")
ult.centrar_ventana(main,1366,768)
main.title("El Corral")
main.resizable(0, 0)
#-----funcion salir------ 
def Exit():
    sure = messagebox.askyesno("Salir","¿Seguro que quieres salir?", parent=main)
    if sure == True:
        main.destroy()
        
main.protocol("WM_DELETE_WINDOW", Exit)
#---funvion abrir ventana empleado
def emp():
    main.withdraw()
    os.system("python employee.py")
    main.deiconify()

#---- funcion abrir ventana administrador 
def adm():
    main.withdraw()
    os.system("python admin.py")
    main.deiconify()


#----- importamos el diseño de nuestra ventana -----
label1 = Label(main)
label1.place(relx=0, rely=0, width=1366, height=768)
img = PhotoImage(file="./images/main1.png")
label1.configure(image=img)
 #------le damos un titulo---------
label_title = Label(main, text="INGRESAR", font=("Impact", 40), bg="#ffffff", fg="#d46c91")
label_title.place(relx=0.5, rely=0.2, anchor="center")
#---- creamos un foton con imafen de fondo que es empleados ---
button1 = Button(main)
button1.place(relx=0.316, rely=0.446, width=146, height=130)
button1.configure(relief="flat")
button1.configure(overrelief="flat")
button1.configure(activebackground="#ffffff")
button1.configure(cursor="hand2")
button1.configure(foreground="#ffffff")
button1.configure(background="#ffffff")
button1.configure(borderwidth="0")
img2 = PhotoImage(file="./images/empleado.png")
button1.configure(image=img2)
button1.configure(command=emp)
#---- cremos un texto cajero -----
label2 = Label(text="Cajero", bg="#ffffff",fg="#d46c91",font=("Arial", 15))
label2.place(relx=0.316, rely=0.446 + 0.175, width=146, height=30)
#-----creamos un boton  con imagen  de adminitrador ----
button2 = Button(main)
button2.place(relx=0.566, rely=0.448, width=146, height=130)
button2.configure(relief="flat")
button2.configure(overrelief="flat")
button2.configure(activebackground="#ffffff")
button2.configure(cursor="hand2")
button2.configure(foreground="#ffffff")
button2.configure(background="#ffffff")
button2.configure(borderwidth="0")
img3 = PhotoImage(file="./images/administrador.png")
button2.configure(image=img3)
button2.configure(command=adm)
#---- creamos un texto  administrador --------
label2 = Label(text="Administrador", bg="#ffffff",fg="#d46c91",font=("Arial", 15))
label2.place(relx=0.566, rely=0.446 + 0.175, width=146, height=30)
main.mainloop()
