import smtplib
import string
import secrets

# Функция генерации пароля
def generate_password(length=4):
    if length < 4:
        raise ValueError("Длина пароля должна быть не менее 4 символов")

    password = ''.join(secrets.choice(string.digits) for _ in range(length))
    return password

# Функция отправки электронного письма
def send_email(to_address, subject, body, generated_password):
    # Ваши учетные данные для почтового сервера
    smtp_server = 'smtp.mail.ru'
    smtp_port = 465
    smtp_username = 'pwz-and_10@mail.ru'
    smtp_password = 'mTjEwnu1cXWvAbp7PBEa'

    # Создание соединения с почтовым сервером
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.login(smtp_username, smtp_password)

    # Формирование сообщения с включением сгенерированного пароля
    message = f"Subject: {subject}\n\n{body} {generated_password}"

    # Изменение кодировки сообщения на 'utf-8'
    message = message.encode('utf-8')
    
    # Отправка письма
    server.sendmail(smtp_username, to_address, message)

    # Закрытие соединения
    server.quit()

# Пример использования
generated_password = generate_password(length=4)
print("Сгенерированный пароль:", generated_password)

# Замените 'your_email@example.com' и 'recipient@example.com' соответствующими адресами
send_email('pwz-and_10@mail.ru', 'Новый пароль', 'Ваш новый пароль:', generated_password)
