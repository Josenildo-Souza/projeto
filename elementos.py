# -*- coding: utf-8 -*-
"""
Created on Mon May 14 15:25:59 2018

@jls2
"""
#import Criptografia as cp

dic_elementos = {}



def cadastrar_elementos(dic_elementos):
    cpf = input("Digite o CPF do Tripulante: ")
    if cpf in dic_elementos:
            print("Esse CPF ja esta Cadastrado!")

    else:
        nome = input("Digite o nome do tripulante: ")
        funcao = input("Digite o cargo(Função) do tirpulante: ")
        data_de_nascimento = input("Digite a data de nascimento do tripulante: ")
        data_de_embarque = input("Digite a data de embarque: ")
        porto_de_referencia = input("Digite o porto de Referencia do tripulante: ")
        passaporte = input("Digite o nº do passaporte: ")
        matricula = input("Digite o nº da matricula: ")
        print("Tripulante Cadastrado com Sucesso!")
        dic_elementos[cpf]=(nome, funcao, data_de_nascimento, data_de_embarque, porto_de_referencia, passaporte, matricula)


def buscar_elementos(dic_elementos):
    continua = True
    while continua == True:
        elemento_buscado = input("Digite o cpf do tripulante: ")

        if elemento_buscado in dic_elementos:
            print(dic_elementos[elemento_buscado])
#            loog = login + str(data()) + 'Busca de tripulante efetuada'
#            log(loog)
            escolha = input("Deseja outro Tripulante? (s/n) ")
            if escolha == "s":
                continua = True
            else:
                continua = False
        else:
            print("Tripulante nao encontrado em nosso banco de dados!")
            escolha1 = input("Deseja buscar outro Tripulante? s/n ")
            if escolha1 == "s":
                continua = True
            else:
                continua = False



def buscar_cargo(dic_elementos):
    continua = True
    while continua == True:
        resultados = []
        cargo_buscado = input("Digite o cargo do tripulante: ")
        continua = False
        for cpf in dic_elementos:
            if dic_elementos[cpf][1] == cargo_buscado:
                resultados.append(dic_elementos[cpf])
        if len(resultados)== 0:
            print("Nenhum Tripulante com esse cargo")
            entrada = input("Deseja buscar outro Tripulante? (s/n) ")
            if entrada == "s":
                continua = True
            else:
                continua = False
            
    
        else:
            for i in resultados:
                print(i)                
        

def remover_elementos(dic_elementos):
    continua = True
    while continua == True:
        cpf = input("Digite o cpf que deseja para remover o Tripulante: ")
        if cpf in dic_elementos:
            dic_elementos.pop(cpf)
            print("Tripulante Removido com Sucesso!")
            continua = False
    
        else:
            entrada=input("Tripulante nao encontrado, deseja buscar outro?(s/n) ")
            if entrada=="s":
                continua=True
            elif entrada=="n":
                continua=False
                    

def atualizar_elementos(dic_elementos):
    continua = True
    while continua == True:
        cpf = input("Digite o cpf do Tripulante que vc quer atualizar: ")
        if cpf in dic_elementos:
            dic_elementos.pop(cpf)
            cadastrar_elementos(dic_elementos)
            print("Tripulante Atualizado com Sucesso!")
            continua = False
        else:
            continuar=input("Tripulante nao encontrado, deseja buscar outro?(s/n) ")
            if continuar=="s":
                continua=True
            elif continuar=="n":
                continua=False


def mostrar_todos_os_elementos(dic_elementos):
    
    if len(dic_elementos)==0:
        print("O dicionario de Tripulantes está vazio!")
    else:
        for chave in dic_elementos:
            print(dic_elementos[chave])
            

###########################################
def ordenar_elementos(dic_elementos):
    lista = []
    for chave in dic_elementos:
        lista.append(chave)
    lista.sort()
    return lista

       
def impressao_ordenada(dic_elementos):
    arq = open("impressao.txt", "w")
    lista = ordenar_elementos(dic_elementos)
    for chave in lista:
        arq.write(chave+':\n')
        arq.write("Nome: "+ dic_elementos[chave][0]+"\n")
        arq.write("Função: "+ dic_elementos[chave][1]+"\n")
        arq.write("Data de Nascimento: "+ dic_elementos[chave][2]+"\n")
        arq.write("Data de Embarque: "+ dic_elementos[chave][3]+"\n")
        arq.write("Porto de Referencia: "+ dic_elementos[chave][4]+"\n")
        arq.write("Passaporte: "+ dic_elementos[chave][5]+"\n")
        arq.write("Matricula: "+ dic_elementos[chave][6]+"\n\n")
    arq.close()
  
        