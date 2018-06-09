# -*- coding: utf-8 -*-
"""
Created on Mon May 14 15:25:59 2018

@jls2
"""
from datetime import date, datetime

def data():
    hoje = date.today()
    dia = hoje.day
    mes = hoje.month
    ano = hoje.year
    
    return (str(dia)+'/'+str(mes)+'/'+str(ano))


def hora():

    agora = datetime.now()
    horas=agora.hour
    minutos=agora.minute
    segundos=agora.second

    return(str(horas)+':'+str(minutos)+':'+str(segundos))


def log():    
    try:
        log = open('log.txt', 'a')
    except FileNotFoundError:
        log = open('log.txt', 'w')
    
    usuario = input("Digite seu login: ")
    
    comando = -1
    while comando != 0:
        comando = int(input("Pesquisa (n1), Adição (n2), Sair(n0): "))
        if comando == 1:
            #codigo da pesquisa
            def exibir_log():
                log = open('logs.txt', 'a')
                texto = log.read()
                lista_log = texto.replit('---')
                lista = []
                for i in lista_log:
                    if i != '' and i != ' ':
                        lista.append(i)
                print(texto)
                print(lista)
            
            log.write(usuario+': realizou uma pesquisa\n')#, data(), hora())
            
        
        elif comando == 2:
            #código da adição
    #        def add_log():
            
            log.write(usuario+': adicinou um novo elemento\n')#, data(), hora())
    #        data()
    #        hora()
        elif comando == 0:
            #código do saída
            log.write(usuario+': fez logout\n')#, data(), hora())
    #        data()
    #       hora()
            log.close()
    