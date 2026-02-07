class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade

    def setgrade(self, grade):
        self.__grade = grade

    def getgrade(self):
        return self.__grade

    def displayinfo(self):
        print(f"Name: {self.name}")
        print(f"Grade: {self.__grade}")
def main():
    s1 = Student("Ahmed", "A")

    s1.displayinfo()

    s1.setgrade("A+")

    s1.displayinfo()


if __name__ == "__main__":
    main()
