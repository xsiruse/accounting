from application.salary import *
from application.db.people import *
from datetime import *


def main():
    print(datetime.now())
    calculate_salary()
    get_employees()


if __name__ == '__main__':
    main()
