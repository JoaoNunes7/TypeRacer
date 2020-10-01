from tkinter import *
import tkinter.font as font
import sys
from tkinter import messagebox

sys.path.append('/usr/local/lib/python3.6/dist-packages/')
import pyjokes
import time

estado = 1
#JANELA PRINCIPAL
window = Tk()
helv36 = font.Font(family='Helvetica', size=36)
window.title("Type Racer")
window.geometry("1250x800")
#window.configure(bg="grey")
imagem = PhotoImage(file = "/home/joao/Documentos/Projetos/ProjetoTypeRacer/keyboard_background.png")
background_label = Label(window, image=imagem)
background_label.place(x=0,y=0,relwidth=1, relheight=1)
def janelaCorrida():
    janela = Toplevel(window)
    janela.title("Corrida")
    janela.geometry("1250x800")
    imagem2 = PhotoImage(file="/home/joao/Documentos/Projetos/ProjetoTypeRacer/keyboard_background.png")
    background_label2 = Label(janela, image=imagem)
    background_label2.place(x=0, y=0, relwidth=1, relheight=1)
    piada = pyjokes.get_joke('en','neutral')
    helv01 = font.Font(family='Helvetica', size=15)
    frase = Label(janela, text=piada, font=helv01)
    frase.place(x=25, y=150)
    stringT = StringVar()
    textBox = Entry(janela, width=100, textvariable=stringT)
    textBox.grid(row=0, column=1)
    textBox.place(x=25,y=200)
    textBox.focus()
    countador_palavras = len(piada.split())
    t0 = time.time()
    botaoSubmit = Button(janela, command=lambda: resultado(janela, stringT,countador_palavras,t0,piada), width=10, height=1, font=helv01, text="Show Result")
    botaoSubmit.place(x=550, y=300)


def resultado(janela, stringT,countador_palavras,t0,piada):
    texto = stringT.get()
    print(texto)
    t1 = time.time()
    acc = len(set(texto.split()) & set(piada.split()))
    acc = (acc/countador_palavras)*100
    acc = round(acc, 2)
    tempo = t1-t0
    tempo = round(tempo, 2)
    palvavrasPM = (countador_palavras/tempo)
    palvavrasPM = round(palvavrasPM, 2)
    messagebox.showinfo(title="Result", message='Acc: '+ str(acc) + '%' +  '\nTempo: ' + str(tempo) + '\nPalavrasPM: '  + str(palvavrasPM))
    global estado
    estado = 0
    if (estado == 0):
        janela.destroy()

btnPrincipal=Button(window, text="Play", command=janelaCorrida, width=15, height=1, font=helv36)
btnPrincipal.place(x=400, y=300)

mainloop()
