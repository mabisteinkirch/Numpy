
#criação utilizando funções
#forma automatica - criação do tamanho que vc gostaria
#ex 0 - 99
#primeiro parametro, final, de quanto em quanto quer que incremente - passo/intervalo
#o final nao conta, vai sempre um a menos - igual a função range do python
c = np.arange(0, 100, 1)

print(c)

#só um parametro
#coloca ate onde termina, que nao inclue ele e faz o passo ser um por default
d = np.arange(10)


#dois parametros
#inicia no 10 e vai ate 19 de um em um
e = np.arange(10, 20)

# permite um array uniformemetnte espaçado e define quantos elementos vc qr em um determinado intervalo
f = np.linspace (1, 10, 10)
# 1 inicio, 2 fim inclue o numero que termina, quantos elementos vc quer entre 1 a 10
print('-='*50)

#4 parametro para nao incluir o final... nao inclui o 10
f = np.linspace (1, 10, 10, endpoint=False)

#arrays comuns

#10 uns
a = np.ones (10)

#usa o shape para criar essa função
a = np.ones ((10, 10))

#10 zeros
a = np.zeros (10)
a = np.zeros ((10, 10))
print (a)

#radom
#numeros aleatorios de 0 a 1
h = np.random.rand(10)
print (h)
#nao usa o shape nesse caso
h = np.random.rand(10, 10)
print (h)

#cria uma matriz identidade
m = np.eye (3)

#cria uma matriz identidade e vc tem que falar qual a matriz que quer cocoar na diagnonal
m = np.diag (np.array([1, 2, 3, 4]))
print (m)