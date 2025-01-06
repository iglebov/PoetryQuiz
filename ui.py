import random
import tkinter as tk
from tkinter import ttk

from poetry import poetry_dict


class UI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Poetry Quiz")
        self.root.configure(background="gray")
        self.root.geometry("900x600")

        self.poetry_part = tk.StringVar()
        self.poetry_titles = [element for element in poetry_dict.keys()]
        self.poetry_showing_name = ""
        self.poetry_showing = []

        self.step = 0
        self.last_step = 0
        self.mistakes = 0
        self.poetry_label = tk.Label(
            self.root, textvariable=self.poetry_part, font="Arial 26"
        )

        self.start_label = tk.Label(self.root, text="Poetry Quiz", font="Arial 36")
        self.start_label.pack(fill="both", expand=True)
        self.start_button = tk.Button(
            self.root,
            text="Начать игру",
            background="white",
            foreground="black",
            highlightbackground="green",
            highlightthickness=2.5,
            font="Arial 24",
            command=self.play_game,
            justify=tk.CENTER,
        )
        self.start_button.pack(expand=True)

        self.poetry_button = tk.Button(
            self.root,
            text="Посмотреть стихотворения",
            background="white",
            foreground="black",
            highlightbackground="orange",
            highlightthickness=2.5,
            font="Arial 24",
            command=self.open_poetry_menu,
            justify=tk.CENTER,
        )
        self.poetry_button.pack(expand=True)

        self.exit_button = tk.Button(
            self.root,
            text="Завершить игру",
            background="white",
            foreground="black",
            highlightbackground="red",
            highlightthickness=2.5,
            font="Arial 24",
            command=self.destroy_ui,
            justify=tk.CENTER,
        )
        self.exit_button.pack(expand=True)

        self.another_poetry = tk.Button(
            self.root,
            background="white",
            text="Выбрать другое стихотворение",
            foreground="black",
            highlightbackground="orange",
            highlightthickness=2.5,
            font="Arial 24",
            command=self.change_poetry,
            justify=tk.CENTER,
        )

        self.first_answer_button = tk.Button(
            self.root,
            background="white",
            foreground="black",
            highlightbackground="green",
            highlightthickness=2.5,
            font="Arial 20",
            justify=tk.CENTER,
        )
        self.first_answer_button.bind("<Button-1>", self.next_pick)

        self.second_answer_button = tk.Button(
            self.root,
            background="white",
            foreground="black",
            highlightbackground="green",
            highlightthickness=2.5,
            font="Arial 20",
            justify=tk.CENTER,
        )
        self.second_answer_button.bind("<Button-1>", self.next_pick)

        self.third_answer_button = tk.Button(
            self.root,
            background="white",
            foreground="black",
            highlightbackground="green",
            highlightthickness=2.5,
            font="Arial 20",
            justify=tk.CENTER,
        )
        self.third_answer_button.bind("<Button-1>", self.next_pick)

        self.poetry_choices = ttk.Combobox(
            self.root, values=self.poetry_titles, font="Arial 18"
        )
        self.poetry_choices.set("Выберите стихотворение")
        self.poetry_choices.bind("<<ComboboxSelected>>", self.open_poetry)

        self.go_back_button = tk.Button(
            self.root,
            text="Назад",
            background="white",
            foreground="black",
            highlightbackground="red",
            highlightthickness=2.5,
            font="Arial 24",
            command=self.go_back_to_menu,
            justify=tk.CENTER,
        )

    def start_ui(self) -> None:
        self.root.mainloop()

    def destroy_ui(self) -> None:
        self.root.destroy()

    def play_game(self) -> None:
        self.hide_elements(
            self.start_label,
            self.start_button,
            self.exit_button,
            self.poetry_button,
        )

        self.poetry_showing_name = random.choice(list(poetry_dict.keys()))
        self.poetry_showing = poetry_dict[self.poetry_showing_name]
        self.last_step = len(self.poetry_showing)
        self.poetry_part.set(self.poetry_showing[self.step])
        self.poetry_label.configure(font="Arial 26")
        self.poetry_label.pack(fill="both", expand=True)
        self.set_all_buttons(
            poetry_showing_name=self.poetry_showing_name,
            poetry_showing=self.poetry_showing,
            step=self.step,
        )
        self.place_elements(
            self.first_answer_button,
            self.second_answer_button,
            self.third_answer_button,
            self.another_poetry,
            self.go_back_button,
        )

    def open_poetry_menu(self) -> None:
        self.hide_elements(
            self.start_label,
            self.start_button,
            self.exit_button,
            self.poetry_button,
        )

        self.poetry_choices.pack(side="top", expand=2)
        self.go_back_button.pack(side="bottom", expand=2)

    def open_poetry(self, _: tk.Event) -> None:
        """Выводим стихотворение из списка."""
        poetry_rows = poetry_dict[self.poetry_choices.get()]
        poetry = self.build_poetry(poetry_rows)
        self.poetry_part.set(poetry)
        self.poetry_label.configure(font="Arial 16")
        self.poetry_label.pack(fill="both", expand=True)

    def go_back_to_menu(self) -> None:
        self.hide_elements(
            self.poetry_label,
            self.poetry_choices,
            self.first_answer_button,
            self.second_answer_button,
            self.third_answer_button,
            self.another_poetry,
            self.go_back_button,
        )

        self.start_label.pack(fill="both", expand=True)
        self.place_elements(self.start_button, self.poetry_button, self.exit_button)

    def change_poetry(self) -> None:
        if self.another_poetry["text"] == "Сыграть заново":
            self.hide_elements(
                self.poetry_label,
                self.first_answer_button,
                self.second_answer_button,
                self.third_answer_button,
                self.another_poetry,
                self.go_back_button,
            )

            self.another_poetry.configure(text="Выбрать другое стихотворение")
            self.poetry_label.configure(font="Arial 26")
            self.poetry_label.pack(fill="both", expand=True)
            self.first_answer_button.pack(side="top", expand=2)
            self.second_answer_button.pack(side="top", expand=2)
            self.third_answer_button.pack(side="top", expand=2)
            self.another_poetry.configure(text="Выбрать другое стихотворение")
            self.another_poetry.pack(side="top", expand=2)
            self.go_back_button.pack(side="top", expand=2)

        self.poetry_showing_name = random.choice(list(poetry_dict.keys()))
        self.poetry_showing = poetry_dict[self.poetry_showing_name]
        self.step = 0
        self.set_all_buttons(
            self.poetry_showing_name,
            self.poetry_showing,
            self.step,
        )

        self.last_step = len(self.poetry_showing)

    def build_poetry(self, poetry_rows: list) -> str:
        poetry = self.poetry_choices.get().upper() + "\n\n"
        return poetry + "\n".join(poetry_rows)

    def set_all_buttons(
        self, poetry_showing_name: str, poetry_showing: list, step: int
    ) -> None:
        self.poetry_part.set(poetry_showing[step])
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

        for button in (
            self.first_answer_button,
            self.second_answer_button,
            self.third_answer_button,
        ):
            text_for_button = random.choice(text)
            button.configure(text=text_for_button)

            del text[text.index(text_for_button)]

    def next_pick(self, event: tk.Event) -> None:
        if self.step < (self.last_step - 2):
            self.step += 1
            if self.check_answer(event.widget._name, self.step):  # noqa
                self.set_all_buttons(
                    poetry_showing_name=self.poetry_showing_name,
                    poetry_showing=self.poetry_showing,
                    step=self.step,
                )
            return

        self.finish_game()

    def check_answer(self, button_id: str, step: int) -> bool:
        right_answer = self.poetry_showing[step]
        picked_answer = self.get_clicked_button_text(button_id)
        if right_answer != picked_answer:
            self.finish_game(True)
            return False
        return True

    def get_clicked_button_text(self, button_id: str) -> str:
        return {
            "!button5": self.first_answer_button["text"],
            "!button6": self.second_answer_button["text"],
            "!button7": self.third_answer_button["text"],
        }[button_id]

    def finish_game(self, lost: bool = False) -> None:
        self.hide_elements(
            self.first_answer_button,
            self.second_answer_button,
            self.third_answer_button,
        )
        self.another_poetry.configure(text="Сыграть заново")
        if lost:
            self.poetry_part.set(f"Упс!\n\nВы допустили ошибку.\n\nПопробуйте заново.")
        else:
            self.poetry_part.set("Поздравляю!\n\nВы полностью угадали стихотворение!")

    @staticmethod
    def place_elements(*elements) -> None:
        for element in elements:
            element.pack(side="top", expand=2)

    @staticmethod
    def hide_elements(*elements) -> None:
        for element in elements:
            element.pack_forget()
