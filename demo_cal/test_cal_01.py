import pytest


class TestCal:
    data_list_01=[('999+3',1002),('115.5+0.5',116),('0.9+167',167.9),('289.18+22',311.18)]
    @pytest.mark.parametrize('datas,expected',data_list_01)
    def test_cal_add(self,datas,expected):
        print(eval(datas))
        assert eval(datas) == expected, "计算结果错误"

    data_list_02= [('999/3',333),('387.3/3',129.1),('640/4.1',156.09756097560978),('182.11/0.94',193.73404255319153),('2728.63/5',545.726)]
    @pytest.mark.parametrize('datas,expected',data_list_02)
    def test_cal_div(self,datas,expected):
        print(eval(datas))
        assert eval(datas) == expected, "计算结果错误"
