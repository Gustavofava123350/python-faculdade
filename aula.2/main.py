preco_ingresso = 25.00
ingressos_disponiveis = 100

print(f"Bem-vindo à Bilheteria! O preço do ingresso é R${preco_ingresso:.2f} e temos {ingressos_disponiveis} ingressos disponíveis.")

# Perguntar idade
idade = int(input('Digite sua idade: '))

# Verificação de maioridade
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

# Recomendação de filmes
if idade <= 12:
    print('Recomendação de filmes para crianças')
elif idade <= 17:
    print('Recomendação de filmes para adolescentes')
else:
    print('Recomendação de filmes para adultos')

# Compra de ingressos (apenas adultos)
if idade >= 18:
    quantidade_desejada = int(input('Digite a quantidade de ingressos que deseja comprar: '))

    if quantidade_desejada > 0 and quantidade_desejada <= ingressos_disponiveis:
        total_preco = quantidade_desejada * preco_ingresso
        ingressos_disponiveis -= quantidade_desejada
        print(f'Compra realizada com sucesso! O total é R${total_preco:.2f}.')
        print(f'Restam {ingressos_disponiveis} ingressos disponíveis.')
    elif quantidade_desejada > ingressos_disponiveis:
        print(f'Desculpe, só temos {ingressos_disponiveis} ingressos disponíveis.')
    else:
        print('Quantidade de ingressos inválida.')
