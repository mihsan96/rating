# -*- coding: utf-8 -*-
from src.Types import DataType
from src.CalcRating import CalcRating
import pytest


class TestCalcRating:
    @pytest.fixture()
    def input_data(self) -> tuple[DataType, int]:
        data = {
            'Иванов Иван Иванович':
                [('математика', 67),
                 ('литература', 100.0),
                 ('программирование', 91.0)],
            'Петров Петр Петрович':
                [('математика', 78),
                 ('химия', 87.0),
                 ('социология', 61.0)],
            'Сидоров Сидор Сидорович':
                [('математика', 90),
                 ('физика', 11.0),
                 ('биология', 11.0)],
            'Козлова Анна Игоревна':
                [('математика', 11),
                 ('химия', 13.0),
                 ('физика', 18.0)],
            'Смирнов Алексей Александрович':
                [('математика', 82),
                 ('литература', 76.0),
                 ('история', 89.0)],
            'Васильева Екатерина Викторовна':
                [('математика', 70),
                 ('английский', 92.0),
                 ('география', 84.0)],
            'Михайлов Дмитрий Петрович':
                [('математика', 88),
                 ('биология', 79.0),
                 ('история', 67.0)],
            'Кузнецова Ольга Сергеевна':
                [('математика', 75),
                 ('социология', 72.0),
                 ('английский', 91.0)],
            'Лебедев Артем Алексеевич':
                [('математика', 94),
                 ('программирование', 96.0),
                 ('физика', 87.0)],
            'Андреева Мария Андреевна':
                [('математика', 80),
                 ('литература', 85.0),
                 ('география', 73.0)]}

        rating_scores = 1
        return data, rating_scores

    def test_init_calc_rating(self,
                              input_data: tuple[DataType, int]) \
            -> None:
        calc_rating = CalcRating(input_data[0])
        assert input_data[0] == calc_rating.data
