import tkinter as tk
from tkinter import ttk
import crud as crud

class PrincipalBD:
    def __init__(self, win):
        self.objBD = crud.AppBD()
        self.lblCodigo=tk.Label(win, text="Código do Produto: ")
        self.lblNome=tk.Label(win, text="Nome do produto: ")
        self.lblPreco=tk.Label(win, text="Preço: ")

        self.txtCodigo=tk.Entry(bd=3)
        self.txtNome=tk.Entry()
        self.txtPreco=tk.Entry()
        self.btnCadastrar=tk.Button(win, text='Cadastrar', command=self.fCadastrarProduto)
        self.btnAtualizar=tk.Button(win, text='Atualizar', command=self.fAtualizarProduto)
        self.btnExcluir=tk.Button(win, text='Excluir', command=self.fExcluirProduto)
        self.btnLimpar=tk.Button(win, text='Limpar', command=self.fLimparTela)

        self.dadosColunas = ("Código", "Nome", "Preço")
        self.treeProdutos = ttk.Treeview(win, columns=self.dadosColunas, selectmode='browse')
        self.verscrlbar = ttk.Scrollbar(win, orient="vertical", command=self.treeProdutos.yview)
        self.verscrlbar.pack(side='right', fill='x')
        self.treeProdutos.configure(yscrollcommand=self.verscrlbar.set)
        self.treeProdutos.heading("Código",text="Código")
        self.treeProdutos.heading("Nome",text="Nome")
        self.treeProdutos.heading("Preço",text="Preço")

        self.treeProdutos.column("Código",minwidth=0, width=100)
        self.treeProdutos.column("Nome",minwidth=0, width=100)
        self.treeProdutos.column("Preço",minwidth=0, width=100)

        self.treeProdutos.pack(padx=10, pady=10)
        self.treeProdutos.bind("<<TreeviewSelect>>", self.apresentarRegistrosSelecionados)

        self.lblCodigo.place(x=100,y=50)
        self.txtCodigo.place(x=250,y=50)

        self.lblNome.place(x=100,y=100)
        self.txtNome.place(x=250,y=100)

        self.lblPreco.place(x=100,y=150)
        self.txtPreco.place(x=250,y=150)

        self.btnCadastrar.place(x=100,y=200)
        self.btnAtualizar.place(x=200,y=200)
        self.btnExcluir.place(x=300,y=200)
        self.btnLimpar.place(x=400,y=200)

        self.treeProdutos.place(x=100,y=300)
        self.verscrlbar.place(x=805,y=300,height=225)
        self.carregarDadosIniciais()

    def apresentarRegistrosSelecionados(self, event):
        self.fLimparTela()
        for selection in self.treeProdutos.selection():
            item = self.treeProdutos.item(selection)
            codigo, nome, preco = item["values"][0:3]
            self.txtCodigo.insert(0, codigo)
            self.txtNome.insert(0, nome)
            self.txtPreco.insert(0, preco)

    def carregarDadosIniciais(self):
        try:
            self.id = 0
            self.iid = 0
            registros = self.objBD.selecionarDados()
            print("********** DADOS DISPONÍVEIS NO BD ***********")
            for item in registros:
                codigo = item[0]
                nome = item[1]
                preco = item[2]
                print("Código = ", codigo)
                print("Nome = ", nome)
                print("Preço = ", preco, "\n")

                self.treeProdutos.insert('', 'end', iid=self.iid, values=(codigo,nome,preco))
                self.iid = self.iid + 1
                self.id = self.id + 1
                print('Dados da base')
        except:
            print("Não existem dados para carregar")

    def fLerCampos(self):
        try:
            print("************ DADOS DISPONÍVEIS *************")
            codigo = int(self.txtCodigo.get())
            print("Código", codigo)
            nome = self.txtNome.get()
            print("Nome", nome)
            preco = float(self.txtPreco.get())
            print('Preço', preco)
            print("Leitura dos dados feita")
        except:
            print("Não foi possível ler os dados")
        return codigo, nome, preco

    def fCadastrarProduto(self):
        try:
            print("********* DADOS DISPONÍVEIS ************")
            codigo, nome, preco = self.fLerCampos()
            self.objBD.inserirDados(codigo, nome, preco)
            self.treeProdutos.insert('', 'end', iid=self.iid, values=(codigo, nome, preco))
            self.iid = self.iid + 1
            self.id = self.id + 1
            self.fLimparTela()
            print("Produto Cadastrado")
        except:
            print("Não foi possível cadastrar o produto")

    def fAtualizarProduto(self):
        try:
            print("********* DADOS DISPONÍVEIS ************")
            codigo, nome, preco = self.fLerCampos()
            self.objBD.atualizarDadosDados(codigo, nome, preco)
            self.treeProdutos.delete(*self.treeProdutos.get_children())
            self.carregarDadosIniciais()
            self.fLimparTela()
            print("Produto atualizado")
        except:
            print("Não foi possível atualizar o produto")

    def fExcluirProduto(self):
        try:
            print("********* DADOS DISPONÍVEIS ************")
            codigo, nome, preco = self.fLerCampos()
            self.objBD.excluirDadosDados(codigo, nome, preco)
            self.treeProdutos.delete(*self.treeProdutos.get_children())
            self.carregarDadosIniciais()
            self.fLimparTela()
            print("Produto excluído")
        except:
            print("Não foi possível excluir o produto")

    def fLimparTela(self):
        try:
            print("********* DADOS DISPONÍVEIS ************")
            self.txtCodigo.delete(0, tk.END)
            self.txtNome.delete(0, tk.END)
            self.txtPreco.delete(0, tk.END)
            print("Campos limpos")
        except:
            print("Não foi possível limpar os campos")

janela = tk.Tk()
principal = PrincipalBD(janela)
janela.title("Aplicação CRUD")
janela.geometry("820x600+10+10")
janela.mainloop()