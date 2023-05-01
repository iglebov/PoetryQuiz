# Импортируем модуль "random" для случайного выбора стихотворений
import random

# Импортируем модуль tkinter для создания графического интерфейса
import tkinter as tk
from tkinter import ttk

# Импортируем словарь со стихотворениями
from extra.poetry import poetry_dict


class PoetryQuizInterface:
    # Создаём графический интерфейс
    root = tk.Tk()
    root.title("Poetry Quiz")
    root.configure(background="gray")
    root.geometry("900x600")
    # Переменная для вывода строк стихотворения
    poetry_part = tk.StringVar()
    # Лист с названиями всех стихотворений
    poetry_titles = [element for element in poetry_dict.keys()]
    # Переменная для хранения названия стихотворения
    poetry_showing_name = ""
    # Лист для строк стихотворения
    poetry_showing = []
    # Прохождение стихотворения (актуальный шаг)
    step = 0
    # Граница стихотворения (последний шаг)
    last_step = 0
    # Счетчик допущенных игроком ошибок
    mistakes = 0

    @staticmethod
    def start_ui() -> None:
        """Запускает интерфейс."""
        PoetryQuizInterface.root.mainloop()

    @staticmethod
    def destroy_ui() -> None:
        """Закрывает интерфейс."""
        PoetryQuizInterface.root.destroy()

    @staticmethod
    def play_game() -> None:
        """Создает основное окно для стихотворения."""
        # Скрываем детали меню
        PoetryQuizInterface.hide_elements(
            PoetryQuizInterface.start_label,
            PoetryQuizInterface.start_button,
            PoetryQuizInterface.exit_button,
            PoetryQuizInterface.poetry_button,
        )
        # Выбираем стихотворение
        PoetryQuizInterface.poetry_showing_name = random.choice(
            list(poetry_dict.keys())
        )
        PoetryQuizInterface.poetry_showing = poetry_dict[
            PoetryQuizInterface.poetry_showing_name
        ]
        PoetryQuizInterface.last_step = len(PoetryQuizInterface.poetry_showing)
        # Выводим строки стихотворения
        PoetryQuizInterface.poetry_part.set(
            PoetryQuizInterface.poetry_showing[PoetryQuizInterface.step]
        )
        PoetryQuizInterface.poetry_label.configure(font="Arial 26")
        PoetryQuizInterface.poetry_label.pack(fill="both", expand=True)
        # Настраиваем кнопки для ответов
        PoetryQuizInterface.set_all_buttons(
            poetry_showing_name=PoetryQuizInterface.poetry_showing_name,
            poetry_showing=PoetryQuizInterface.poetry_showing,
            step=PoetryQuizInterface.step,
        )
        # Размещаем кнопки для ответов
        PoetryQuizInterface.place_elements(
            PoetryQuizInterface.first_answer_button,
            PoetryQuizInterface.second_answer_button,
            PoetryQuizInterface.third_answer_button,
            PoetryQuizInterface.another_poetry,
            PoetryQuizInterface.go_back_button
        )

    @staticmethod
    def open_poetry_menu() -> None:
        """Открывает меню со стихотворенями."""
        # Убираем лишние элементы интерфейса
        PoetryQuizInterface.hide_elements(
            PoetryQuizInterface.start_label,
            PoetryQuizInterface.start_button,
            PoetryQuizInterface.exit_button,
            PoetryQuizInterface.poetry_button,
        )
        # ComboBox для выбора стихотворения
        PoetryQuizInterface.poetry_choices.pack(side="top", expand=2)
        # Кнопка для возвращения в меню
        PoetryQuizInterface.go_back_button.pack(side="bottom", expand=2)

    @staticmethod
    def open_poetry(event: tk.Event) -> None:
        """Выводим стихотворение из списка."""
        # Получаем все строки стихотворения
        poetry_rows = poetry_dict[PoetryQuizInterface.poetry_choices.get()]
        # "Собираем" стихотворение
        poetry = PoetryQuizInterface.build_poetry(poetry_rows)
        # Выводим стихотворение
        PoetryQuizInterface.poetry_part.set(poetry)
        PoetryQuizInterface.poetry_label.configure(font="Arial 16")
        PoetryQuizInterface.poetry_label.pack(fill="both", expand=True)

    @staticmethod
    def go_back_to_menu() -> None:
        """Возвращаемся в меню."""
        # Название игры
        PoetryQuizInterface.start_label.pack(fill="both", expand=True)
        PoetryQuizInterface.place_elements(
            PoetryQuizInterface.start_button,
            PoetryQuizInterface.poetry_button,
            PoetryQuizInterface.exit_button
        )
        # Скрываем лишние элементы интерфейса
        PoetryQuizInterface.hide_elements(
            PoetryQuizInterface.poetry_label,
            PoetryQuizInterface.poetry_choices,
            PoetryQuizInterface.first_answer_button,
            PoetryQuizInterface.second_answer_button,
            PoetryQuizInterface.third_answer_button,
            PoetryQuizInterface.another_poetry,
            PoetryQuizInterface.go_back_button,
        )

    @staticmethod
    def change_poetry() -> None:
        """Выбирает случайно другое стихотворение."""
        if PoetryQuizInterface.another_poetry["text"] == "Сыграть заново":
            # Убираем виджеты с экрана
            PoetryQuizInterface.another_poetry.configure(
                text="Выбрать другое стихотворение"
            )
            PoetryQuizInterface.hide_elements(
                PoetryQuizInterface.poetry_label,
                PoetryQuizInterface.first_answer_button,
                PoetryQuizInterface.second_answer_button,
                PoetryQuizInterface.third_answer_button,
                PoetryQuizInterface.another_poetry,
                PoetryQuizInterface.go_back_button,
            )
            # Выводим строки стихотворения
            PoetryQuizInterface.poetry_label.configure(font="Arial 26")
            PoetryQuizInterface.poetry_label.pack(fill="both", expand=True)
            # Добавляем кнопки для ответов

            PoetryQuizInterface.first_answer_button.pack(side="top", expand=2)
            PoetryQuizInterface.second_answer_button.pack(side="top", expand=2)
            PoetryQuizInterface.third_answer_button.pack(side="top", expand=2)
            # Кнопка для выбора нового стихотворения
            PoetryQuizInterface.another_poetry.configure(
                text="Выбрать другое стихотворение"
            )
            PoetryQuizInterface.another_poetry.pack(side="top", expand=2)
            # Кнопка для возвращения в меню
            PoetryQuizInterface.go_back_button.pack(side="top", expand=2)
        # Выбираем имя стихотворения
        PoetryQuizInterface.poetry_showing_name = random.choice(
            list(poetry_dict.keys())
        )
        # Получаем список со строками стихотворения
        PoetryQuizInterface.poetry_showing = poetry_dict[
            PoetryQuizInterface.poetry_showing_name
        ]
        # Устанавливаем шаг начала стихотворения
        PoetryQuizInterface.step = 0
        # Устанавливаем шаг конца стихотворения
        PoetryQuizInterface.last_step = len(PoetryQuizInterface.poetry_showing)
        # Устанавливаем значение 3-х кнопок для выбора следующей строки стихотворения
        PoetryQuizInterface.set_all_buttons(
            PoetryQuizInterface.poetry_showing_name,
            PoetryQuizInterface.poetry_showing,
            PoetryQuizInterface.step,
        )

    @staticmethod
    def build_poetry(poetry_rows: list) -> str:
        """Собирает стихотворение для вывода."""
        # Добавляем в начало стихотворения его название заглавными буквами и отступ
        poetry = PoetryQuizInterface.poetry_choices.get().upper() + "\n\n"
        for string in poetry_rows:
            poetry += string + "\n"
        return poetry

    @staticmethod
    def set_all_buttons(
        poetry_showing_name: str, poetry_showing: list, step: int
    ) -> None:
        """Устанавливает текст всего."""
        # Переходим на новую строку стихотворения
        PoetryQuizInterface.poetry_part.set(poetry_showing[step])
        # Выбираем стихотворение для первой кнопки
        first_poetry = random.choice(list(poetry_dict.keys()))
        while first_poetry == poetry_showing_name:
            first_poetry = random.choice(list(poetry_dict.keys()))
        # Выбираем стихотворение для второй кнопки
        second_poetry = random.choice(list(poetry_dict.keys()))
        while second_poetry in [first_poetry, poetry_showing_name]:
            second_poetry = random.choice(list(poetry_dict.keys()))
        # Выбираем строку для первой кнопки
        first_poetry = random.choice(poetry_dict[first_poetry])
        # Выбираем строку для второй кнопки
        second_poetry = random.choice(poetry_dict[second_poetry])
        # Выбираем строки для третьей кнопки
        right_poetry = poetry_showing[step + 1]
        # Кнопки для выбора ответа
        text = [first_poetry, second_poetry, right_poetry]
        for button in [
            "first_answer_button",
            "second_answer_button",
            "third_answer_button",
        ]:
            text_for_button = random.choice(text)
            del text[text.index(text_for_button)]
            var = getattr(PoetryQuizInterface, button)
            var.configure(text=text_for_button)

    @staticmethod
    def next_pick(event: tk.Event) -> None:
        """Выполняет переход к следующему (шагу) строке стихотворения."""
        if PoetryQuizInterface.step < PoetryQuizInterface.last_step - 2:
            # Увеличиваем шаг
            PoetryQuizInterface.step += 1
            # Проверяем ответ на правильность
            if PoetryQuizInterface.check_answer(
                event.widget._name, PoetryQuizInterface.step
            ):  # noqa
                # Настраиваем кнопки для ответов
                PoetryQuizInterface.set_all_buttons(
                    poetry_showing_name=PoetryQuizInterface.poetry_showing_name,
                    poetry_showing=PoetryQuizInterface.poetry_showing,
                    step=PoetryQuizInterface.step,
                )
        else:
            # Завершаем игру
            PoetryQuizInterface.finish_game()

    @staticmethod
    def check_answer(button_id: str, step: int) -> bool:
        """Проверяет правильная ли была выбрана строка."""
        right_answer = PoetryQuizInterface.poetry_showing[step]
        picked_answer = PoetryQuizInterface.get_clicked_button_text(button_id)
        if right_answer != picked_answer:
            PoetryQuizInterface.finish_game(True)
            return False
        return True

    @staticmethod
    def get_clicked_button_text(button_id: str):
        # Идентификатор кнопок для проверки правильности ответа
        buttons_data = {
            "!button5": PoetryQuizInterface.first_answer_button["text"],
            "!button6": PoetryQuizInterface.second_answer_button["text"],
            "!button7": PoetryQuizInterface.third_answer_button["text"],
        }
        return buttons_data[button_id]

    @staticmethod
    def finish_game(lost: bool = False) -> None:
        # Скрываем кнопки
        PoetryQuizInterface.hide_elements(
            PoetryQuizInterface.first_answer_button,
            PoetryQuizInterface.second_answer_button,
            PoetryQuizInterface.third_answer_button,
        )

        # Меняем название кнопки для смены стихотворения
        PoetryQuizInterface.another_poetry.configure(text="Сыграть заново")
        # Выводим результат
        if lost:
            PoetryQuizInterface.poetry_part.set(
                f"Упс!\n\nВы допустили ошибку.\n\nПопробуйте заново."
            )
        else:
            PoetryQuizInterface.poetry_part.set(
                "Поздравляю!\n\nВы полностью угадали стихотворение!"
            )

    @staticmethod
    def place_elements(*elements):
        for element in elements:
            element.pack(side="top", expand=2)

    @staticmethod
    def hide_elements(*elements):
        for element in elements:
            element.pack_forget()



    """Важные элементы"""

    # Label для вывода стихотворения
    poetry_label = tk.Label(root, textvariable=poetry_part, font="Arial 26")

    """Главное меню"""

    # Название игры
    start_label = tk.Label(root, text="Poetry Quiz", font="Arial 36")
    start_label.pack(fill="both", expand=True)

    # Кнопка для старта игры
    start_button = tk.Button(
        root,
        text="Начать игру",
        background="white",
        foreground="black",
        highlightbackground="green",
        highlightthickness=2.5,
        font="Arial 24",
        command=play_game,
        justify=tk.CENTER,
    )
    start_button.pack(expand=True)

    # Кнопка для просмотра всех стихотворений
    poetry_button = tk.Button(
        root,
        text="Посмотреть стихотворения",
        background="white",
        foreground="black",
        highlightbackground="orange",
        highlightthickness=2.5,
        font="Arial 24",
        command=open_poetry_menu,
        justify=tk.CENTER,
    )
    poetry_button.pack(expand=True)

    # Кнопка для завершения игры
    exit_button = tk.Button(
        root,
        text="Завершить игру",
        background="white",
        foreground="black",
        highlightbackground="red",
        highlightthickness=2.5,
        font="Arial 24",
        command=destroy_ui,
        justify=tk.CENTER,
    )
    exit_button.pack(expand=True)

    """Начать игру"""

    # Кнопка для выбора нового стихотворения
    another_poetry = tk.Button(
        root,
        background="white",
        text="Выбрать другое стихотворение",
        foreground="black",
        highlightbackground="orange",
        highlightthickness=2.5,
        font="Arial 24",
        command=change_poetry,
        justify=tk.CENTER,
    )

    # Кнопка № 1 для выбора ответа
    first_answer_button = tk.Button(
        root,
        background="white",
        foreground="black",
        highlightbackground="green",
        highlightthickness=2.5,
        font="Arial 20",
        justify=tk.CENTER,
    )
    first_answer_button.bind("<Button-1>", next_pick)

    # Кнопка № 2 для выбора ответа
    second_answer_button = tk.Button(
        root,
        background="white",
        foreground="black",
        highlightbackground="green",
        highlightthickness=2.5,
        font="Arial 20",
        justify=tk.CENTER,
    )
    second_answer_button.bind("<Button-1>", next_pick)

    # Кнопка № 3 для выбора ответа
    third_answer_button = tk.Button(
        root,
        background="white",
        foreground="black",
        highlightbackground="green",
        highlightthickness=2.5,
        font="Arial 20",
        justify=tk.CENTER,
    )
    third_answer_button.bind("<Button-1>", next_pick)

    """Посмотреть стихотворения"""

    # ComboBox для выбора стихотворения
    poetry_choices = ttk.Combobox(root, values=poetry_titles, font="Arial 18")
    poetry_choices.set("Выберите стихотворение")

    # Следим за выбором стихотворения из списка
    poetry_choices.bind("<<ComboboxSelected>>", open_poetry)

    # Кнопка для возвращения в меню
    go_back_button = tk.Button(
        root,
        text="Назад",
        background="white",
        foreground="black",
        highlightbackground="red",
        highlightthickness=2.5,
        font="Arial 24",
        command=go_back_to_menu,
        justify=tk.CENTER,
    )
