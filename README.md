# Телеграм Бот для форматирования Python кода

@format_py_bot 

Этот бот предназначен для форматирования Python кода, отправленного пользователем в виде файла с расширением `.py`. Бот считывает отправленный файл, и отправляет пользователю в виде текста.

## Использование

1. Отправьте боту файл с расширением `.py`.
2. Бот выведет содержимое файла в виде отформатированного текста с подсветкой синтаксиса Python.

## Команды

- `/start` - Начать взаимодействие с ботом.
- Введите `/` для просмотра списка команд и их описания.

## Установка и запуск

1. Создайте файл `.env` и напишите в нем токен вашего бота таким образом:

```python
TOKEN='YOUR_TOKEN'
```

3. Установите необходимые библиотеки:

```
pip install pyTelegramBotAPI
pip install python-dotenv
```

4. Запустите бота:

```
python bot.py
```
