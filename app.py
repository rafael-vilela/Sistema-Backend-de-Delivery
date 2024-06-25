import os

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

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma das opções acima: '))
    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar restaurantes')
    elif opcao_escolhida == 4:
        finalizar_app()
    else:
        print('Opção inválida')

def main():
    exibir_nome()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
