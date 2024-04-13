lista = [12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]

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
def achar_numeros_pares():
  pares = []
  for numero in lista:
    if numero % 2 == 0:
      pares.append(numero)
  return pares ;
def ocorencias_do_primeiro_numero():
  con = 0
  for numero in lista:
      if numero == 12:
          con += 1
  return con
def media_da_lista():
  soma = 0
  for numero in lista:
    soma = soma + numero;
  media = soma / len(lista);
  return media;


def soma_dos_elementos_negativos():
  soma = 0;
  for numero in lista:
    if numero < 0:
      soma = numero + soma;
  return soma


print(lista)
while True :

  print("*************************************************************************");
  print("menu: \na.maior element \nb.menor elemento\nc.numeros pares\nd.número de ocorrências do primeiro elemento da lista\ne. média dos elementos\nf.soma dos elementos de valor negativo\n!digite 0 para sair !");
  res = input("=>")

  if res == 'a':
    maior_elemento = achar_maior_elemento();
    print(f"Maior elemento da lista  == {maior_elemento}");
  if res == 'b':
    menor_elemeto = achar_menor_elemento();
    print(f"Menor elemento da lista == {menor_elemeto}");
  if res == 'c':
    numeros_pares = achar_numeros_pares();
    print(f"Numeros parares da lista {numeros_pares}") ;
  if res == 'd':
    ocorencias_do_primeiro = ocorencias_do_primeiro_numero();
    print(f"Numero de ocorencisa do primeiro numero e {ocorencias_do_primeiro}");
  if res == 'e':
    media = media_da_lista();
    print(f"A media da lista e {media}") ;
  if res == 'f':
    soma_dos_negativos = soma_dos_elementos_negativos();
    print(f"A soma do elementos negativos e {soma_dos_negativos}");
  if res == '0':
    break;
  else:
    print();