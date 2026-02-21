import pytest
from src.stack import MyStack


class TestMyStack:

    def test_push_and_pop(self):
        stc = MyStack()
        stc.push(1)
        stc.push(2)
        stc.push(3)
        assert stc.pop() == 3
        assert stc.pop() == 2
        assert stc.pop() == 1
        with pytest.raises(ValueError):
            stc.pop()

    def test_peek(self):
        stack = MyStack()
        stack.push(10)
        assert stack.get_stack_peek() == 10
        stack.push(20)
        assert stack.get_stack_peek() == 20
        stack.pop()
        assert stack.get_stack_peek() == 10
        stack.pop()
        with pytest.raises(ValueError):
            stack.get_stack_peek()

    def test_size_and_empty(self):
        stack = MyStack()
        assert stack.is_stack_empty() is True
        assert stack.get_stack_size() == 0
        stack.push('a')
        assert stack.is_stack_empty() is False
        assert stack.get_stack_size() == 1
        stack.push('b')
        assert stack.get_stack_size() == 2
        stack.pop()
        assert stack.get_stack_size() == 1
        stack.pop()
        assert stack.is_stack_empty() is True   

    def test_get_stacl_elements(self):
        s  = MyStack()
        s.push(1)
        s.push(2)
        s.push(1000)
        s.push(-90)

        assert s.get_stack_peek() == -90
        assert s.get_stack_size() == 4
        assert s.get_stack_elements() == [1,2,1000,-90]
        s.pop()
        assert s.get_stack_peek() == 1000
        assert s.get_stack_size() == 3
        assert s.get_stack_elements() == [1,2,1000]


