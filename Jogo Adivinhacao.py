from random import randint

seu_nome = input('Olá, qual seu nome?')
print(
    f'Okay! {seu_nome}, eu estou escolhendo um número de 1 até 10, você consegue adivinhar? '

)
numero_adivinhado = randint(1, 10)
numero_tentativas = 3 

for tentativa in range(1, numero_tentativas + 1):
  numero_escolhido = int(input('escolha um número'))
  if numero_escolhido == numero_adivinhado:
    print(f'Parabéns, você acertou em {tentativa} tentativas!')
    break 
  elif numero_escolhido > numero_adivinhado:
    print('Escolha um número menor!')
  else:
    print('Escolha um número maior!')
print(f'O número era {numero_adivinhado}. Obrigado por jogar!')
