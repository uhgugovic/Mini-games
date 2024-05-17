import tkinter as tk
from tkinter import ttk

from mini_games import sum_game, game_2048, snake, tetris, minesweeper, slot_machine, tic_tac_toe


class GameLauncher:
    def __init__(self, master):
        # Инициализация основного окна программы
        self.master = master
        master.title("Программа запуска игр")
        master.geometry("400x540")

        # Настройка стилей
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), padding=10)
        style.configure("TLabel", font=("Helvetica", 14), padding=10)
        style.configure("TFrame", background="#f0f0f0")

        # Список игр
        self.game_list = [
            ("2048", self.start_2048_game),
            ("Сумма", self.start_sum_game),
            ("Змейка", self.start_snake_game),
            ("Тетрис", self.start_tetris_game),
            ("Сапер", self.start_minesweeper_game),
            ("Слот-машина", self.start_slot_machine_game),
            ("Крестики-нолики", self.start_tic_tac_toe_game),
        ]

        # Настройка интерфейса
        self.setup_ui()

    def setup_ui(self):
        # Создание основного фрейма
        main_frame = ttk.Frame(self.master, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Заголовок
        title_label = ttk.Label(main_frame, text="Выберите игру для запуска")
        title_label.pack(pady=10)

        # Фрейм для кнопок
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        # Создание кнопок для каждой игры
        for game_name, game_command in self.game_list:
            button = ttk.Button(button_frame, text=game_name, command=game_command)
            button.pack(pady=5, fill=tk.X)

    def start_sum_game(self):
        # Запуск игры "Сложение чисел"
        game = sum_game.SumGame()
        game.start_game()

    def start_2048_game(self):
        # Запуск игры "2048"
        game = game_2048.Game2048()
        game.start_game()

    def start_snake_game(self):
        # Запуск игры "Змейка"
        game = snake.SnakeGame()
        game.start_game()

    def start_tetris_game(self):
        # Запуск игры "Тетрис"
        game = tetris.TetrisGame()
        game.start_game()

    def start_minesweeper_game(self):
        # Запуск игры "Сапер"
        game = minesweeper.MinesweeperGame()
        game.start_game()

    def start_slot_machine_game(self):
        # Запуск игры "Слот-машина"
        game = slot_machine.SlotMachineGame()
        game.start_game()
        
    def start_tic_tac_toe_game(self):
        # Запуск игры "Крестики-нолики"
        game = tic_tac_toe.TicTacToeGame()
        game.start_game()
