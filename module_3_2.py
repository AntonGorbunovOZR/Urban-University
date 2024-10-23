def send_email(message, recipient, sender="university.help@gmail.com"):

    string1 = f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}"
    string2 = "Нельзя отправить письмо самому себе!"
    string3 = f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}."
    string4 = f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}."

    a = "@"

    while 1 > 0:
        if recipient.endswith(('.com', '.ru', '.net')) and sender.endswith(('.com', '.ru', '.net')):
            if a not in recipient and sender:
                print(string1)
                break
        else:
            print(string1)
            break
        if sender == recipient:
            print(string2)
            break
        elif sender == "university.help@gmail.com":
            print(string3)
            break
        elif sender != "university.help@gmail.com":
            print(string4)
            break


send_email('just message', 'gtonygmail.ru')
send_email('just message', 'gtonyg@mail.com')
send_email('just message', 'university.help@gmail.com')
send_email('just message', 'gtonyg@mail.com', '@.com')
