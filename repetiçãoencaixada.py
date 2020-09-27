"""
Devolve o fatorial do número digitado. 
Finaliza após receber o número 0.
"""

numero_digitado = 1 

while numero_digitado != 0:

	numero_digitado = int(input("Digite um número: "))
	
	fatorial = 1
	numero = numero_digitado
	while numero>0:
		fatorial = numero * fatorial
		numero = numero - 1
		
	print (fatorial)