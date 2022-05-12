
#nao usa o shape nesse caso
h = np.random.rand(10, 10)
print (h)

#cria uma matriz identidade
m = np.eye (3)

#cria uma matriz identidade e vc tem que falar qual a matriz que quer cocoar na diagnonal
m = np.diag (np.array([1, 2, 3, 4]))
print (m)

#aula3
#indexação e cortes (slice) de arrays
e = np.arange(10,20)

a [0]
a [-11] #?

h = np.random.rand(3, 3)

h[0] #primeira linha e todas as colunas
h[0][1]

#mudar o valor
h[0][1] = 2
print(h)

#posição x ate y - slice
#nao inclui a ultima posição
print(e[3:5])
print(e[2:]) #vai ate o final

#slice com mais de uma dimensão
print(h[0:2,1])
print(h[0:2]) #pega as duas primeiras linhas toda - todas as colunas
print(h[0:2, 3]) #pega as duas primeiras linhas toda - terceira colunas

#passo
e = np.arange(10,20)
print(e[2:9]) #começa posicao 2 ate 8 indo de 1 em um
print(e[2:9:2]) #começa posicao 2 ate 8 pulando de 2 em 2
print(e[8:2:-1]) #começa posicao 8 ate 3 invertido com passo 1

#imagem
from skimage