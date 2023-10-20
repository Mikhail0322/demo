


Описание команд



//Добавление пользователя 
curl -X POST http://127.0.0.1:5000/users/user1
curl -X POST http://127.0.0.1:5000/users/user3

user1 - имя пользователя
user3 - имя пользователя

ответ:
{"response":"ok"}


//// Получение списка пользователей
curl -X GET http://127.0.0.1:5000/users

ответ:
"{\"user1\"}"
либо 
{}


// Добавление поста определенному пользователю
curl -X POST http://127.0.0.1:5000/posts/user1 -d "Post #1"

user1 - имя пользователя
"Post #1" - текстовые данные содержимого поста

ответ:
{"response":"ok"}


// Получение всех постов
curl -X GET http://127.0.0.1:5000/posts
ответ:
"{\"Post #1\"}"


// Получение постов от определеннго пользователя
curl -X GET http://127.0.0.1:5000/posts/user1 
user1 - имя пользователя
"{\"Post #1\"}"


// Изменения ранее созданого поста
curl -X PUT http://127.0.0.1:5000/posts/user1/0 -d "New Post #11111"
user1 - имя пользователя
0 - индекс поста

ответ:
{"response":"ok"}


// Удаление поста
curl -X DELETE http://127.0.0.1:5000/posts/user1/0
user1 - имя пользователя
0 - индекс поста

ответ:
{"response":"ok"}






Для тестирования:

curl -X POST http://127.0.0.1:5000/users/user1

curl -X GET http://127.0.0.1:5000/users

curl -X POST http://127.0.0.1:5000/users/user1

curl -X POST http://127.0.0.1:5000/users/user3

curl -X POST http://127.0.0.1:5000/posts/user1 -d "Post #1"

curl -X GET http://127.0.0.1:5000/posts/user3

curl -X GET http://127.0.0.1:5000/posts/user1
 
curl -X GET http://127.0.0.1:5000/users

curl -X GET http://127.0.0.1:5000/posts

curl -X PUT http://127.0.0.1:5000/posts/user1/0 -d "Post #11111"

curl -X GET http://127.0.0.1:5000/posts

curl -X DELETE http://127.0.0.1:5000/posts/user1/0

curl -X GET http://127.0.0.1:5000/posts













