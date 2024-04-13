lista = [-10, -8, 0, 1, 2, 5, -2,-4]

def achar_maior_elemento():
  maior_elemento = 0
  for numero in lista:
    if numero > maior_elemento:
      maior_elemento = numero;
  return maior_elemento;

def achar_menor_elemento():
  menor_elemento = 0
  for numero in lista:
    if numero < menor_elemento:
      menor_elemento = numero;
  return menor_elemento;

def media_da_lista():
  soma = 0
  for numero in lista:
    soma = soma + numero;
  media = soma / len(lista);
  return media;

print(lista)
while True:
  print("Menu:\n\t(a)para a maior \n\t(b)para a menor \n\t(c)temperatura media \n\tdigite 0 para encera o programa ");
  res = input('=>')
  if res == 'a':
    maior_elemento = achar_maior_elemento();
    print(f"Maior temperatura  == {maior_elemento}");
  if res == 'b':
    menor_elemeto = achar_menor_elemento();
    print(f"Menor temperatura == {menor_elemeto}");
  if res == 'c':
    media = media_da_lista();
    print(f'A media da tamperatura em MONS == {media}');
  if res == '0':
    break;
