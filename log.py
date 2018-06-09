# -*- coding: utf-8 -*-
"""
@jls2
"""
def comparar_datas(palavra):
    data_usuario = input("Digite a data :")
    palavra = open("log.txt", "r")
    lista =[]
    string = ""
    linha = palavra.readline()
    while string != "":
        data = recuperar_data(palavra)
        if data == data_usuario:
            lista.append(linha)
        linha = palavra.readline()
    return lista



def comparar_usuarios():
    user = input("Digite o usuario: ")
    palavra = open("log.txt", "r")
    lista_user=[]
    string=""
    linha = palavra.readline()
    while string != "":
        usuario = recuperar_data(palavra)
        if usuario == user:
            lista_user.append(linha)
        linha= palavra.readline()
    return lista_user
    
        
        
def recuperar_data(palavra):
    palavra = open("log.txt", "r")
    data = ""
    for i in reversed(palavra):
        if i != " ":
            data +=i
        else:
            return reversed(data)
        

def recuperar_usuario(palavra):
    palavra = open("log.txt", "r")
    usuario = ""
    for i in palavra:
        if i !=" ":
            usuario +=1
        else:
            return usuario
