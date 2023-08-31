# Solution
В папке "solution" находится notebook solution.ipynb с решением задачи. В нем процесс считывания и обработки данных, а также обучение модели. В качестве модели была взята модель ruDialoGPT-medium (https://huggingface.co/tinkoff-ai/ruDialoGPT-medium). После обучения модель была сохранена на Google Диск (ссылка ниже).
# Telegram Bot
1. Для использования обученной модели был создан телеграм бот. Телеграм бот находится в папке "bot" и запускается скриптом "main.py".
2. Скрипт model.py отвечает за генерацию продолжения диалога на основе введенных данных от пользователя. Для использования модели в скрипте model.py надо скачать модель с Google Диска (https://drive.google.com/file/d/193AXRQ2VsQQf1gmtImSGjokwU6Qs-Yw6/view?usp=sharing) и поместить в папку "bot".

# Docker
Telegram Bot обернут в Docker. Docker создавался в Windows. Для использования докера следуйте следующим инструкциям:
1. Установить докер.
2. Заклонить репозиторий в удобную для вас папку.
3. Редактировать Dockerfile, указав ваш токен от телеграм бота вместо X: ENV BOT_TOKEN = X.
4. run `docker build -t chatbot .`
5. run `docker run -p 8000:8080 chatbot`
