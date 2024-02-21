

import json
import re
import os
from os import system, name 
from time import sleep

def validar_str(nome_estudantes):
    nome_valido = False
    while not nome_valido:    
        nome = input(nome_estudantes)
        standard = re.compile(r'^[a-zA-Z\s]+$') # lista do que eu aceito.
        if standard.match(nome): # condição para comparar padrão com parâmetro
            nome_valido = True
        else:
            print('Digite um nome válido')
    return nome # uma função para validar str

def validar_int(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric(): 
            valor = int(n) 
            ok = True 
        else:
            print('Erro! Digite valor valido') 
        if ok: 
            break 
    return valor 

def validar_cpf(cpf_estudante): 
    cpf_valido = False
    while not cpf_valido:    
        cpf = input(cpf_estudante)
        standard = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$') # lista do que eu aceito.
        if standard.match(cpf): # condição para comparar padrão com parâmetro
            cpf_valido = True
        else:
            print('Digite um CPF válido')
    return cpf

def clear(): 
    # Função que limpa o código
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

def loading():
# Simula carregamento de dados
    for i in range(3):
        print('carregando' + '.' *i, end='\r')
        sleep(0.3)

def closing():
    # Simula finalização do programa
    for i in range(3):
        print('carregando' + '.' *i, end='\r')
        sleep(0.5)  
        print('Programa encerrado.')
        exit()

def salvar_dados(data):
    # Função de chamar json
    with open('data_base.json', 'w') as arquivo:
        json.dump(data, arquivo)

def carregar_dados():
    # Verifica se o arquivo existe
    if not os.path.isfile('data_base.json'):
        # Se o arquivo não existir, cria um dicionário vazio e salva como um arquivo JSON
        data = {"estudantes": [],"professores": [],"disciplinas": [],"turmas": [],"matri": []}
        salvar_dados(data)
        print('Banco de dados criado com sucesso.')
    else:
        # Se o arquivo existir, carrega o arquivo JSON
        try: 
            with open('data_base.json') as arquivo:
                data = json.load(arquivo)
        except FileNotFoundError:
            data = {}
            print('Banco de dados não encontrado.')
    return data

def menu_principal():
    print('\033[1;35m')
    print(f'SISTEMA PUC - MENU PRINCIPAL')
    print('(0). Gerenciar estudantes\n(1). Gerenciar professores\n(2). Gerenciar disciplinas\n(3). Gerenciar turmas\n(4). Gerenciar matrículas\n(5). Sair') 
    op = input('>: ') 
    while True:
        if op == '0': 
            loading()
            clear()
            alunos()
        elif op == '1':
            loading()
            clear()
            professores()
        elif op == '2':
            loading()
            clear()
            disciplinas()
        elif op == '3':
            loading()
            clear()          
            turmas()
        elif op == '4':
            loading()
            clear()    
            matriculas()
        elif op == '5':
            closing()
        else:
            loading()
            clear()
            print('Você digitou errado: ') 
        return menu_principal() 

def alunos():
    def criar_estudante():
        # Carrega os dados do sistema
        data = carregar_dados()
        # Solicita as informações do estudante a ser cadastrado
        print('Registro Estudante')
        nome_estudante = validar_str('Nome: ')
        cpf_estudante = validar_cpf('CPF: ###.###.###-##: ')
        id_estudante = validar_int('Matrícula: ')
        # Verifica se não há a lista de estudantes nos dados existentes
        if data is None:
            novoestu = {'Nome':nome_estudante,'Cpf':cpf_estudante, 'Id':id_estudante}
            data = {'estudantes': [novoestu]}
            salvar_dados(data)
            return
        # Verifica se a lista de estudantes já existe nos dados    
        if "estudantes" not in data:
            data["estudantes"] = []
        # Verifica se o CPF do estudante já foi cadastrado como professor    
        for professor in data['professores']:
            if professor['Cpf'] == cpf_estudante:
                print('CPF já cadastrado no sistema!\n')     
                return criar_estudante()   
        # Verifica se o CPF do estudante já foi cadastrado anteriormente             
        for estudante in data['estudantes']:
            if estudante['Cpf'] == cpf_estudante:
                print('CPF já cadastrado no sistema!\n')     
                return criar_estudante()
        # Verifica se a matrícula do estudante já foi cadastrada anteriormente        
        for estudante in data['estudantes']:
            if estudante['Id'] == id_estudante:
                print('Matrícula já cadastrada no sistema!\n')             
                return criar_estudante()
        # Se todas as verificações passaram, adiciona o novo estudante à lista de estudantes nos dados        
        novoestu = {'Nome':nome_estudante,'Cpf':cpf_estudante,'Id':id_estudante,}
        data["estudantes"].append(novoestu)
        salvar_dados(data)
        # Exibe uma mensagem de sucesso e encerra a função
        clear()
        print(f'Estudante cadastrado com sucesso!')
        return

    def listar_estudantes():
        data = carregar_dados()
        print('Lista de Estudante')
        # Verifica se há estudantes cadastrados
        if "estudantes" not in data or not data["estudantes"]:
            # Se não houver, exibe uma mensagem informando que não há estudantes cadastrados
            print('Não há estudantes cadastrados.')
        else:
            # Se houver, itera sobre a lista de estudantes e exibe as informações de cada um
            for estudante in data["estudantes"]:
                print(f'Nome: {estudante["Nome"]} | CPF: {estudante["Cpf"]} | Matrícula: {estudante["Id"]}')

    def buscar_estudantes():
        # Carrega os dados do sistema
        data = carregar_dados()
        print('Buscar um cadastro')
        # Verifica se há estudantes cadastrados
        if "estudantes" not in data or not data["estudantes"]:
            # Se não houver, exibe uma mensagem informando que não há estudantes cadastrados
            print('Não há estudantes cadastrados.')
        else:
            # Se houver, solicita o número de matrícula do estudante a ser buscado
            id = validar_int('Matrícula: ')
            # Itera sobre a lista de estudantes buscando o estudante com o número de matrícula informado
            for estudante in data["estudantes"]:
                if estudante["Id"] == id:
                    # Se encontrar, exibe as informações do estudante e retorna
                    print(f'Nome:{estudante["Nome"]} Cpf:{estudante["Cpf"]} Matrícula:{estudante["Id"]}')
                    return
            # Se não encontrar, exibe uma mensagem informando que o estudante não foi encontrado        
            print('Não achamos esse estudante')

    def atualizar_estudante():
        # Carrega os dados do sistema
        data = carregar_dados()
        print('Atualizar Cadastro')
        # Verifica se há estudantes cadastrados
        if "estudantes" not in data or not data["estudantes"]:
            # Se não houver, exibe uma mensagem informando que não há estudantes cadastrados
            print('Não há estudantes cadastrados.')
        else:
            # Se houver, solicita o número de matrícula do estudante a ser atualizado
            id = validar_int('Digite a Matrícula: ')
            # Itera sobre a lista de estudantes buscando o estudante com o número de matrícula informado
            for estudante in data.get("estudantes", []):
                if estudante["Id"] == id:
                    # Se encontrar, solicita o novo nome e CPF do estudante
                    nome = validar_str('Digite o novo nome: ')
                    cpf = validar_cpf('Digite o novo CPF: ')
                    # Verifica se já existe um estudante com o novo CPF ou novo nome
                    for novo_estudante in data["estudantes"]:
                        if novo_estudante["Cpf"] == cpf or novo_estudante["Nome"] == nome:
                            # Se já existir, exibe uma mensagem informando que já há um cadastro com esses dados e retorna
                            print('Já cadastrado!')
                            return
                    # Atualiza os dados do estudante        
                    estudante["Nome"] = nome
                    estudante["Cpf"] = cpf
                    # Salva os dados atualizados e exibe uma mensagem de sucesso
                    salvar_dados(data)
                    clear()
                    # Se não encontrar, exibe uma mensagem informando que o estudante não foi encontrado
                    print('Dados atualizados com sucesso')
                    return
        print('Não fora encontrado dado algum!')

    def excluir_estudante():
        # Carrega os dados do sistema
        data = carregar_dados()
        print('Excluir um cadastro')
        # Verifica se há estudantes cadastrados
        if "estudantes" not in data or not data["estudantes"]:
            # Se não houver, exibe uma mensagem informando que não há estudantes cadastrados
            print('Não há estudantes cadastrados.')
        else:
            # Pede a matrícula do estudante a ser excluído.
            id = validar_int("Digite a matrícula pra excluir: ")
            # Verifica se a matrícula existe e a exclui.
            for index, estudantes in enumerate(data["estudantes"]):
                if estudantes["Id"] == id:
                    del data["estudantes"][index]
                    # Salva os dados atualizados no arquivo.
                    salvar_dados(data)
                    # Limpa a tela e exibe a mensagem de sucesso.
                    clear()
                    print('Excluído com sucesso!')
                    return
            # Se a matrícula não for encontrada, exibe a mensagem correspondente.
            print('Matrícula não encontrada!')

    def menu_estudantes():
        # Menu Estudantes
        print('\033[1;35m')
        print(f'MENU ESTUDANTES') 
        print('(0). Criar registro\n(1). Listar registros\n(2). Buscar registros\n(3). Atualizar registros\n(4). Excluir\n(5). Voltar')
        op = input('>: ') 
        while True: 
            if op == '0':
                loading()
                clear()
                criar_estudante() 
            elif op =='1':
                loading()
                clear()
                listar_estudantes()
            elif op =='2':
                loading()
                clear()
                buscar_estudantes() 
            elif op =='3':
                loading()
                clear()
                atualizar_estudante()
            elif op =='4':
                loading()
                clear()
                excluir_estudante()
            elif op =='5':
                loading()
                clear()
                return menu_principal()
            else:
                loading()
                clear()
                print('Você digitou errado!')
            return menu_estudantes() 
    menu_estudantes()

def professores():
    # Carrega os dados do arquivo
    def criar_professores():
        data = carregar_dados()
        # Solicita as informações do professor para o usuário
        print('Registro Professor')
        nome_professor = validar_str('Nome: ')
        cpf_professor = validar_cpf('CPF: ###.###.###-##: ')
        id_professor = validar_int('Código do professor: ')
        # Verifica se os dados estão vazios
        if data is None:
            data_profs = {'Nome':nome_professor,'Cpf':cpf_professor,'Id':id_professor}
            data.append(data_profs)
            salvar_dados(data)
            print(f'Professor cadastrado com sucesso!\n')
        # Verifica se a lista de professores ainda não foi criada
        if "professores" not in data:
            data["professores"] = []
        # Verifica se o CPF já está cadastrado no sistema
        for estudante in data['estudantes']:
            if estudante['Cpf'] == cpf_professor:
                print('CPF já cadastrado no sistema!\n')     
                return criar_professores()    
        # Verifica se o código já está cadastrado no sistema
        for professor in data["professores"]:
            if professor['Id'] == id_professor:
                print('Código já cadastrado no sistema!\n')
                return criar_professores()
        # Verifica se o CPF já está cadastrado em outro professor
        for professor in data["professores"]:
            if professor['Cpf'] == cpf_professor:
                print('CPF já cadastrado no sistema!')
                return criar_professores()
        # Cria um dicionário com os dados do professor
        data_profs = {'Nome':nome_professor,'Cpf':cpf_professor,'Id':id_professor}
        # Adiciona o dicionário à lista de professores
        data["professores"].append(data_profs)
        # Salva os dados do sistema
        salvar_dados(data)
        print(f'Professor cadastrado com sucesso!')

    def listar_professores():
        # Carrega os dados do arquivo json
        data = carregar_dados()
        print('Lista de Professores')
        # Verifica se existem professores cadastrados
        if "professores" not in data or not data["professores"]:
            print('Não há professores cadastrados.')
        else:
            # Percorre a lista de professores e imprime as informações de cada um
            for professor in data["professores"]:
                print(f'Nome: {professor["Nome"]} | CPF: {professor["Cpf"]} | Matrícula: {professor["Id"]}')

    def buscar_professores():
        # Carrega os dados do arquivo
        data = carregar_dados()
        print('Busque um cadastro')
        # Verifica se há professores cadastrados
        if "professores" not in data or not data["professores"]:
            print('Não há professores cadastrados.')
        else:
            # Solicita ao usuário que informe o código do professor
            id = validar_int('Código: ')
            # Percorre a lista de professores para encontrar o professor com o código informado
            for professor in data["professores"]:
                if professor["Id"] == id:
                    # Exibe as informações do professor correspondente ao código informado
                    print(f'Nome:{professor["Nome"]} Cpf:{professor["Cpf"]} Código:{professor["Id"]}')
                    return
            # Se não encontrou nenhum professor com o código informado, exibe uma mensagem indicando que não foi encontrado
            print('Não achamos esse professor')

    def atualizar_professores():
        # Carrega os dados existentes
        data = carregar_dados()
        print('Atualizar Cadastro')
        # Verifica se há professores cadastrados
        if "professores" not in data or not data["professores"]:
            print('Não há professores cadastrados.')
        else:
            # Pede ao usuário para digitar o código do professor a ser atualizado
            id = validar_int('Digite o Código: ')
            # Verifica se o código existe nos dado
            for professor in data.get("professores", []):
                if professor["Id"] == id:
                    # Pede ao usuário para digitar o novo nome e CPF do professor
                    nome = validar_str('Digite o novo nome: ')
                    cpf = validar_cpf('Digite o novo CPF: ')
                    # Verifica se o novo nome ou CPF já existem em outros professores cadastrados
                    for novo_professor in data["professores"]:
                        if novo_professor["Cpf"] == cpf or novo_professor["Nome"] == nome:
                            print('Já cadastrado!')
                            return
                    # Atualiza o nome e CPF do professor e salva os dados atualizados
                    professor["Nome"] = nome
                    professor["Cpf"] = cpf
                    salvar_dados(data)
                    print('Dados atualizados com sucesso')
                    return
            print('Não achamos esse professor')

    def excluir_professores():
        # Carrega os dados salvos
        data = carregar_dados()
        # Exibe mensagem de exclusão e verifica se há professores cadastrados
        print('Excluir um cadastro')
        if "professores" not in data or not data["professores"]:
            print('Não há professores cadastrados.')
        else:
            # Solicita o código do professor a ser excluído
            id = validar_int("Digite o código para excluir: ")
            # Percorre a lista de professores e verifica se o código informado existe
            for index, professores in enumerate(data["professores"]):
                if professores["Id"] == id:
                    # Se encontrado, remove o professor da lista, salva os dados e exibe mensagem de sucesso
                    del data["professores"][index]
                    salvar_dados(data)
                    clear()
                    print('Excluído com sucesso!')
                    return
            # Se não encontrado, exibe mensagem de erro        
            print('Código não encontrado!')

    def menu_professores():
        # Menu Professores
        print('\033[1;35m')
        print(f'MENU PROFESSORES') 
        print('(0). Criar registro\n(1). Listar registros\n(2). Buscar registros\n(3). Atualizar registros\n(4). Excluir\n(5). Voltar')
        op = input('>: ') 
        while True: 
            if op == '0':
                clear()
                loading()
                clear()
                criar_professores()
            elif op =='1':
                clear()
                loading()
                clear()
                listar_professores()
            elif op =='2':
                clear()
                loading()
                clear()
                buscar_professores() 
            elif op =='3':
                clear()
                loading()
                clear()
                atualizar_professores()
            elif op =='4':
                clear()
                loading()
                clear()
                excluir_professores()
            elif op =='5':
                clear()
                loading()
                clear()
                return menu_principal()
            else:
                clear()
                loading()
                clear()
                print('Você digitou errado!')
            return menu_principal()
    menu_professores()

def disciplinas():
    def criar_disciplinas():
        # Carrega os dados do sistema
        data = carregar_dados()
        # Solicita os dados da disciplina a ser cadastrada
        print('Registro Disciplinas')
        nome_disciplina = validar_str('Nome da disciplina: ')
        id_disciplina = validar_int('Código da disciplina: ')
        # Verifica se o sistema ainda não possui nenhuma disciplina cadastrada
        if data is None:
            # Cria um novo registro de disciplina e adiciona ao sistema
            data_disc = {'Nome':nome_disciplina, 'Id':id_disciplina}
            data.append(data_disc)
            salvar_dados(data)
            print(f'Dados cadastrados com sucesso')
        # Caso o sistema já possua outras disciplinas cadastradas
        if "disciplinas" not in data:
            data["disciplinas"] = []
        # Verifica se o código da disciplina já está cadastrado no sistema
        for disciplina in data["disciplinas"]:
            if disciplina['Id'] == id_disciplina:
                print('Código já cadastrado, tente novamente!\n')
                return criar_disciplinas()
        # Verifica se o nome da disciplina já está cadastrado no sistema
        for disciplina in data["disciplinas"]:
            if disciplina['Nome'] == nome_disciplina:
                print('Nome já cadastrado no sistema, tente novamente!\n')
                return criar_disciplinas()        
        # Adiciona o novo registro de disciplina ao sistema e salva os dados
        data_disc = {'Nome':nome_disciplina, 'Id':id_disciplina}
        data["disciplinas"].append(data_disc)
        salvar_dados(data)
        print(f'Dados cadastrados com sucesso')

    def listar_disciplinas():
        # Carrega os dados do arquivo
        data = carregar_dados()
        print('Lista de Disciplinas')
        # Verifica se existem disciplinas cadastradas
        if "disciplinas" not in data or not data["disciplinas"]:
            print('Não há disciplinas cadastradas.')
        else:
            # Itera sobre a lista de disciplinas e imprime os dados de cada uma
            for disciplina in data["disciplinas"]:
                print(f'Nome: {disciplina["Nome"]} | Código: {disciplina["Id"]}')

    def buscar_disciplinas():
        # Carrega os dados do sistema
        data = carregar_dados()
        print('Busque uma disciplina')
        # Verifica se existem disciplinas cadastradas
        if "disciplinas" not in data or not data["disciplinas"]:
            print('Não há disciplinas cadastrados.')
        else:
            # Solicita o código da disciplina a ser buscada
            id = validar_int('Código: ')
            # Busca a disciplina com o código informado
            for disciplina in data["disciplinas"]:
                if disciplina["Id"] == id:
                    print(f'Nome:{disciplina["Nome"]} Código:{disciplina["Id"]}')
                    return
            # Caso não encontre a disciplina com o código informado        
            print('Não achamos essa disciplina')

    def atualizar_disciplinas():
        # Carrega os dados salvos
        data = carregar_dados()
        print('Atualizar Disciplinas')
        # Verifica se há disciplinas cadastradas
        if "disciplinas" not in data or not data["disciplinas"]:
            print('Não há disciplinas cadastrados.')
        else:
            # Pede ao usuário o ID da disciplina que deseja atualizar
            id = validar_int('Digite o Código: ')
            # Busca a disciplina com o ID informado
            for disciplina in data.get("disciplinas", []):
                if disciplina["Id"] == id:
                    # Pede ao usuário o novo nome e ID da disciplina
                    nome = validar_str('Digite o novo nome: ')
                    id = validar_int('Digite o novo ID: ')
                    # Verifica se o novo nome e ID já estão cadastrados em outras disciplinas
                    for novo_disciplina in data["disciplinas"]:
                        if novo_disciplina["Id"] == id or novo_disciplina["Nome"] == nome:
                            print('Dado já cadastrado!')
                            return
                    # Atualiza os dados da disciplina        
                    disciplina["Nome"] = nome
                    disciplina["Id"] = id
                    # Salva os dados atualizados
                    salvar_dados(data)
                    print('Dados atualizados com sucesso')
                    # Caso não encontre a disciplina com o ID informado, imprime mensagem de erro
                    return
            print('Não fora encontrado dado algum!')

    def excluir_disciplinas():
        # Carrega os dados
        data = carregar_dados()
        print('Excluir um cadastro')
        # Verifica se há disciplinas cadastradas
        if "disciplinas" not in data or not data["disciplinas"]:
            print('Não há disciplinas cadastrados.')
        # Solicita o código da disciplina a ser excluída
        else:
            # Percorre a lista de disciplinas
            id = validar_int("Digite o código para excluir: ")
            for index, disciplinas in enumerate(data["disciplinas"]):
                # Verifica se a disciplina a ser excluída está cadastrada
                if disciplinas["Id"] == id:
                    # Remove a disciplina da lista
                    del data["disciplinas"][index]
                    # Salva os dados atualizados
                    salvar_dados(data)
                    clear()
                    print('Excluído com sucesso!')
                    return
            # Caso o código não seja encontrado, imprime mensagem de erro
            print('Código não encontrado!')

    def menu_disciplinas():
        # Menu Disciplinas
        print('\033[1;35m')
        print(f'MENU Disciplinas') 
        print('(0). Criar registro\n(1). Listar registros\n(2). Buscar registros\n(3). Atualizar registros\n(4). Excluir\n(5). Voltar')
        op = input('>: ') 
        while True: 
            if op == '0':
                clear()
                loading()
                clear()
                criar_disciplinas()
            elif op =='1':
                clear()
                loading()
                clear()
                listar_disciplinas()
            elif op =='2':
                clear()
                loading()
                clear()
                buscar_disciplinas()
            elif op =='3':
                clear()
                loading()
                clear()
                atualizar_disciplinas()
            elif op =='4':
                clear()
                loading()
                clear()
                excluir_disciplinas()
            elif op =='5':
                clear()
                loading()
                clear()
                return menu_principal()
            else:
                clear()
                loading()
                clear()
                print('Você digitou errado!')
            return menu_principal()
    menu_disciplinas()

def turmas():
    def criar_turmas():
        # Carrega os dados já existentes
        data = carregar_dados()
        # Variáveis para validar se o professor e a disciplina existem
        professor_existe = False 
        disciplina_existe = False
        # Solicita ao usuário informações para cadastrar uma nova turma
        print('Registro Turma\n')
        id_turma = validar_int('Código da Turma: ')
        id_professor = validar_int('Código do Professor: ')
        id_dis = validar_int('Código da Disciplina: ')
        # Verifica se há dados existentes
        if data is None:
            # Se não houver dados, cria um novo registro de turma
            data_turma = {'turma_id':id_turma,'professor_id':id_professor,'disciplina_id':id_dis}
            data.append(data_turma)
            salvar_dados(data)
            print(f'Turma cadastrada com sucesso!')
        # Verifica se há turmas já cadastradas
        if "turmas" not in data:
            data["turmas"] = [] 
        # Valida se o professor existe
        for professor in data['professores']: 
            # Valida se o professor existe
            if professor['Id'] == id_professor:
                professor_existe = True
        # Se o professor não existir, exibe mensagem de erro e retorna
        if professor_existe == False:
            print('Registro do professor não foi encontrado')
            return 
        # Valida se a disciplina existe
        for disciplina in data['disciplinas']:
            if disciplina['Id'] == id_dis:
                disciplina_existe = True
        # Se a disciplina não existir, exibe mensagem de erro e retorna
        if disciplina_existe == False:
            print('Registro da disciplina não foi encontrado')
            return
        # Valida se o código da turma já existe
        for turma in data['turmas']:
            if turma['turma_id'] == id_turma:
                print('Código da turma já existe')
                return 
        # Valida se o professor já está cadastrado em outra turma
        for turma in data['turmas']:
            if turma['professor_id'] == id_professor:
                print('Esse professor já existe')
                return
        # Valida se a disciplina já está cadastrada em outra turma
        for turma in data['turmas']:
            if turma['disciplina_id'] == id_dis:
                print('Essa disciplina já existe')
                return        
        # Se todas as validações foram bem sucedidas, cadastra a nova turma
        data_turma = {'turma_id':id_turma,'professor_id':id_professor,'disciplina_id':id_dis}
        data["turmas"].append(data_turma)
        salvar_dados(data)
        print(f'Turma cadastrada com sucesso!')

    def listar_turmas():
        # Carrega os dados
        data = carregar_dados()
        # Exibe título da lista de turmas
        print('Lista de Turmas')
        # Verifica se há turmas cadastradas
        if "turmas" not in data or not data["turmas"]:
            print('Não há turmas cadastradas.')
        else:
            # Percorre todas as turmas cadastradas
            for turma in data["turmas"]:
                # Exibe os dados da turma
                print(f'Turma: {turma["turma_id"]} | Professor Id: {turma["professor_id"]} | Disciplina Id {turma["disciplina_id"]}')

    def atualizar_turmas():
        # Carrega os dados
        data = carregar_dados()
        print('Atualizar Turmas')
        # Verifica se há turmas cadastradas
        if "turmas" not in data or not data["turmas"]:
            print('Não há turmas cadastrados.')
        else:
            # Recebe o ID atual da turma a ser atualizada
            id = validar_int('Digite o Código: ')
            # Verifica se a turma com o ID atual existe
            for turma in data.get("turmas", []):
                if turma["turma_id"] == id:
                    # Recebe o novo ID a ser inserido
                    id_novo = validar_int('Digite o novo ID: ')
                    # Verifica se já existe uma turma com o novo ID
                    for nova_turma in data["turmas"]:
                        if nova_turma["turma_id"] == id_novo:
                            print('Já cadastrado!')
                            return
                    # Atualiza o ID da turma
                    turma["turma_id"] = id_novo
                    salvar_dados(data)
                    print('Dados atualizados com sucesso')
                    return
            print('Não fora encontrado dado algum!')

    def excluir_turmas():
        # Carrega os dados
        data = carregar_dados()
        print('Excluir um cadastro')
        # Verifica se há turmas cadastradas
        if "turmas" not in data or not data["turmas"]:
            print('Não há turmas cadastradas.')
        else:
            id = validar_int("Digite o código para excluir: ")
            for index, turmas in enumerate(data["turmas"]):
                # Procura a turma com o id informado e a exclui
                if turmas["turma_id"] == id:
                    del data["turmas"][index]
                    salvar_dados(data)
                    clear()
                    print('Excluído com sucesso!')
                    return
            # Caso não encontre a turma com o id informado, informa que não foi encontrada
            print('Código não encontrado!')

    # Menu Turmas
    def menu_turmas():
        print('\033[1;35m')
        print(f'MENU TURMAS') 
        print('(0). Criar registro\n(1). Listar registros\n(2). Atualizar registros\n(3). Excluir\n(4). Voltar')
        op = input('>: ') 
        while True: 
            if op == '0':
                clear()
                loading()
                clear()
                criar_turmas()
            elif op =='1':
                clear()
                loading()
                clear()
                listar_turmas()
            elif op =='2':
                clear()
                loading()
                clear()
                atualizar_turmas()
            elif op =='3':
                clear()
                loading()
                clear()
                excluir_turmas()
            elif op =='4':
                clear()
                loading()
                clear()
                return menu_principal()
            else:
                clear()
                loading()
                clear()
                print('Você digitou errado!')
            return menu_principal()
    menu_turmas()

def matriculas():
    def criar_matriculas():
        # Carrega os dados do arquivo
        data = carregar_dados()
        # Inicializa as variáveis de verificação de existência de estudante e disciplina
        turma_existe = False
        estudante_existe = False
        print('Registro Disciplina\n')
        # Solicita código da turma, do estudante e da disciplina
        id_turma = validar_int('Código da Turma: ')
        id_estudante = validar_int('Código do Estudante: ')
        # Se não há dados, adiciona a turma diretamente
        if data is None:
            data_matri = {'turma_id':id_turma,'estudante_id':id_estudante}
            data.append(data_matri)
            salvar_dados(data)
            print(f'Turma cadastrada com sucesso!')
        # Se não existem matriculas, adiciona a lista de turmas vazia
        if "matri" not in data:
            data["matri"] = []
        # Verifica se o estudante existe
        for estudante in data['estudantes']:
            if estudante['Id'] == id_estudante:
                estudante_existe  = True
        # Se o estudante não existe, exibe mensagem e encerra a função
        if estudante_existe == False:
            print('Registro do estudante não foi encontrado')
            return
        # Verifica se a turma existe
        for turma in data['turmas']:
            if turma['turma_id'] == id_turma:
                turma_existe = True
        # Se a turma não existe, exibe mensagem e encerra a função
        if turma_existe == False:
            print('Registro da turma não foi encontrado')
            return
        # Verifica se o estudante já existe
        for estudante in data['matri']:
            if estudante['estudante_id'] == id_estudante:
                print('Esse estudante já existe')
                return
        # Verifica se a disciplina já está associada a alguma turma
        for turma in data['matri']:
            if turma['turma_id'] == id_turma:
                print('Essa disciplina já existe')
                return
        # Adiciona a turma na lista de turmas e salva os dados no arquivo
        data_matri = {'turma_id':id_turma,'estudante_id':id_estudante}
        data["matri"].append(data_matri)
        salvar_dados(data)
        print(f'Matrícula cadastrada com sucesso!')        

    def listar_matriculas():
        # Carrega os dados do arquivo
        data = carregar_dados()
        print('Lista de Matriculas')
        # Verifica se há matrículas cadastradas
        if "matri" not in data or not data["matri"]:
            # Caso não haja, imprime uma mensagem informando
            print('Não há matriculas cadastradas.')
        else:
            # Caso haja, itera sobre as matrículas e imprime os dados
            for matri in data["matri"]:
                print(f'Turma: {matri["turma_id"]} | Estudante Id: {matri["estudante_id"]}')

    def atualizar_matriculas():
        # Carrega os dados do arquivo
        data = carregar_dados()
        # Exibe mensagem de cabeçalho
        print('Atualizar Matriculas')
        # Verifica se há matrículas cadastradas
        if "matri" not in data or not data["matri"]:
            print('Não há matrículas cadastrados.')
        else:
            # Solicita o código da turma a ser atualizada
            id = validar_int('Digite o Código: ')
            # Percorre todas as turmas cadastradas
            for turma in data.get("matri", []):
                # Verifica se a turma atual é a que precisa ser atualizada
                if turma["turma_id"] == id:
                    # Solicita o novo ID da turma
                    id_novo = validar_int('Digite o novo ID: ')
                    # Verifica se o novo ID já está cadastrado
                    for nova_turma in data["matri"]:
                        if nova_turma["turma_id"] == id_novo:
                            print('Já cadastrado!')
                            return
                    # Atualiza o ID da turma
                    turma["turma_id"] = id_novo
                    # Salva os dados atualizados no arquivo
                    salvar_dados(data)
                    # Exibe mensagem de sucesso
                    print('Dados atualizados com sucesso')
                    return
            print('Não fora encontrado dado algum!')

    def excluir_matriculas():
        # Carrega os dados do arquivo
        data = carregar_dados()
        print('Excluir um cadastro')
        # Verifica se há matrículas cadastradas
        if "matri" not in data or not data["matri"]:
            print('Não há matrículas cadastrados.')
        else:
            # Solicita o código da turma a ser excluída
            id = validar_int("Digite o código para excluir: ")
            # Percorre todas as turmas cadastradas
            for index, matriculas in enumerate(data["matri"]):
                # Verifica se a turma atual é a que precisa ser excluída
                if matriculas["turma_id"] == id:
                    # Exclui a turma
                    del data["matri"][index]
                    # Salva os dados atualizados no arquivo
                    salvar_dados(data)
                    clear()
                    # Exibe mensagem de sucesso
                    print('Excluído com sucesso!')
                    return
            # Exibe mensagem de erro se a turma não foi encontrada
            print('Código não encontrado!')

    # Menu Matrículas
    def menu_matriculas():
        print('\033[1;35m')
        print(f'MENU MATRICULAS') 
        print('(0). Criar registro\n(1). Listar registros\n(2). Atualizar registros\n(3). Excluir\n(4). Voltar')
        op = input('>: ') 
        while True: 
            if op == '0':
                clear()
                loading()
                clear()
                criar_matriculas()
            elif op =='1':
                clear()
                loading()
                clear()
                listar_matriculas()
            elif op =='2':
                clear()
                loading()
                clear()
                atualizar_matriculas()
            elif op =='3':
                clear()
                loading()
                clear()
                excluir_matriculas()
            elif op =='4':
                clear()
                loading()
                clear()
                return menu_principal()
            else:
                clear()
                loading()
                clear()
                print('Você digitou errado!')
            return menu_principal()
    menu_matriculas()

menu_principal()
