lista_colaboradores = []
id_global = 0

def cadastrar_colaborador(id):
    id_pessoa = int(input('Número do ID: '))
    nome = str(input('Nome do colaborador: '))
    setor = str(input('Nome do setor: '))
    pagamento_colaborador = int(input('Pagamento do colaborador R$'))
    id = {'id_pessoa': id_pessoa, 'nome': nome, 'setor': setor, 'pagamento_colaborador': pagamento_colaborador}
    lista_colaboradores.append(id.copy())            #Faz a copia do dicionario pra uma lista


def consultar_colaborador():
    while True:
        print('-' * 30, 'Consultar Colaborador', '-' * 30)
        consulta = str(input('''       [1] Consultar Todos os colaboradores
        [2] Consultar por ID
        [3] Consultar por Setor
        [4] Retornar ao Menu'''))
        if consulta == '1':
            for colaboradores in lista_colaboradores:
                for key, values in colaboradores.items():  #Tira todos os itens do dicionario
                    print(f'{key}: {values}')
        elif consulta == '2':
            id_pessoa = int(input('Número do ID do Colaborador: '))
            for colaboradores in lista_colaboradores:    #para pegar o ID da pessoa
                if colaboradores['id_pessoa'] == id_pessoa:
                    for key, values in colaboradores.items():
                        print(f'{key}: {values}')
        elif consulta == '3':
            setor = str(input('Nome do Setor: '))
            for colaboradores in lista_colaboradores:  # para pegar o setor da pessoa
                if colaboradores['setor'] == setor:
                    for key, values in colaboradores.items():
                        print(f'{key}: {values}')
                else:
                    print('Setor INEXISTENTE!')
                    continue
        elif consulta == '4':
            print('Retornando ao Menu...')
            return
        else:
            print('Digite somente as opções acima!')




def remover_colaborador():
    remover = int(input('Qual colaborador você deseja remover? '))
    for colaboradores in lista_colaboradores:  # para pegar o ID da pessoa
        if colaboradores['id_pessoa'] == remover:
            lista_colaboradores.remove(colaboradores)
            print('Colaborador removido com sucesso!')
        else:
            print('Colaborador inexistente')




print('Bem-vindo ao Gerenciamento Profissional de Danyel Gusthavo')
while True:
    print('-'*30, 'MENU PRINCIPAL', '-'*30)
    menu_principal = str(input('''         [1] Cadastrar Colaborador
         [2] Consultar Colaborador
         [3] Remover Colaborador
         [4] Encerrar Programa
        '''))
    if menu_principal == '1':
        id_global += 1
        cadastrar_colaborador(id_global)
    elif menu_principal == '2':
        consultar_colaborador()
    elif menu_principal == '3':
        remover_colaborador()
    elif menu_principal == '4':
        print('Programa encerrado!')
        break
    else:
        print('Opção inválida!')
        continue




