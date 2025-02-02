Для подключения к бд в контейнере на винде надо узнать хост, а он может быть не 127.0.0.1, поэтому
для начала выведи список всех контейнеров:
    docker container ls        
а потом выведи инфу по контейнеру с бд, берем параметр "IPAddress":
    docker inspect id_контейнера


По alembic
1) создать рабочую директорию alembic: alembic init -t async alembic 
2) создать новую асинхронную миграцию: alembic revision --autogenerate -m "имя миграции"
3) применить последнюю миграцию alembic upgrade head
