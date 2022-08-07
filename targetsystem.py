'''
Exercicio 1
'''
indice=13
soma=0
k=0

while k <indice:
    k=k+1
    soma= soma+k

# 91
print(soma)

'''
Exercicio 2
'''
n = int(input("Pertence a sequencia de fibonacci?"))
seq=[]
def rec_fib(n):
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
    return n

def fibonacci(n):
    for i in range(10):
        seq.append(rec_fib(i))
        #print(seq)

fibonacci(n)

for i in seq:
    if i<=n:
        if i==n:
            print("Pertence a sequencia de fibonacci")
            break
    else:
        print("Não pertence a sequencia")
        break
''''''
'''
Exercicio 5
'''
texto="FAÇA O SEU MELHOR ENQUANTO NÃO PUDER FAZER ALGO MELHOR AINDA"
tam = len(texto)
for i in range(1,len(texto)+1):
    print(texto[tam-i],end='')
