import os
import random
import telebot
from dotenv import load_dotenv

# Завантажуємо змінні оточення з файлу .env
load_dotenv()

# Зчитуємо токен бота (сам токен зберігається лише у файлі .env)
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Перевіряємо, чи знайдено токен перед запуском
if not BOT_TOKEN:
    raise ValueError("Помилка: не знайдено BOT_TOKEN у файлі .env!")

# Ініціалізуємо бота
bot = telebot.TeleBot(BOT_TOKEN)

# Список із 5 випадкових реакцій на команду /feed (годування)
FEED_RESPONSES = [
    "Ням-ням! Піксельний улюбленець з'їв смачну рибку і замуркотів. Ситість відновлено!",
    "Хрум-хрум! Вихованець із задоволенням погриз хрустке печиво.",
    "Ура, обід! Твій улюбленець поїв і тепер радісно стрибає по екрану.",
    "Смакота! Вихованець випив теплого молока і вклався трохи подрімати.",
    "Дякую за турботу! Тепер у твого улюбленця повно енергії для нових ігор."
]

# Список із 5 випадкових реакцій на команду /play (гра)
PLAY_RESPONSES = [
    "Ти кинув улюбленцю гумовий м'ячик — він зловив його в повітрі! Настрій на висоті!",
    "Вихованець весело бігає за сонячним зайчиком по екрану. Щастя зашкалює!",
    "Ви погралися в хованки: улюбленець заховався за кнопку меню, але ти його знайшов!",
    "Улюбленець впіймав іграшковий бантик і гордо приніс його тобі. Настрій чудовий!",
    "Веселі стрибки вдалися на славу! Улюбленець трохи втомився, але дуже задоволений."
]

# Обробник команди /start — знайомство та запуск
@bot.message_handler(commands=['start'])
def handle_start(message):
    welcome_text = (
        "Привіт! Я PocketPet Bot — твій віртуальний улюбленець.\n\n"
        "Я допоможу тобі трохи відпочити під час навчання. "
        "Тисни /feed, щоб погодувати мене, /play — щоб погратися, "
        "або /help, щоб переглянути всі команди."
    )
    bot.send_message(message.chat.id, welcome_text)

# Обробник команди /help — коротка інструкція
@bot.message_handler(commands=['help'])
def handle_help(message):
    help_text = (
        "Інструкція з догляду за улюбленцем:\n\n"
        "/start — запустити віртуального улюбленця\n"
        "/help — показати список усіх команд\n"
        "/feed — погодувати вихованця та відновити ситість\n"
        "/play — погратися з вихованцем (м'ячик або бантик)"
    )
    bot.send_message(message.chat.id, help_text)

# Обробник команди /feed — годування вихованця
@bot.message_handler(commands=['feed'])
def handle_feed(message):
    # Обираємо одну випадкову відповідь зі списку годування
    reaction = random.choice(FEED_RESPONSES)
    bot.send_message(message.chat.id, reaction)

# Обробник команди /play — гра з вихованцем
@bot.message_handler(commands=['play'])
def handle_play(message):
    # Обираємо одну випадкову відповідь зі списку ігор
    reaction = random.choice(PLAY_RESPONSES)
    bot.send_message(message.chat.id, reaction)

# Запускаємо нескінченний цикл опитування серверів Telegram
if name == "main":
    print("PocketPet Bot успішно запущений...")
    bot.polling(none_stop=True)
