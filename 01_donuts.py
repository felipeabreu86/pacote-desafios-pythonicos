"""
01. donuts

Dado um contador inteiro do numero de donuts, retorne uma string
com o formato 'Number of donuts: <count>' onde <count> é o numero
recebido. Entretanto, se o contador for 10 ou mais, use a palavra 'many'
ao invés do contador.
Exemplo: donuts(5) retorna 'Number of donuts: 5'
e donuts(23) retorna 'Number of donuts: many'
"""


def donuts(count):
    if not isinstance(count, int):
        return 'Number of donuts must be an integer'
    elif count < 0:
        return 'Number of donuts must be greater than or equal to zero'
    else:
        return f'Number of donuts: {count if count < 10 else "many"}'


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(donuts, -1, 'Number of donuts must be greater than or equal to zero')
    test(donuts, 0, 'Number of donuts: 0')
    test(donuts, 4, 'Number of donuts: 4')
    test(donuts, 9, 'Number of donuts: 9')
    test(donuts, 10, 'Number of donuts: many')
    test(donuts, 99, 'Number of donuts: many')
    test(donuts, 10.2, 'Number of donuts must be an integer')
    test(donuts, 'test', 'Number of donuts must be an integer')
