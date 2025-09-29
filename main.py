import datetime
from application.salary import calculate_salary
from application.db.people import get_employees
import requests


def main():

    current_date = datetime.date.today()
    print(f"Текущая дата: {current_date}")


    calculate_salary()
    get_employees()


    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    if response.status_code == 200:
        data = response.json()
        print(f"Курс USD к EUR: {data['rates']['EUR']}")
    else:
        print("Не удалось получить данные о курсах.")


if __name__ == '__main__':
    main()