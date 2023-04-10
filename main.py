from tkinter import *

# Função para lidar com o evento de clique no botão
def obter_signo():
    data = entry_data.get()
    # Extrair o dia e o mês da data informada
    dia = int(data[0:2])
    mes = int(data[3:5])

    # Dicionário com os intervalos de datas dos signos
    signos = {
        "Áries": [(3, 21), (4, 20)],
        "Touro": [(4, 21), (5, 20)],
        "Gêmeos": [(5, 21), (6, 20)],
        "Câncer": [(6, 21), (7, 22)],
        "Leão": [(7, 23), (8, 22)],
        "Virgem": [(8, 23), (9, 22)],
        "Libra": [(9, 23), (10, 22)],
        "Escorpião": [(10, 23), (11, 21)],
        "Sagitário": [(11, 22), (12, 21)],
        "Capricórnio": [(12, 22), (1, 20)],
        "Aquário": [(1, 21), (2, 19)],
        "Peixes": [(2, 20), (3, 20)]
    }

    # Verificar a data em relação aos intervalos de datas dos signos
    for signo, intervalo in signos.items():
        if (mes == intervalo[0][0] and dia >= intervalo[0][1]) or \
           (mes == intervalo[1][0] and dia <= intervalo[1][1]):
            resultado.configure(text=f"Seu signo é: {signo}")
            return

    resultado.configure(text="Data inválida ou não corresponde a um signo.")

# Função para formatar a data automaticamente enquanto o usuário digita
def formatar_data(*args):
    entrada = entry_data.get()
    entrada = entrada.replace('/', '')  # Remover todas as barras de data atuais
    tamanho = len(entrada)
    if tamanho >= 2:
        entrada = entrada[:2] + '/' + entrada[2:]  # Inserir barra após o dia
    if tamanho >= 4:
        entrada = entrada[:5] + '/' + entrada[5:]  # Inserir barra após o mês
    if tamanho > 8:
        entrada = entrada[:8]  # Limitar o tamanho da entrada em 8 caracteres
    entry_data.delete(0, END)
    entry_data.insert(0, entrada)

# Criação da janela
janela1 = Tk()
janela1.title("Descubra o seu signo")
janela1.geometry('400x100')


# Criação da caixa de entrada para a data
entry_data = Entry(janela1)
entry_data.pack()

# Chamar a função de formatação de data quando ocorrerem eventos de entrada na caixa de entrada
entry_data.bind("<KeyRelease>", formatar_data)

# Criação do botão para obter o signo
botao_ok = Button(janela1, text="Obter Signo", command=obter_signo)
botao_ok.pack()

# Criação do rótulo para exibir o resultado
resultado = Label(janela1, text="")
resultado.pack()

janela1.mainloop()
