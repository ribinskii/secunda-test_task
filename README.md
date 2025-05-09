# Введение
Выполненная работа является техническим заданием.

# Архитектура
Сервис построен на основе луковой архитектуры.

```bash
secunda-test_task
└── app
    ├── core # Ядро сервиса
    │   ├── entities # Бизнес сущности
    │   ├── repositories # Интерфейс бд
    │   └── services # Бизнес логика
    └── infrastructure # Внешние сервисы
          ├── controllers # Контроллеры (RestAPI, gRPC, GraphQL и т.д.)
          └── db # Имплементация бд
```

# Запуск проекта
Для запуска используется утилита make.
Перед использование утилиты установите и запустите docker.
Все комнады выполняются в корневой дирретории.

Команды

* Запуск сервиса

```bash
make up
```

* Остановка контейнеров
```bash
make stop
```

* Остановка и удаление контейнеров
```bash
make down
```

* Переустановка всех контейнеров
```bash
make rebuild
```

* Статус всех контейнеров
```bash
make ps
```

* Полная очистка созданного docker-окружения.
```bash
make clean
```

# Доступ к API
* Доступ к API осуществляется постредством статического ключа.
Http заголовок для отправки ключа и значение ключа находятся в .env.
* Для доступа к АPI через Swagger введите значение ключа слева в верхнем углу Swagger UI.

# Примечание
* Для сокращения времени разработки обработка ошибок не реализована.
* Для сокращения времени разарботки логирование не реализовано.
* Для упрощения запуска проекта .env добавлен в репозиторий.
* Для сокращения времени разработки аннотации типов добавлены не везде.
* Для сокращения времени разработки функционал не покрыл тестами.