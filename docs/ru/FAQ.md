Некоторые вопросы задаются часто, поэтому мы предоставили список для пользователей, которые сталкиваются с подобными проблемами.

## Требуется ли GPU?

- **Вопрос**:  
Требуется ли GPU, так как программа использует искусственный интеллект для распознавания и извлечения документов?

- **Ответ**:  
**GPU не требуется.** Но если у вас есть GPU, программа автоматически использует его для повышения производительности.

## Загрузка прервана?

- **Вопрос**:  
Я столкнулся со следующей ошибкой прерывания при загрузке модели. Что мне делать?

  ![image](https://github.com/user-attachments/assets/3c4eed44-3d9b-4e2f-a224-a58edca718c2)

- **Ответ**:  
Сеть подвергается помехам, пожалуйста, используйте стабильное сетевое соединение или попробуйте обойти вмешательство в сеть.

## Как обновиться до последней версии？

- **Вопрос**:  
Я хочу использовать некоторые функции последней версии, как мне её обновить?

- **Ответ**:  
`pip install -U pdf2zh`

## Указанные файлы не существуют: example.pdf

- **Проблема**:  
При выполнении программы пользователи могут получить следующие сообщения: `The following files do not exist: example.pdf`, если документ не был найден.

- **Решение**:
  - Откройте командную строку в каталоге, где находится файл, или
  - Введите полный путь к файлу непосредственно после pdf2zh, или
  - Используйте интерактивный режим `pdf2zh -i` для прямого перетаскивания файлов

## Ошибка SSL и другие проблемы с сетью

- **Проблема**:  
При загрузке моделей с hugging face пользователи из Китая могут столкнуться с ошибкой сети. Например, в [issue #55](https://github.com/PDFMathTranslate/PDFMathTranslate-next/issues/55), [#70](https://github.com/PDFMathTranslate/PDFMathTranslate-next/issues/70).

- **Решение**:
  - [Обход GFW](https://github.com/clash-verge-rev/clash-verge-rev).
  - [Использовать зеркало Hugging Face](https://hf-mirror.com/).
  - [Использовать портативную версию](https://github.com/PDFMathTranslate/PDFMathTranslate-next?tab=readme-ov-file#method-ii-portable).
  - [Использовать Docker](https://github.com/PDFMathTranslate/PDFMathTranslate-next#docker).
  - [Обновить сертификаты](https://stackoverflow.com/questions/51925384/unable-to-get-local-issuer-certificate-when-using-requests), как предложено в [issue #55](https://github.com/PDFMathTranslate/PDFMathTranslate-next/issues/55).

## Локальный сервер недоступен

Пожалуйста, смотрите ниже.

## Ошибка при запуске GUI с использованием 0.0.0.0

- **Проблема**:  
Использование прокси-программ в глобальном режиме может препятствовать корректному запуску Gradio. Например, в [issue #77](https://github.com/PDFMathTranslate/PDFMathTranslate-next/issues/77).

- **Решение**:  
Используйте режим правил

  ![image](https://github.com/user-attachments/assets/b1f2b16a-eb6a-4c03-995c-332ef1d82c96)

<div align="right"> 
<h6><small>Часть содержимого этой страницы была переведена GPT и может содержать ошибки.</small></h6>