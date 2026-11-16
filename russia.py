
import tkinter as tk
import random
from datetime import datetime

# ==========================================
# RUSSKY.EXE — THE RUSSIAN MODE
# ==========================================

BG = "#101116"
CARD = "#1b1c24"
RED = "#d93645"
WHITE = "#f5f5f5"
GREY = "#999ba8"
GREEN = "#65d69a"

root = tk.Tk()
root.title("RUSSKY.EXE — Russian Mode")
root.geometry("850x720")
root.minsize(650, 650)
root.configure(bg=BG)

tea_count = 0
activated = False

# Funny Russian phrases with French translations

PHRASES = [
    ("Без чая даже Wi-Fi не работает.",
     "Sans thé, même le Wi-Fi ne fonctionne pas."),

    ("Мой компьютер устал больше меня.",
     "Mon ordinateur est plus fatigué que moi."),

    ("Если холодильник пуст, значит, пора паниковать.",
     "Si le réfrigérateur est vide, il est temps de paniquer."),

    ("Умный человек сначала пьёт чай, потом думает.",
     "Une personne intelligente boit d'abord du thé, puis réfléchit."),

    ("Зима близко, а я всё ещё без шапки.",
     "L'hiver approche et je n'ai toujours pas de bonnet."),

    ("Кот спит, значит, всё под контролем.",
     "Le chat dort, donc tout est sous contrôle."),

    ("Интернет медленный, зато чай горячий.",
     "Internet est lent, mais le thé est chaud."),

    ("Пельмени решают все проблемы.",
     "Les pelmenis résolvent tous les problèmes."),

    ("Я не опоздал, я просто пришёл по-русски.",
     "Je ne suis pas en retard, je suis simplement arrivé à la russe."),

    ("Сегодня хороший день, чтобы ничего не делать.",
     "Aujourd'hui est une bonne journée pour ne rien faire."),

    ("Моя сила — это чай и печенье.",
     "Ma force, c'est le thé et les biscuits."),

    ("Даже медведь иногда хочет поспать.",
     "Même un ours a parfois envie de dormir.")
]

PROVERBS = [
    ("Без труда не вытащишь и рыбку из пруда.",
     "Sans effort, tu ne sortiras même pas un poisson de l'étang."),

    ("Тише едешь — дальше будешь.",
     "Qui va doucement va loin."),

    ("Семь раз отмерь, один раз отрежь.",
     "Mesure sept fois, coupe une fois."),

    ("Не имей сто рублей, а имей сто друзей.",
     "Mieux vaut avoir cent amis que cent roubles."),

    ("На ошибках учатся.",
     "On apprend de ses erreurs.")
]

FAKE_PROVERBS = [
    ("Если чай остыл, значит, ты слишком много думал.",
     "Si le thé a refroidi, c'est que tu as trop réfléchi."),

    ("Медведь не спрашивает разрешения у леса.",
     "L'ours ne demande pas la permission à la forêt."),

    ("Кто рано встаёт, тот первым пьёт чай.",
     "Celui qui se lève tôt boit le thé en premier."),

    ("Если Wi-Fi пропал, ищи смысл жизни.",
     "Si le Wi-Fi disparaît, cherche le sens de la vie."),

    ("Лучше десять блинов, чем одна проблема.",
     "Mieux vaut dix blinis qu'un seul problème.")
]

FIRST_NAMES = [
    "Dmitri", "Alexei", "Ivan", "Nikolai",
    "Mikhail", "Vladimir", "Sergei", "Pavel",
    "Andrei", "Boris", "Yuri", "Anton"
]

LAST_NAMES = [
    "Ivanov", "Petrov", "Smirnov", "Volkov",
    "Sokolov", "Kuznetsov", "Popov", "Morozov",
    "Lebedev", "Orlov", "Romanov", "Novikov"
]


# ==========================================
# HELPERS
# ==========================================

def clear_content():
    for widget in content.winfo_children():
        widget.destroy()


def section_title(text):
    tk.Label(
        content,
        text=text,
        font=("Arial", 19, "bold"),
        bg=CARD,
        fg=WHITE
    ).pack(pady=(15, 10))


def show_message(title, russian, french, extra=""):
    clear_content()

    section_title(title)

    tk.Label(
        content,
        text="🇷🇺",
        font=("Arial", 45),
        bg=CARD,
        fg=WHITE
    ).pack(pady=15)

    tk.Label(
        content,
        text=russian,
        font=("Arial", 19, "bold"),
        bg=CARD,
        fg=WHITE,
        wraplength=650,
        justify="center"
    ).pack(padx=25, pady=15)

    tk.Label(
        content,
        text="FRENCH TRANSLATION",
        font=("Arial", 9, "bold"),
        bg=CARD,
        fg=RED
    ).pack(pady=(20, 5))

    tk.Label(
        content,
        text=french,
        font=("Arial", 15),
        bg=CARD,
        fg=GREY,
        wraplength=650,
        justify="center"
    ).pack(padx=25, pady=10)

    if extra:
        tk.Label(
            content,
            text=extra,
            font=("Arial", 11),
            bg=CARD,
            fg=GREEN
        ).pack(pady=15)


def random_phrase():
    russian, french = random.choice(PHRASES)
    show_message("RANDOM RUSSIAN PHRASE", russian, french)


def random_proverb():
    russian, french = random.choice(FAKE_PROVERBS)
    show_message("RUSSIAN WISDOM GENERATOR", russian, french,
                 "100% scientifically unverified wisdom.")


def real_proverb():
    russian, french = random.choice(PROVERBS)
    show_message("REAL RUSSIAN PROVERB", russian, french,
                 "A traditional Russian proverb.")


def generate_name():
    first = random.choice(FIRST_NAMES)
    last = random.choice(LAST_NAMES)

    show_message(
        "RUSSIAN NAME GENERATOR",
        first + " " + last,
        "Your randomly generated Russian name is:",
        "Congratulations. Your imaginary passport is ready."
    )


def add_tea():
    global tea_count
    tea_count += 1
    tea_value.config(text=str(tea_count))
    show_message(
        "TEA COUNTER",
        "Чай — это жизнь.",
        "Le thé, c'est la vie.",
        f"You have consumed {tea_count} virtual cups of tea. ☕"
    )


def activate():
    global activated
    activated = not activated

    if activated:
        activate_button.config(
            text="🇷🇺 RUSSIAN MODE ACTIVATED",
            bg=GREEN,
            fg=BG
        )
        status.config(text="SYSTEM STATUS: FULLY RUSSIAN 🇷🇺", fg=GREEN)
        random_phrase()
    else:
        activate_button.config(
            text="ACTIVATE RUSSIAN MODE",
            bg=RED,
            fg=WHITE
        )
        status.config(text="SYSTEM STATUS: NORMAL", fg=GREY)
        clear_content()
        welcome()


def welcome():
    clear_content()

    section_title("WELCOME TO RUSSKY.EXE")

    tk.Label(
        content,
        text="🇷🇺",
        font=("Arial", 65),
        bg=CARD
    ).pack(pady=20)

    tk.Label(
        content,
        text="Добро пожаловать!",
        font=("Arial", 27, "bold"),
        bg=CARD,
        fg=WHITE
    ).pack(pady=8)

    tk.Label(
        content,
        text="Welcome to Russian Mode!",
        font=("Arial", 15),
        bg=CARD,
        fg=GREY
    ).pack(pady=5)

    tk.Label(
        content,
        text="Choose a feature from the menu to get started.",
        font=("Arial", 11),
        bg=CARD,
        fg=GREY
    ).pack(pady=20)

    tk.Label(
        content,
        text="☕  WARNING: HIGH LEVELS OF TEA DETECTED",
        font=("Arial", 10, "bold"),
        bg=CARD,
        fg=GREEN
    ).pack(pady=15)


# ==========================================
# MAIN HEADER
# ==========================================

header = tk.Frame(root, bg=BG)
header.pack(fill="x", padx=35, pady=25)

tk.Label(
    header,
    text="РУССКИЙ.EXE",
    font=("Arial", 25, "bold"),
    bg=BG,
    fg=WHITE
).pack(side="left")

tk.Label(
    header,
    text="VERSION 1.0",
    font=("Arial", 10, "bold"),
    bg=BG,
    fg=GREY
).pack(side="right")


# ==========================================
# STATUS
# ==========================================

status = tk.Label(
    root,
    text="SYSTEM STATUS: NORMAL",
    font=("Arial", 10, "bold"),
    bg=BG,
    fg=GREY
)
status.pack(pady=5)


# ==========================================
# ACTIVATE BUTTON
# ==========================================

activate_button = tk.Button(
    root,
    text="ACTIVATE RUSSIAN MODE",
    font=("Arial", 13, "bold"),
    bg=RED,
    fg=WHITE,
    activebackground="#ef5260",
    activeforeground=WHITE,
    relief="flat",
    padx=20,
    pady=15,
    command=activate
)
activate_button.pack(pady=15)


# ==========================================
# MAIN CONTENT
# ==========================================

content = tk.Frame(
    root,
    bg=CARD,
    highlightbackground="#343641",
    highlightthickness=1
)
content.pack(fill="both", expand=True, padx=35, pady=15)


# ==========================================
# MENU
# ==========================================

menu = tk.Frame(root, bg=BG)
menu.pack(fill="x", padx=25, pady=10)

def menu_button(text, command):
    tk.Button(
        menu,
        text=text,
        command=command,
        bg="#242631",
        fg=WHITE,
        activebackground=RED,
        activeforeground=WHITE,
        font=("Arial", 9, "bold"),
        relief="flat",
        padx=10,
        pady=12
    ).pack(side="left", expand=True, fill="x", padx=3)


menu_button("💬 Phrase", random_phrase)
menu_button("🧠 Wisdom", random_proverb)
menu_button("📜 Proverbs", real_proverb)
menu_button("👤 Name", generate_name)
menu_button("☕ Tea", add_tea)


# ==========================================
# TEA COUNTER
# ==========================================

tea_frame = tk.Frame(root, bg=BG)
tea_frame.pack(pady=8)

tk.Label(
    tea_frame,
    text="VIRTUAL TEA CONSUMPTION:",
    font=("Arial", 9, "bold"),
    bg=BG,
    fg=GREY
).pack(side="left", padx=8)

tea_value = tk.Label(
    tea_frame,
    text="0",
    font=("Arial", 12, "bold"),
    bg=BG,
    fg=GREEN
)
tea_value.pack(side="left")


# ==========================================
# FOOTER
# ==========================================

tk.Label(
    root,
    text="RUSSKY.EXE © 2026 | MADE WITH ☕ AND PYTHON",
    font=("Arial", 9),
    bg=BG,
    fg="#666875"
).pack(pady=15)


# ==========================================
# START
# ==========================================

welcome()

root.mainloop()
