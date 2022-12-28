# JupyterHub
## Информация по развёртыванию
Инструкция  по развёртыванию:
1. В командной строке написать docker-compose build, чтобы собрать образы
```
docker-compose build
```
2. В командной строке написать docker-compose up, чтобы создать контейнеры
```
docker-compose up
```
3. В строке поиска браузера написать 127.0.0.1:80
```
127.0.0.1:80
```
Инструкция по закрытию:
1. Заходим в командную строку и нажимаем Ctrl+C
2. В командной строке написать docker-compose down --remove-orphans, чтобы остановить и удалить контейнеры, которые были созданы в предыдущем запуске docker-compose up
```
docker-compose down --remove-orphans
```
## Аунтификация
Введите логин admin и пароль admin. После этого будет создан аккаунт с данными. При этом права администратора есть только у пользователя c именем admin.
