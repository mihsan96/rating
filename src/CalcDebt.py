from DataReaderXML import DataReaderXML
from Types import DataType


class CalcDebt:
    def __init__(self, data: DataType):
        self.data = data
        self.debt_count = 0

    def calc(self):
        for student in self.data:
            scores = 0
            for subject in self.data[student]:
                if subject[1] < 61:
                    scores += 1
            if scores == 2:
                self.debt_count += 1
        return self.debt_count


if __name__ == "__main__":
    data = DataReaderXML().read('../data/data.xml')
    print(data)
    print(CalcDebt(data).calc())
