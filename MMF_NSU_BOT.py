# coding: utf-8

import telebot
from telebot import types
import time
from datetime import date
from docxtpl import DocxTemplate
import os

doc1 = DocxTemplate("resources/Zayavlenie_na_povishenie_ocenki.docx")
doc2 = DocxTemplate("resources/Zayavlenie_na_otchislenie_po_sobstv.docx")
doc3 = DocxTemplate("resources/Zayavlenie_na_kray_srok.docx")
doc4 = DocxTemplate("resources/Zayavlenie_na_propusk_po_uvag.docx")
doc5 = DocxTemplate("resources/Obxodnoi_list.docx")

bot = telebot.TeleBot('token')


class Spravka:
    def __init__(self, list1, destination, doc, answer):
        self.function_list = list1
        self.iterator = 0
        self.user = None
        self.destination = destination
        self.template = doc
        self.answer = answer
        self.generate_function = spravka_generate
        self.document = None;

    def Next(self, msg):
        self.iterator += 1
        if (self.iterator == len(self.function_list)):
            answer = "Ваша справка.\nХотите ли вы отослать справку зам. декана? Введите 'Да'/'Нет'"
            msg = bot.send_message(msg.chat.id, text=answer)
            self.generate_function(msg, self)
        else:
            answer = self.answer[self.iterator]
            msg = bot.send_message(msg.chat.id, text=answer)
            bot.register_next_step_handler(msg, self.function_list[self.iterator], self)


class User:
    def __init__(self, name):
        self.surname = name
        self.name = None
        self.fathername = None
        self.telephone = None
        self.course = None
        self.group = None
        self.number_zachetki = None
        self.date = None
        self.grade = None
        self.subject1 = None
        self.year = None
        self.date1 = None
        self.exams_amount = None
        self.reason = None
        self.subject2 = []
        self.date2 = []


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Вопросы по учебной составляющей")
    btn2 = types.KeyboardButton("Заявления")
    btn3 = types.KeyboardButton("Полезная информация")
    markup.add(btn1, btn2, btn3)
    try:
        bot.send_message(message.chat.id, text="Выберите раздел".format(message.from_user), reply_markup=markup)
    except (ConnectionAbortedError, ConnectionResetError, ConnectionRefusedError, ConnectionError):
        time.sleep(5)
        print("That was an error (connection)")
        bot.send_message(message.chat.id, text="Выберите раздел".format(message.from_user), reply_markup=markup)


def state(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Заявление на пересдачу с целью повышения оценки")
    btn2 = types.KeyboardButton("Заявление на отчисление по собственному желанию")
    btn3 = types.KeyboardButton("Заявление на крайний срок ликвидации задолженности")
    btn4 = types.KeyboardButton("Заявление на пропуск по уважительной причине")
    btn5 = types.KeyboardButton("Обходной лист")
    btn6 = types.KeyboardButton("Здесь нет моего заявления")
    back = types.KeyboardButton("Вернуться в главное меню")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, back)
    bot.send_message(message.chat.id,
                     text="1. Заявление на пересдачу с целью повышения оценки\n2. Заявление на отчисление по собственному желанию\n3. Заявление на крайний срок\n4. Заявление на пропуск по уважительной причине\n5. Обходной лист\n6. Здесь нет моего заявления\n7. Вернуться в главное меню",
                     reply_markup=markup)
    try:
        bot.send_message
    except ConnectionResetError:
        start(message)
        print("That was an error (connection)")


def process_surname_step(message, spravka):
    if (message.text == "Отмена"):
        state(message)
        return

    surname = message.text
    spravka.user = User(surname)
    spravka.Next(message)


def process_name_step(message, spravka):
    if (message.text == "Отмена"):
        state(message)
        return

    name = message.text
    spravka.user.name = name
    spravka.Next(message)


def process_fathername_step(message, spravka):
    if (message.text == "Отмена"):
        state(message)
        return

    fathername = message.text
    spravka.user.fathername = fathername
    spravka.Next(message)


def process_telephone_step(message, spravka):
    if (message.text == "Отмена"):
        state(message)
        return

    telephone = message.text
    spravka.user.telephone = telephone
    spravka.Next(message)


def process_course_step(message, spravka):
    if (message.text == "Отмена"):
        state(message)
        return

    course = message.text
    spravka.user.course = course
    spravka.Next(message)


def process_group_step(message, spravka):
    if (message.text == "Отмена"):
        state(message)
        return

    group = message.text
    spravka.user.group = group
    spravka.Next(message)


def process_zachetka_step(message, spravka):
    if (message.text == "Отмена"):
        state(message)
        return

    number_zachetki = message.text
    spravka.user.number_zachetki = number_zachetki
    spravka.Next(message)


def process_date_step(message, spravka):
    if (message.text == "Отмена"):
        state(message)
        return

    date = message.text
    spravka.user.date = date
    spravka.Next(message)


def process_grade_step(message, spravka):
    if (message.text == "Отмена"):
        state(message)
        return

    grade = message.text
    spravka.user.grade = grade
    spravka.Next(message)


def process_subject1_step(message, spravka):
    if (message.text == "Отмена"):
        state(message)
        return

    subject1 = message.text
    spravka.user.subject1 = subject1
    spravka.user.subject2.append(subject1)
    spravka.Next(message)


def process_year_step(message, spravka):
    if (message.text == "Отмена"):
        state(message)
        return

    year = message.text
    spravka.user.year = year
    spravka.Next(message)


def process_date1_step(message, spravka):
    if (message.text == "Отмена"):
        state(message)
        return

    date1 = message.text
    spravka.user.date1 = date1
    spravka.user.date2.append(date1)
    spravka.Next(message)


def process_reason_step(message, spravka):
    if (message.text == "Отмена"):
        state(message)
        return

    reason = message.text
    spravka.user.reason = reason
    spravka.Next(message)


def process_exams_amount_step(message, spravka):
    if (message.text == "Отмена"):
        print(spravka.user.exams_amount)
        state(message)
        return

    exams_amount = message.text
    exams_amount = int(message.text)
    additional_handlers = [process_subject1_step, process_date1_step] * exams_amount
    spravka.answer += ["Введите название экзамена", "Введите дату экзамена"] * exams_amount
    spravka.function_list += additional_handlers
    spravka.user.exams_amount = exams_amount
    spravka.Next(message)


def spravka_generate(message, spravka):
    today = date.today()
    context = {'name1': spravka.user.surname, 'name2': spravka.user.name,
               'name3': spravka.user.fathername, 'n1': spravka.user.telephone,
               'n2': spravka.user.course, 'n3': spravka.user.group,
               'n4': spravka.user.number_zachetki, 'n5': spravka.user.grade,
               'subject1': spravka.user.subject1, 'date': ("{}.{}.{}".format(today.day, today.month, today.year)),
               'year': spravka.user.year, 'date1': spravka.user.date1}
    spravka.template.render(context)
    name = spravka.user.surname + '_' + os.path.basename(spravka.destination)
    spravka.template.save(name)
    with open(name, 'rb') as doc_new:
        bot.send_document(message.chat.id, doc_new)
    bot.register_next_step_handler(message, message_send, spravka)


def list_spravka_generate(message, spravka):
    today = date.today()
    context = {'name1': spravka.user.surname, 'name2': spravka.user.name,
               'name3': spravka.user.fathername, 'n1': spravka.user.telephone,
               'n2': spravka.user.course, 'n3': spravka.user.group,
               'n4': spravka.user.number_zachetki, 'date': ("{}.{}.{}".format(today.day, today.month, today.year)),
               'reason': spravka.user.reason}
    for i in range(1, 6):
        context['subject' + str(i)] = "_______________________"
        context['date' + str(i)] = "_______________________"
    for i in range(spravka.user.exams_amount):
        context['subject' + str(i + 1)] = spravka.user.subject2[i]
        context['date' + str(i + 1)] = spravka.user.date2[i]
    spravka.template.render(context)
    name = spravka.user.surname + '_' + os.path.basename(spravka.destination)
    spravka.template.save(name)
    with open(name, 'rb') as doc_new:
        bot.send_document(message.chat.id, doc_new)
    bot.register_next_step_handler(message, message_send, spravka)


def message_send(message, spravka):
    name = spravka.user.surname + '_' + os.path.basename(spravka.destination)
    if (message.text != "Да"):
        answer1 = "Документ не был отослан"
        bot.send_message(message.chat.id, answer1)
        state(message)
    elif (message.text == "Да"):
        answer2 = "Документ отослан"
        bot.send_message(message.chat.id, answer2)
        with open(name, 'rb') as doc:
            bot.send_document('-996920516', doc)
        state(message)
    os.remove(name)


@bot.message_handler(content_types=['text'])
def func(message):
    print(message.text)
    if (message.text == "Вопросы по учебной составляющей"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Стипендии")
        btn2 = types.KeyboardButton("Вопросы по сессии")
        btn3 = types.KeyboardButton("Вопросы по уч. процессу")
        btn4 = types.KeyboardButton("Оплата услуг НГУ")
        btn5 = types.KeyboardButton("Карточка специализации")
        btn6 = types.KeyboardButton("Восстановление, отчисление, перевод")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, back)
        try:
            bot.send_message(message.chat.id, text="Выберите раздел", reply_markup=markup)
        except ConnectionResetError:
            start(message)
            print("That was an error (connection)")

    elif (message.text == "Заявления"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Заявление на пересдачу с целью повышения оценки")
        btn2 = types.KeyboardButton("Заявление на отчисление по собственному желанию")
        btn3 = types.KeyboardButton("Заявление на крайний срок ликвидации задолженности")
        btn4 = types.KeyboardButton("Заявление на пропуск по уважительной причине")
        btn5 = types.KeyboardButton("Обходной лист")
        btn6 = types.KeyboardButton("Здесь нет моего заявления")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, back)
        try:
            bot.send_message(message.chat.id,
                             text="1. Заявление на пересдачу с целью повышения оценки\n2. Заявление на отчисление по собственному желанию\n3. Заявление на крайний срок\n4. Заявление на пропуск по уважительной причине\n5. Обходной лист\n6. Здесь нет моего заявления\n7. Вернуться в главное меню",
                             reply_markup=markup)
        except ConnectionResetError:
            start(message)
            print("That was an error (connection)")

    elif (message.text == "Заявление на пересдачу с целью повышения оценки"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Отмена")
        markup.add(btn1)
        answer = "Введите Фамилию, если вы захотите отменить ввод, нажмите кнопку 'Отмена'"
        spravka = Spravka([process_surname_step, process_name_step, process_fathername_step, process_telephone_step,
                           process_course_step, process_group_step, process_zachetka_step, process_grade_step,
                           process_subject1_step],
                          'povishenie.docx',
                          doc1,
                          ["Введите Фамилию", "Введите Имя", "Введите Отчество", "Введите телефон", "Введите курс",
                           "Введите группу", "Введите номер зачетной книжки",
                           "Введите оценку по предмету, который хотите пересдать",
                           "Введите название предмета, который хотите пересдать"])
        try:
            bot.send_message(message.chat.id, text=answer, reply_markup=markup)
        except ConnectionResetError:
            start(message)
            print("That was an error (connection)")
        bot.register_next_step_handler(message, process_surname_step, spravka)

    elif (message.text == "Заявление на отчисление по собственному желанию"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Отмена")
        markup.add(btn1)
        answer = "Введите Фамилию, если вы захотите отменить ввод, нажмите кнопку 'Отмена'"
        spravka = Spravka([process_surname_step, process_name_step, process_fathername_step, process_telephone_step,
                           process_course_step, process_group_step, process_zachetka_step],
                          'otchislenie.docx',
                          doc2,
                          ["Введите Фамилию", "Введите Имя", "Введите Отчество", "Введите телефон", "Введите курс",
                           "Введите группу", "Введите номер зачетной книжки"])
        try:
            bot.send_message(message.chat.id, text=answer, reply_markup=markup)
        except ConnectionResetError:
            start(message)
            print("That was an error (connection)")
        bot.register_next_step_handler(message, process_surname_step, spravka)

    elif (message.text == "Заявление на крайний срок ликвидации задолженности"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Отмена")
        markup.add(btn1)
        answer = "Введите Фамилию, если вы захотите отменить ввод, нажмите кнопку 'Отмена'"
        spravka = Spravka([process_surname_step, process_name_step, process_fathername_step, process_telephone_step,
                           process_course_step, process_group_step, process_zachetka_step, process_subject1_step,
                           process_grade_step, process_year_step, process_date1_step],
                          'kray_srok.docx',
                          doc3,
                          ["Введите Фамилию", "Введите Имя", "Введите Отчество", "Введите телефон", "Введите курс",
                           "Введите группу", "Введите номер зачетной книжки",
                           "Введите название предмета, по которому просите установить крайний срок ликвидации",
                           "Введите номер семестра, в котором вы проходили этот предмет",
                           "Введите учебный год, в котором вы проходили этот предмет, в формате __2_ - __2_",
                           "Введите дату, на которую вы хотите установить крайний срок ликвидации"])
        try:
            bot.send_message(message.chat.id, text=answer, reply_markup=markup)
        except ConnectionResetError:
            start(message)
            print("That was an error (connection)")
        bot.register_next_step_handler(message, process_surname_step, spravka)

    elif (message.text == "Заявление на пропуск по уважительной причине"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Отмена")
        markup.add(btn1)
        answer = "Введите Фамилию, если вы захотите отменить ввод, нажмите кнопку 'Отмена'"
        spravka = Spravka([process_surname_step, process_name_step, process_fathername_step, process_telephone_step,
                           process_course_step, process_group_step, process_zachetka_step, process_reason_step,
                           process_exams_amount_step],
                          'propusk.docx',
                          doc4,
                          ["Введите Фамилию", "Введите Имя", "Введите Отчество", "Введите телефон", "Введите курс",
                           "Введите группу", "Введите номер зачетной книжки",
                           "Введите уважительную причину пропуска экзамена/ов",
                           "Введите количество предметов (цифрой, от 1 до 5)"])
        spravka.generate_function = list_spravka_generate
        try:
            bot.send_message(message.chat.id, text=answer, reply_markup=markup)
        except ConnectionResetError:
            start(message)
            print("That was an error (connection)")
        bot.register_next_step_handler(message, process_surname_step, spravka)

    elif (message.text == "Обходной лист"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Отмена")
        markup.add(btn1)
        answer = "Введите Фамилию, если вы захотите отменить ввод, нажмите кнопку 'Отмена'"
        spravka = Spravka([process_surname_step, process_name_step, process_fathername_step, process_subject1_step],
                          'obx_list.docx',
                          doc5,
                          ["Введите Фамилию", "Введите Имя", "Введите Отчество",
                           "Введите причину (отчисление, перевод, окончание и т.д.)"])
        try:
            bot.send_message(message.chat.id, text=answer, reply_markup=markup)
        except ConnectionResetError:
            start(message)
            print("That was an error (connection)")
        bot.register_next_step_handler(message, process_surname_step, spravka)

    elif (message.text == "Стипендии"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Когда стипендия?")
        btn2 = types.KeyboardButton("За что сняли стипендию?")
        btn3 = types.KeyboardButton("Как оформить социальную стипендию?")
        btn4 = types.KeyboardButton("Нет моего вопроса")
        back = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn3, btn4, back)
        bot.send_message(message.chat.id,
                         text="1. Когда стипендия?\n2. За что сняли стипендию?\n3. Как оформить социальную стипендию?\n4. Нет моего вопроса\n5. Назад\n(нажмите на кнопку, чтобы перейти к вопросу)",
                         reply_markup=markup)
    elif (message.text == "Когда стипендия?"):
        answer = "Обычная стипендия выплачивается в течении первой недели нового месяца. Социальная стипендия выплачивается в течении месяца.Стипендия NSU+ первый семестр выплачивается вместе с обычной стипендией.\n Во втором семестре выплата стипендии NSU+ производится по мере поступления средств и выплачивается за весь прошедший период(с начала второго семестра) и ежемесячно за оставшиеся месяцы по июнь включительно."
        bot.send_message(message.chat.id, answer)
    elif (message.text == "За что сняли стипендию?"):
        answer = "Обычная стипендия снимается после получения оценки ‘неудовлетворительно’ или ‘удовлетворительно’ при первой попытке сдачи зачёта или экзамена, а также в случае сдачи зачета/экзамена не в срок.\n У социальной стипендии может закончиться срок назначения."
        bot.send_message(message.chat.id, answer)
    elif (message.text == "Как оформить социальную стипендию?"):
        answer = "Если студент проживает в Новосибирске(или не в Новосибирске), и семья считается нуждающейся и получает какие-то соц. пособия от государства( например, является многодетной семьей), то студент может получить справку в органах соц. защиты о том, что он является получателем какой-либо гос. социальной помощи и на основании этой справки назначается социальная стипендия.\n Другой путь: студент проживает в общежитии и прописан в общежитии. Он может оформить социальную стипендию здесь. Собирает для этого документы, идёт в комплексный центр, сдаёт документы туда и ему начисляют какую-то государственную помощь в виде некоторой суммы и дают уведомление. Студент идёт в органы соц. защиты, досдаёт туда документы вместе с уведомлением и получает справку, на основании которой ему могут назначить стипедию в вузе. Стипендия назначается на один год. В справке указана дата, когда назначена социальная помощь. Отсчет года начинается с этой даты. Стипендию возможно продлить через год, но для этого необходимо заново принести справку из органов соц. защиты. Социальную стипендию снять не могут. Только если человек отчислился - стипендия снимается.Также на основе получения социальной помощи возможно получение мат. помощи.\n Комплексный центр социального обслуживания населения:\n - ул. Иванова, 11а, тел. 332-45-47, каб.18\n - ул. Софийская, 4, тел. 306-48-02\n Отдел пособий и социальных выплат Советского района:\n -  ул. проспект Академика Лаврентьева, 14, тел. 333-20-82, приёмные дни: пн, ср, чт, 9:00 - 17:30, обед: 13:00 - 14:00\n Документы для выдачи справки на социальную стипендию:\n1)В комплексный центр социального обслуживания населения:\n Справка из деканата НГУ об обучении на очном бюджетном отделении и её копия\n Копия паспорта (2 шт)\n справка из общежития и её копия\n справка о стипендии (к. 521 ректорского корпуса)\n копия СНИЛС\n реквизиты счёта\n копия свидетельства о регистрации по месту пребывания (2 шт)\n В результате вы получите социальную помощь и Уведомление.\n2) Далее, в Отдел пособий и социальных выплат Советского района:\n Уведомление\n справка из деканата НГУ об обучении на очном бюджетном отделении\n копия паспорта\n копия свидетельства о регистрации по месту пребывания\n В результате вы получите справку, которую нужно принести в деканат."
        bot.send_message(message.chat.id, answer)

    elif (message.text == "Вопросы по сессии"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Что делать, 2 за экзамен?")
        btn2 = types.KeyboardButton("Что делать, 2 за пересдачу?")
        btn3 = types.KeyboardButton("Можно ли пересдать 3?")
        btn4 = types.KeyboardButton("Что такое повторки?")
        btn5 = types.KeyboardButton("Сколько пересдач?")
        btn6 = types.KeyboardButton("Сколько можно пересдач?")
        btn7 = types.KeyboardButton("Нет моего вопроса")
        back = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, back)
        bot.send_message(message.chat.id,
                         text="1. Что делать, 2 за экзамен?\n2. Что делать, 2 за пересдачу?\n3. Можно ли пересдать 3?\n4. Что такое повторки?\n5. Сколько пересдач?\n6. Сколько можно пересдач?\n7. Нет моего вопроса\n8. Назад\n(нажмите на кнопку, чтобы перейти к вопросу)",
                         reply_markup=markup)
    elif (message.text == "Что делать, 2 за экзамен?"):
        answer = "В случае полученной двойки вам будет назначена пересдача в один из каникулярных дней.\nПересдача проходит в том же формате, что и экзамен. Также снимается обычная стипендия."
        bot.send_message(message.chat.id, answer)
    elif (message.text == "Что делать, 2 за пересдачу?"):
        answer = "В случае полученной двойки за пересдачу, вам будет назначена вторая пересдача в течении первого месяца следующего семестра. Пересдача проходит с комиссией, состав комиссии можно узнать в графике пересдач на сайте факультета."
        bot.send_message(message.chat.id, answer)
    elif (message.text == "Можно ли пересдать 3?"):
        answer = "Вы можете подать заявление на пересдачу с целью повышения оценки в Деканат. Имейте ввиду, что в случае пересдачи на более высокую оценку, возобновление выплаты стипендии не произойдёт."
        bot.send_message(message.chat.id, answer)
    elif (message.text == "Что такое повторки?"):
        answer = "По предметам, не продолжающимся в следующем семестре, существует возможность взять повторный курс. Что это такое? Повторный курс — это возможность прослушать предмет еще раз (лекции и семинары) перед комиссионной сдачей. Однако, есть несколько нюансов:\n 1) Количество попыток не увеличивается.\n 2) Курс проходит через год, в соответствующем семестре в дополнение к основному расписанию (достаточно нагруженному).\n 3) Повторный курс платный (первое прочтение вам оплачивает государство).\n 4) Разрешается взять только один повторный курс в семестр.\n Кроме того, повторный курс — это исключительный случай, когда других вариантов у вас просто нет. Поэтому решение по каждому студенту принимается индивидуально. Грубо говоря, не работать весь семестр, не ходить на сдачи, а потом брать повторный курс нельзя.\n Если вы хотите взять повторный курс, обратитесь к заместителю декана по вашему потоку."
        bot.send_message(message.chat.id, answer)
    elif (message.text == "Сколько пересдач?"):
        answer = "У каждого экзамена или зачёта две пересдачи."
        bot.send_message(message.chat.id, answer)
    elif (message.text == "Сколько можно пересдач?"):
        answer = "Вам могут предоставить ещё попытки пересдач, если некоторые из попыток вы пропустили по уважительной причине. Для этого вам необходимо написать заявление с просьбой предоставить ещё одну попытку сдачи и с доказательством уважительной причины пропуска."
        bot.send_message(message.chat.id, answer)

    elif (message.text == "Вопросы по уч. процессу"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Что делать, если заболел?")
        btn2 = types.KeyboardButton("Что делать, если пропустил много занятий?")
        btn3 = types.KeyboardButton("Что делать, если не могу получить зачёт?")
        btn4 = types.KeyboardButton("Можно ли поменять преподавателя?")
        btn5 = types.KeyboardButton("Можно ходить на занятия с другой группой?")
        btn6 = types.KeyboardButton("Нет моего вопроса")
        back = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, back)
        bot.send_message(message.chat.id,
                         text="1. Что делать, если заболел?\n2. Что делать, если пропустил много занятий?\n3. Что делать, если не могу получить зачёт?\n4. Можно ли поменять преподавателя?\n5. Можно ходить на занятия с другой группой?\n6. Нет моего вопроса\n7. Назад\n(нажмите на кнопку, чтобы перейти к вопросу)",
                         reply_markup=markup)
    elif (message.text == "Что делать, если заболел?"):
        answer = "Начинайте наблюдаться у терапевта в процессе лечения. По окончании лечения вы можете получить у терапевта справку с временным промежутком вашей болезни. Эту справку вы можете предоставить преподавателям, заместителю декана вашего потока, для закрытия пропусков по уважительной причине."
        bot.send_message(message.chat.id, answer)
    elif (message.text == "Что делать, если пропустил много занятий?"):
        answer = "Вам стоит узнать у своих семинаристов по дисциплинам, как наверстать упущенное, попросить помощи у своих одногруппников или сопоточников. Если у пропусков есть уважительная причина, поговорите с заместителем декана по потоку вашего курса, объясните ситуацию, принесите ему соответствующие справки или расписки."
        bot.send_message(message.chat.id, answer)
    elif (message.text == "Что делать, если не могу получить зачёт?"):
        answer = "Свяжитесь с заместителем декана по потоку вашего курса, проконсультируйтесь, попробуйте решить эту проблему вместе с ним."
        bot.send_message(message.chat.id, answer)
    elif (message.text == "Можно ли поменять преподавателя?"):
        answer = "Да. Для этого вам необходимо написать соответствующее заявление, которое мы можем помочь вам оформить. Необходимо согласие преподавателя, от которого уходите и к которому уходите. Дополнительно стоит проконсультироваться с заместителем декана по вашему потоку."
        bot.send_message(message.chat.id, answer)
    elif (message.text == "Можно ходить на занятия с другой группой?"):
        answer = "Можно. Необходимо согласие преподавателя, к которому вы хотите ходить на занятия. Но имейте ввиду, если вы не собираетесь переводиться от своего преподавателя, то вам необходимо посещать занятия у обоих преподавателей.\nЕсли вы собираетесь ходить к тому же преподавателю, но в другое время, также нужно договориться об этом с преподавателем."
        bot.send_message(message.chat.id, answer)

    elif (message.text == "Оплата услуг НГУ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как оплатить общежитие?")
        btn2 = types.KeyboardButton("Сроки оплаты общежития.")
        btn3 = types.KeyboardButton("Сколько стоит обучение?")
        btn4 = types.KeyboardButton("Когда оплачивать?")
        btn5 = types.KeyboardButton("Куда оплачивать?")
        btn6 = types.KeyboardButton("Можно ли оплатить в рассрочку?")
        btn7 = types.KeyboardButton("Нет моего вопроса")
        back = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, back)
        bot.send_message(message.chat.id,
                         text="1. Как оплатить общежитие?\n2. Сроки оплаты общежития.\n3. Сколько стоит обучение?\n4. Когда оплачивать?\n5. Куда оплачивать?\n6. Можно ли оплатить в рассрочку?\n7. Нет моего вопроса\n8. Назад\n(нажмите на кнопку, чтобы перейти к вопросу)",
                         reply_markup=markup)
    elif (message.text == "Как оплатить общежитие?"):
        answer = "Оплатить проживание можно в кассе НГУ (ул. Пирогова д.1, 1 этаж) или в терминалах, расположенных:\n 1) Холл общ. №1а (ул. Ляпунова, 4).\n 2) Холл общ. №1б (ул. Ляпунова, 2).\n 3) Холл общ. №10 (ул. Пирогова, 10).\n 4) Холл главного корпуса (ул. Пирогова, 2)."
        bot.send_message(message.chat.id, answer)
    elif (message.text == "Сроки оплаты общежития."):
        answer = "Сроки оплаты: за первый семестр – до 10 сентября,\n за второй семестр – до 10 февраля,\n за летний период – до 30 июня текущего года."
        bot.send_message(message.chat.id, answer)
    elif (message.text == "Сколько стоит обучение?"):
        answer = "Из приказов о стоимости на 2022-2023г.\n Бакалавриат:\n 1-й курс: 177000 руб/год,\n 2-й курс: 174723 руб/год,\n 3-й и 4-й курс: 172556 руб/год.\n Магистратура:\n 1-й курс: 182000 руб/год,\n 2-й курс: 179920 руб/год."
        bot.send_message(message.chat.id, answer)
    elif (message.text == "Когда оплачивать?"):
        answer = "Дата 1-го платежа 1 курса обучения - до 31 августа (по программам бакалавриата/специалитета);\n до 25 августа (по программам магистратуры/аспирантуры/ординатуры);\n дата 1-го платежа текущего учебного года* – до __*;\n дата 1-го платежа остальных курсов обучения – до 10 сентября;\n сумма 1-го платежа текущего учебного года – не менее 50% стоимости текущего учебного года;\n дата 2-го платежа текущего учебного года – до 1 марта;\n сумма 2-го платежа текущего учебного года – в совокупности с 1-м платежом текущего учебного года должна составлять не менее 100% стоимости текущего учебного года.\n * дата 1-го платежа текущего учебного года указывается УМО структурного подразделения для обучающихся, восстанавливающихся (переведенных) для обучения."
        bot.send_message(message.chat.id, answer)
    elif (message.text == "Куда оплачивать?"):
        answer = "Реквизиты для перечисления денежных средств для граждан Российской Федерации:\n ИНН 5408106490, КПП 540801001,\n Получатель: УФК по Новосибирской области (НГУ л/с 30516Щ44680),\n Банк получателя: СИБИРСКОЕ ГУ БАНКА РОССИИ//УФК по Новосибирской области г. Новосибирск,\n Казначейский счет № 03214643000000015100,\n ЕКС (кор/сч) № 40102810445370000043 БИК ТОФК 015004950, КБК 00000000000000000130 (доходы от оказания услуг, выполнение НИР, госконтракты),\n ОКПО 02068930, ОКТМО 50701000, ОГРН 1025403658565, оплата по договору № (указать номер договора) за обучение (указать ФИО «Обучающегося» полностью).\n Реквизиты для перечисления денежных средств для граждан стран СНГ:\n Банк получателя – Филиал «Центральный» Банка ВТБ (ПАО) в г. Москве,\n БИК банка 044525411,\n Кор. счет 30101810145250000411,\n Р/с получателя 40503810716034000002,\n Наименование получателя - Новосибирский государственный университет,\n Адрес - 630090, г. Новосибирск, ул. Пирогова, 2,\n ИНН 5408106490, КПП 540801001.\n Оплата через Интернет: nsu.ru/n/online-pay-gpb (для платежей на территории Российской Федерации с рублевых карт комиссия не взимается)."
        bot.send_message(message.chat.id, answer)
    elif (message.text == "Можно ли оплатить в рассрочку?"):
        answer = "Можно. Уточняйте детали в бансковских отделениях."
        bot.send_message(message.chat.id, answer)

    elif (message.text == "Карточка специализации"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Что это такое?")
        btn2 = types.KeyboardButton("Когда выдают?")
        btn3 = types.KeyboardButton("Как заполнять?")
        btn4 = types.KeyboardButton("Как найти научного руководителя?")
        btn5 = types.KeyboardButton("До какого числа нужно заполнить?")
        btn6 = types.KeyboardButton("Что писать в графу спец. курсы?")
        btn7 = types.KeyboardButton("Сколько нужно спец. курсов?")
        btn8 = types.KeyboardButton("Как делать отчёт по науч. практике?")
        btn9 = types.KeyboardButton("Сроки научной практики?")
        btn10 = types.KeyboardButton(
            "Можно ли иметь научного руководителя до 3 курса? Когда можно начать заниматься наукой в институте?")
        btn11 = types.KeyboardButton("Нет моего вопроса")
        back = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, back)
        bot.send_message(message.chat.id,
                         text="1. Что это такое?\n2. Когда выдают?\n3. Как заполнять?\n4. Как найти научного руководителя?\n5. До какого числа нужно заполнить?\n6. Что писать в графу спец. курсы?\n7. Сколько нужно спец. курсов?\n8. Как делать отчёт по науч. практике?\n9. Сроки научной практики?\n10. Можно ли иметь научного руководителя до 3 курса? Когда можно начать заниматься наукой в институте?\n11. Нет моего вопроса\n12. Назад\n(нажмите на кнопку, чтобы перейти к вопросу)",
                         reply_markup=markup)
    elif (message.text == "Что это такое?"):
        answer = "Карточка специализация это способ контролирования и оптимизации поиска научного руководителя."
        bot.send_message(message.chat.id, answer)
    elif (message.text == "Когда выдают?"):
        answer = "В начале третьего курса."
        bot.send_message(message.chat.id, answer)
    elif (message.text == "Как заполнять?"):
        answer = "В карточке специализации написаны поля: ФИО студента, Номер группы и т.д. Все поля обязательны к заполнению, помимо заполнения полей, необходимо получить подпись научного руководителя, подпись секретаря кафедры, подпись заведующего кафедрой и подпись самого студента."
        bot.send_message(message.chat.id, answer)
    elif (message.text == "Как найти научного руководителя?"):
        answer = "Вам необходимо ходить на представление кафедр, активно смотреть и читать статьи по интересующей теме и обращать внимание на статьи с НГУ, тогда найти научного руководителя будет не так сложно. Можно попросить деканат  помочь связаться с научным руководителем. Также есть сайт: http://rnew.tilda.ws/specialization"
        bot.send_message(message.chat.id, answer)
    elif (message.text == "До какого числа нужно заполнить?"):
        answer = "Предельный срок сдачи - конец 7-ого семестра"
        bot.send_message(message.chat.id, answer)
    elif (message.text == "Что писать в графу спец. курсы?"):
        answer = "Список спец. курсов и спец. семинаров кафедр, которые ты обязуешься пройти."
        bot.send_message(message.chat.id, answer)
    elif (message.text == "Сколько нужно спец. курсов?"):
        answer = "Всё зависит от кафедр. Количество спец. курсов не ограничено, но общий срок - не менее года."
        bot.send_message(message.chat.id, answer)
    elif (message.text == "Как делать отчёт по науч. практике?"):
        answer = "Получить отчёт, заполнить поля и подписать так же у научного руководителя, получив оценку, получив подпись секретаря кафедры и заведующего кафедрой, а также не забыть выступить на кафедре."
        bot.send_message(message.chat.id, answer)
    elif (message.text == "Сроки научной практики?"):
        answer = "6-й семестр - научная практика;\n7-й семестр - производственная практика;\n8-й семестр - дипломная практика."
        bot.send_message(message.chat.id, answer)
    elif (
            message.text == "Можно ли иметь научного руководителя до 3 курса? Когда можно начать заниматься наукой в институте?"):
        answer = "Можно начать прямо со второго курса."
        bot.send_message(message.chat.id, answer)

    elif (message.text == "Восстановление, отчисление, перевод"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("За что могут отчислить?")
        btn2 = types.KeyboardButton("Как восстановиться?")
        btn3 = types.KeyboardButton("Как поменять поток?")
        btn4 = types.KeyboardButton("Как поменять направление?")
        btn5 = types.KeyboardButton("Как перейти на другой факультет?")
        btn6 = types.KeyboardButton(
            "Что происходит с почтой после отчисления, выпуска, или ухода в академический отпуск?")
        btn7 = types.KeyboardButton("Нет моего вопроса")
        back = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, back)
        bot.send_message(message.chat.id,
                         text="1. За что могут отчислить?\n2. Как восстановиться?\n3. Как поменять поток?\n4. Как поменять направление?\n5. Как перейти на другой факультет?\n6. Что происходит с почтой после отчисления, выпуска, или ухода в академический отпуск?\n7. Нет моего вопроса\n8. Назад\n(нажмите на кнопку, чтобы перейти к вопросу)",
                         reply_markup=markup)
    elif (message.text == "За что могут отчислить?"):
        answer = "Коснемся только того случая, когда студент будет отчислен по решению деканата ММФ. Самая, к сожалению, частая причина отчисления – это академическая неуспеваемость. А именно, получение по хотя бы одному предмету трех неудовлетворительных оценок (неявка/незачет/неудовлетворительно). Конечно же, имеется в виду неявка по неуважительной причине. Еще раз отметим, что данное правило касается любого предмета.\n Также поводом для отчисления может быть нарушение графика платежей, указанного в договоре об оказании платных образовательных услуг. Иными словами – существенная просрочка оплаты договора о платном обучении. Поэтому желательно о задержке оплаты информировать заместителя декана по вашему курсу во избежание проблем.\n Кроме того, причиной для отчисления является невыход из академического отпуска. Выход происходит не автоматически, поэтому вам по окончании академического отпуска необходимо написать заявление о выходе из него. Отсутствие данного заявления в течение пяти дней после окончания срока академического отпуска может стать причиной для отчисления.\n Студент может быть отчислен и в том случае, если были выявлены нарушения порядка приёма в НГУ со стороны обучающегося, за счет которых он оказался незаконно зачисленным в НГУ.\n Кроме указанных выше причин, в НГУ есть и отчисление как мера дисциплинарного взыскания. Отчислены могут быть студенты, которые систематически нарушают правила внутреннего распорядка НГУ, правила проживания в общежитии, прогуливают пары и т.д., однако исправляться не планируют.\n В исключительных случаях отчислить могут и за одно или два нарушения какого-либо правила, но эти нарушения должны быть действительно серьезными."
        bot.send_message(message.chat.id, answer)
    elif (message.text == "Как восстановиться?"):
        answer = "Восстановиться на ММФ на бюджетной основе могут студенты, обучавшиеся ранее на бюджете и отчислившиеся по собственному желанию. В случае отчисления студента решением деканата за неуспеваемость или обучения на платной основе восстановиться можно только на платной основе. Студенты, отчисленные за дисциплинарные взыскания, восстановиться не могут ни на бюджетной основе, ни на платной. Восстановление возможно только при наличии свободных бюджетных/платных мест в начало того семестра, из которого студент был отчислен. Все ранее сданные предметы после восстановления будут перезачтены с теми же оценками, а предметы, которые сданы не были, необходимо будет прослушать и сдать заново. На это отводится три попытки (основная сдача, первая и вторая пересдачи). Для того, чтобы восстановиться, нужно до начала семестра связаться с заместителем декана по тому курсу, на который вы будете восстанавливаться, узнать у него о наличии мест для восстановления и написать заявление. Далее процедура будет отличаться в зависимости от того, на какой основе вы будете восстанавливаться (бюджетной/платной), и необходимости брать повторные курсы. Обо всем этом лучше уточнить у заместителя декана перед восстановлением."
        bot.send_message(message.chat.id, answer)
    elif (message.text == "Как поменять поток?"):
        answer = "Понятие потока – это наше внутреннее разделение, которое никак не регламентируется в документах. Поэтому процедура будет описана через привычные понятия смены группы или направления подготовки.\n 1) Если вы обучаетесь на направлении «Математика и механика» и хотите сменить поток, то для вас есть возможность сделать это без смены направления (только на 1 или 2 курсе). Для этого вам нужно до начала или в первые две недели семестра обратиться к заместителю декана по вашему курсу, описать ему ситуацию и выбрать группу, в которую вы будете переводиться. Далее необходимо написать заявление на имя декана с просьбой перевести вас в выбранную группу. Необходимым условием одобрения этого заявление является наличие уважительной причины для перевода: принятие вас на один из профилей ММФ, специализация на одной из кафедр, чем-то подтверждаемое желание заниматься определенной областью математики и т.д. Затем остается только дождаться одобрения заявления на заседании деканата.\n 2) Если вы обучаетесь на направлении «Математика и компьютерные науки», то ситуация будет немного сложнее. Для смены потока необходимо будет сменить направление. В этом случае причина должна быть более существенной, чем при смене группы. Точного перечня причин сейчас нет, но можно отметить самые частые: перевод на один из профилей ММФ, специализация на кафедре (подтвержденная карточкой специализации), начало работы с научным руководителем по тематике другого направления и т.д. Основная часть переводов между направлениями проходит перед третьим курсом, когда все студенты выбирают себе научного руководителя и практику."
        bot.send_message(message.chat.id, answer)
    elif (message.text == "Как поменять направление?"):
        answer = "Каждая кафедра привязана к одному из четырех направлений («Математика», «Математика и компьютерные науки», «Прикладная математика и информатика», «Механика и математическое моделирование»), а учебные планы направлений начинают отличаться с третьего курса за счет уклона в определенную область математики. Единственной уважительной причиной перевода между направлением в этот период является специализация на кафедре, подтвержденная заполненной карточкой специализации или хотя бы бумагой от научного руководителя. (Комментарий: перед третьим курсом студенты МиМ или переводятся на МКН, или пишут бумагу с просьбой распределить их на одно из трех направлений внутри МиМ. Студенты МКН либо остаются у себя, либо переводятся на одно из трех других направлений). Для перевода всё так же нужно будет заполнить заявление, в нем указать нужное для перевода направление, указать причину и приложить подтверждение. После одобрения заявления на заседании деканата вы будете переведены на нужное направление."
        bot.send_message(message.chat.id, answer)
    elif (message.text == "Как перейти на другой факультет?"):
        answer = "При ответе на данный вопрос будем предполагать, что вы уже нашли ВУЗ/факультет, который согласен взять вас к себе переводом.  Коснемся далее только самой процедуры перевода. Первым делом необходимо заказать в деканате ММФ академическую справку – документ, в котором перечислены все сданные вами на данный момент дисциплины с оценками и количеством часов. Далее необходимо с академической справкой обратиться в ВУЗ/факультет, готовый вас принять, и отдать им ее вместе с заявлением о переводе. За 2-3 дня для вас готовится справка о переводе (документ, подтверждающий, что данный ВУЗ готов принять вас переводом из НГУ на определенное направление подготовки) и приложение к ней с описанием дисциплин, которые будут перезачтены, переаттестованы или составят академическую разницу. Затем с этими документами вам нужно подойти в деканат ММФ, написать заявление об отчислении переводом и отдать его вместе с полученными справками. И, наконец, вам остается только забрать выписку из приказа об отчислении переводом и принести ее в ваш новый ВУЗ вместе с заявлением и академической справкой (если вам их вернули)."
        bot.send_message(message.chat.id, answer)
    elif (message.text == "Что происходит с почтой после отчисления, выпуска, или ухода в академический отпуск?"):
        answer = "У вас остается бессрочный доступ к Вашей университетской почте, документам, презентациям и прочим материалам, созданным во время обучения. Однако через 30 дней адрес Вашей университетской электронной почты будет изменен на @alumni.nsu.ru. По сути, у вас просто сменится адрес электронной почты - всё остальное останется, как было.\nВ случае отчисления, если вы собираетесь восстановиться - после восстановления адрес почты обратно изменится на @g.nsu.ru и вы будете определены в новую для себя группу.\nАналогично и с выходом из академического отпуска."
        bot.send_message(message.chat.id, answer)

    elif (message.text == "Нет моего вопроса"):
        answer = "Если вашего вопроса нет в списке, то вы можете обратиться в деканат лично, либо же написать Сергею Геннадьевичу в телеграмме: https://t.me/Sergey_Steve. Часы приема https://www.nsu.ru/n/mathematics-mechanics-department/team/deanery/"
        bot.send_message(message.chat.id, answer)
    elif (message.text == "Здесь нет моего заявления"):
        answer = "Если вашего заявления нет в списке, то вы можете обратиться в деканат лично, либо воспользоваться сайтом https://www.nsu.ru/n/mathematics-mechanics-department/studentam/templates/"
        bot.send_message(message.chat.id, answer)

    elif (message.text == "Полезная информация"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Стикерпак ММФ")
        btn2 = types.KeyboardButton("Брендбук ММФ")
        btn3 = types.KeyboardButton("Сайт с научными руководителями")
        btn4 = types.KeyboardButton("Секции НГУ")
        btn5 = types.KeyboardButton("Кружки НГУ")
        btn6 = types.KeyboardButton("События НГУ")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, back)
        bot.send_message(message.chat.id,
                         text="1. Стикерпак ММФ\n2. Брендбук ММФ\n3. Сайт с научными руководителями\n4. Секции НГУ\n5. Кружки НГУ\n6. События НГУ\n7. Вернуться в главное меню",
                         reply_markup=markup)

    elif (message.text == "Стикерпак ММФ"):
        answer = "https://t.me/addstickers/mmfnsu"
        bot.send_message(message.chat.id, answer)

    elif (message.text == "Брендбук ММФ"):
        answer = "https://mca.nsu.ru/mmfstyle"
        bot.send_message(message.chat.id, answer)

    elif (message.text == "Сайт с научными руководителями"):
        answer = "http://rnew.tilda.ws/specialization"
        bot.send_message(message.chat.id, answer)

    elif (message.text == "Секции НГУ"):
        answer = "Список секций на фотографии, для записи приходите по расписанию"
        bot.send_message(message.chat.id, answer)
        bot.send_photo(message.chat.id, open('resources/sections.jpg', 'rb'))

    elif (message.text == "Кружки НГУ"):
        answer = "Юмористические клубы:\n -Юмористический клуб ММФ НГУ “Контора Братьев Дивановых”:\n https://vk.com/kontorabrd\n -Юмористический клуб “Квант”:\n https://vk.com/clubquant\n -Юмористический клуб “Maximin”:\n https://vk.com/maximin_club\nМузыкальные клубы:\n -Музклуб НГУ:\n https://vk.com/musclub_nsu\n -Академический хор НГУ:\n https://vk.com/club132862\nТанцевальные клубы:\n -Студия современного танца DaNSU:\n https://vk.com/contemp_dance_nsu\n -Вальсы НГУ\n https://vk.com/nsk_waltz\n -Студия исторического и ирландского танца 'Медиваль':\n https://vk.com/medieval_dances\nПрофессиональные клубы:\n -Команда НГУ по информационной безопасности SUSLo.PAS:\n https://vk.com/suslopas\n -Клуб 'Future Professional':\n https://vk.com/futureprofessional_nsu\n -Кейс-клуб НГУ:\n https://vk.com/caseclubnsu\n -Клуб парламентских дебатов НГУ:\n https://vk.com/nsu_debate\n -Секция горного туризма НГУ:\n https://vk.com/mountainnsu\n -SMBA - саморазвитие и бизнес:\n https://vk.com/nsu_smba\n -Financial Club NSU:\n https://vk.com/financialclubnsu\n -Экоклуб НГУ:\n https://vk.com/ecoclub_nsu\nСтуденческие СМИ:\n -Студенческое радио ‘Кактус’:\n https://vk.com/radiocactus\n -Межвузовский журнал Under the Universities (UU):\n https://vk.com/uumagazine\n -Фотоклуб НГУ:\n https://vk.com/nsu_photoclub\n -Место Встречи. Сибирь:\n https://vk.com/mestovstrechisib\nДосуговые клубы:\n -Клуб интеллектуальных игр НГУ:\n https://vk.com/kii_nsu\n -Клуб настольных игр НГУ:\n https://vk.com/games_odina\n -Книжный клуб НГУ:\n https://vk.com/bookclub_nsu\n -NSU.ESPORTS | Киберспортивное сообщество НГУ:\n https://vk.com/nsu.esports\n -Киноклуб НГУ:\n https://vk.com/nsu_cinemaclub\n -Литературный клуб ‘ПолLitera et cetera’:\n https://vk.com/club189569514\n -Клуб Мафии НГУ | Тихий Дон:\n https://vk.com/mafia_silent_don\n -Клуб настольных ролевых игр НГУ ‘Лабиринт историй’:\n https://vk.com/club130673094\n -Бридж-клуб НГУ:\n https://vk.com/bridge_nsu\n -Ридинг группа ‘Дигма’ НГУ:\n https://vk.com/digma_nsu\nИнтернациональные клубы:\n -Siberian English Club:\n https://vk.com/club5009\n -International Students Club:\n https://vk.com/club179366027\nОбщественная деятельность:\n -Добровольцы НГУ:\n https://vk.com/dobrovolc_nsu\n -Штаб студенческих отрядов НГУ:\n https://vk.com/shtab_so_nsu\n -Профсоюз студентов НГУ:\n https://vk.com/profkom_nsu\n -Отдел психологической поддержки НГУ:\n https://vk.com/club171744825\n -Студенческий спортивный клуб ENOT:\n https://vk.com/nsu_enot\n -Объединенный совет обучающихся:\n https://vk.com/oso_nsu\n"
        bot.send_message(message.chat.id, answer)

    elif (message.text == "События НГУ"):
        answer = "https://t.me/nsuniversity"
        bot.send_message(message.chat.id, answer)

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Вопросы по учебной составляющей")
        button2 = types.KeyboardButton("Заявления")
        button3 = types.KeyboardButton("Полезная информация")
        markup.add(button1, button2, button3)
        try:
            bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
        except ConnectionResetError:
            start(message)
            print("That was an error (connection)")

    elif (message.text == "Назад"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Стипендии")
        btn2 = types.KeyboardButton("Вопросы по сессии")
        btn3 = types.KeyboardButton("Вопросы по уч. процессу")
        btn4 = types.KeyboardButton("Оплата услуг НГУ")
        btn5 = types.KeyboardButton("Карточка специализации")
        btn6 = types.KeyboardButton("Восстановление, отчисление, перевод")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, back)
        try:
            bot.send_message(message.chat.id, text="Вы вернулись к выбору разделов", reply_markup=markup)
        except ConnectionResetError:
            start(message)
            print("That was an error (connection)")

    else:
        try:
            bot.send_message(message.chat.id, text="Неизвестная команда")
        except:
            print("That was an error")
            start(message)
            bot.polling(none_stop=True)


while True:
    try:
        bot.polling(none_stop=True)
    finally:
        print("That was an error")
