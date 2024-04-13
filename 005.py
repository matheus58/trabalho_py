lista = [9,8,7,12,0,13,21]
def lista_de_pares():
  pares=[];
  for numero in lista :
    if numero % 2 == 0 :
      pares.append(numero);
  return pares;
def lista_de_impares():
  impares=[]
  for numero in lista :
    if numero % 2 == 1 :
      impares.append(numero)
  return impares;

print("Menu:\n\tDigite 0 para encerrar o progrma\n\tDigite (a) para listar os numeros pares\n\tDigite (b)para listar os impares")
while True :
  res = input('=>')
  if res == 'a':
    pares = lista_de_pares();
    print(f'todos o numeros pares da lista sao {pares}');
  if res == 'b':
    impares = lista_de_impares();
    print(f'todos o numeros impares da lista soa {impares}')
  if res == '0':
    break;
  else :
    print('!!Digite Novamente!!')