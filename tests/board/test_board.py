import numpy as np
from evottt.ttt.board import Board, GameResult

def test_position_is_empty():
    board = Board()
    assert board.position_is_empty(0)
    assert board.position_is_empty(1)
    assert board.position_is_empty(2)
    assert board.position_is_empty(3)
    assert board.position_is_empty(4)
    assert board.position_is_empty(5)
    assert board.position_is_empty(6)
    assert board.position_is_empty(7)
    assert board.position_is_empty(8)

    board.apply_move(0, 0)
    assert not board.position_is_empty(0)
    board.apply_move(5, 0)
    assert not board.position_is_empty(5)

def test_position_contains_player():
    board = Board()
    for position in range(9):
        assert not board.position_contains_player(position, 0)
        assert not board.position_contains_player(position, 1)

    board.apply_move(0, 0)
    board.apply_move(4, 1)
    board.apply_move(8, 0)
    assert board.position_contains_player(0, 0)
    assert board.position_contains_player(4, 1)
    assert board.position_contains_player(8, 0)

def test_valid_moves_empty_board():
    board = Board()
    assert board.get_valid_moves() == 0b111111111

def test_valid_moves_non_empty_board():
    board = Board()

    board.apply_move(0, 0)
    assert board.get_valid_moves() == 0b111111110

    board.apply_move(4, 1)
    board.apply_move(5, 0)
    assert board.get_valid_moves() == 0b111001110

def test_player_wins():
    board = Board()
    assert board.get_result() == GameResult.ONGOING

    board.apply_move(0, 0)
    board.apply_move(1, 0)
    board.apply_move(2, 0)
    assert board.get_result() == GameResult.X_WINS

    board = Board()
    board.apply_move(0, 1)
    board.apply_move(1, 1)
    board.apply_move(2, 1)
    assert board.get_result() == GameResult.O_WINS

    board = Board()
    board.apply_move(0, 1)
    board.apply_move(1, 0)
    board.apply_move(2, 1)
    assert board.get_result() == GameResult.ONGOING

def test_horizontal_wins():
    board = Board()
    board.apply_move(0, 0)
    board.apply_move(3, 0)
    board.apply_move(6, 0)
    assert board.get_result() == GameResult.X_WINS

    board = Board()
    board.apply_move(1, 0)
    board.apply_move(4, 0)
    board.apply_move(7, 0)
    assert board.get_result() == GameResult.X_WINS

    board = Board()
    board.apply_move(2, 0)
    board.apply_move(5, 0)
    board.apply_move(8, 0)
    assert board.get_result() == GameResult.X_WINS

def test_vertical_wins():
    board = Board()
    board.apply_move(0, 0)
    board.apply_move(1, 0)
    board.apply_move(2, 0)
    assert board.get_result() == GameResult.X_WINS

    board = Board()
    board.apply_move(3, 0)
    board.apply_move(4, 0)
    board.apply_move(5, 0)
    assert board.get_result() == GameResult.X_WINS

    board = Board()
    board.apply_move(6, 0)
    board.apply_move(7, 0)
    board.apply_move(8, 0)
    assert board.get_result() == GameResult.X_WINS

def test_diagonal_wins():
    board = Board()
    board.apply_move(0, 0)
    board.apply_move(4, 0)
    board.apply_move(8, 0)
    assert board.get_result() == GameResult.X_WINS

    board = Board()
    board.apply_move(2, 0)
    board.apply_move(4, 0)
    board.apply_move(6, 0)
    assert board.get_result() == GameResult.X_WINS

def test_get_position():
    board = Board()
    for position in range(9):
        assert board.get_position(position) == 2

    board.apply_move(0, 0)
    assert board.get_position(0) == 0
    assert board.get_position(1) == 2

    board.apply_move(1, 1)
    assert board.get_position(0) == 0
    assert board.get_position(1) == 1
    assert board.get_position(2) == 2

def test_get_neural_representation():
    board = Board()
    assert np.array_equal(board.get_neural_representation(), np.array([0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=float))

    board.apply_move(0, 0)
    assert np.array_equal(board.get_neural_representation(), np.array([1, 0, 0, 0, 0, 0, 0, 0, 0], dtype=float))

    board.apply_move(1, 1)
    assert np.array_equal(board.get_neural_representation(), np.array([1, -1, 0, 0, 0, 0, 0, 0, 0], dtype=float))

    board.apply_move(8, 0)
    board.apply_move(5, 1)
    assert np.array_equal(board.get_neural_representation(), np.array([1, -1, 0, 0, 0, -1, 0, 0, 1], dtype=float))

    board.apply_move(6, 1)
    board.apply_move(7, 1)
    assert np.array_equal(board.get_neural_representation(), np.array([1, -1, 0, 0, 0, -1, -1, -1, 1], dtype=float))
