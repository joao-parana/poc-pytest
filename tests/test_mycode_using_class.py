from mypkg.mycode import Stack
import pytest

@pytest.fixture
def stack():
    return Stack()

# Podemos organizar TestCases em classes ordinárias do Python
# Use: python3 -m pytest -m smoke  tests/test_mycode_using_class.py
# Veja exemplo abaixo:

class SampleTestCaseClass:
    @pytest.mark.smoke
    def test_constructor():
        s = Stack()
        assert len(s) == 0
    
    @pytest.mark.smoke
    def test_push(stack):
        stack.push(5)
        assert len(stack) == 1
        assert stack.pop() == 5

