class DataHolder:
    def __init__(self, keys):
        self.__data = {}

        for key in keys:
            self.__data[key] = []

    def print(self):
        print(self.__data)

    def print_pretty(self):
        for key in self.__data:
            print(f"\nKEY: {key}, DATA:\n")
            print("-----------------------")
            print(self.__data[key])
            print("-----------------------")

    def extract_row(self, row):
        i = 0
        for key in self.__data:
            try:
                info = float(row[i])
            except:
                info = row[i]

            self.__data[key].append(info)
            i += 1

    def get_by_key(self, key):
        return self.__data[key]

    def get_keys(self):
        return self.__data.keys()

    def del_by_key(self, key):
        del self.__data[key]

    def get_without(self, keys):
        data = self.__data
        for key in keys:
            del data[key]

        return data
