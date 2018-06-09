# -*- coding: utf-8 -*-
"""
Created on Mon May 14 15:25:59 2018

@jls2
"""
#ChavePublica {e,n}
#ChavePrivada {d,n}
import Criptografia as cp
import Usuarios  as us
import elementos as el
import data as dt

dic_usuario={}
dic_elementos={}
dic_usuario["adm"]=("adm", "0")
usuario = ''
try:
    log = open('log.txt', 'a')
except:
    log = open('log.txt', 'w')


def menu_nivel(nivel):
    global usuario
    print("""NIVEIS DE USUARIO:
-----------------
0 - GG =Gerente geral = Super usuario
1 - CMT = COMANDANTE = Gerente
2 - 1ON = 1ºoficial = Tecnico
3 - PON = PRATICANTE OFICIAL DE NAUTICA = Estagiario
""")

        
    if nivel == "3":
        parada = True
        while parada == True:
            print("PON = Estagiario")
                
            opcao = input("""Menu opçoes:
[1]-Buscar Tripulante
[2]-Mostrar Todos Tripulantes
[3]-Menu Principal
[4]-Sair
Escolha a opçao: """)
                
                
            if opcao =="1":
                log.write(usuario+ 'fez uma pesquisa'+ dt.data()+ dt.hora())
                log.write("\n")
                el.buscar_elementos(dic_elementos)
                
            elif opcao == "2":
                log.write(usuario+ 'visualizou todos os elementos'+ dt.data()+ dt.hora())
                log.write("\n")
                el.mostrar_todos_os_elementos(dic_elementos)
           
            elif opcao == "3":
                menu_principal()
                 
            elif opcao == "4":
                menu_sair()
                parada = False
                


    elif nivel == "2":
        parada = True
        while parada:
            print("1ON = Tecnico")
            
            opcao = input("""Menu opçoes:
    [1]-Buscar Tripulante
    [2]-Mostrar Todos Tripulantes
    [3]-Buscar Tripulante por Cargo
    [4]-Cadastrar Tripulante
    [5]-Menu Principal
    [6]-Sair
    Escolha a opçao: """)

                
            if opcao == "1":
                log.write(usuario+ 'fez uma pesquisa'+ dt.data()+ dt.hora())
                log.write("\n")
                el.buscar_elementos(dic_elementos)
                
            elif opcao == "2":
                log.write(usuario+ 'visualizou todos os elementos'+ dt.data()+ dt.hora())
                log.write("\n")
                el.mostrar_todos_os_elementos(dic_elementos)
                
            elif opcao == "3":
                log.write(usuario+ 'Fez uma pesquisa pelo cargo'+ dt.data()+ dt.hora())
                log.write("\n")
                el.buscar_cargo(dic_elementos)
                
            elif opcao == "4":
                log.write(usuario+ 'cadastrou um tripulante'+ dt.data()+ dt.hora())
                log.write("\n")
                el.cadastrar_elementos(dic_elementos)
            
            elif opcao == "5":
                menu_principal()
                
            elif opcao == "6":
                menu_sair()
                parada = False



    elif nivel == "1":
        parada = True
        while parada == True:
            print("CMT = Gerente")
            
            opcao = input("""Menu opçoes:
    [1]-Buscar Tripulante #buscar elementos
    [2]-Mostrar Todos Tripulantes
    [3]-Buscar Tripulante por Cargo #buscar cargo
    [4]-Cadastrar Tripulante
    [5]-Remover Tripulante
    [6]-Atualizar Tripulante
    [7]-Ordenaçao Tripulante
    [8]-Impressão Ordenada
    [9]-Menu Principal
    [10]-Sair
    
    Escolha a opçao: """)
                

            if opcao == "1":
                log.write(usuario+ 'fez uma pesquisa'+ dt.data()+ dt.hora())
                log.write("\n")
                el.buscar_elementos(dic_elementos)
            
            elif opcao == "2":
                log.write(usuario+ 'visualizou todos os elementos'+ dt.data()+ dt.hora())
                log.write("\n")
                el.mostrar_todos_os_elementos(dic_elementos)
                
            elif opcao == "3":
                log.write(usuario+ 'Fez uma pesquisa dos tripulantes pelo cargo'+ dt.data()+ dt.hora())
                log.write("\n")
                el.buscar_cargo(dic_elementos)                
                
            elif opcao == "4":
                log.write(usuario+ 'cadastrou um tripulante'+ dt.data()+ dt.hora())
                log.write("\n")
                el.cadastrar_elementos(dic_elementos)
                
            elif opcao == "5":
                log.write(usuario+ 'Fez remoçao de tripulante'+ dt.data()+ dt.hora())
                log.write("\n")
                el.remover_elementos(dic_elementos)
                
            elif opcao == "6":
                log.write(usuario+ 'Fez atualizaçao de tripulante'+ dt.data()+ dt.hora())
                log.write("\n")
                el.atualizar_elementos(dic_elementos)
                
            elif opcao == "7":
                log.write(usuario+ 'Fez ordenaçao de tripulante pelo cpf'+ dt.data()+ dt.hora())
                log.write("\n")
                el.ordenar_elementos(dic_elementos)
            
            elif opcao == "8":
                log.write(usuario+ 'Fez impressao de tripulante pelo cpf'+ dt.data()+ dt.hora())
                log.write("\n")
                el.impressao_ordenada(dic_elementos)
            
            elif opcao == "9":
                menu_principal()
                
            elif opcao == "10":
                menu_sair()
                parada = False



    elif nivel == "0":
        parada=True
        cp.descriptografar_elementos("elementos.txt", dic_elementos)
        while parada == True:
            
            print("GG = Super usuario")
            opcao = input("""Menu opçoes:
    [1]-Buscar Tripulante
    [2]-Mostrar Todos Tripulantes
    [3]-Buscar Tripulante por Cargo
    [4]-Cadastrar Tripulante
    [5]-Remover Tripulante
    [6]-Atualizar Tripulante
    [7]-Ordenaçao Tripulante
    [8]-Impressão Ordenada
    [9]-Alterar o nivel do usuario
    [10]-Remover Usuario
    [11]-Menu Principal
    [12]-Sair
    Escolha a opçao: """)


            if opcao == "1":
                log.write(usuario+ 'fez uma pesquisa'+ dt.data()+ dt.hora())
                el.buscar_elementos(dic_elementos)
            
            elif opcao == "2":
                log.write(usuario+ 'visualizou todos os elementos'+ dt.data()+ dt.hora())
                el.mostrar_todos_os_elementos(dic_elementos)
                
            elif opcao == "3":
                log.write(usuario+ 'Fez uma pesquisa dos tripulantes pelo cargo'+ dt.data()+ dt.hora())
                el.buscar_cargo(dic_elementos) 
                
            elif opcao == "4":
                log.write(usuario+ 'cadastrou um tripulante'+ dt.data()+ dt.hora())
                el.cadastrar_elementos(dic_elementos)
                
            elif opcao == "5":
                log.write(usuario+ 'Fez remoçao de tripulante'+ dt.data()+ dt.hora())
                el.remover_elementos(dic_elementos)
                
            elif opcao == "6":
                log.write(usuario+ 'Fez atualizaçao de tripulante'+ dt.data()+ dt.hora())
                el.atualizar_elementos(dic_elementos)
                
            elif opcao == "7":
                log.write(usuario+ 'Fez ordenaçao de tripulante pelo cpf'+ dt.data()+ dt.hora())
                el.ordenar_elementos(dic_elementos)
                
            elif opcao == "8":
                log.write(usuario+ 'Fez impressao de tripulante pelo cpf'+ dt.data()+ dt.hora())
                el.impressao_ordenada(dic_elementos)
                
            elif opcao == "9":
                log.write(usuario+ 'Fez alteraçao do nivel de Usuario'+ dt.data()+ dt.hora())
                us.alterar_nivel_usuario(dic_usuario)
                
            elif opcao == "10":
                log.write(usuario+ 'Fez remoçao de Usuario'+ dt.data()+ dt.hora())
                log.write("\n")
                us.remover_usuario(dic_usuario)
            
            elif opcao == "11":
                    usuario = ''
                    menu_principal()
                
            elif opcao == "12":
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
    cp.criptografar_usuarios(dic_usuario, "usuarios.txt")
    cp.criptografar_elementos(dic_elementos, "elementos.txt")
    print("Fechando Programa")


def menu_sair():
    continua=True
    while continua==True:
        entrada=input("Confirma saída do programa? s/n ")

        if entrada=="s":
            sair()
            continua=False
        elif entrada == "n":
            menu_principal()
        else:

            print("Opção inválida! digite s/n ")


def menu_principal():
    print("""MENU DE OPÇAO
[1]=Login
[2]=Cadastro usuario
[3]=Sair
""")
    global usuario
  #  cp.decifrar_usuarios("Usuarios.txt", dic_usuario)
    
    while usuario == "":
        entrada=input("Digite opção: ")

        if entrada=="1":
            user = input("Digite o nome de usuário: ")
            password = input("Digite sua senha: ")
            acesso = login(dic_usuario, user, password)
            print(acesso)
    
        elif entrada == "2":
#            log.write(usuario+ 'Fez alteraçao do nivel de Usuario', dt.data(), dt.hora())
            us.cadastrar_usuario(dic_usuario)
        elif entrada=="3":
            menu_sair()
        else:
            print("Opção inválida!")
    
    return acesso

            
def main():
    nivel = menu_principal()
    menu_nivel(nivel)

main()
log.close()


