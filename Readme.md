# Документация API Gateway


# Сервис личного кабинета


## Базовый ендпоинт: `/get/token/`


## Token:
Ресурс для работы с токенами.


> GET '/get/token/'


Получает два токена: access, refresh.


| Name | Type |
|:--------:|:-----:|
| access | str |
| refresh | str |


Пример ответа:
'{
  "status_code": 200,
  "detail": "OK",
  "headers": null
}'


## Обязательно уточнение:
Сервис не будет работать если не передать токены в эндпоинт /get/token/


## Базовый ендпоинт: `/logout/`


## Logout:
Ресурс для удаления токенов из cookie.


> GET '/logout/'


Эндпоинт сам достает токены из cookie и утилизирует их.


Пример ответа:
'{
  "status_code": 200,
  "detail": "OK",
  "headers": null
}'


## Базовый ендпоинт: `/predict/`


## Predict:
Ресурс для получения специальностей и вероятности поступления на них.


> POST '/predict/'


Обязательные данные подлежащие заполнению.


| Name | Type |
|:----------:|:---------:|
| top_n | str |
| age | int |
| gender | Literal['М','Ж'] |
| sport | str |
| foreign | str |
| gpa | float |
| points | int |
| bonus_points | int |
| exams | List[str] |
| priority | int |
| education | str |
| study_form | Literal["Очная", "Заочная", "Очно-Заочная"] |


Пример ответа:
''


Разработчик api рекомендательной системы и классификатора.
GitHub: https://github.com/Andr171p


## Free:
Ресурс для получения упрощенной рекомендации.


> POST '/predict/free'


Обязательные данные подлежащие заполнению.


| Name | Type |
|:----------:|:-------:|
| year | int |
| gender | Literal['М','Ж'] |
| gpa | float |
| points | int |
| direction | str |


Пример ответа:
0.54


Разработчик api упрощенной рекомендации.
GitHub: https://github.com/Andr171p


## Базовый ендпоинт: `/answer/`


## Answer:
Чат на основе gigachat отвечающий на вопросы связынне с ТИУ.


> GET '/answer/'



Принимает параметр message.


| Name | Type |
|:----------:|:-------:|
| message | str |

Пример вопроса:
'что такое ТИУ'
Пример ответа:
'{
  "answer": "Тюменский индустриальный университет (ТИУ) — это высшее учебное заведение в Тюмени, которое специализируется на подготовке специалистов для нефтегазовой и строительной отраслей."
}'


Разработчик api упрощенной рекомендации.
GitHub: https://github.com/Andr171p

