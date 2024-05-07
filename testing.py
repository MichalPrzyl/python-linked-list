import pytest
from node import LinkedList


def test_create_linked_list():
    l_list = LinkedList()
    assert l_list.first_node == None
    assert l_list.last_node == None

class TestAddingNodes:

    @pytest.fixture
    def l_list(self):
        l_list = LinkedList()
        return l_list

    def test_l_list_with_one_element(self, l_list):
        l_list.add_node("hello")
        assert l_list.first_node.value == "hello"
        assert l_list.last_node.value == "hello"

    def test_l_list_with_two_elements_head_and_tail(self, l_list):
        l_list.add_node("hello")
        l_list.add_node("world")
        assert l_list.first_node.value == "hello"
        assert l_list.last_node.value == "world"

    def test_l_list_with_two_elements_pointer_to_next(self, l_list):
        l_list.add_node("hello")
        l_list.add_node("world")
        assert l_list.first_node.next_node == l_list.last_node

    def test_l_list_with_three_elements_head_and_tail(self, l_list):
        l_list.add_node("hello")
        l_list.add_node("world")
        l_list.add_node("whatsup")
        assert l_list.first_node.value == "hello"
        assert l_list.last_node.value == "whatsup"

    def test_l_list_with_three_elements_pointer_to_next(self, l_list):
        l_list.add_node("hello")
        l_list.add_node("world")
        l_list.add_node("whatsup")
        assert l_list.first_node.next_node.value == "world"
