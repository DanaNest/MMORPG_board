### Module D16 - итоговое задание
Upd. 13/11 - ночь
1. [x] Пользователи имеют возможность зарегистрироваться в нём по e-mail, получив письмо с кодом подтверждения регистрации.
2. [x] После регистрации пользователям становится доступно создание и редактирование объявлений. (и удаление)
3. [x] Объявления состоят из заголовка и текста, внутри которого могут быть картинки, встроенные видео и другой контент. (реализовано через CKeditor)
4. [x] Пользователи могут отправлять отклики на объявления других пользователей, состоящие из простого текста.
5. [x] При отправке отклика пользователь получает e-mail с оповещением о нём.
6. [x] Также пользователю доступна приватная страница с откликами на его объявления, внутри которой он может фильтровать отклики по объявлениям, удалять их (убирает из списка видимых для всех, кроме автора отклика) и принимать (при принятии отклика пользователю, оставившему отклик, также должно прийти уведомление).
7. [x] Кроме того, пользователь обязательно должен определить объявление в одну из следующих категорий: Танки, Хилы, ДД, Торговцы, Гилдмастеры, Квестгиверы, Кузнецы, Кожевники, Зельевары, Мастера заклинаний.
8. [x] Возможность отправлять пользователям новостные рассылки. (раз в неделю по понедельникам в 8 утра всем пользователям все новости за неделю)






[//]: # (Upd. 13/11 - утро)

[//]: # (Отклоненный отклик виден только автору отклика.)

[//]: # (Добавлена ссылка на новости в профиле.)

[//]: # ()
[//]: # (Upd. 12/11)

[//]: # (Добавлена приватная страница, фильтрация по объявлениям.)

[//]: # (Изменена модель Response, добавлен список статусов. )

[//]: # (Объединила в одну функцию принять и отклонить отклик.)

[//]: # ()
[//]: # (Upd. 11/11)

[//]: # (Добавлены отклики: оставлять может только не автор объявления. Принять может только автор.)

[//]: # (Все отклики видно на странице объявленния.)

[//]: # (Исправлена невозможность загрузить картинки на сервер пользователями &#40;не админом&#41; установкой библиотеки pillow.)

[//]: # ()
[//]: # (Upd. 10/11)

[//]: # (Доведено до ума вход/выход, добавлено отображение текущего пользователя. Попытка сделать личную страницу пока провалена.)

[//]: # (Добавлена форма ckeditor при добавлении с сайта, в виджете почему-то кнопки ютуба и аплоада картинок нет.)

[//]: # (Добавлено удаление поста и видимость удаления/редактирования для авторизованных пользователей.)

[//]: # ()
[//]: # (Upd. 9/11 )

[//]: # (Добавлена отправка письма с кодом подтверждения при регистрации юзера. &#40;День прожит не зря!&#41;)

[//]: # ()
[//]: # (6/11)

[//]: # (Кнопка ютуба добавлена, а также возможность заливать картинки в посты)

[//]: # (Корректное отображение имени категории в шаблоне)