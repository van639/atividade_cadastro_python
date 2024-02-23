from tkinter import *
from tkinter.ttk import *
janela = Tk()
porce = ''
def funcao():
    global a
    progresso['value']= progresso['value']+10
    porce = progresso['value']
    if porce < 30:
        resposta = f'{porce}% Você e burro'
    elif 60 > porce > 31:
        resposta = f'{porce}% Seu conhecimento é mediano'
    elif porce > 60:
        resposta = f'{porce}% Você é um genio' 
    else:
        resposta = ''

    a = resposta

def cadastro():
    curso = ''
    if var1.get() == 1:
        curso += 'Python, '
    if var2.get() == 1:
        curso += 'Java, '
    if var3.get() == 1:
        curso += 'C#, '
    if var.get() == 1:
        s = 'Masculino'
    else:
        ''
    if var.get() == 2:
        s ='Feminino'
    unidadeCurso = lista.get(ANCHOR)
    name = nome.get()
    txtCadastro['text']= f'Cadastro realizado {name} do sexo {s} \n cursando: {curso} na unidade de {unidadeCurso}\n seu nivel de conhecimento é {a}'

#Nome
txt = Label(janela, text= 'Qual é seu nome?').pack()
nome = Entry(janela, width=50)
nome.pack()
#Sexo
txt2 = Label(janela, text= 'Qual o sexo?').pack()
var = IntVar()
Rb1 = Radiobutton(janela, text='Masculino', variable=var, value=1)
Rb1.pack()
Rb2 = Radiobutton(janela, text='Feminino', variable=var, value=2)
Rb2.pack()
#Estado
etq2 = Label(janela, text="Qual unidade do curso?").pack()
frame = Frame(janela)
scrollbar = Scrollbar(frame, orient=VERTICAL)
lista=Listbox(frame,width=20, height=5, yscrollcommand=scrollbar.set)
scrollbar.config(command= lista.yview)
scrollbar.pack(side=RIGHT, fill=Y)
frame.pack()
lista.pack()
minhalista = ['São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Alagoas', "Amazonas", "Roraima", 'Acre']
for item in minhalista:
    lista.insert(END, item)
#Curso
etq3 = Label(janela, text='Qual curso?')
var1 = IntVar()
Checkbutton(janela, text='Python', variable=var1).pack()
var2 = IntVar()
Checkbutton(janela, text='Java', variable=var2).pack()
var3 = IntVar()
Checkbutton(janela, text='C#', variable=var3).pack()

etq4 = Label(janela, text='Qual o seu nivel de conhecimento na area? ').pack()
progresso = Progressbar(janela, length= 300, value= 0 )
progresso.pack()
btnProgresso = Button(janela, text='Avanço', command=funcao).pack()
btn = Button(janela, text='cadastrar', command=cadastro).pack()
txtCadastro = Label(janela, text = '')
txtCadastro.pack()
janela.geometry('500x500+50+10')
janela.mainloop()