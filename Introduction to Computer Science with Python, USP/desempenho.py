# Comparar o desempenho de dois algorítimos utilizando o módulo time.
import random
import time
def selectionsort(lista):
  size=len(lista)
  for(step)in(range(size)):
    min_idx=step
    for(i)in(range(step+1,size)):
      if(lista[i])<(lista[min_idx]):
        min_idx=i
    (lista[step],lista[min_idx])=(lista[min_idx],lista[step])
  return lista
def bubblesort(lista):
  fim=len(lista)
  for(i)in(range(fim-1,0,-1)):
    for(j)in(range(i)):
      if(lista[j])>(lista[j+1]):
        (lista[j]),(lista[j+1])=(lista[j+1]),(lista[j])
  return lista
def lista_aleatoria(self,n):
  lista=[(0)for(each)in(range(n))]
  for(i)in(range(n)):
    lista[i]=random.randrange(1000)
    return lista
def compara_sort(self,n):
  lista_1=lista_aleatoria(self, n)
  lista_2=lista_1[:]
  before=time.time()
  bubblesort(lista_1)
  after=time.time()
  print('Desempenho da bubblesort: ',after-before)
  before=time.time()
  selectionsort(lista_2)
  after=time.time()
  print('Desempenho da selectionsort: ',after-before)
class classe:
  lista=[]
  compara_sort(lista,1000)
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!