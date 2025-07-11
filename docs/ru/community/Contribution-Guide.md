# Вклад в проект

> [!CAUTION]
>
> Текущие сопровождающие проекта исследуют автоматизированную интернационализацию документации. Поэтому любые PR, связанные с интернационализацией/переводом документации, НЕ будут приниматься!
>
> Пожалуйста, НЕ отправляйте PR, связанные с интернационализацией/переводом документации!

Спасибо за ваш интерес к этому проекту! Прежде чем начать вносить свой вклад, пожалуйста, уделите немного времени, чтобы прочитать следующие рекомендации, чтобы ваш вклад мог быть легко принят.

## Типы вкладов, которые не принимаются

1. Интернационализация/перевод документации
2. Вклад, связанный с основной инфраструктурой, такой как HTTP API и т. д.
3. Проблемы, явно помеченные как "No help needed" (включая проблемы в репозиториях [Byaidu/PDFMathTranslate](Byaidu/PDFMathTranslate) и [PDFMathTranslate/PDFMathTranslate-next](PDFMathTranslate/PDFMathTranslate-next)).
4. Другие вклады, которые модераторы сочтут неуместными.
5. Вклад в документацию, но изменение документации на языках, отличных от английского.
6. PR, требующие изменения PDF-файлов.

Пожалуйста, НЕ отправляйте PR, связанные с вышеуказанными типами.

> [!NOTE]
>
> Если вы хотите внести вклад в документацию, пожалуйста, **изменяйте только английскую версию документации**. Другие языковые версии переводятся самими участниками.

## Процесс внесения вклада

1. Форкните этот репозиторий и клонируйте его локально.
2. Создайте новую ветку: `git checkout -b feature/<feature-name>`.
3. Разрабатывайте и убедитесь, что ваш код соответствует требованиям.
4. Зафиксируйте изменения:
   ```bash
   git add .
   git commit -m "<semantic commit message>"
   ```
5. Отправьте изменения в ваш репозиторий: `git push origin feature/<feature-name>`.
6. Создайте PR на GitHub, предоставьте подробное описание и запросите ревью у [@awwaawwa](https://github.com/awwaawwa).
7. Убедитесь, что все автоматические проверки пройдены.

> [!TIP]
>
> Вам не нужно ждать, пока разработка будет полностью завершена, чтобы создать PR. Создание PR на раннем этапе позволяет нам проверить вашу реализацию и дать рекомендации.
>
> Если у вас есть вопросы по исходному коду или связанным темам, пожалуйста, свяжитесь с сопровождающим по адресу aw@funstory.ai.
>
> Файлы ресурсов для версии 2.0 доступны в [BabelDOC](https://github.com/funstory-ai/BabelDOC). Код для загрузки связанных ресурсов находится в BabelDOC. Если вы хотите добавить новые файлы ресурсов, пожалуйста, свяжитесь с сопровождающим BabelDOC по адресу aw@funstory.ai.

## Основные требования

<h4 id="sop">1. Рабочий процесс</h4>

- Пожалуйста, сделайте форк из ветки `main` и разрабатывайте на своей форкнутой ветке.
   - При отправке Pull Request (PR) предоставьте подробное описание ваших изменений.
   - Если ваш PR не проходит автоматические проверки (указывается как `checks failed` с красным крестиком), пожалуйста, проверьте соответствующие `details` и внесите изменения в свою заявку, чтобы новый PR прошел все проверки.


<h4 id="dev&test">2. Разработка и тестирование</h4>

- Используйте команду `pip install -e .` для разработки и тестирования.


<h4 id="format">3. Форматирование кода</h4>

- Настройте инструмент `pre-commit` и включите `black` и `flake8` для форматирования кода.


<h4 id="requpdate">4. Обновление зависимостей</h4>

- Если вы добавляете новые зависимости, пожалуйста, своевременно обновите список зависимостей в файле `pyproject.toml`.


<h4 id="docupdate">5. Обновления документации</h4>

- Если вы добавляете новые параметры командной строки, пожалуйста, обновите список параметров командной строки во всех языковых версиях файла `README.md` соответствующим образом.


<h4 id="commitmsg">6. Сообщения коммитов</h4>

- Используйте [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/), например: `feat(translator): add openai`.


<h4 id="codestyle">7. Стиль кодирования</h4>

- Убедитесь, что ваш код соответствует базовым стандартам стиля кодирования.
   - Используйте либо snake_case, либо camelCase для именования переменных.


<h4 id="doctypo">8. Форматирование документации</h4>

- Для форматирования `README.md` следуйте [Руководству по написанию текстов на китайском языке](https://github.com/sparanoid/chinese-copywriting-guidelines).
   - Убедитесь, что документация на английском и китайском языках всегда актуальна; обновления документации на других языках необязательны.

## Добавление движка перевода

1. Добавьте новый класс конфигурации переводчика в файл `pdf2zh/config/translate_engine_model.py`.
2. Добавьте экземпляр нового класса конфигурации переводчика в псевдоним типа `TRANSLATION_ENGINE_SETTING_TYPE` в том же файле.
3. Добавьте новый класс реализации переводчика в папку `pdf2zh/translator/translator_impl`.

> [!NOTE]
>
> Этот проект не намерен поддерживать какие-либо движки перевода с RPS (запросами в секунду) ниже 4. Пожалуйста, не отправляйте поддержку для таких движков.

## Структура проекта

- **config folder**: Система конфигурации.
- **translator folder**: Реализации, связанные с переводчиком.
- **gui.py**: Предоставляет графический интерфейс.
- **const.py**: Некоторые константы.
- **main.py**: Предоставляет инструмент командной строки.
- **high_level.py**: Высокоуровневые интерфейсы на основе BabelDOC.
- **http_api.py**: Предоставляет HTTP API (не запущено).

## Свяжитесь с нами

Если у вас есть какие-либо вопросы, отправьте отзыв через Issue или присоединяйтесь к нашей группе в Telegram. Спасибо за ваш вклад!

> [!TIP]
>
> [Immersive Translate](https://immersivetranslate.com) спонсирует ежемесячные коды Pro-подписки для активных участников этого проекта. Подробности смотрите здесь: [BabelDOC/PDFMathTranslate Contributor Reward Rules](https://funstory-ai.github.io/BabelDOC/CONTRIBUTOR_REWARD/)

<div align="right"> 
<h6><small>Часть содержимого этой страницы была переведена GPT и может содержать ошибки.</small></h6>