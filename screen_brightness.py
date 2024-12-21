import tkinter as tk
import screen_brightness_control as sbc

# Функция для изменения яркости
def change_brightness(value):
    # Устанавливаем яркость в соответствии со значением ползунка
    sbc.set_brightness(int(value))

# Создаем главное окно
root = tk.Tk()
root.title("Управление яркостью экрана")

# Получаем текущее значение яркости
current_brightness = sbc.get_brightness()

# Создаем ползунок для управления яркостью
brightness_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Яркость", command=change_brightness)
brightness_slider.set(current_brightness)  # Устанавливаем текущее значение
brightness_slider.pack()

# Запускаем главный цикл приложения
root.mainloop()
