# ## RM555189
# print("Bem vido a nossa loja")
# endereco_cliente = input("Digite seu endereço de entrega: ")
# ano_nascimento = input("Digite o seu ano de nascimento")
# idade = 2024 - int(ano_nascimento)
#
# if idade <18:
#     print("Vc é menor de idade e n pode beber ")
# else:
#     print("Selecione um dos vinhos da casa")
#     opcao = int(input("Digite o numero correspondete de sua preferencia"))
#     quantidade_garrafas = int(input("Quantas garrafas vc quer comprar?"))
#     print("1. Vinho Tinto")
#     print("2. Vinho seco")
#
#     if opcao ==1:
#             preco_unidade = 50
#     elif opcao ==2:
#             preco_unidade = 40
#
#     if preco_unidade > 0:
#             preco_total = quantidade_garrafas * preco_unidade
#
#     if preco_total >100:
#             frete = "parabens vc ganhou frete grais"
#     else:
#         preco_total +=10
#         frete = "Taxa inclusa no frete "
#
# print("Obrigado por comprar")
# print(f"Valor total da compra foi :R${preco_total:.2f}")
# print(f"Endereço de entrega : {endereco_cliente}")
# print(frete)
#

# # Mensagem de boas-vindas
# print("Bem-vindo(a) à nossa loja!")
# nome_cliente = input("Por favor, digite seu nome: ")
#
# # Perguntando o endereço
# endereco_cliente = input("Por favor, digite seu endereço de entrega: ")
#
# # Perguntando a data de nascimento
# ano_nascimento = int(input("Por favor, digite o ano do seu nascimento: "))
# idade = 2024 - ano_nascimento
#
# # Verificando se o cliente é menor ou maior de idade
# if idade < 18:
#     print("Desculpe, você é menor de idade e não pode comprar bebidas alcoólicas.")
# else:
#     print("Selecione uma das opções de vinho da casa:")
#     print("1. Vinho tinto premium")
#     print("2. Vinho branco seco")
#     opcao = int(input("Digite o número correspondente à sua escolha: "))
#
#     # Perguntando a quantidade de garrafas
#     quantidade_garrafas = int(input("Quantas garrafas você gostaria de comprar? "))
#
#     # Calculando o preço total
#     if opcao == 1:
#         preco_unitario = 50  # Preço do vinho tinto premium
#     elif opcao == 2:
#         preco_unitario = 40  # Preço do vinho branco seco
#     else:
#         preco_unitario = 0   # Opção inválida
#
#     if preco_unitario > 0:
#         preco_total = quantidade_garrafas * preco_unitario
#
#         # Verificando se há frete grátis
#         if preco_total > 100:
#             mensagem_frete = "Parabéns! Você tem direito a frete grátis."
#         else:
#             preco_total += 10  # Taxa de entrega
#             mensagem_frete = "Taxa de entrega de R$10,00 será aplicada."
#
#         # Mensagem de agradecimento com valor total e endereço de entrega
#         print("\nObrigado por sua compra, {}!".format(nome_cliente))
#         print("Valor total da compra: R${:.2f}".format(preco_total))
#         print("Endereço de entrega: {}".format(endereco_cliente))
#         print(mensagem_frete)
#     else:
#         print("Opção de vinho inválida. Por favor, selecione uma das opções disponíveis.")

# senha_cadastrada = '1234'
# senha = input('Diga a sua senha: ')
# tentativas = 1
# while senha != senha_cadastrada and tentativas <3:
#     print(f"vc é hacker ? So mais {3 - tentativas} tentativas")
#     senha = input("Diga sua senha: ")
#     tentativas += 1
# if senha == senha_cadastrada:
#     print("Acesso liberado")
# else:
#     print("Sai hacker")

# vinho1 = 'Chapinha'
# vinho2 = 'cantinho do vale '
# vinho3 = "Sangue de boi"
# print(f"nos temos:\n{vinho1}\n{vinho2}\n{vinho3}")
# opcao = input("Diga sua escolha")
# # while opcao != vinho1 and opcao != vinho2 and opcao != vinho3:
# #     print('Opção invalida')
# #     print(f"nos temos: \n{vinho1}\n{vinho2}\n{vinho3}")
# #     opcao = input("Diga sua escolha: ")
#
# while opcao == vinho1 or opcao == vinho2 or opcao == vinho3:
#     print('Opção invalida')
#     print(f"nos temos: \n{vinho1}\n{vinho2}\n{vinho3}")
#     opcao = input("Diga sua escolha: ")

# i =0
# soma = 0
# while i < 100:
#     i += 1
#     soma += i

# ex1
# nota = int(input("Diga uma nota entre 1 a 10"))
# while nota > 10:
#     nota = int(input("digite um numero"))
# print(f"sua nota é {nota}")

# ex2
# nome = input('Digite o seu nome: ')
# while len(nome) <= 3 :
#     print("Ele precisa ter mais que 3 caracteres! ")
#     nome = input('Digite o seu nome: ')
#
# idade = int(input("Digite a sua idade: "))
# while idade < 0 and idade > 150 :
#     print("Digite uma idade válida!")
#     idade = input("Digite a sua idade: ")
#
# salario = int(input("Digite o seu salário: "))
# while salario < 0 :
#     print("Digite um salário válido!")
#     salario = input("Digite o seu salário: ")
#
# sexo = input("Digite o seu sexo 'f' ou 'm': ")
# while sexo == "f" and "m" :
#     print("Digite um sexo válido (f ou m)!")
#     sexo = input("Digite o seu sexo 'f' ou 'm': ")
#
# estado = input("Digite o seu estado civil 's', 'c', 'v' ou 'd': ")
# while   estado != 's' and estado != 'c' and estado != 'v' and estado != 'd':
#     print("Digite um estado válido: (s, c, v ou d)!")
#     estado = input("Digite o seu estado civil 's', 'c', 'v' ou 'd': ")

# ex3
# populacaoA = 80000
# populacaoB = 200000
# ano = 0
# while populacaoA <populacaoB:
#     populacaoA += (populacaoB *3)/100
#     populacaoB += (populacaoA *1.5)/100
#     ano +=1
# print(f"serão necessario {ano} anos")

# ex4
# i = 1
# soma = 0
# while i <=5:
#     valor = float(input(f"Diga o {i}° valor: "))
#     soma += valor
#     media = soma /2
#     i += 1
# print(f"os seus numeros foram {media}")

# i = 0
# soma = 0
# while True :
#     num = int(input("diga um numero"))
#     soma += num
#     i + 1
#     if i==5:
#         break

# ex5
# num1 = int(input("digite um numero: "))
# num2 = int(input("digite um numero: "))
# if num1 > num2 :
#     aux = num1
#     num1 = num2
#     num2 = aux
#
# while num1 < num2 - 1:
#     num1 += 1
#     print(num1)

# ex6
# nome = input('Digite o seu nome: ')
# senha = input("Digite sua senha: ")
#
# while nome == senha:
#     print("o nome e senha não podem ser iguais!")
#     nome = input('Digite o seu nome: ')
#     senha = input("Digite sua senha: ")
# print(f"oi {nome}")

# ex7
# numero = int(input("digite um numero entre 1 e 10"))
# if numero < 1 or numero > 10:
#     print("Numero invalido. Digite um numero entre 1 e 10")
# else:
#     print(f"tabuada de {numero}: ")
#     contador = 1
#     while contador <= 10:
#         resultado = numero * contador
#         print(f"{numero} x {contador} = {resultado}")
#         contador += 1

# ex8
# n = int(input("Digite o numero que deseja gerar: "))
# if n <=0:
#     print("Numero invalido. Digite um numero maior que zero")
# else:
#     primeiro_termo = 1
#     segundo_termo = 1
#     contador = 2
#     print(f"serie ate o {n} termo")
#     print(primeiro_termo)
#     print(segundo_termo)
#     while contador < n:
#         prximo_termo = primeiro_termo + segundo_termo
#         print(prximo_termo)
#         primeiro_termo = segundo_termo
#         segundo_termo = prximo_termo
#         contador += 1

# ex 9
# quantidade_pares = 0
# quantidade_impares = 0
# contador = 0
# while contador < 10:
#     numero = int(input(f"Digite o numero inteiro:"))
#     if numero % 2 ==0:
#         quantidade_pares += 1
#     else:
#         quantidade_impares += 1
#     contador += 1
# print(f"quantidade de numeros pares: {quantidade_pares}")
# print(f"quantidade de numeros impares: {quantidade_impares}")

# ex10
# valor = int(input("Digite um valor: "))
# resultado = 1
# contador = 1
# while contador <= valor:
#     resultado *= contador
#     contador += 1
# print(resultado)

# ex11
valor = int(input("digite um numero inteiro"))
while True :
    if valor /1:
        print("é primo")
        break
    else:
        print("não é primo")
        break

