# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def InvertDigits(K):
    # Преобразуем число в строку, чтобы можно было перевернуть его
    str_K = str(K)
    # Переворачиваем строку
    reversed_str_K = str_K[::-1]
    # Преобразуем строку обратно в число
    reversed_K = int(reversed_str_K)
    # Записываем результат в K
    K = reversed_K
    # Возвращаем K
    return K