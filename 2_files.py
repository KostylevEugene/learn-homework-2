"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('referat.txt', 'r', encoding='utf-8') as newfile:
        content = newfile.read()
        
    # подсчет длины строки
    print(len(content))
        
    # деления строки на список
    '''ch_content = content
    ch_content = ch_content.replace('.', '')
    ch_content = ch_content.replace(',', '')
    ch_content = ch_content.replace(':', '')
    ch_content = ch_content.replace('«', '')
    ch_content = ch_content.replace('»', '')
    ch_content = ch_content.replace('!', '')
    ch_content = ch_content.replace('-', '')'''
                
    print(len(content.split(' ')))

    # замена точки на восклицательные знаки
    ch_content = content.replace('.', '!')
    print(ch_content)

    # запись результата в файл
    with open('referat2.txt', 'w', encoding='utf-8') as newerfile:
        newerfile.write(ch_content)



if __name__ == "__main__":
    main()
