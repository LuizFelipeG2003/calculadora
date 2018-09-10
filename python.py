A = int(input('Digite o primeiro numero: '))
B = int(input('Digite o segundo numero: '))
operaçao = input('Diga qual a operaçao: ')

if operaçao == "+":
	print('A soma do primeiro numero e do segundo numero e igual a {}'.format(A + B))
elif operaçao == "-":
	print('A subtraçao do primeiro numero e do segundo e igual a {}'.format(A - B))	
elif operaçao == "*":
	print('A multiplicaçao do primeiro numero e do segundo e igual a {}'.format(A * B))
elif operaçao == "/":
	print('A divisao do primeiro numero e do segundo e igual a {}'.format(A / B))
