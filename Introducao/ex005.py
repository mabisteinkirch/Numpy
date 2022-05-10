import numpy as np

#criação utilizando funções
#forma automatica - criação do tamanho que vc gostaria
#ex 0 - 99
#primeiro parametro: onde começa, segundo parametro: onde termina, terceiro paramero: passo/intervalo
#o final nao conta, vai sempre um a menos - igual a função range do python
a = np.arange(0, 100, 1)

print(a)