# Артефакт: "Копилка на мечту" (Трекер накоплений)
# Автор: Тюкалова Виктория

# Коллекция: история всех накоплений по датам/событиям
history = {}

# Функция 1: Считает остаток до мечты, возвращает результат
def calculate_remaining(target, saved):
    remaining = target - saved
    return max(0, remaining)

# Функция 2: Считает процент выполнения, возвращает строку
def calculate_progress(target, saved):
    if target <= 0:
        return "0%"
    percent = (saved / target) * 100
    if percent > 100:
        percent = 100
    return f"{percent:.1f}%"

# Функция 3: Добавляет событие в историю
def add_to_history(amount, comment="Пополнение"):
    record_id = len(history) + 1
    history[record_id] = {"sum": amount, "comment": comment}
    return record_id

# Функция 4: Вывод статистики
def show_status(target, saved):
    print("\n" + "=" * 40)
    print("          СТАТУС ТВОЕЙ МЕЧТЫ")
    print("=" * 40)
    remaining = calculate_remaining(target, saved)
    progress = calculate_progress(target, saved)
    
    print(f"Цель:            {target} руб.")
    print(f"Накоплено:       {saved} руб.")
    print(f"Осталось:        {remaining} руб.")
    print(f"Прогресс:        {progress}")
    print("-" * 40)
    
    # Полоска прогресса
    bar_length = 20
    filled = int((saved / target) * bar_length) if target > 0 else 0
    filled = min(filled, bar_length)
    bar = "█" * filled + "░" * (bar_length - filled)
    print(f"[{bar}] {progress}")
    print("=" * 40)
    
    # Показ истории
    if history:
        print("\nПоследние пополнения:")
        for rec_id, data in history.items():
            print(f"  #{rec_id}: +{data['sum']} руб. ({data['comment']})")
    print()

# Функция 5: План накоплений
def show_plan(remaining, days=30):
    if remaining <= 0:
        print("\n Ты уже накопил на мечту! Можно покупать!")
        return
    daily = remaining / days
    weekly = daily * 7
    monthly = daily * 30
    print(f"\nЧтобы дойти до цели за {days} дней, нужно откладывать:")
    print(f"  В день:    {daily:.2f} руб.")
    print(f"  В неделю:  {weekly:.2f} руб.")
    print(f"  В месяц:   {monthly:.2f} руб.\n")

# Основной цикл программы
def main():
    print("=" * 40)
    print("    КОПИЛКА НА МЕЧТУ")
    print("=" * 40)
    print("Привет! Я помогу тебе накопить на то,")
    print("о чём ты мечтаешь. Поехали!\n")
    
    # Ввод цели и начальной суммы
    try:
        target = float(input("Сколько стоит твоя мечта (в рублях)? "))
        if target <= 0:
            print("Стоимость должна быть больше нуля. Запусти программу заново.")
            return
    except ValueError:
        print("Ошибка: нужно ввести число. Запусти программу заново.")
        return
    
    try:
        saved = float(input("Сколько ты уже накопил (в рублях)? "))
        if saved < 0:
            saved = 0
    except ValueError:
        saved = 0
        print("Ввод не распознан, начнём с 0 руб.")
    
    # Меню
    while True:
        print("\nМЕНЮ:")
        print("  1. Пополнить копилку")
        print("  2. Посмотреть статус мечты")
        print("  3. План накоплений")
        print("  4. Выход")
        choice = input("Выбери действие (1-4): ").strip()
        
        if choice == "1":
            try:
                amount = float(input("Сколько добавляешь? "))
                if amount <= 0:
                    print("Сумма должна быть больше нуля!")
                    continue
                comment = input("Комментарий (Enter — пропустить): ").strip()
                if not comment:
                    comment = "Пополнение"
                
                saved += amount 
                add_to_history(amount, comment)
                print(f"Отлично! Теперь у тебя {saved} руб.")
            except ValueError:
                print("Ошибка: нужно ввести число!")
                
        elif choice == "2":
            show_status(target, saved)
            
        elif choice == "3":
            remaining = calculate_remaining(target, saved)
            show_plan(remaining)
            
        elif choice == "4":
            print("\nДо встречи! Иди к своей мечте! ✨")
            break
        else:
            print("Неверный ввод. Попробуй снова (1-4).")

# Автоматические проверки
if __name__ == "__main__":
    # Проверка 1: Обычный сценарий — считаем остаток
    assert calculate_remaining(1000, 400) == 600, "Ошибка: остаток посчитан неверно"
    # Проверка 2: Граничный сценарий — накоплено больше цели
    assert calculate_remaining(1000, 1500) == 0, "Ошибка: остаток не может быть отрицательным"
    # Проверка 3: Процент выполнения
    assert calculate_progress(1000, 500) == "50.0%", "Ошибка: процент посчитан неверно"
    # Проверка 4: Добавление в историю
    history.clear()
    add_to_history(100, "тест")
    assert len(history) == 1, "Ошибка: запись не добавилась в историю"
    assert history[1]["sum"] == 100, "Ошибка: сумма в истории неверная"
    
    print("Все проверки пройдены\n")
    main()