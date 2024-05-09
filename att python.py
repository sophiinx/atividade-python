from tkinter import *

janela = Tk()
janela.title("Contador de Calorias")
janela.geometry('400x400')

refeicoes = []

def adicionar_refeicao():
  refeicao = refeicao_entry.get()
  calorias = calorias_entry.get()
  refeicoes.append((refeicao, int (calorias)))
  resultado_Label.config(text= "Refeição: " + refeicao +
"\nCalorias: " + calorias)
def calcular_total_calorias():
  total_calorias = sum(calorias for _, calorias in refeicoes)
  resultado_Label.config(text="Total de Calorias: " + str(total_calorias))

refeicao_label = Label (janela, text="Refeição: ", width=10)
refeicao_label.grid(column=0, row=0,padx=10, pady=10)                      
refeicao_entry = Entry(janela, bg='grey', width=20)
refeicao_entry.grid(column=1,row=0, padx=10, pady=10)

calorias_Label= Label(janela, text="Calorias: ", width=10)
calorias_Label.grid(column=0, row=1,padx=10, pady=10)
calorias_entry = Entry(janela, bg='grey', width=20)
calorias_entry.grid(column=1, row=1, padx=10, pady=10)

  
adicionar_botao = Button(janela, text="Adicionar", command= adicionar_refeicao)
adicionar_botao.grid(column=1,row=2, padx=10, pady=10)

calcular_botao= Button(janela, text="Calcular Total de calorias", command=calcular_total_calorias) 
calcular_botao.grid(column=1,row=5, padx=10, pady=10)


resultado_Label = Label(janela,text="", width=40)
resultado_Label.grid(column=0, row=4, columnspan=3, padx=10, pady=10)

janela.mainloop()