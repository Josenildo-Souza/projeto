# -*- coding: utf-8 -*-
"""
Created on Mon May 14 15:25:59 2018

@jls2
"""
dic_elementos ={}
dic_usuario = {}
dic_usuario["adm"]=("adm", "0")


def cadastrar_usuario(dic_usuario):
    continua = True
    while continua == True:
        login = input("Digite o Login: ")
                
        if login in dic_usuario:

            print("Usuario ja cadastrado!")
            continua = False
            

        else:
           senha = input("Digite a senha: ")
           nivel_usuario = "3"
           print("Usuario Cadastrado com Sucesso!")
           dic_usuario[login]=(senha, nivel_usuario)
           continua = False

def remover_usuario(dic_usuario):
    login=input("Digite o login que deseja remover: ")
    continua = True
    while continua == True:
        if login in dic_usuario:
            dic_usuario.pop(login)
            print("Login: ",login,"removido!")
            continua = False 
                
        else:
            entrada=input("Usuario nao encontrado, deseja buscar outro?(s/n) ")
            if entrada=="s":
                continua=True
            elif entrada=="n":
                continua=False



def alterar_nivel_usuario():
    login = input("Digite o login que deseja modificar: ")
    continua = True
    while continua == True:
        if login in dic_usuario:           
            print("Login Localizado!")
            novo_nivel = input("Digite o novo nivel do usuario"+login+":")
            dic_usuario[login] = (dic_usuario[login][0], novo_nivel)
            continua = False
       
        else:
            entrada=input("Usuario nao encontrado, deseja buscar outro?(s/n) ")
            if entrada=="s":
                continua=True
            elif entrada=="n":
                continua=False