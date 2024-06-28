import os

restaurantes = [{'nome':'Pizza', 'categoria':'pizzaria','ativo':False},
                {'nome':'Hamburguer', 'categoria':'hamburgueria','ativo':True},
                {'nome':'sushi', 'categoria':'japao','ativo':False},
                ]

def exibir_nome():
    print('R̷a̷f̷a̷e̷l̷ D̷e̷l̷i̷v̷e̷r̷y̷\n')

def voltar_menu():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def exibir_opcoes():
    print('1. Cadastrar restaurantes')
    print('2. Listar restaurantes')
    print('3. Ativar restaurantes')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    exibir_subtitulo('Encerrando o app...\n')

def opcao_invalida():
    exibir_subtitulo('Opção inválida')
    voltar_menu()

def exibir_subtitulo(texto=''):
    os.system('cls')
    linha = '*' *(len(texto))
    print(linha)
    print(texto)
    print(linha)



def cadastro_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite qual a categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_menu()

def listar_restaurantes():
    exibir_subtitulo('...Listando restaurantes...\n')

    print(f'{'Nome do restaurante'.ljust(21)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_rest = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'.{nome_rest.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_menu()

def alterar_status():
    exibir_subtitulo()
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o STATUS: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            voltar_menu()
    if not restaurante_encontrado:
            print('O restaurante não foi encontrado')
            voltar_menu()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma das opções acima: '))
        if opcao_escolhida == 1:
            cadastro_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_status()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()   

def main():
    os.system('cls')
    exibir_nome()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()