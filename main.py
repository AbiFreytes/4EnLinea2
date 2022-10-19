from exception import NoSpace, NoValidNumber
from game import Rules
import pprint


def main():
    game = Rules()
    pprint.pprint(game.board)
    name_players(game)
    while True:
        cc = choose_col(game)
        if cc == False:
            break
        if game.check_winner() == True:
            pprint.pprint(f'El juego ha terminado. Felicitaciones: {game.winner}, has ganado')
            keep_playing = input('¿Quiere jugar otra vez?(Y/N): ')
            if keep_playing == 'Y' or keep_playing == 'y':
                game = Rules()
                pprint.pprint(game.board)
                name_players(game)
                continue
            else:
                break

def name_players(game):
    player1 = input('Seleccione un caracter que identifique al jugador 1 dentro del juego: ')
    player2 = input('Seleccione un caracter que identifique al jugador 2 dentro del juego: ')
    game.players(player1, player2)


def choose_col(game):
    try:
        col_input = input('Ingrese la columna en la que quiere colocar la ficha(ADVERTENCIA: comienza desde el 0 y termina en 7): ')
        if col_input == 'q':
            return False
        col_input = int(col_input)
        try:
            if game.insert_marker(col_input):
                pprint.pprint(game.board)
        except NoSpace:
            pprint.pprint('La columna esta llena, elija otra')
    except ValueError:
        pprint.pprint('No se ha ingresado un numero, intente nuevamente')
    except NoValidNumber:
        pprint.pprint('La columna ingresada no existe, intente nuevamente')


if __name__ == '__main__':
    main()
