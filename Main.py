# -*- coding: utf-8 -*-
"""
Created on Mon May 14 15:25:59 2018

@jls2
"""
#ChavePublica {e,n}
#ChavePrivada {d,n}
#import Criptografia as cp
import Usuarios  as us
import elementos as el
#import data as dt

dic_usuario={}
dic_elementos={}
dic_usuario["adm"]=("adm", "0")
usuario = ''


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
                    menu_sair()
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
                menu_sair()
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
                menu_sair()
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
                us.alterar_nivel_usuario(dic_usuario)
                
            elif opcao == "9":
                us.remover_usuario(dic_usuario)
            
            elif opcao == "10":
                    menu_principal()
                
            elif opcao == "11":
                 menu_sair()
                 parada = False
                
    else:
        print("Esse nivel nao existe , digite um nivel valido!")



def login(dicionario, login, senha):
    global usuario
    if not login in dicionario:
        return -1
    else:
        if dicionario[login][0] == senha:
            usuario = login
            return dicionario[login][1]
        else:
            return -1

              
def sair():
    print("Salvando dados...")#função para atualizar os dados
    print("Fechando Programa")


def menu_sair():
    continua=True
    while continua==True:
        entrada=input("Confirma saída do programa? s/n")

        if entrada=="s":
            sair()
            continua=False
        elif entrada == "n":
            menu_principal()
        else:

            print("Opção inválida! digite s/n")


def menu_principal():
    print("""MENU DE OPÇAO
[1]=Login
[2]=Cadastro usuario
[3]=Sair
""")
    global usuario
    
    while usuario == "":
        entrada=input("Digite opção: ")

        if entrada=="1":
            user = input("Digite o nome de usuário: ")
            password = input("Digite sua senha: ")
            acesso = login(dic_usuario, user, password)
    
        elif entrada == "2":
            us.cadastrar_usuario()
        elif entrada=="3":
            menu_sair()
        else:
            print("Opção inválida!")
    
    return acesso

            
def main():
    nivel = menu_principal()
    menu_nivel(nivel)

main()

'''
cp.criptografar_usuarios(dic_usuario, "usuarios.txt")
cp.decifrar_usuarios("Usuarios.txt", dic_usuario)
cp.criptografar_elementos(dic_elementos, "elementos.txt")
cp.descriptografar_elementos("elementos.txt", dic_elementos)

'''

