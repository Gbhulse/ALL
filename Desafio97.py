def escreva(txt):
    cont = len(txt)
    for c in range(0, cont):
        print('-=', end=(''))
    print('')
    print(txt)
    for c in range(0, cont):
        print('-=', end=(''))
    print('')


escreva('Amor')
escreva('Amor i love you xoxo')