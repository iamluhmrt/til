"""
Nome: Luiz Martins
Curso: Análise e Desenvolvimento de Sistemas
Bem simples:
Passo 1 - Digite pip install prettytable no terminal.
Pronto!
:D agora pode executar meu código!
"""

# Lista que armazena as informações dos estudantes.
lista = []

# Importa biblioteca
import re
# importa tabela 
from prettytable import PrettyTable

def validate_str(nome_est): # uma função para validar str
    standard = r'^[a-zA-Z\s]+$' # lista do que eu aceito.
    if re.match(standard, nome_est): # condição para comparar padrão com parâmetro
      return True
    else:
      return False
  # regex 

# Valida se um número é int, se não for, ele repete até satisfazer a condição.
def leia_int(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric(): # verifica se a entrada é um número inteiro
            valor = int(n) # converte a entrada para um número inteiro
            ok = True # define ok como True para sair do loop
        else:
            print('Erro! Digite valor valido') # mensagem de erro caso a entrada não seja um número inteiro
        if ok: # sai do loop se ok é True
            break # sai do loop se ok é True
    return valor # retorna o valor inteiro 


# Tabela pra listar aluno de forma organizada.
def tabela(lista):
    tabela_aluno = PrettyTable()
    print('\033[1;35m')
    tabela_aluno.field_names = ['Nome', 'Idade', 'Turma', 'Matrícula']
    for info in lista:
      tabela_aluno.add_row([info['nome'],info['idade'],info['turma'],info['matricula']])
    return tabela_aluno

# Textos e linhas 
def header(txt):
    print(line()) # imprime uma linha de asteriscos para separar o texto
    print(txt.center(33)) # imprime o texto centralizado com 33 caracteres de largura
    print(line()) # imprime outra linha de asteriscos para separar o texto



# Textos e linhas
def line(tam=33):
    return  '*' * tam  # retorna uma linha de asteriscos com a largura especificada (33 por padrão)

def main_menu():
    print('\033[1;35m')
    header(f'SISTEMA PUC - MENU PRINCIPAL') # Mostra um cabeçalho na tela
    items = [ # Lista com items do menu.
    'Gerenciar estudantes',
    'Gerenciar professores ',
    'Gerenciar disciplinas ',
    'Gerenciar turmas ',
    'Gerenciar matrículas ',
    'Sair ', 
    ]
    for i, item in enumerate(items): # Para cada item da lista uma numeração.
      print(i, item, sep='. ') # Imprime os items separado por um . e um espaço.
    op = input('>: ') # Entrada de dados sem definir nenhum tipo de dado (mas por padrão é str.)
    while True: # Definido True para evitar uso de váriavel. 
      if op == '0': # Se o usuário digitar '0' vai ir pro menu de estudantes.
        menu_estudantes()
      elif op == '1':
        header('Em desenvolvimento')
      elif op == '2':
        header('Em desenvolvimento')
      elif op == '3':          
        header('Em desenvolvimento')
      elif op == '4':
        header('Em desenvolvimento')
      elif op == '5':
        print('Saindo...')
        exit() # Função que encerra o programa (quando usava o break dava uns problemas.)
      else:
        header('Você digitou errado: ') 
      return main_menu() # Toda vez que as condições não forem satisfeitas vai continuar retornando no menu principal.

def menu_estudantes():
    print('\033[1;35m')
    header(f'MENU ESTUDANTES') # Mostra um cabeçalho na tela
    items = [ # Lista com items do menu.
    (f'Criar registro'),
    (f'Listar registros'),
    (f'Buscar registros'), 
    (f'Atualizar registros'), 
    (f'Excluir um registro'), 
    (f'Voltar menu'),
    ]
    for i, item in enumerate(items): # Para cada item da lista uma numeração.
      print(i,  item, sep='. ') # Imprime os items separado por um . e um espaço.
    op = input('>: ') # Entrada de dados sem definir nenhum tipo de dado (mas por padrão é str.)
    while True: # Definido True para evitar uso de váriavel. 
      if op == '0':
        criar_aluno() 
      elif op =='1':
        listar_estudantes()
      elif op =='2':
        buscar_registros() 
      elif op =='3':
        header('Em desenvolvimento')
      elif op =='4':
        header('Em desenvolvimento')  
      elif op =='5':
        return main_menu()
      else:
        header('Você digitou errado!')
      return menu_estudantes() # Toda vez que as condições não forem satisfeitas vai continuar retornando no menu de estudantes

# Criar aluno e armazenar dados em lista
# Validação se matricula é a mesma ou não
def criar_aluno():
    header('REGISTRO')  # Mostra um cabeçalho na tela
    nome_est = input('Digite o nome: ')
    if validate_str(nome_est): # Valida os espaços/não aceita número, aceita de a-zA-Z.  
      idade_est = leia_int('Digite a idade: ') 
      turma_est = input('Digite a turma: ')  
      matricula_est = leia_int('Digite a matrícula: ')  
      for estudante in lista:  # Verifica se a matrícula digitada já existe na lista de estudantes
          if estudante['matricula'] == matricula_est:  
            # Se a matrícula já existir, mostra uma mensagem de erro e chama novamente a função criar_Aluno
              print('Matrícula já existe!')
              return criar_aluno()
      info = {  # Cria um dicionário com as informações do estudante que serão adicionadas na lista de estudantes
        'nome':nome_est,
        'idade':idade_est,
        'turma':turma_est,
        'matricula':matricula_est,
        }
      lista.append(info)  # Adiciona as informações do estudante na lista de estudantes
      header(f'Estudante cadastrado com sucesso!')  # Mostra uma mensagem informando que o estudante foi cadastrado com sucesso
      return menu_estudantes()  # Chama a função menu_estudantes para mostrar o menu de opções de estudantes
    else:
      print('Erro! Digite valor valido')
      return criar_aluno()

# IF:   Verifica se tem informações
# ELSE: Lista as informações
def listar_estudantes():
    if len(lista) == 0: # Verifica se na lista tem algo dentro da lista.
      print('\n')
      header('Não há estudantes cadastrados!')  # Se não tiver nada mostra uma mensagem informando que não há estudantes
    else:
      print(tabela(lista)) # Se tiver alunos ele vai imprimir as informações dos estudantes na lista.
      


# Função para buscar um registro
def buscar_registros():
    # Verifica se a lista de estudantes está vazia
    if len(lista) == 0: 
      # Se estiver vazia, exibe uma mensagem de erro
      print('\n')
      header('Não há registros no sistema') 
    else:
        # Cria um dicionário vazio para armazenar o estudante encontrado
        busca = {}
        # Pede ao usuário a matrícula do estudante a ser procurado
        matricula_est = leia_int('Digite a matrícula: ')
        # Procura o estudante com a matrícula fornecida na lista de estudantes
        for estudante in lista: 
          if estudante['matricula'] == matricula_est:
            busca = estudante
            break
        # Verifica se o estudante foi encontrado
        if busca:
          # Se foi encontrado, exibe as informações do estudante em uma tabela
          print(tabela([busca])) 
        else:
          # Se não foi encontrado, exibe uma mensagem de erro
          header('Matrícula não encontrada!')    
        
    # Retorna ao menu principal de estudantes
    return menu_estudantes()

if __name__ == '__main__':
   main_menu()
