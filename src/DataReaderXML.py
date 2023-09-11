from abc import ABC
from DataReader import DataReader
from Types import DataType
import pandas as pd
import numpy as np


class DataReaderXML(DataReader, ABC):
    def __init__(self, ) -> None:
        self.students = {}

    @staticmethod
    def _normalize_student(name: str, scores: dict[str, int | float]) -> DataType:
        normalized_student = {}
        normalized_scores = []
        for subject in scores:
            score = scores[subject]
            if not np.isnan(score):
                normalized_scores.append((subject, score))
        normalized_student[name] = normalized_scores
        return normalized_student

    def _get_all_students(self, df: pd.DataFrame) -> DataType:
        data = df.to_dict(orient='index')
        for student in data:
            normalized_student = self._normalize_student(student,
                                                         data[student])
            self.students |= normalized_student
        return self.students

    def read(self, path: str) -> DataType:
        df = pd.read_xml(path)
        df.set_index('ФИО', inplace=True)
        return self._get_all_students(df)


if __name__ == "__main__":
    path_xml = '../data/data.xml'
    reader = DataReaderXML().read(path_xml)
    print(reader)
