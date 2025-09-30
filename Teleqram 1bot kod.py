import asyncio
from telegram import Bot
import random

TOKEN = "7834612035:AAFl9PE2P_ZRw6WwtQslBLK1G70qmjmavlM"
CHANNEL = "@konputerenginer"

# Kod nümunələri
kodlar = [
    "Python: print('Salam, dünya!')",
    "C: printf('Salam, dünya!');",
    "Java: System.out.println('Salam, dünya!');",
    "JavaScript: console.log('Salam, dünya!');"
]

# Programming tips
tips = [
    "Tip: Funksiyalarınızı kiçik və təkrar istifadə oluna bilən edin.",
    "Tip: Kodunuzu oxunaqlı yazmaq üçün şərhlər əlavə edin.",
    "Tip: Version control (Git) istifadə edin.",
    "Tip: Hər gün kiçik bir kod yazmaq sizi yaxşı proqramçı edir."
]

async def main():
    bot = Bot(token=TOKEN)
    while True:
        kod_mesaj = random.choice(kodlar)
        tip_mesaj = random.choice(tips)
        mesaj = f"💻 Bugünkü proqramlaşdırma məlumatı:\n\n{kod_mesaj}\n\n💡 Tip: {tip_mesaj}"
        
        await bot.send_message(chat_id=CHANNEL, text=mesaj)
        print("Mesaj göndərildi!")  # Terminalda yoxlama üçün
        await asyncio.sleep(86400)  # 1 gün gözləmə

asyncio.run(main())
