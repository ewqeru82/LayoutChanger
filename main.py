from pynput import keyboard
import os
from dict1 import eng_to_rus
import subprocess


def switch_layout(text):
    """Преобразует текст из английской раскладки в русскую."""
    return ''.join([eng_to_rus.get(char, char) for char in text])


def on_activate():
    try:
        var = subprocess.check_output("xsel", universal_newlines=True)
        transformed_text = switch_layout(var)

        # Копирование преобразованного текста в буфер обмена
        os.system(f'echo "{transformed_text}" | xsel -b')

        # print(
        #     "Преобразованный текст скопирован в буфер обмена. Нажмите Ctrl+V для вставки.")

        # print(f"Скопированный текст: {var}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    # Возвращаем False, чтобы остановить слушатель
    return False


listener = keyboard.GlobalHotKeys({
    '<ctrl>+y': on_activate
})

# print("Нажмите Ctrl+Shift для активации горячей клавиши.")
listener.start()

listener.join()
