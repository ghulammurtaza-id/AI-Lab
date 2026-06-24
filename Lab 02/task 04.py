class Employee:
    def __init__(self, id, name):
        self.name = name
        self.id = id

    def work(self):
        print("Employee is doing his work")


class Manager(Employee):
    def __init__(self, id, name):
        super().__init__(id, name)

    def work(self):
        print(f"{self.name} is doing Management work")


class Developer(Employee):
    def __init__(self, id, name):
        super().__init__(id, name)

    def work(self):
        print(f"{self.name} is doing Development tech work")


class Designer(Employee):
    def __init__(self, id, name):
        super().__init__(id, name)

    def work(self):
        print(f"{self.name} is doing Designing stuff")


def main():
    e1 = Employee(1, "Rehman")
    m1 = Manager(2, "Murtaza")
    d1 = Developer(3, "Ahmed")
    ds1 = Designer(4, "Rahib")


    e1.work()
    m1.work()
    d1.work()
    ds1.work()


if __name__ == "__main__":
    main()
