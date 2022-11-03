import pytest


@pytest.fixture(scope="module", autouse=True)
def test_hits_01():
    yield
    print("测试结束")

@pytest.fixture(scope="function", autouse=True)
def test_hits_02():
    print("开始计算")
    yield
    print("结束计算")


