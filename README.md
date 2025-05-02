---Telegram Kripto Fiyat Botu---

Bu Telegram botu, CoinGecko API'sini kullanarak Bitcoin, Ethereum, Solana, Binance Coin, XRP ve Avalanchegibi kripto para birimlerinin anlık fiyatlarını kullanıcılarla paylaşır. Bot, belirli saatlerde (örneğin, her gün saat 09:00 ve 21:00) bu bilgileri kullanıcıya gönderir.

Bu projeyi çalıştırmak için aşağıdaki gereksinimlere sahip olmanız gerekir:
- Python 3.6 veya üstü
- `requests` kütüphanesi
- `python-telegram-bot` kütüphanesi
- `schedule` kütüphanesi
- `.env` dosyası
Projenizin kök dizininde .env adında bir dosya oluşturun. Bu dosyada, Telegram botunuzun token'ı ve chat ID bilgilerinizi saklayacağız. .env dosyasına aşağıdaki gibi bir içerik ekleyin:
TOKEN='YOUR_BOT_TOKEN'
CHAT_ID='YOUR_CHAT_ID'
