import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
login = os.getenv('LOGIN')
passward = os.getenv('PASSWARD')

site = 'dvmn.org'
freand_name = 'Дима'
my_name = 'Егор'

letter = """From: egorkazasheby@mail.ru
To: egorkazasheby@mail.ru
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8;"""

mail = """ {letter}

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""". format(letter = letter )


mail = mail.replace('%website%', 'https://dvmn.org/referrals/y7KP7bIwm1I47w0dKrebOShcJ96dRCeX0523n8Jb/')
mail = mail.replace('%friend_name%', 'Дима')
mail = mail.replace('%my_name%', 'Егор')
mail = mail.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.mail.ru:465')
server.login(login, passward)
server.sendmail('egorkazasheby@mail.ru', 'egorkazasheby@mail.ru', mail)
server.quit()

