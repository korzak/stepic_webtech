### рабочее окружение
- nginx 1.4.6
- python 2.7.6
- gunicorn 17.5
- django 1.6.1
- каждый step в новой виртуальной машне

### создание проекта в рамках курса на stepic.org
Репозиторий должен быть склонирован в директорию `/home/box/web`  на виртуальной машине.

Загрузка кода в виртуальную машину происходит через github. Т.е. вы редактируете (и проверяете) код вашего проекта локально на вашей машине, после этого делаете `git push`, после этого делаете `git pull` в терминале stepic.
```bash
git clone https://github.com/itsanti/stepic_webtech.git /home/box/web
bash /home/box/web/init.sh
```
### полезные ссылки
- тестирование регулярных выражений https://regex101.com/#pcre
- введение в git https://githowto.com/ru

### ТЗ проекта ASK
дизайн проекта - https://stepic.org/s/84N9O01j

##### назначение ##### 
пишем сервис ответов на вопросы. мы можем:
- зарегистрироваться
- задать вопрос
- ответить на вопрос
- поставить лайк вопросу (изменяем рейтинг)

##### сущности проекта ##### 
1. **пользователь** - email имя пароль авка
2. **вопрос** - заголовок текст автор рейтинг
3. **ответ** - текст вопрос автор флаг "правильности"
4. **лайк** - вопрос пользователь

##### формы и страницы проекта #####
url: `/` regex: `^$` title: *главная страница* desc:
список "популярных" вопросов за последнюю неделю в порядке убывания рейтинга.

url: `/login/` regex: `^login/` title: *страница авторизации* desc: пользователь вводит email/пароль и авторизуется в системе.

url: `/signup/` regex: `^signup/` title: *страница регистрации* desc: пользователь вводит email/пароль/имя/аватарку и регистрируется.

url: `/question/123/` regex: `^question/(\d+)/` title: *страница одного вопроса* desc: выводится текст конкретного вопроса и список ответов на него. авторизованные могут добавить свой ответ.

url: `/ask/` regex: `^ask/` title: *страница добавления вопроса* desc: авторизованный может задать вопрос, после чего перейдет на страницу этого вопроса.

url: `/popular/` regex: `^popular/` title: *пока нет* desc: ...

url: `/new/` regex: `^new/` title: *список новых вопросов* desc: список вопросов по дате добавления, начиная с самого свежего.

url: `/like/123/` regex: `^like/(\d+)/` title: *ajax запрос* desc: пользователь ставит лайк, который увеличивает рейтиг вопроса. для 1 вопроса 1 лайк от данного пользователя.