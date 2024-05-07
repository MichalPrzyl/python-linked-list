import pytest
from node import LinkedList, Node


def test_create_linked_list():
    l_list = LinkedList()
    assert l_list.first_node == None
    assert l_list.last_node == None

class TestAddingNodes:

    @pytest.fixture
    def setup(self):
        self.l_list = LinkedList()

    def test_l_list_with_one_element(self, setup):
        self.l_list.add_node("hello")
        assert self.l_list.first_node.value == "hello"
        assert self.l_list.last_node.value == "hello"

    def test_l_list_with_two_elements_head_and_tail(self, setup):
        self.l_list.add_node("hello")
        self.l_list.add_node("world")
        assert self.l_list.first_node.value == "hello"
        assert self.l_list.last_node.value == "world"

    def test_l_list_with_two_elements_pointer_to_next(self, setup):
        self.l_list.add_node("hello")
        self.l_list.add_node("world")
        assert self.l_list.first_node.next_node == self.l_list.last_node

    def test_l_list_with_three_elements_head_and_tail(self, setup):
        self.l_list.add_node("hello")
        self.l_list.add_node("world")
        self.l_list.add_node("whatsup")
        assert self.l_list.first_node.value == "hello"
        assert self.l_list.last_node.value == "whatsup"

    def test_l_list_with_three_elements_pointer_to_next(self, setup):
        self.l_list.add_node("hello")
        self.l_list.add_node("world")
        self.l_list.add_node("whatsup")
        assert self.l_list.first_node.next_node.value == "world"