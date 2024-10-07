#--*-- encoding: cp1251 --*--
class Client:
    def __init__(self, client_id, last_name, first_name, middle_name, passport_number, passport_series):
        self.__client_id = client_id
        self.__last_name = last_name
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__passport_number = passport_number
        self.__passport_series = passport_series

    def get_client_id(self):
        return self.__client_id

    def get_last_name(self):
        return self.__last_name

    def get_first_name(self):
        return self.__first_name

    def get_middle_name(self):
        return self.__middle_name

    def get_passport_number(self):
        return self.__passport_number

    def get_passport_series(self):
        return self.__passport_series


    def set_client_id(self, client_id):
        self.__client_id = client_id

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_middle_name(self, middle_name):
        self.__middle_name = middle_name

    def set_passport_number(self, passport_number):
        self.__passport_number = passport_number

    def set_passport_series(self, passport_series):
        self.__passport_series = passport_series


    def display_client_info(self):
        print(f"Client ID: {self.__client_id}")
        print(f"Last Name: {self.__last_name}")
        print(f"First Name: {self.__first_name}")
        print(f"Middle Name: {self.__middle_name}")
        print(f"Passport Number: {self.__passport_number}")
        print(f"Passport Series: {self.__passport_series}")


if __name__ == "__main__":
    client = Client(1, "Ivanov", "Ivan", "Ivanovich", "4444", "666666")

    client.display_client_info()  

    client.set_first_name("Sergey")
    client.set_last_name("Sergeev")

    client.display_client_info()

