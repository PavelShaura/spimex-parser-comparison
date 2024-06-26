# SPIMEX Trading Results Parser

Этот проект представляет собой aсинхронный и синхронный парсер на Python 3.10, который скачивает бюллетени по итогам торгов с сайта Санкт-Петербургской Международной Товарно-сырьевой биржи (https://spimex.com/markets/oil_products/trades/results/), извлекает необходимые данные и сохраняет их в базу данных.
### Проведено сравнение времени выполнения синхронного и асинхронного парсера.
Синхронный:
<img width="941" alt="sync_parse" src="https://github.com/PavelShaura/spimex-parser-comparison/blob/main/screen/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202024-06-26%2016-39-33.png">

Асинхронный:
<img width="941" alt="async_parse" src="https://github.com/PavelShaura/spimex-parser-comparison/blob/main/screen/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202024-06-26%2016-39-49.png">

## Установка

1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/PavelShaura/spimex-parser-comparison.git
   cd spimex-parser-comparison

2. Создайте виртуальное окружение и активируйте его:

`python -m venv venv`
`source venv/bin/activate` 
 
Для Windows используйте 
`venv\Scripts\activate`

3. Установите зависимости:

`pip install poetry` `poetry install`

4. Создайте файл .env в корневой директории проекта на примере файла .env_example

## Запуск

1.Запустите Docker Compose:

`docker-compose up -d`

2. Запустите парсер:

`python app/main.py`

Данные сохраняются в таблицу spimex_trading_results по итогам торгов начиная с 2023 года.


Веб-фреймворки и библиотеки

    aiohttp: Асинхронная библиотека для выполнения HTTP-запросов, что позволяет эффективно скачивать бюллетени с сайта биржи.
    BeautifulSoup4: Библиотека для парсинга HTML и XML документов, используемая для извлечения данных из загруженных бюллетеней.
    xlrd: Библиотека для работы с Excel файлами, используемая для чтения данных из загруженных бюллетеней.

База данных

    PostgreSQL: Реляционная база данных, используемая для хранения данных по итогам торгов.
    SQLAlchemy: ORM (Object-Relational Mapping) библиотека для Python, используемая для взаимодействия с базой данных.
    asyncpg: Асинхронный драйвер для PostgreSQL, обеспечивающий эффективное выполнение запросов к базе данных.

Управление зависимостями и настройками

    Pydantic: Библиотека для валидации данных и управления настройками, используемая для определения моделей данных.
    python-dotenv: Библиотека для загрузки переменных окружения из файла .env, что упрощает управление конфигурацией проекта.