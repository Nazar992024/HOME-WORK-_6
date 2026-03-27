import colorama

all_attributes = dir(colorama)

print("--- Інтроспекція бібліотеки colorama ---")
print(f"Загальна кількість атрибутів: {len(all_attributes)}")

important_stuff = ['Fore', 'Back', 'Style', 'init']

print("\nНайважливіші атрибути та методи:")

for item in important_stuff:
    attr = getattr(colorama, item)
    print(f"\nОб'єкт: {item}")
    print(f"Тип: {type(attr)}")
    print(f"Опис: {attr.__doc__ if attr.__doc__ else 'Немає опису'}")

# Коментар до роботи:
# 1. Fore (Foreground) - колір тексту.
# 2. Back (Background) - колір фону.
# 3. Style - яскравість та скидання налаштувань.
# 4. init() - ініціалізація роботи бібліотеки.