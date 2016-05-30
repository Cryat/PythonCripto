# Daniela Duarte nr 78542 / Joao Esteves nr 78304 / Pedro Guerreiro nr 78264

def calcula_e (n):
    '''
    calcula_e : int --> int
    calcula_e (n) devolve o primeiro numero co-primo com n
    '''
    if isinstance (n,int) and n > 0:
        for e in range (2, n+1):
            if n % e != 0:
                return e
    else:
        raise ValueError ( 'calcula_e: n nao e um numero inteiro positivo')
# Ciclo comeca no numero 2, ou seja o primeiro numero  por qual (n) podera ou nao ser divisivel por e, o ciclo termina quando (n) nao for divisivel por (e).


def calcula_d (e,n):
    '''
    calcula_d : int x int --> int
    calcula_d (e, n) devolve o valor de d, que respeita a condicao 
    (d * e == n * k + 1)
    '''
    if isinstance (e,int) and isinstance (n,int) and e > 0 and n >0 :
        k = calcula_k (e, n)
        d = (n * k + 1) // e
        return d
# Atraves do k que e obtido na funcao calcula_k a funcao calcula_d resolve a expressao d = (n * k + 1) // e.
        
def calcula_k (e, n):
    '''
    calcula_k : int x int --> int
    calcula_k (e, n) devolve o valor de k de modo a que este seja um numero 
    inteiro e respeite a condicao (d * e == n * k + 1)
    '''
    for k in range (1, n + 1):
        if (n * k + 1)% e == 0:
            return k
# A funcao calcula k de modo a que n * k + 1)% e == 0 para que seja possivel que d tome um valor inteiro positivo.

def crivo(n):
    '''
    crivo : int --> list
    crivo (n) devolve uma lista com todos os numeros primos menores que n
    '''
    if isinstance (n, int):
        lista = list(range(2, n+1))
        i = 0
        while lista[i] <= int(pow(n,1/2)):
            remove_multiplos(lista, i)
            i = i + 1
        return lista
    # O ciclo termina quando o elemento de indice i da lista de primos for menor ou igual que a raiz quadrada de (n) tal como e descrito o processo de procura de primos pelo crivo de Erastotenes, ou seja para-se de remover multiplos uma vez que a condicao lista[i] <= int(pow(n,1/2)) seja infrigida.

def remove_multiplos(lista, i):
    '''
    remove_multiplos : lista x int --> lista (embora nao exista um return)
    remove multiplos (lista, i) remove todos os numeros nao primos da lista
    que recebe
    '''
    for j in range(len(lista)-1, i, -1):
        if lista[j] % lista[i] == 0:
            del(lista[j])
    # Durante este ciclo for sempre que o elemento de indice j da lista for divisivel pelo elemento de indice i e eliminado o elemento de indice j da lista.
            
def calcula_esimo_primo(n):
    '''
    calcula_esimo_primo : int --> int
    calcula_esimo_primo (n) devolve o n-esimo numero primo
    '''
    lista= crivo(n*10)
    return lista[n-1]
# Utilizando o resultado obtido pelo crivo, ou seja uma lista de numeros primos, esta funcao selecciona o primo pretendido atraves de um indice dado.

def encripta (N,i,j):
    '''
    encripta : int x int x int --> int
    encripta (N, i, j) devolve a mensagem encriptada utilizando i e j como os 
    primos geradores da chave e N como a mensagem original
    '''
    if isinstance (N, int) and isinstance (i, int) and isinstance (j, int) and N > 0 and i > 0 and j > 0:
        m = calcula_m (i, j)
        n = calcula_n (i, j)
        e = calcula_e(n)
        if N < m :
            C = (N**e)% m
            return C
        else:
            raise ValueError ("encripta: a mensagem tem de ser inferior a "+str(m))
# Utiliza as funcoes calcula_m , calcula_n , e calcula_e.

def decifra (C, i, j):
    '''
    decifra : int x int x int --> int
    decifra (C, i, j): devolve o valor da mensagem original que tivera sido
    encriptada utilizando i e j como geradores da chave e C como a mensagem 
    encriptada
    '''
    if isinstance (C, int) and isinstance (i, int) and isinstance (j, int) and C > 0 and i > 0 and j > 0:
        m = calcula_m (i, j)
        n = calcula_n (i, j)
        e = calcula_e (n)
        d = calcula_d (e, n)
        if C < m:
            N = (C**d) % m
            return N
        else:
            raise ValueError ("decifra: a mensagem tem de ser inferior a "+str(m))
        
# Utiliza as funcoes calcula_m , calcula_n , calcula_e , e calcula_d.
    

def calcula_m (i, j):
    '''
    calcula_m : int x int --> int
    calcula_m (i, j) devolve o valor de m que resulta da multiplicacao
    do i-esimo primo com o j-esimo primo
    '''
    m = (calcula_esimo_primo (i)) * (calcula_esimo_primo (j))
    return m

def calcula_n (i , j):
    '''
    calcula_n : int x int --> int
    calcula_n (i, j) devolve o valor de n que resulta da multiplicacao do
    i-esimo primo -1 com o j-esimo primo -1
    '''    
    n = (calcula_esimo_primo (i)-1) * (calcula_esimo_primo (j)-1)
    return n
  