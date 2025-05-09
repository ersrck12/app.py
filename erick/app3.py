#python
# jogo da velha (tic tac toe) em python
# tabuleiro representado por uma lista de 9 posicoes (inicialmente vazias)
board = ['' for _ in range (9)]
def print_board():
    """
    
    exibe o tabuleiro atual formatado com as marcaçoedos jogadores
    formato:
    | X | o | X |
    | o | o | o |
    | X | o | X |
    """

    #cria cada linha do tabuleiro usando a formaçao de string
    row = '|  {}  |  {}  |  {}  |'.format(board [0], board[1], board[2])