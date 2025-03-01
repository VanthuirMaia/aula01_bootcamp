constante_atual = 1000

# Solicite ao usuario que digite seu nome
nome = input("Digite o seu nome: ")

# Solicite ao usuari oque digite o valor do seu salario
# Converta a entrada para um numero de ponto flutuante (float)
salario = float(input("Digite o valor do seu salario: "))

# Solicite ao usuario que digite o valor do bonus recebido
# Converta a entrada para um numero de ponto flutuante (float)
bonus = float(input("Digite o valor do bonus recebido: "))

# Caucule o valor do bonus final
bonus_final = constante_atual + salario * bonus

# Imprima o KPI para o usuario


print(f"O usuario {nome} tem um KPI de {bonus_final}")