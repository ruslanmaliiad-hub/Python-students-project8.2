# Автор: Маліяд Р.О.
# Завдання: створити текстовий файл і записати прізвище та питання

def main():
    try:
        with open("students_questions.txt", "w", encoding="utf-8") as file:
            file.write("Студент 1: Маліяд.Р.О.\n")
            file.write("Питання: Що таке змінна у Python і як її оголосити?\n")
        print("Файл створено і заповнено успішно.")
    except Exception as e:
        print(f"Помилка під час роботи з файлом: {e}")

if __name__ == "__main__":
    main()
