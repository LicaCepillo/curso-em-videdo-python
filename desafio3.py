# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

n1 = int(input('Digite um número :'))
ante = n1 - 1
suce = n1 + 1
print('O antecessor do número digitado é {}, e o seu sucessor é {}'.format(ante,suce))

# Crie um algorítimo que leia um número e mostre o seu dobro, seu tripo e a raiz quadrada

n2 = int(input('Digite um número :'))
d = n2 * 2
t = n2 * 3
rq = n2**(1/2)
print('O dobro do número digitado é {}\n o triplo  é {}\n e sua raiz quadrada é {}'.format(d,t,rq))


# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1+nota2)/2

print('A média do aluno é {}'.format(media))

# Escreva um programa que leia um valor em metros e o exiba convertido em cemtímetros e milímetros.

metro = float(input('Digite um valor em metros: '))
cm = metro/100
mm = metro / 1000
print('A conversão do valor digitado é {} cm e {} mm'.format(cm,mm))