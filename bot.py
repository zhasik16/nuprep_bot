import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Username администраторов
ADMIN_USERNAMES = ["@Nurbolna", "@mmagzhan1"]

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    
    welcome_text = (
        f"👋 **Hi there! Welcome to NUET Prep Bot!**\n\n"
        f"🎯 **We help students prepare for the Nazarbayev University Entrance Test (NUET) with proven systems.**\n\n"
        f"📚 **Choose what you'd like to explore:**"
    )
    
    keyboard = [
        [InlineKeyboardButton("📘 NUET Self-Study Course (Math + Critical Thinking)", callback_data='self_study_course')],
        [InlineKeyboardButton("📝 NUET Mock Tests + Video Solutions (Math + Critical Thinking)", callback_data='mock_tests')],
        [InlineKeyboardButton("🎁 Free NUET Materials", callback_data='free_materials')],
        [InlineKeyboardButton("ℹ️ About NUET", callback_data='about_nuet')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode='Markdown')

# Обработчик нажатий на кнопки
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'self_study_course':
        await show_self_study_course(query)
    elif query.data == 'mock_tests':
        await show_mock_tests(query)
    elif query.data == 'free_materials':
        await show_free_materials(query)
    elif query.data == 'about_nuet':
        await show_about_nuet(query)
    elif query.data == 'main_menu':
        await main_menu(query)
    elif query.data == 'buy_self_study':
        await initiate_self_study_payment(query, context)
    elif query.data == 'buy_mock_package':
        await initiate_mock_tests_payment(query, context)
    elif query.data == 'download_strategy':
        await download_strategy_guide(query)
    elif query.data == 'download_formulas':
        await download_formula_sheet(query)

# Показать Self-Study Course
async def show_self_study_course(query):
    text = (
        "🎓 **NUET Self-Study Course**\n\n"
        "✅ **Covers Mathematics and Critical Thinking**\n"
        "🔄 **Step-by-step system:** Watch video → Do Homework → Pass Test (80%+) → Unlock next lesson\n"
        "⚡ **Automatic progress unlock keeps you motivated**\n"
        "🌍 **Learn anytime, anywhere**\n\n"
        "💵 **Price:** 100,000 KZT\n"
        "🔥 **Special Offer:** Pay within 24 hours → only 50,000 KZT"
    )
    
    keyboard = [
        [InlineKeyboardButton("🛒 Buy Self-Study Course", callback_data='buy_self_study')],
        [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data='main_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(text, reply_markup=reply_markup, parse_mode='Markdown')

# Показать Mock Tests
async def show_mock_tests(query):
    text = (
        "📊 **NUET Mock Tests + Video Solutions**\n\n"
        "🎯 **Full NUET-style Mocks:** Mathematics + Critical Thinking\n"
        "📈 **Instantly check your score**\n"
        "🔍 **Review every mistake with detailed video solutions**\n"
        "🏆 **Train exactly like in the real exam**\n\n"
        "💵 **Price:** 6,000 KZT / month\n"
        "🔥 **Special Offer:** Pay within 24 hours → get full access until NUET exam for only 15,000 KZT (instead of 30,000 KZT)"
    )
    
    keyboard = [
        [InlineKeyboardButton("🛒 Buy Mock Package", callback_data='buy_mock_package')],
        [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data='main_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(text, reply_markup=reply_markup, parse_mode='Markdown')

# Показать Free Materials
async def show_free_materials(query):
    text = (
        "🎁 **Free NUET Materials**\n\n"
        "📚 **Get free resources prepared by NUET experts:**\n"
        "• 📋 PDF Guide: NUET Prep Strategy — 7 Step Process\n"
        "• 📊 Formula Sheet: All Key Mathematics Formulas\n\n"
        "🚀 **Download below and start your preparation today!**"
    )
    
    keyboard = [
        [InlineKeyboardButton("📥 Download NUET Strategy Guide", callback_data='download_strategy')],
        [InlineKeyboardButton("📥 Download Math Formula Sheet", callback_data='download_formulas')],
        [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data='main_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(text, reply_markup=reply_markup, parse_mode='Markdown')

# Показать About NUET
async def show_about_nuet(query):
    text = (
        "ℹ️ **What is NUET?**\n\n"
        "🎯 **NUET = Nazarbayev University Entrance Test.**\n"
        "**It consists of:**\n"
        "1️⃣ **Mathematics** (Problem Solving + Logic)\n"
        "2️⃣ **Critical Thinking**\n\n"
        "💪 **Our courses focus on these core parts of NUET.**\n"
        "⭐ **They are designed by teachers who scored 221/240 and helped dozens of students win NU Grants.**"
    )
    
    keyboard = [
        [InlineKeyboardButton("📘 Self-Study Course", callback_data='self_study_course')],
        [InlineKeyboardButton("📝 Mock Tests", callback_data='mock_tests')],
        [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data='main_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(text, reply_markup=reply_markup, parse_mode='Markdown')

# Главное меню
async def main_menu(query):
    text = (
        "🏠 **Main Menu**\n\n"
        "👋 **Hi there! Welcome to NUET Prep Bot!**\n"
        "🎯 **We help students prepare for the Nazarbayev University Entrance Test (NUET) with proven systems.**\n\n"
        "📚 **Choose what you'd like to explore:**"
    )
    
    keyboard = [
        [InlineKeyboardButton("📘 NUET Self-Study Course (Math + Critical Thinking)", callback_data='self_study_course')],
        [InlineKeyboardButton("📝 NUET Mock Tests + Video Solutions (Math + Critical Thinking)", callback_data='mock_tests')],
        [InlineKeyboardButton("🎁 Free NUET Materials", callback_data='free_materials')],
        [InlineKeyboardButton("ℹ️ About NUET", callback_data='about_nuet')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(text, reply_markup=reply_markup, parse_mode='Markdown')

# Инициировать оплату Self-Study Course
async def initiate_self_study_payment(query, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.update({
        'course_type': 'self_study',
        'course_name': 'NUET Self-Study Course',
        'course_price': '50,000 KZT (special offer)',
        'user_id': query.from_user.id,
        'user_name': query.from_user.full_name,
        'user_username': query.from_user.username
    })
    
    text = (
        "💳 **Payment for NUET Self-Study Course**\n\n"
        "🔥 **Special Offer:** 50,000 KZT (valid for 24 hours)\n\n"
        "📋 **To complete your purchase:**\n\n"
        "1️⃣ **Make payment using the link below:**\n"
        "🔗 [Pay via Kaspi](https://pay.kaspi.kz/pay/gozdx2ic)\n\n"
        "2️⃣ **Amount to pay: 50,000 KZT**\n\n"
        "3️⃣ **After payment, please send to this chat:**\n"
        "   • 📸 Payment confirmation screenshot\n"
        "   • 👤 Your full name in the file caption\n\n"
        "⏰ **Admin will verify and activate your access within 24 hours!**"
    )
    
    keyboard = [
        [InlineKeyboardButton("⬅️ Back to Course", callback_data='self_study_course')],
        [InlineKeyboardButton("🏠 Main Menu", callback_data='main_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(text, reply_markup=reply_markup, parse_mode='Markdown')

# Инициировать оплату Mock Tests
async def initiate_mock_tests_payment(query, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.update({
        'course_type': 'mock_tests',
        'course_name': 'NUET Mock Tests + Video Solutions',
        'course_price': '15,000 KZT (full access until exam)',
        'user_id': query.from_user.id,
        'user_name': query.from_user.full_name,
        'user_username': query.from_user.username
    })
    
    text = (
        "💳 **Payment for NUET Mock Tests + Video Solutions**\n\n"
        "🔥 **Special Offer:** 15,000 KZT for full access until NUET exam\n\n"
        "📋 **To complete your purchase:**\n\n"
        "1️⃣ **Make payment using the link below:**\n"
        "🔗 [Pay via Kaspi](https://pay.kaspi.kz/pay/gozdx2ic)\n\n"
        "2️⃣ **Amount to pay: 15,000 KZT**\n\n"
        "3️⃣ **After payment, please send to this chat:**\n"
        "   • 📸 Payment confirmation screenshot\n"
        "   • 👤 Your full name in the file caption\n\n"
        "⏰ **Admin will verify and activate your access within 24 hours!**"
    )
    
    keyboard = [
        [InlineKeyboardButton("⬅️ Back to Package", callback_data='mock_tests')],
        [InlineKeyboardButton("🏠 Main Menu", callback_data='main_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(text, reply_markup=reply_markup, parse_mode='Markdown')

# Скачать Strategy Guide
async def download_strategy_guide(query):
    text = (
        "📚 **NUET Prep Strategy — 7 Step Process**\n\n"
        "✅ **This comprehensive guide will help you:**\n"
        "• 📅 Create an effective study plan\n"
        "• 🧠 Master both Math and Critical Thinking sections\n"
        "• ⏱️ Manage your time during the exam\n"
        "• ⚠️ Avoid common mistakes\n\n"
        "🔗 **Download link:** [NUET Strategy Guide](https://example.com/nuet-strategy-guide.pdf)\n\n"
        "🎓 **Good luck with your preparation!** ✨"
    )
    
    keyboard = [
        [InlineKeyboardButton("📊 Download Math Formula Sheet", callback_data='download_formulas')],
        [InlineKeyboardButton("⬅️ Back to Free Materials", callback_data='free_materials')],
        [InlineKeyboardButton("🏠 Main Menu", callback_data='main_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(text, reply_markup=reply_markup, parse_mode='Markdown')

# Скачать Formula Sheet
async def download_formula_sheet(query):
    text = (
        "📊 **All Key Mathematics Formulas for NUET**\n\n"
        "✅ **This formula sheet contains:**\n"
        "• ➕ Algebra formulas and rules\n"
        "• 📐 Geometry theorems and formulas\n"
        "• 📏 Trigonometry identities\n"
        "• 💡 Problem-solving shortcuts\n\n"
        "🔗 **Download link:** [Math Formula Sheet](https://example.com/nuet-formula-sheet.pdf)\n\n"
        "📝 **Perfect for quick revision before the exam!** 🚀"
    )
    
    keyboard = [
        [InlineKeyboardButton("📚 Download Strategy Guide", callback_data='download_strategy')],
        [InlineKeyboardButton("⬅️ Back to Free Materials", callback_data='free_materials')],
        [InlineKeyboardButton("🏠 Main Menu", callback_data='main_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(text, reply_markup=reply_markup, parse_mode='Markdown')

# Обработка файлов (скриншоты оплаты)
async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_fio = update.message.caption or "Full name not provided"
    
    # Получаем сохраненные данные
    course_type = context.user_data.get('course_type', 'unknown')
    course_name = context.user_data.get('course_name', 'unknown course')
    course_price = context.user_data.get('course_price', 'unknown')
    
    user_info = {
        'id': user.id,
        'name': user.full_name,
        'username': f"@{user.username}" if user.username else "not provided"
    }
    
    # Формируем сообщение для администратора
    admin_text = (
        f"📨 **NEW PAYMENT RECEIVED** 💰\n\n"
        f"👤 **Customer:** {user_info['name']}\n"
        f"📛 **Username:** {user_info['username']}\n"
        f"🆔 **ID:** {user_info['id']}\n"
        f"📝 **Full Name:** {user_fio}\n"
        f"🎓 **Course:** {course_name}\n"
        f"💵 **Amount:** {course_price}\n\n"
        f"✅ **Payment confirmation file attached below**"
    )
    
    try:
        # Отправляем уведомление всем администраторам
        for admin_username in ADMIN_USERNAMES:
            try:
                await context.bot.send_message(
                    chat_id=admin_username,
                    text=admin_text,
                    parse_mode='Markdown'
                )
                
                # Пересылаем файл администратору
                if update.message.document:
                    await context.bot.send_document(
                        chat_id=admin_username,
                        document=update.message.document.file_id,
                        caption=f"📄 Document from {user_info['name']}"
                    )
                elif update.message.photo:
                    await context.bot.send_photo(
                        chat_id=admin_username,
                        photo=update.message.photo[-1].file_id,
                        caption=f"📸 Screenshot from {user_info['name']}"
                    )
                    
            except Exception as e:
                logger.error(f"Error sending to admin {admin_username}: {e}")
        
        # Подтверждаем получение пользователю
        confirmation_text = (
            f"✅ **File received successfully!** 📨\n\n"
            f"📋 **Your details:**\n"
            f"• 👤 Full Name: {user_fio}\n"
            f"• 🎓 Course: {course_name}\n"
            f"• 💵 Amount: {course_price}\n"
            f"• 📛 Username: {user_info['username']}\n\n"
            f"⏳ **What's next?**\n"
            f"Admin will verify your payment and contact you within 24 hours to activate your access.\n\n"
            f"💬 **For questions:** {', '.join(ADMIN_USERNAMES)}\n"
            f"⏰ **Processing time:** up to 24 hours"
        )
        
        await update.message.reply_text(confirmation_text, parse_mode='Markdown')
        
    except Exception as e:
        logger.error(f"Error sending to admin: {e}")
        await update.message.reply_text(
            "❌ **Error occurred while sending.** Please try again later or contact " + ', '.join(ADMIN_USERNAMES),
            parse_mode='Markdown'
        )

# Обработчик текстовых сообщений
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📨 **To confirm your payment, please send a screenshot or PDF document.**\n"
        "⚠️ **Don't forget to include your full name in the file caption!**",
        parse_mode='Markdown'
    )

# Обработчик ошибок
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error("❌ Error processing request:", exc_info=context.error)

# Основная функция
def main():
    # Создаем приложение
    application = Application.builder().token("8478166259:AAH3YeNVDKFWCuEttHJTsjqdJU0jmqunUp0").build()
    
    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_handler(MessageHandler(filters.Document.ALL | filters.PHOTO, handle_file))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    application.add_error_handler(error_handler)
    
    # Запускаем бота
    application.run_polling()
    print("✅ Bot is running and ready! 🚀")

if __name__ == '__main__':
    main()