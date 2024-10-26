# faça um programa que leia dados do usuario
# questao =int(input('Digite um numero 1 ou 2 '))
# if(questao == 1):
#  nome = input('nome ')
#  sobrenome = input('sobrenome ')
#  idade = int(input('idade '))
#  listaA = [nome, sobrenome, idade]
#  print(listaA[2])


# # Faça um programa onde o usuario informa um numero de 1 a 12 em seguida imprima qual mes que se refere
# else: 
    
#  listames = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
#  n = int(input('Digite um número de 1 a 12 referente ao mes '))
#  n = n - 1

# print(listames[n])


#extra: Faça um menu onde o usuario consiga selecionar qual questao quer executar


# class Usuario():
#     def __init__(self, nome, sobrenome, idade):
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.idade = idade
# usuarioabc = Usuario(input("Nome do usuario: "))
# print(usuarioabc.idade)

# class Vendedor:
#     def __init__(self, nome,sobrenome, idade, cidade):
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.idade = idade
#         self.cidade = cidade
#     def informacaoSaida(self):
#         print(f'Olá, meu nome é',self.nome,'Meu sobrenome é',self.sobrenome, ', tenho ',self.idade, 'e moro em', self.cidade)
# vendedor1 = Vendedor(input('Nome: '),input('sobrenome: '),input('idade: '),input('ciade: '))
# vendedor2 = Vendedor(input('Nome: '),input('sobrenome: '),input('idade: '),input('ciade: '))

# vendedor1.informacaoSaida()
# vendedor2.informacaoSaida()

#Criar uma classe chamada "carro" com os aributos marca, ano e cor.Em seguida, crie um objeto dessa classe e imprima os atributos
# class Carro:
#     def __init__(self, marca, ano, cor):
#       self.marca = marca
#       self.ano = ano
#       self.cor = cor
#     def informacaoSaida(self):
#       print(f'A marca do carro é: ', self.marca, 'o ano do carro e: ',self.ano, 'possui a cor ', self.cor)

# especificacao1 = Carro(input('marca: '),input('ano: '),input('cor: '))
# especificacao2 = Carro(input('marca: '),input('ano: '),input('cor: '))

# especificacao1.informacaoSaida()
# especificacao2.informacaoSaida()

class Pessoa:
   def __init__(self, nome, sobrenome, cpf , idade, cidade):
      self.nome = nome
      self.sobrenome = sobrenome
      self.cpf = cpf
      self.idade = idade
      self.cidde = cidade
   def informacaoSaida(self):
      print(f' O nome do usuario é: ',self.nome,'sobrenome: ', self.sobrenome,'com o cpf', self.cpf,'com idade: ',self.idade,'e mora em: ',self.cidade)

dados1 = Pessoa(input('nome: '), input('sobrenome: '), input('cpf: '), input('idade: '), input('cidade: '))
dados2 = Pessoa(input('nome: '), input('sobrenome: '), input('cpf: '), input('idade: '), input('cidade: '))  

dados1.informacaoSaida()
dados2.informacaoSaida()
