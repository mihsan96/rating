# -*- coding: utf-8 -*-
import os
from src.Types import DataType
from src.CalcQuartile import CalcQuartile
import pytest


class TestCalcRating:
    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, dict[str, int | float]]:
        root_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = f'{root_dir}/data_test.json'

        q_3 = {'Лебедев Артем Алексеевич': 92.33333333333333,
               'Козлова Анна Игоревна': 92.0,
               'Морозов Павел Сергеевич': 89.33333333333333,
               'Петрова Ирина Сергеевна': 87.33333333333333}
        return file_path, q_3

    def test_init_calc_quartile(self,
                                file_and_data_content:
                                tuple[DataType, int | float]) \
            -> None:
        calc_rating = CalcQuartile(file_and_data_content[0])
        assert file_and_data_content[0] == calc_rating.data
