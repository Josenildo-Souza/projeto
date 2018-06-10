# -*- coding: utf-8 -*-
"""
@jls2
"""
import data as dt

#def busca_user():
#pass

def Log(User, acao):
    arquivo = open ("log.txt", "a")
    agr = datetime.date.now()
    arquivo.write("{}: {} as {} {}\n.".format(usuario, acao, dt.hora(), dt.data()))
    arquivo.close()
    

def recuperar_usuario(linha):
    user = ""
    for item in linha:
        if item != ":":
            usuario += item
        else:
            return usuario

def recuperar_data(linha):
    data=""
    for item in linha:
        if item !=" ":
            data = ""
        elif item != " " and item != ".":
            data +=item
        return data


def ler_user(user):
    arquivo = open ("log.txt", "r")
    acao = arquivo.readline()
    lista_acao=[]
    while acao != "":
        if recuperar_usuario(acao) == user:
            lista_acao.append(acao)
        acao = arquivo.readline()
    return lista_acao
            
def ler_data(data):
    arquivo = open("log.txt", "r")    
    acao = arquivo.readline()
    lista_acao=[]
    while acao != "":
        if recuperar_usuario(acao) == data:
            lista_acao.append(acao)
        acao = arquivo.readline()
    return lista_acao



'''
def buscar_log():
    opcao = input("Digite a opção desejada de busca pelo log 1-Data, 2-Usuario ")
    if opcao == "1":
        resultado = comparar_datas()
        print(resultado)
        for linha in resultado:
            print (linha)
    elif opcao == "2":
        resultado = comparar_usuarios()
        print(resultado)
        for linha in resultado:
            print (linha)
    else:
        print("Essa opção nao eh valida!")
        
    
def comparar_datas():
    data_usuario = input("Digite a data (dd/mm/aaaa): ")
    palavra = open("log.txt", "r")
    lista = []
    linha = palavra.readline()
    while linha != "":
        data = recuperar_arquivo_log(linha)
        if str(data_usuario) == str(data):
            lista.append(linha)
        linha = palavra.readline()        
    return lista
   

def comparar_usuarios():
    user = input("Digite o usuario: ")
    palavra = open("log.txt", "r")
    lista_user=[]
    linha = palavra.readline()
    while linha != "":
        usuario = recuperar_arquivo_log(linha)
        if usuario == user:
            lista_user.append(linha)
        linha= palavra.readline()
    return lista_user



def recuperar_arquivo(string):
    arq = open("log.txt", "a")
    agora=datetime.datetime.now()
    for item in arq:
    arquivo.write("{}: {} as {} {}\n".format(usuario, acao()+" "+ dt.hora()+" "+ dt.data())
    arq.close()
    


   
for c in string:
        if c != '#' and c != '\n':
            aux += c
        elif c != '\n':
            y = int(aux)
            aux = ''
            x = chr((y**d)%n)
            texto += x
    return texto


    
def recuperar_data(palavra):
    data = ""
    for i in reversed(palavra):
        if i != " ":
            data +=i
        else:
            return data[-1::-1]

        
    
def recuperar_usuario(palavra):
    palavra = open("log.txt", "r")
    usuario = ""
    for i in palavra:
        if i !=" ":
            usuario +=i
        else:
            return usuario
 '''