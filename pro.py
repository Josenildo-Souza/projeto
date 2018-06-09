dic_elementos = {}
dic_usuario = {}
dic_usuario["adm"]=("adm", "0")


def recuperar_chaves(arq):
    arquivo = open (arq, "r")
    linha = arquivo.readline()
    arquivo.close()
    aux = ""
    for c in linha:
        if c != " ":
            aux += c
        else:
            num1 = int(aux)
            aux = ""
    num2 = int(aux)
    return num1, num2


def criptografar_string(string, e, n):
    codigo = ""
    for x in string:
        y = (ord(x)**e)%n
        codigo += str(y)+"#"
    return codigo


def decifrar_codigo(string, d, n):
    texto = ""
    aux = ""
    for c in string:
        if c != "#" and c != "\n":
            aux += c
        elif c != "\n":
            y = int(aux)
            aux = ""
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
        arquivo.write("---")
        arquivo.close()
     

def descriptografar_elementos(arq, dic_elemntos):
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

        if linha == "\n":
            linha = arquivo.readline()
    return dic_elementos


def cadastrar_elementos(dic_elementos):
    cpf = input("Digite o cpf do tripulante: ")
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
            escolha = input("Deseja outro Tripulante? s/n")
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
#    continua = True
#    while continua == True:
    resultados = []
    cargo_buscado = input("Digite o cargo do tripulante: ")
    
    for cpf in dic_elementos:
        if dic_elementos[cpf][1] == cargo_buscado:
            resultados.append(dic_elementos[cpf])
    if len(resultados)== 0:
        print("Nenhum tripulante com esse cargo")

    else:
        for i in resultados:
            print(i)
                    

def remover_elementos(dic_elementos):
    continua = True
    while continua == True:
        cpf = input("Digite o cpf que deseja para remover o tripulante: ")
        if cpf in dic_elementos:
            dic_elementos.pop(cpf)
            print("Elemento Removido com Sucesso!")
            continua = False
    
        else:
            continuar=input("Usuario nao encontrado, deseja buscar outro?(s/n) ")
            if continuar=="s":
                continua=True
            elif continuar=="n":
                continua=False
                    

def atualizar_elementos(dic_elementos):
    continua = True
    while continua == True:
        cpf = input("Digite o cpf do usuario que vc quer atualizar: ")
        if cpf in dic_elementos:
            dic_elementos.pop(cpf)
            cadastrar_elementos(dic_elementos)
            print("Tripulante Atualizado com Sucesso!")
            continua = False
        else:
            continuar=input("Usuario nao encontrado, deseja buscar outro?(s/n) ")
            if continuar=="s":
                continua=True
            elif continuar=="n":
                continua=False


def mostrar_todos_os_elementos(dic_elementos):
    
    if len(dic_elementos)==0:
        print("O dicionario de Elementos está vazio!")
    else:
        for chave in dic_elementos:
            print(dic_elementos[chave])


#def ordenar_elementos(dic_elementos):

#    print('Exibindo tripulantes Ordenados:')
#    for chave in sorted(dic_elementos):
#        print ("%s: %s" % (chave, dic_elementos[chave]))


def ordenar_elementos(dic_elementos):
    lista_ordenada = list(dic_lelementos.keys())
    lista_ordenada.sort
    for chave in lista_ordenada:
        print(chave, "=", dic_elementos[key])
    

    
#    if len(dic_elementos) <= 1:
#        valor = dic_elementos

#    else:
#        for chave in dic_elemntos:
#            for chave in range(0, len(dic_elementos)-1):
            
        

'''
def ordenar_elementos(dic_elementos):
    #ordenar o cpf
    lista_ordem = []
    continua = True
    while continua == True:
        for i in dic_elementos:
            lista_ordem.append(i)
            
        #ordenar a lista
        for x in range(1, len(lista_ordem)):
            indice = x-1
            while lista_ordem[indice] > lista_ordem[indice + 1] and indice >= 0:
                lista_ordem[indice], lista_ordem[indice + 1] = lista_ordem[indice + 1], lista_ordem[indice]
                indice = indice - 1

        for y in lista_ordem:
            print(dic_elementos[y])

'''

#def impresaao_elementos(dic):    
#    for i in dic:
#        print(dic)


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
    [3]-Sair
    Escolha a opçao: """)
                    
                if opcao =="1":
                    buscar_elementos(dic_elementos)
                    
                elif opcao == "2":
                    mostrar_todos_os_elementos(dic_elementos)
                    
                elif opcao == "3":
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
    [5]-Sair
    Escolha a opçao: """)

                
            if opcao == "1":
                buscar_elementos(dic_elementos)
                
            elif opcao == "2":
                mostrar_todos_os_elementos(dic_elementos)
                
            elif opcao == "3":
                buscar_cargo(dic_elementos)
                
            elif opcao == "4":
                cadastrar_elementos(dic_elementos)
                
            elif opcao == "5":
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
    [8]-Sair
    
    Escolha a opçao: """)

            if opcao == "1":
                buscar_elementos(dic_elementos)
            
            elif opcao == "2":
                mostrar_todos_os_elementos(dic_elementos)
                
            elif opcao == "3":
                buscar_cargo(dic_elementos)                
                
            elif opcao == "4":
                cadastrar_elementos(dic_elementos)
                
            elif opcao == "5":
                remover_elementos(dic_elementos)
                
            if opcao == "6":
                atualizar_elementos(dic_elementos)
                
            elif opcao == "7":
                ordenar_elementos(dic_elementos)
                
            elif opcao == "8":
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
    [10]-Sair
    Escolha a opçao: """)


            if opcao == "1":
                buscar_elementos(dic_elementos)
            
            elif opcao == "2":
                mostrar_todos_os_elementos(dic_elementos)
                
            elif opcao == "3":
                buscar_cargo(dic_elementos) 
                
            elif opcao == "4":
                cadastrar_elementos(dic_elementos)
                
            elif opcao == "5":
                remover_elementos(dic_elementos)
                
            elif opcao == "6":
                atualizar_elementos(dic_elementos)
                
            elif opcao == "7":
                ordenar_elementos(dic_elementos)
                
            elif opcao == "8":
                alterar_nivel_usuario(dic_usuario)
                
            elif opcao == "9":
                remover_usuario(dic_usuario)    
                
            elif opcao == "10":
                 menu_sair()
                 parada = False
                
    else:
        print("Esse nivel nao existe , digite um nivel valido!")


def remover_usuario(dic_usuario):
    login=input("Digite o login que deseja remover: ")
    continua = True
    while continua == True:
        if login in dic_usuario:
            dic_usuario.pop(login)
            print("Login: ",login,"removido!")
            continua = False 
                
        else:
            continuar=input("Usuario nao encontrado, deseja buscar outro?(s/n) ")
            if continuar=="s":
                continua=True
            elif continuar=="n":
                continua=False


def alterar_nivel_usuario(dic_usuario):
    login = input("Digite o login que deseja modificar: ")
    continua = True
    while continua == True:
        if login in dic_usuario:           
            print("Login Localizado!")
            novo_nivel = input("Digite o novo nivel do usuario"+login+":")
            dic_usuario[login] = (dic_usuario[login][0], novo_nivel)
            continua = False
       
        else:
            continuar=input("Usuario nao encontrado, deseja buscar outro?(s/n) ")
            if continuar=="s":
                continua=True
            elif continuar=="n":
                continua=False


            
usuario = ''

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
            cadastrar_usuario(dic_usuario)
        elif entrada=="3":
            menu_sair()
        else:
            print("Opção inválida!")
    
    return acesso

            
def main():
    nivel = menu_principal()
    menu_nivel(nivel)

main()

criptografar_usuarios(dic_usuario, "usuarios.txt")
decifrar_usuarios("Usuarios.txt", dic_usuario)
criptografar_elementos(dic_elementos, "elementos.txt")
descriptografar_elementos("elementos.txt", dic_elementos)
