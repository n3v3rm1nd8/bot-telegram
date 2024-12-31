import socket
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Define el comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('¡Hola! para empezar un escaneo usa /scan')

# Función para manejar el comando /ip
async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Obtén los argumentos enviados con el comando
    if context.args:
        ip = context.args[0]  # El primer argumento después de /ip
        await update.message.reply_text(f"Escaneando...")

        #ports = range(1, 65536)
        ports = range(1, 100)
        #cont = 0
        for port in ports:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.1)
                try:
                    result = sock.connect_ex((ip, port))
                    srv = socket.getservbyport(port)
                    if result == 0:
                        await update.message.reply_text(f'*[+] {port} open ({srv})*', parse_mode='Markdown')
                except:
                        pass
                sock.close()
        await update.message.reply_text(f'_[!] Finalizado_', parse_mode='Markdown')
    else:
        await update.message.reply_text("Por favor, envíame una IP después del comando. Ejemplo: /scan 192.168.1.1")

def main():
    # Token de tu bot
    TOKEN = "7946883953:AAHer_lQNuljsj_UFfnvkwxNTg8KjidEMNQ"
    
    # Crea la aplicación con ApplicationBuilder
    app = ApplicationBuilder().token(TOKEN).build()

    # Agrega manejadores
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("scan", scan))

    # Inicia el bot
    app.run_polling()

if __name__ == '__main__':
    main()