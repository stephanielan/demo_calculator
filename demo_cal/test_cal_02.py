import pytest
import yaml


class TestCal:
    @pytest.mark.parametrize('datas',yaml.safe_load(open("./data01.yml")))
    def test_cal_add(self,datas):
            cal = datas[0]['data']
            res = datas[1]['data']
            print(f"式子{datas[0]['data']}相加为:{datas[1]['data']}")
            assert eval(cal) == res,"计算结果错误"

    @pytest.mark.parametrize('datas', yaml.safe_load(open("./data02.yml")))
    def test_cal_div(self,datas):
        for i in range(3):
            cal = datas[i]['data']
            res = datas[i+3]['data']
            print(f"式子{datas[i]['data']}相除为:{datas[i+3]['data']}")
            assert eval(cal) == res,"计算结果错误"

