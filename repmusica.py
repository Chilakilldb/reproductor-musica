from tkinter import * #Importar libreria
raiz=Tk()
import pygame,sys 
from pygame.locals import*
from tkinter import filedialog
from PIL import ImageTk,Image



pygame.init()#Este metodo inicia la libreria pygame
    
def OpenSong():
    Song= filedialog.askopenfilename()
    print(Song)
    pygame.mixer.music.load(Song)

    pass

def PlaySong():
    pygame.mixer.music.play()
    pass

def StopSong():
    pygame.mixer.music.stop()
    pass

def ResumeSong():
    pygame.mixer.music.unpause()
    pass

def PauseSong():
    pygame.mixer.music.pause()
    pass

def VolumUpper():
    nivelVolumen= pygame.mixer.music.get_volume()+0.1
    pygame.mixer.music.set_volume(nivelVolumen)
    
def VolumLower():
    nivelVolumen=pygame.mixer.music.get_volume()-0.1
    pygame.mixer.music.set_volume(nivelVolumen)


raiz.title("Re pro-ductor")
raiz.geometry("1000x500")
raiz.resizable(1,1)

#marco
framePrincipal= Frame(raiz,bg="#1d1d1d",width=600, height=400)
framePrincipal.pack(fil="both", expand=1)


#imagen
im=Image.open("lavaca.jpg")
imRe=im.resize((200,150))
imagen=ImageTk.PhotoImage(imRe)

imlabel=Label(framePrincipal,image=imagen)
imlabel.place(relx=0.4,rely=0.12)


#Titulo reprodeucor
TituloReproductor=Label(framePrincipal,text="Reproductor GUI", font=("Jokerman",20),bg="#4d4d4d",fg="#f4f4f4")# , despues del tamaño de fuente pone una tipografia(negritas, subrayado, etc)
TituloReproductor.pack()

#Boton Open File
BotonOpenFile=Button(framePrincipal,text="Open File",font=("SWGothg",20),bg="#5dc460"
                     ,fg="#1d1d1d",width=8,height=1,bd=0,highlightthickness=0,command=OpenSong)#Command llama la funcion Opensong que pregunta por la direccion de un archivo
BotonOpenFile.place(relx=0.42,rely=0.57)

#BotonPlay
BotonPlay=Button(framePrincipal,text="Play",font=("SWGothg",20),bg="#00ffee"
                     ,fg="#1d1d1d",width=8,height=1,bd=0,highlightthickness=0,command=PlaySong)
BotonPlay.place(relx=0.24,rely=0.65)

#BotonPause
BotonPause=Button(framePrincipal,text="Pause",font=("SWGothg",20),bg="#009985"
                     ,fg="#1d1d1d",width=8,height=1,bd=0,highlightthickness=0,command=PauseSong)
BotonPause.place(relx=0.15,rely=0.5)

#BotonResume
BotonResm=Button(framePrincipal,text="Resume",font=("SWGothg",20),bg="#00ffee"
                     ,fg="#1d1d1d",width=8,height=1,bd=0,highlightthickness=0,command=ResumeSong)
BotonResm.place(relx=0.60,rely=0.65)

#Boton Stop
BotonStop=Button(framePrincipal,text="Stop",font=("SWGothg",20),bg="#009985"
                     ,fg="#1d1d1d",width=8,height=1,bd=0,highlightthickness=0,command=StopSong)
BotonStop.place(relx=0.69,rely=0.5)

#Boton subir Volumen
Botonsv=Button(framePrincipal,text="+",font=("SWGothe",20),bg="#334eaf"
                     ,fg="#1d1d1d",width=8,height=1,bd=0,highlightthickness=0,command=VolumUpper)
Botonsv.place(relx=0.20,rely=0.2)

#Boton bajar Volumen
Botonbv=Button(framePrincipal,text="-",font=("SWGothe",20),bg="#0088ff"
                     ,fg="#1d1d1d",width=8,height=1,bd=0,highlightthickness=0,command=VolumLower)
Botonbv.place(relx=0.65,rely=0.2)




raiz.mainloop()