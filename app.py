import os

restaurantes = ['Pizzaria 1', 'Hamburgueria A']

def exibir_nome():
    print('R̷a̷f̷a̷e̷l̷ D̷e̷l̷i̷v̷e̷r̷y̷\n')

def exibir_opcoes():
    print('1. Cadastrar restaurantes')
    print('2. Listar restaurantes')
    print('3. Ativar restaurantes')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Encerrando o app...\n')

def opcao_invalida():
    input('Digite uma tecla para voltar ao inicio')
    main()

def cadastro_novo_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def listar_restaurantes():
    os.system('cls')
    print ('Listando restaurantes...\n')
    for restaurante in restaurantes:
        print(f'.{restaurante}')
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma das opções acima: '))
        if opcao_escolhida == 1:
            cadastro_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurantes')
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