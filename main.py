import json
from json.decoder import JSONDecodeError
from estudantes import *
from disciplinas import *
from professores import *
from turmas import *
from matriculas import *


def escrever_json(data, file_name):
    with open(file_name + '.json', 'w') as f:
        json.dump(data, f, indent=4)
        f.close()


def ler_json(file_name):
    data = {}
    try:
        with open(file_name + '.json', 'r') as f:
            data = json.load(f)
            f.close()
            return data
    except FileNotFoundError:
        escrever_json(data, file_name)
        return data
    except JSONDecodeError:
        escrever_json(data, file_name)
        return data


def criar_novo_registro(file_name):
    data = ler_json(file_name)
    novo = {}
    id = '1'
    ids = [int(k) for k in data.keys()]
    if len(ids) != 0:
        id = str(max(ids) + 1)
    colunas = eval(file_name)
    print('INCLUSÃO', file_name, '\n')
    for coluna in colunas:
        print('Informe', coluna)
        valor = input()
        novo[coluna] = valor
    data[id] = novo
    escrever_json(data, file_name)


def ler_registro(file_name):
    data = ler_json(file_name)
    registro = None
    identificador = None
    sim = True
    while sim:
        identificador = input('Entre com o ID:')
        if identificador in data.keys():
            registro = data[identificador]
            print('Registro =', registro)            
        else:
            print('ID sem registro!')        
        resposta = input('Deseja buscar outro ID? (s/n)').lower()
        if 'n' in resposta:
            sim = False
    return registro, identificador


def atualizar_registro(file_name):
    data = ler_json(file_name)
    print('ATUALIZAÇÃO', file_name, '\n')
    registro, identificador = ler_registro(file_name)
    if registro is None or identificador is None:
        print('O ID do registro não pode ser nulo!')
        finalizar_programa()
    colunas = eval(file_name)
    for coluna in colunas:
        valor = input('Informe novo valor para ' + coluna + '\n' + '> ')
        registro[coluna] = valor
    data[identificador] = registro
    escrever_json(data, file_name)
    print('Registro {identificador} alterado!')


def remover_registro(file_name):
    data = ler_json(file_name)
    print('EXCLUSÃO', file_name, '\n')
    registro, identificador = ler_registro(file_name)
    if registro is None or identificador is None:
        print('O ID do registro não pode ser nulo!')
    else:
        print('Confirma a remoção do ID:', identificador, '? (s/n)\n'
                                                          'OBS: Essa operação não pode ser desfeita.')
        confirma = input().lower()
        if 's' in confirma:
            data.pop(identificador)
            escrever_json(data, file_name)
            print('Registro', identificador, 'removido!')
        else:
            print('A remoção do registro:', identificador, 'foi cancelada.')


def buscar_por_coluna(file_name):
    data = ler_json(file_name)
    print('BUSCA', file_name, '\n')
    if len(data) == 0:
        print('Base vazia.')
    else:
        while True:
            resultados = {}
            texto = input('Entre com o termo que deseja buscar: ').lower()
            for identificador, registro in data.items():
                for coluna, valor in registro.items():
                    if texto in valor.lower():
                        resultados[identificador] = registro
                        continue
            print(resultados)
            refazer = input('Deseja buscar por outro termo? (s/n)')
            if 's' not in refazer:
                break


def listar_registro(file_name):
    data = ler_json(file_name)
    print('LISTAGEM', file_name, '\n')
    if len(data) == 0:
        print('Base vazia!')
    else:
        print(json.dumps(data, indent=4, sort_keys=True), '\n')
    input('Tecle uma tecla para continuar ...')


def finalizar_programa():
    print('Finalizando o programa...')
    exit(0)


def limpar_tela():
    print('\n' * 100)


def operacao(tabela):
    opcoes = ['1', '2', '3', '4', '5', '6']
    ativo = True
    while ativo:
        limpar_tela()
        print(
            'O que você deseja fazer na base', tabela, ':\n'
                                                       '(1) Criar novo registro.\n'
                                                       '(2) Alterar registro.\n'
                                                       '(3) Ler registros.\n'
                                                       '(4) Apagar registro.\n'
                                                       '(5) Listar registro.\n'
                                                       '(6) Voltar menu.\n\n'
                                                       '> '
        )
        opcao = input().lower()
        if opcao not in opcoes:
            input('Opção inválida. Tente novamente...')
        else:
            limpar_tela()
            if opcao == '1':
                criar_novo_registro(tabela)
            elif opcao == '2':
                atualizar_registro(tabela)
            elif opcao == '3':
                ler_registro(tabela)
            elif opcao == '4':
                remover_registro(tabela)
            elif opcao == '5':
                listar_registro(tabela)
            elif opcao == '6':
                ativo = False


def menu():
    opcoes = ['1', '2', '3', '4', '5', '6']
    ativo = True
    while ativo:
        limpar_tela()
        opcao = input(
            'Selecione a opção desejada:\n'
            '(1) Gerenciar estudantes.\n'
            '(2) Gerenciar professores.\n'
            '(3) Gerenciar disciplinas.\n'
            '(4) Gerenciar turmas.\n'
            '(5) Gerenciar matriculas.\n'
            '(6) Sair.\n\n'
            '> '
        ).lower()
        if opcao in opcoes:
            if opcao == '1':
                operacao(tabela1)
            elif opcao == '2':
                operacao(tabela2)
            elif opcao == '3':
                operacao(tabela3)
            elif opcao == '4':
                operacao(tabela4)
            elif opcao == '5':
                operacao(tabela5)
            elif opcao == '6':
                ativo = False
        else:
            print('Opção {} inválida. Tente novamente.'.format(opcao))
            input('Pressione qualquer tecla para continuar...')
    finalizar_programa()


if __name__ == '__main__':
    estudantes = ['codigo_estudante', 'nome_estudante', 'sobrenome_estudante']
    professores = ['codigo_professor', 'nome_professor', 'sobrenome_professor']
    disciplinas = ['codigo_disciplina', 'nome_disciplina']
    turmas = ['codigo_turma', 'cod_professor', 'cod_disciplina']
    matriculas = ['codigo_turma', 'codigo_estudante']

    tabela1 = 'estudantes'
    tabela2 = 'professores'
    tabela3 = 'disciplinas'
    tabela4 = 'turmas'
    tabela5 = 'matriculas'
    menu()
