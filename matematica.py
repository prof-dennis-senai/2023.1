def soma(x,y) -> int:
    if isinstance(x, str):
        try:
            x = float(x)
        except:
            x = int(x)

    if isinstance(y, str):
        try:
            y = float(y)
        except:
            y = int(y)

    
    return x+y

def subtracao(x,y):
    return x-y

def multiplicacao(x,y):
    return x*y

def divisao(x,y):
    return x/y