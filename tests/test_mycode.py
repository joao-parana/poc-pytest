import pytest
from mypkg.mycode import Stack


@pytest.fixture
def stack():
    return Stack()

@pytest.mark.skip(reason= "To simple to be tested")
def test_constructor():
    s = Stack()
    # assert isinstance(s, Stack)
    assert len(s) == 0

@pytest.mark.smoke
def test_push(stack):
    stack.push(3)
    assert len(stack) == 1

@pytest.mark.smoke
def test_pop(stack):
    stack.push("Hello")
    stack.push("World")
    assert len(stack) == 2
    assert stack.pop() == "World"
    assert stack.pop() == "Hello"
    assert stack.pop() is None

@pytest.mark.smoke
@pytest.mark.xfail
def test_pop_fail(stack):
    stack.push(100)
    assert len(stack) == 1
    assert stack.pop() == 100
    assert stack.pop() is int
