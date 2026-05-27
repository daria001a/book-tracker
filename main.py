import json
import os

FILENAME = "books.json"

def load_books():
    """Загружает список книг из JSON-файла."""
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_books(books):
    """Сохраняет список книг в JSON-файл."""
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

def add_book():
    """Добавляет новую книгу с проверкой на дубликаты и валидацией оценки."""
    books = load_books()
    print("\n--- Добавление новой книги ---")
    author = input("Введите автора: ").strip()
    title = input("Введите название книги: ").strip()
    
    # Шаг 8: Проверка на дубликаты (Решение Issue #1)
    for book in books:
        if book["author"].lower() == author.lower() and book["title"].lower() == title.lower():
            print(f"Ошибка: Книга '{title}' автора {author} уже есть в трекере!")
            return

    # Валидация оценки
    while True:
        try:
            rating = int(input("Введите оценку (от 1 до 5): "))
            if 1 <= rating <= 5:
                break
            print("Оценка должна быть целым числом от 1 до 5.")
        except ValueError:
            print("Пожалуйста, введите корректное число.")

    date_read = input("Введите дату прочтения (например, ДД.ММ.ГГГГ): ").strip()

    new_book = {
        "author": author,
        "title": title,
        "rating": rating,
        "date": date_read
    }
    
    books.append(new_book)
    save_books(books)
    print(f"Успешно: Книга '{title}' добавлена!")

def show_all_books():
    """Выводит список всех сохраненных книг."""
    books = load_books()
    if not books:
        print("\nВаш трекер пока пуст. Самое время добавить первую книгу!")
        return
    
    print("\n--- Список прочитанных книг ---")
    for idx, book in enumerate(books, 1):
        print(f"{idx}. «{book['title']}» — {book['author']} | Оценка: {book['rating']}/5 | Дата: {book['date']}")

def show_average_rating():
    """Считает и выводит среднюю оценку по всем книгам."""
    books = load_books()
    if not books:
        print("\nНет данных для расчета средней оценки.")
        return
    
    total_rating = sum(book["rating"] for book in books)
    avg = total_rating / len(books)
    print(f"\nСредняя оценка ваших книг: {avg:.2f} из 5")

def show_author_stats():
    """Выводит количество прочитанных книг по каждому автору."""
    books = load_books()
    if not books:
        print("\nНет данных для составления статистики.")
        return
    
    stats = {}
    for book in books:
        author = book["author"]
        stats[author] = stats.get(author, 0) + 1
        
    print("\n--- Статистика по авторам ---")
    for author, count in stats.items():
        print(f"Автор: {author} — Прочитано книг: {count}")

def delete_book():
    """Удаляет книгу по её индексу в списке."""
    books = load_books()
    if not books:
        print("\nНечего удалять, список книг пуст.")
        return
        
    show_all_books()
    print("\n--- Удаление книги ---")
    while True:
            choice = int(input("Введите номер книги для удаления (или 0 для отмены): "))
            if choice == 0:
                return

            if 1 <= choice <= len(books):
                removed = books.pop(choice - 1)

                save_books(books)

                print(f"Успешно: Книга «{removed['title']}» удалена.")

                break

            print("Неверный номер. Выберите индекс из списка выше.")

        except ValueError:

            print("Пожалуйста, введите число.")

def main():
    while True:
        print("\n=== Меню трекера книг ===")
        print("1. Добавить книгу")
        print("2. Показать все книги")

        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")

        print("6. Выход")
        

        choice = input("Выберите действие (1-6): ").strip()
        
        if choice == "1":

            add_book()
        elif choice == "2":
            show_all_books()

        elif choice == "3":
            show_average_rating()
        elif choice == "4":

            show_author_stats()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            print("До встречи! Хорошего чтения.")
            break

        else:
            print("Неверный пункт меню. Попробуйте снова.")

if __name__ == "__main__":
    main()
