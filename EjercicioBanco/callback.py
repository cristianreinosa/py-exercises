
def imprimir(valor):
    print(valor)

def calcular(base, altura, imprimir):
    area = base * altura
    imprimir(area)

base = 50
altura = 5

calcular(base, altura, imprimir)


salario = float(input("ingrese su salario"));


def aux_trans(salario, pago_neto):
    if(salario < 2320000):
        print(f"Salario Neto: {pago_neto + 140606}")
    else:
        print(f"Salario Neto: {pago_neto}")

def pago_neto(salario,aux_trans):
    eps = lambda salario: salario * 0.04
    pension = lambda salario: salario * 0.04
    pago_neto = salario - eps(salario) - pension(salario)
    aux_trans(salario, pago_neto)


pago_neto(salario, aux_trans)

