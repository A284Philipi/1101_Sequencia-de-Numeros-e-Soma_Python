cont = int(0)
while cont == 0:
    a, b = input().split(" ")
    a = int(a)
    b = int(b)
    if (a < 1 or b < 1):
        cont = 1
    else:
        if (a < b):
            c = int()
            c = a
            a = b
            b = c
        lista = []
        soma = int(0)
        while b <= a:
            lista.append(b)
            soma = soma + b
            b = b + 1
        separador = ' '
        print(separador.join(map(str, lista)), 'Sum={}'.format(soma))