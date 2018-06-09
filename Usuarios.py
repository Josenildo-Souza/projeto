# -*- coding: utf-8 -*-
"""
Created on Mon May 14 15:25:59 2018

@jls2
"""
#import elementos as el
dic_usuario = {}
dic_usuario["adm"]=("adm", "0")
dic_elementos ={}

'''
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
                   
                

def menu_nivel(nivel):
    print("""NIVEIS DE USUARIO:
-----------------
0 - GG =Gerente geral = Super usuario
1 - CMT = COMANDANTE = Gerente
2 - 1ON = 1ºoficial = Tecnico
3 - PON = PRATICANTE OFICIAL DE NAUTICA = Estagiario
""")

        
    if nivel == "3":
#        dic_usuario = cp.decifrar_usuario()
#        if dic_usuario[login][1] == "3":
            parada = True
            while parada == True:
                print("PON")
                
                opcao = input("""Menu opçoes:
    [1]-Buscar Tripulante
    [2]-Mostrar Todos Tripulantes
    [3]-Menu Principal
    [4]-Sair
    Escolha a opçao: """)
                    
                if opcao =="1":
                    el.buscar_elementos(dic_elementos)
                    
                elif opcao == "2":
                    el.mostrar_todos_os_elementos(dic_elementos)
               
                elif opcao == "3":
                    menu_principal()
                     
                elif opcao == "4":
                    sair()
                    parada = False
                


    elif nivel == "2":
        parada = True
        while parada:
            print("1ON")
            
            opcao = input("""Menu opçoes:
    [1]-Buscar Tripulante
    [2]-Mostrar Todos Tripulantes
    [3]-Buscar Tripulante por Cargo
    [4]-Cadastrar Tripulante
    [5]-Menu Principal
    [6]-Sair
    Escolha a opçao: """)

                
            if opcao == "1":
                el.buscar_elementos(dic_elementos)
                
            elif opcao == "2":
                el.mostrar_todos_os_elementos(dic_elementos)
                
            elif opcao == "3":
                el.buscar_cargo(dic_elementos)
                
            elif opcao == "4":
                el.cadastrar_elementos(dic_elementos)
            
            elif opcao == "5":
                menu_principal()
                
            elif opcao == "6":
                sair()
                parada = False



    elif nivel == "1":
        parada = True
        while parada == True:
            print("CMT")
            
            opcao = input("""Menu opçoes:
    [1]-Buscar Tripulante #buscar elementos
    [2]-Mostrar Todos Tripulantes
    [3]-Buscar Tripulante por Cargo #buscar cargo
    [4]-Cadastrar Tripulante
    [5]-Remover Tripulante
    [6]-Atualizar Tripulante
    [7]-Ordenaçao Tripulante
    [8]-Menu Principal
    [9]-Sair
    
    Escolha a opçao: """)

            if opcao == "1":
                el.buscar_elementos(dic_elementos)
            
            elif opcao == "2":
                el.mostrar_todos_os_elementos(dic_elementos)
                
            elif opcao == "3":
                el.buscar_cargo(dic_elementos)                
                
            elif opcao == "4":
                el.cadastrar_elementos(dic_elementos)
                
            elif opcao == "5":
                el.remover_elementos(dic_elementos)
                
            elif opcao == "6":
                el.atualizar_elementos(dic_elementos)
                
            elif opcao == "7":
                el.ordenar_elementos(dic_elementos)
            
            elif opcao == "8":
                menu_principal()
                
            elif opcao == "9":
                sair()
                parada = False



    elif nivel == "0":
        parada=True
        while parada == True:
            
            print("Super usuario")
            opcao = input("""Menu opçoes:
    [1]-Buscar Tripulante
    [2]-Mostrar Todos Tripulantes
    [3]-Buscar Tripulante por Cargo
    [4]-Cadastrar Tripulante
    [5]-Remover Tripulante
    [6]-Atualizar Tripulante
    [7]-Ordenaçao Tripulante
    [8]-Alterar o nivel do usuario
    [9]-Remover Usuario
    [10]-Menu Principal
    [11]-Sair
    Escolha a opçao: """)


            if opcao == "1":
                el.buscar_elementos(dic_elementos)
            
            elif opcao == "2":
                el.mostrar_todos_os_elementos(dic_elementos)
                
            elif opcao == "3":
                el.buscar_cargo(dic_elementos) 
                
            elif opcao == "4":
                el.cadastrar_elementos(dic_elementos)
                
            elif opcao == "5":
                el.remover_elementos(dic_elementos)
                
            elif opcao == "6":
                el.atualizar_elementos(dic_elementos)
                
            elif opcao == "7":
                el.ordenar_elementos(dic_elementos)
                
            elif opcao == "8":
                el.alterar_nivel_usuario(dic_usuario)
                
            elif opcao == "9":
                el.remover_usuario(dic_usuario)
            
            elif opcao == "10":
                    menu_principal()
                
            elif opcao == "11":
                 sair()
                 parada = False
                
    else:
        print("Esse nivel nao existe , digite um nivel valido!")

'''

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