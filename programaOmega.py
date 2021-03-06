from time import sleep
from copy import deepcopy

def calcularDesconto(valor, porcentagem):
    desconto = valor * (porcentagem/100)
    resultado = valor - desconto
    return resultado


compra = itens = {}
produtos = []
opcao = [1, 2, 3, 4]
carrinho = []

while True:
    produto = 0
    preco = 0
    print("\033[34m~~" * 20)
    print(f"\033[m{'MERCADO':>23}")
    print("\033[34m~~\033[m" * 20)
    print('1 - Adicionar item\n2 - Adicionar carrinho\n3 - Ver carrinho\n4 - Sair')
    escolha = str(input(':'))
    try:
        escolha = int(escolha)
        if escolha not in opcao:
            print('Essa opção não está na lista')
    except:
        print('Essa opção não está na lista')

    else:
        if escolha == 1:
            try:
                nome = str(input('nome do item: '))
                if nome == "":
                    nome = 'Indefinido'
                valor = float(input('valor: '))
                desconto = str(input('desconto(em %): '))
                itens['Nome'] = nome
                itens['Valor'] = valor
                itens['Desconto'] = desconto
                try:
                    if desconto != 0:
                        desconto = float(desconto)
                        valor = calcularDesconto(valor, desconto)
                        itens['Valor'] = valor
                    else:
                        print('Nenhum desconto atribuído')
                except:
                    print('Nenhum desconto atribuído')

                print(f"valor final = R${valor:.2f}".replace(".", ","))
                print('-'*50)
                produtos.append(itens.copy())
                itens.clear()
                sleep(0.5)
            except:
                print("Ocorreu um erro")
                sleep(0.5)
        elif escolha == 2:
            while True:
                print("\033[34m~~" * 20)
                print(f"\033[m{'ITENS':>23}")
                print("\033[34m~~\033[m"* 20)
                print(f'{"PRODUTO":<10} {"VALOR":>37}')
                print('-='*25)
                totalDeProdutos = []
                for item in range(len(produtos)):
                    produto = produtos[item]['Nome']
                    preco = produtos[item]['Valor']
                    print(f"[{item+1}]{produto:<13} {'R$':>28}{preco:.2f}".replace(".", ","))
                    totalDeProdutos.append(item+1)
                try:
                    escolherProduto = int(input('comprar produto(n): '))
                except:
                    escolherProduto = 0
                    print('Valor invalido')

                if escolherProduto not in (totalDeProdutos):
                    print('Produto não encontrado')
                    break

                print(f'O {produtos[escolherProduto-1]["Nome"]} Foi adicionado ao seu carrinho')
                mercado = deepcopy(produtos[escolherProduto - 1])
                carrinho.append(mercado)
                print('Comprar mais? \n[1]Sim\n[2]Não')
                continuar = int(input(':'))
                while continuar != 1 and continuar != 2:
                    continuar = int(input(':'))
                if continuar == 2:
                    break
            print('-'*50)
            sleep(0.5)
        elif escolha == 3:
            print(f'{"PRODUTO":<10} {"VALOR":>37} {"DESCONTO":>30}')
            print('-=' * 25)
            soma = 0
            try:
                if len(carrinho) == 0:
                    print("Nenhum produto encontrado")
                for c in range(len(carrinho)):
                    produto = carrinho[c]["Nome"]
                    preco = carrinho[c]["Valor"]
                    desconto = carrinho[c]["Desconto"]
                    if desconto == "":
                        desconto = 0
                    print(f'{produto:<13} {"R$":>30}{preco:.2f} {"":<5}{desconto:>20}%')
                    soma += preco
                    print('--' * 25)
                print(f"SOMA TOTAL: R${soma}".replace(".", ","))
            except:
                print("Nenhum produto encontrado")
            input("Enter para continuar")
            sleep(0.5)
        elif escolha == 4:
            for c in range(3):
                print('.', end='')
                sleep(0.3)
            print('\nObrigado por vir')
            break