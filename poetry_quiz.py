import random
import tkinter as tk
from tkinter import ttk

from poetry import poetry_dict


class PoetryQuiz:
    root = tk.Tk()
    root.title("Poetry Quiz")
    root.configure(background="gray")
    root.geometry("900x600")
    poetry_part = tk.StringVar()
    poetry_titles = [element for element in poetry_dict.keys()]
    poetry_showing_name = ""
    poetry_showing = []
    step = 0
    last_step = 0
    mistakes = 0

    @staticmethod
    def start_ui() -> None:
        PoetryQuiz.root.mainloop()

    @staticmethod
    def destroy_ui() -> None:
        PoetryQuiz.root.destroy()

    @staticmethod
    def play_game() -> None:
        PoetryQuiz.hide_elements(
            PoetryQuiz.start_label,
            PoetryQuiz.start_button,
            PoetryQuiz.exit_button,
            PoetryQuiz.poetry_button,
        )
        PoetryQuiz.poetry_showing_name = random.choice(list(poetry_dict.keys()))
        PoetryQuiz.poetry_showing = poetry_dict[PoetryQuiz.poetry_showing_name]
        PoetryQuiz.last_step = len(PoetryQuiz.poetry_showing)
        PoetryQuiz.poetry_part.set(PoetryQuiz.poetry_showing[PoetryQuiz.step])
        PoetryQuiz.poetry_label.configure(font="Arial 26")
        PoetryQuiz.poetry_label.pack(fill="both", expand=True)
        PoetryQuiz.set_all_buttons(
            poetry_showing_name=PoetryQuiz.poetry_showing_name,
            poetry_showing=PoetryQuiz.poetry_showing,
            step=PoetryQuiz.step,
        )
        PoetryQuiz.place_elements(
            PoetryQuiz.first_answer_button,
            PoetryQuiz.second_answer_button,
            PoetryQuiz.third_answer_button,
            PoetryQuiz.another_poetry,
            PoetryQuiz.go_back_button,
        )

    @staticmethod
    def open_poetry_menu() -> None:
        PoetryQuiz.hide_elements(
            PoetryQuiz.start_label,
            PoetryQuiz.start_button,
            PoetryQuiz.exit_button,
            PoetryQuiz.poetry_button,
        )
        PoetryQuiz.poetry_choices.pack(side="top", expand=2)
        PoetryQuiz.go_back_button.pack(side="bottom", expand=2)

    @staticmethod
    def open_poetry(event: tk.Event) -> None:
        """Выводим стихотворение из списка."""
        # Получаем все строки стихотворения
        poetry_rows = poetry_dict[PoetryQuiz.poetry_choices.get()]
        # "Собираем" стихотворение
        poetry = PoetryQuiz.build_poetry(poetry_rows)
        # Выводим стихотворение
        PoetryQuiz.poetry_part.set(poetry)
        PoetryQuiz.poetry_label.configure(font="Arial 16")
        PoetryQuiz.poetry_label.pack(fill="both", expand=True)

    @staticmethod
    def go_back_to_menu() -> None:
        PoetryQuiz.start_label.pack(fill="both", expand=True)
        PoetryQuiz.place_elements(
            PoetryQuiz.start_button, PoetryQuiz.poetry_button, PoetryQuiz.exit_button
        )
        PoetryQuiz.hide_elements(
            PoetryQuiz.poetry_label,
            PoetryQuiz.poetry_choices,
            PoetryQuiz.first_answer_button,
            PoetryQuiz.second_answer_button,
            PoetryQuiz.third_answer_button,
            PoetryQuiz.another_poetry,
            PoetryQuiz.go_back_button,
        )

    @staticmethod
    def change_poetry() -> None:
        if PoetryQuiz.another_poetry["text"] == "Сыграть заново":
            PoetryQuiz.another_poetry.configure(text="Выбрать другое стихотворение")
            PoetryQuiz.hide_elements(
                PoetryQuiz.poetry_label,
                PoetryQuiz.first_answer_button,
                PoetryQuiz.second_answer_button,
                PoetryQuiz.third_answer_button,
                PoetryQuiz.another_poetry,
                PoetryQuiz.go_back_button,
            )
            PoetryQuiz.poetry_label.configure(font="Arial 26")
            PoetryQuiz.poetry_label.pack(fill="both", expand=True)
            PoetryQuiz.first_answer_button.pack(side="top", expand=2)
            PoetryQuiz.second_answer_button.pack(side="top", expand=2)
            PoetryQuiz.third_answer_button.pack(side="top", expand=2)
            PoetryQuiz.another_poetry.configure(text="Выбрать другое стихотворение")
            PoetryQuiz.another_poetry.pack(side="top", expand=2)
            PoetryQuiz.go_back_button.pack(side="top", expand=2)
        PoetryQuiz.poetry_showing_name = random.choice(list(poetry_dict.keys()))
        PoetryQuiz.poetry_showing = poetry_dict[PoetryQuiz.poetry_showing_name]
        PoetryQuiz.step = 0
        PoetryQuiz.last_step = len(PoetryQuiz.poetry_showing)
        PoetryQuiz.set_all_buttons(
            PoetryQuiz.poetry_showing_name,
            PoetryQuiz.poetry_showing,
            PoetryQuiz.step,
        )

    @staticmethod
    def build_poetry(poetry_rows: list) -> str:
        poetry = PoetryQuiz.poetry_choices.get().upper() + "\n\n"
        for string in poetry_rows:
            poetry += string + "\n"
        return poetry

    @staticmethod
    def set_all_buttons(
        poetry_showing_name: str, poetry_showing: list, step: int
    ) -> None:
        PoetryQuiz.poetry_part.set(poetry_showing[step])
        first_poetry = random.choice(list(poetry_dict.keys()))
        while first_poetry == poetry_showing_name:
            first_poetry = random.choice(list(poetry_dict.keys()))
        second_poetry = random.choice(list(poetry_dict.keys()))
        while second_poetry in [first_poetry, poetry_showing_name]:
            second_poetry = random.choice(list(poetry_dict.keys()))
        first_poetry = random.choice(poetry_dict[first_poetry])
        second_poetry = random.choice(poetry_dict[second_poetry])
        right_poetry = poetry_showing[step + 1]
        text = [first_poetry, second_poetry, right_poetry]
        for button in [
            "first_answer_button",
            "second_answer_button",
            "third_answer_button",
        ]:
            text_for_button = random.choice(text)
            del text[text.index(text_for_button)]
            var = getattr(PoetryQuiz, button)
            var.configure(text=text_for_button)

    @staticmethod
    def next_pick(event: tk.Event) -> None:
        if PoetryQuiz.step < PoetryQuiz.last_step - 2:
            PoetryQuiz.step += 1
            if PoetryQuiz.check_answer(event.widget._name, PoetryQuiz.step):  # noqa
                PoetryQuiz.set_all_buttons(
                    poetry_showing_name=PoetryQuiz.poetry_showing_name,
                    poetry_showing=PoetryQuiz.poetry_showing,
                    step=PoetryQuiz.step,
                )
        else:
            PoetryQuiz.finish_game()

    @staticmethod
    def check_answer(button_id: str, step: int) -> bool:
        right_answer = PoetryQuiz.poetry_showing[step]
        picked_answer = PoetryQuiz.get_clicked_button_text(button_id)
        if right_answer != picked_answer:
            PoetryQuiz.finish_game(True)
            return False
        return True

    @staticmethod
    def get_clicked_button_text(button_id: str):
        buttons_data = {
            "!button5": PoetryQuiz.first_answer_button["text"],
            "!button6": PoetryQuiz.second_answer_button["text"],
            "!button7": PoetryQuiz.third_answer_button["text"],
        }
        return buttons_data[button_id]

    @staticmethod
    def finish_game(lost: bool = False) -> None:
        PoetryQuiz.hide_elements(
            PoetryQuiz.first_answer_button,
            PoetryQuiz.second_answer_button,
            PoetryQuiz.third_answer_button,
        )
        PoetryQuiz.another_poetry.configure(text="Сыграть заново")
        if lost:
            PoetryQuiz.poetry_part.set(
                f"Упс!\n\nВы допустили ошибку.\n\nПопробуйте заново."
            )
        else:
            PoetryQuiz.poetry_part.set(
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

    poetry_label = tk.Label(root, textvariable=poetry_part, font="Arial 26")

    start_label = tk.Label(root, text="Poetry Quiz", font="Arial 36")
    start_label.pack(fill="both", expand=True)
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

    poetry_choices = ttk.Combobox(root, values=poetry_titles, font="Arial 18")
    poetry_choices.set("Выберите стихотворение")
    poetry_choices.bind("<<ComboboxSelected>>", open_poetry)

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
