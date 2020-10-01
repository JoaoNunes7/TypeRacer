from tkinter import *
import tkinter.font as font
import sys
sys.path.append('/usr/local/lib/python3.6/dist-packages/')
import pyjokes
import time


#JANELA PRINCIPAL
window = Tk()
helv36 = font.Font(family='Helvetica', size=36)
window.title("Type Racer")
window.geometry("1250x800")
window.configure(bg="grey")


def janelaCorrida():
    janela = Toplevel(window)
    janela.title("Corrida")
    janela.configure(bg="grey")
    janela.geometry("1250x800")
    piada = pyjokes.get_joke('en','neutral')
    helv01 = font.Font(family='Helvetica', size=15)
    frase = Label(janela, text=piada, font=helv01)
    frase.place(x=100, y=150)
    textBox = Text(janela, height=1, width=70)
    textBox.place(x=100,y=200)
    textBox.focus()
    botaoSubmit = Button(janela, text="Submeter", width=10, height=1, font=helv01)
    botaoSubmit.place(x=400,y=300)
    texto = textBox.get("1.0","end-1c")
    countador_palavras = len(piada.split())




    #while (texto==0):
     #   t0 = time.time()
      #  if(texto)
       # acc = len(set(texto.split()) & set(piada.split()))
        #tempo = t1-t0
        #palavrasPorMinuto = (countador_palavras/tempo)
        #resultadoTempo = Label(janela, text=tempo, font=helv01)
        #resultadoTempo.place(x=100, y=400)



btnPrincipal=Button(window, text="Jogar", command=janelaCorrida, width=15, height=1, font=helv36)
btnPrincipal.place(x=400, y=300)

mainloop()
