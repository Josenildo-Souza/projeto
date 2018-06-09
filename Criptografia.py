# -*- coding: utf-8 -*-
"""
Created on Mon May 14 15:25:59 2018
@jls2
"""
dic_elementos = {}
dic_usuario = {}
dic_usuario = {'adm':('adm', '0')}

def recuperar_chaves(arq):
    arquivo = open (arq, 'r')
    linha = arquivo.readline()
    arquivo.close()
    aux = ''
    for c in linha:
        if c != ' ':
            aux += c
        else:
            num1 = int(aux)
            aux = ''
    num2 = int(aux)
    return num1, num2


def criptografar_string(string, e, n):
    codigo = ''
    for x in string:
        y = (ord(x)**e)%n
        codigo += str(y)+'#'
    return codigo


def decifrar_codigo(string, d, n):
    texto = ''
    aux = ''
    for c in string:
        if c != '#' and c != '\n':
            aux += c
        elif c != '\n':
            y = int(aux)
            aux = ''
            x = chr((y**d)%n)
            texto += x
    return texto


def criptografar_usuarios(dic_usuario, arq):
    arquivo = open(arq, "w")
    e, n = recuperar_chaves("chavePublica.txt")
    for chave in dic_usuario:
        arquivo.write(criptografar_string(chave, e, n))
        arquivo.write("\n")
        arquivo.write(criptografar_string(dic_usuario[chave][0], e, n))
        arquivo.write("\n")
        arquivo.write(str(dic_usuario[chave][1]))
        arquivo.write("\n")


def decifrar_usuarios(arq, dic_usuario):
    arquivo = open(arq, "r")
    d, n = recuperar_chaves("chavePrivada.txt")
    linha = arquivo.readline()
    while linha != "":
        chave = decifrar_codigo(linha, d, n)
        linha = arquivo.readline()
        senha = decifrar_codigo(linha, d, n)
        linha = arquivo.readline()
        print(linha)
        acesso = int(linha[0])
        dic_usuario[chave] = (senha, acesso)
        linha = arquivo.readline()
        if linha == "\n":
            linha = arquivo.readline()


def criptografar_elementos(dic_elementos, arq):
    arquivo = open(arq, "w")
    e, n  = recuperar_chaves("chavePublica.txt")
    for chave in dic_elementos:
        arquivo.write(criptografar_string(chave, e, n))
        arquivo.write("\n")
        arquivo.write(criptografar_string(dic_elementos[chave][0], e, n))
        arquivo.write("\n")
        arquivo.write(criptografar_string(dic_elementos[chave][1], e, n))
        arquivo.write("\n")
        arquivo.write(criptografar_string(dic_elementos[chave][2], e, n))
        arquivo.write("\n")
        arquivo.write(criptografar_string(dic_elementos[chave][3], e, n))
        arquivo.write("\n")
        arquivo.write(criptografar_string(dic_elementos[chave][4], e, n))
        arquivo.write("\n")
        arquivo.write(criptografar_string(dic_elementos[chave][5], e, n))
        arquivo.write("\n")
        arquivo.write(criptografar_string(dic_elementos[chave][6], e, n))
        arquivo.write("\n")
    arquivo.close()
     

def descriptografar_elementos(arq, dic_elementos):
    arquivo = open(arq, "r")
    d, n = recuperar_chaves("chavePrivada.txt")
    linha = arquivo.readline()
    while linha != "":
        chave = decifrar_codigo(linha, d, n)
        linha = arquivo.readline()
        nome = decifrar_codigo(linha, d, n)
        linha = arquivo.readline()
        funcao = decifrar_codigo(linha, d, n)
        linha = arquivo.readline()
        data_de_nascimento = decifrar_codigo(linha, d, n)
        linha = arquivo.readline()
        data_de_embarque = decifrar_codigo(linha, d, n)
        linha = arquivo.readline()
        porto_de_referencia = decifrar_codigo(linha, d, n)
        linha = arquivo.readline()
        passaporte = decifrar_codigo(linha, d, n)
        linha = arquivo.readline()
        matricula = decifrar_codigo(linha, d, n)
        dic_elementos[chave]=(nome, funcao, data_de_nascimento, data_de_embarque, porto_de_referencia, passaporte, matricula)
        linha = arquivo.readline()

        if linha == "\n":
            linha = arquivo.readline()
    return dic_elementos




'''
teste = {}
teste["123"]=("maria", "cmt", "23/12/1980", "01/05/2018","Cabo Verde", "fg123645", "123456")
teste["24"] = ("adriano", "1on", "24/04/1990"," 21/01/2017", "itajai", "fg34567", "987654")
criptografar_elementos(teste, 'testando1.txt')
resultado = {}
descriptografar_elementos('testando1.txt', resultado)

teste = {}
teste["adm"]=("adm", "0")
criptografar_usuarios(teste, 'testando.txt')
resultado = {}
decifrar_usuarios('testando.txt', resultado)

descriptografar_elementos("elementos.txt", dic_elementos)
criptografar_usuarios(dic_usuario, "usuarios.txt")
criptografar_elementos(dic_elementos, "elementos.txt")
decifrar_usuarios("Usuarios.txt", dic_usuario)
'''