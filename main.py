import json
import os
from datetime import datetime

BOOKS_FILE = "books.json"

def load_books():
    if not os.path.exists(BOOKS_FILE):
        return []
    try:
        with open(BOOKS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_books(books):
    with open(BOOKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=2)

def add_book(books):
    print("\n--- Добавление книги ---")
    author = input("Введите автора: ").strip()
    if not author:
        print("Ошибка: автор не может быть пустым")
        return
    title = input("Введите название: ").strip()
    if not title:
        print("Ошибка: название не может быть пустым")
        return
    
    # Проверка на дубликаты (Closes #1)
    for book in books:
        if book["author"].lower() == author.lower() and book["title"].lower() == title.lower():
            print("Ошибка: такая книга уже существует!")
            return
    
    while True:
        try:
            rating = int(input("Введите оценку (1-5): "))
            if 1 <= rating <= 5:
                break
            print("Оценка должна быть от 1 до 5")
        except ValueError:
            print("Введите целое число")
    
    date = input("Введите дату прочтения (ГГГГ-ММ-ДД): ").strip()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    
    books.append({
        "author": author,
        "title": title,
        "rating": rating,
        "date": date
    })
    save_books(books)
    print(f"Книга '{title}' добавлена!")

def main():
    books = load_books()
    while True:
        print("\n" + "="*40)
        print("ТРЕКЕР ПРОЧИТАННЫХ КНИГ")
        print("="*40)
        print("1. Добавить книгу")
        print("2. Выход")
        print("-"*40)
        choice = input("Выберите действие: ").strip()
        
        if choice == "1":
            add_book(books)
            books = load_books()
        elif choice == "2":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
