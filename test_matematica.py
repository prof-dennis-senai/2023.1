from matematica import soma
def test_soma_numero_inteiros():
    assert soma(0,0) == 0, 'Na operação de soma de 0 + 0, o resultado deve ser 0!'
    assert soma(1,1) == 2, 'Na operação de soma de 1 + 1, o resultado deve ser 2!'
    assert soma(-2,2) == 0, 'Na operação de soma de -2 + 2, o resultado deve ser 0!'
    assert soma(10,-3) == 7, 'Na operação de soma de 10 + -3, o resultado deve ser 7!'
    assert soma(-1,-1) == -2, 'Na operação de soma de -1 + -1, o resultado deve ser -2!'

def test_soma_numeros_decimais():
    assert soma(0.0,0.0) == 0.0, 'Na operação de soma de 0.0 + 0.0, o resultado deve ser 0.0!'
    assert soma(1.1,1.1) == 2.2, 'Na operação de soma de 1.1 + 1.1, o resultado deve ser 2.2!'
    assert soma(-2.2,2.2) == 0.0, 'Na operação de soma de -2.2 + 2.2, o resultado deve ser 0.0!'
    assert soma(10.5,-3.5) == 7.0, 'Na operação de soma de 10.5 + -3.5, o resultado deve ser 7.0!'
    assert soma(-1.0,-1.0) == -2.0, 'Na operação de soma de -1.0 + -1.0, o resultado deve ser -2.0!'

def test_soma_numeros_strings():
    assert soma('0','0') == 0, 'Na operação de soma de 0 + 0, o resultado deve ser 0!'
    assert soma('1','1') == 2, 'Na operação de soma de 1 + 1, o resultado deve ser 2!'
    assert soma('-2','2') == 0, 'Na operação de soma de -2 + 2, o resultado deve ser 0!'
    assert soma('10','-3') == 7, 'Na operação de soma de 10 + -3, o resultado deve ser 7!'
    assert soma('-1','-1') == -2, 'Na operação de soma de -1 + -1, o resultado deve ser -2!'
    assert soma('10.5','-3.5') == 7.0, 'Na operação de soma de 10.5 + -3.5, o resultado deve ser 7.0!'
    assert soma('10.5','-3.8') == 6.7, 'Na operação de soma de 10.5 + -3.5, o resultado deve ser 6.7!'