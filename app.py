import os

restaurantes = [{'nome':'Pizza Suprema', 'categoria': 'Italiana', 'ativo': False},
                {'nome':'Praça', 'categoria': 'Japonesa', 'ativo': True},
                {'nome':'Cantina', 'categoria': 'Italiana', 'ativo': False}]

def exibir_subtitulo(texto):
    '''Essa função limpa o terminal e apresenta o subtitulo
    
   Outputs:
   - subititulo entre linhas de * 
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_ao_menu_principal():
    '''Essa função restorna ao inicio
    
    Input:
    -Qualquer caracter 
    '''
    input('\ndigite uma tecla para voltar ao menu principal ')
    main()

def exibir_nome_programa():
    '''Essa função exibe o nome do programa
    
    Outputs:
    -Título do programa
    '''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    '''Essa função exibe as opções para acessar
    
    Output:
    -Opções
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Essa função finaliza o programa
    
    Outputs:
    -finalização do programa
    '''
    exibir_subtitulo('Finalizando app')

def opcao_invalida():
    '''Essa opção mostra que o usuário colocou uma opção inválida e retorna ao menu
    
    Outputs:
    -Volta ao menu principal
    '''
    print('Opção inválida\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função apresenta os restaurantes cadastrados no app
    
    Outputs:
    -Mostra a lista de restaurantes
    '''
    exibir_subtitulo('Listando restaurantes')
    a = 1
    print(f"{'Nome do restaurante'.ljust(24)}  |  {'Categoria'.ljust(20)}  |  Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'{a}°. {nome_restaurante.ljust(20)}  |  {categoria.ljust(20)}  |  {ativo} ')
        a += 1
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    '''Essa função cadastra novos restaurantes no app
    
    Inputs:
    -Nome do restaurante
    -Categoria

    Outputs:
    -Adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    print('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante ,
                             'categoria' : categoria , 'ativo' : False}
    restaurantes.append(dados_do_restaurante)
    print(f'o restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Essa função muda o estado do restarante (ativado/desativado)
    
    Inputs:
    -Nome do restaurante

    Outputs:
    -Alterna o estado do restaurante
    '''
    exibir_subtitulo('Alternado estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucessio' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado')
    voltar_ao_menu_principal()


def escolher_opcao():
    '''Essa função permite ao usuario escolher uma opção
    
    Input:
    -Numero da opção escolhida

    Outputs:
    -Chama a função escolhida ou exibe função inválida
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print('Você escolheu a opção ', opcao_escolhida)
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()
            

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()



if __name__ == '__main__':
    main()