# **Fertilizers Store**

---

Веб-приложение интернет-магазина минеральных удобрений.

## Технологии

---

- [ ]  Python
- [ ]  Django framework
- [ ]  PostgreSQL

## Установка зависимостей

---

Для работы программы необходимо установить зависимости из файла `requirements.txt`.

Файл `.env.sample` содержит необходимые для работы переменные окружения.

Для рассылки используйте yandex почту.

## Структура проекта

---

### Приложения

- [ ]  user - интерфейсы для регистрации пользователя интернет-магазина.
- [ ]  catalog - интерфейс интернет-магазина (создание, просмотр, редактирование, удаление).
- [ ]  blog - интерфейс для продвижения интернет-магазина.

### Логика работы

- [ ]  Авторизованный пользователь может добавлять новые товары.
- [ ]  Пользователь может редактировать и удалять свои товары.

### Кеширование

- Низкоуровневое для кеширования списка записей блога.
- Кеширование контроллера отображения данных продукта.
- Кеширование всего веб-приложения (кроме, контроллеров добавления продукта и записей блога).