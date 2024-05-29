from bst import BST
import pytest

@pytest.fixture
def bst():
    bst = BST()
    input = [2,64,17,28,9,10,6]
    for i in input:
        bst.insert(i)
    return bst

def test_insert(bst: BST):
    assert bst.root.value == 2
    assert bst.root.right.value == 64
    assert bst.root.right.left.value == 17
    assert bst.root.right.left.right.value == 28
    assert bst.root.right.left.left.value == 9
    assert bst.root.right.left.left.right.value == 10
    assert bst.root.right.left.left.left.value == 6

def test_search(bst: BST):
    bst.search(64) == True
    bst.search(9) == True
    bst.search(45) == False

def test_in_order_traversal(bst: BST):
    bst.in_order_traversal() == [2,6,9,10,17,28,64]

def test_find_min(bst: BST):
    bst.find_min() == 2

def test_find_max(bst: BST):
    bst.find_max() == 64

def test_height(bst: BST):
    bst.height() == 5

def test_count_leaves(bst: BST):
    bst.count_leaves() == 2

def test_serialize(bst: BST):
    bst.serialize() == "2,6,9,10,17,28,64"

def test_deserialize(bst: BST):
    bst.deserialize("2,64,17,28,9,10,6") 


    