class Node():
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BST():
    
    def __init__(self):
        self.root = None
        
    def insert(self, value: int) -> None:
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right


    def search(self, value: int) -> bool:
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def in_order_traversal(self) -> list[int]:
        def in_ordering(node: Node, ordered_list: list[int]):
            if node is not None:
                in_ordering(node.left, ordered_list)
                ordered_list.append(node.value)
                in_ordering(node.right, ordered_list)

        ordered_list = []
        in_ordering(self.root, ordered_list)
        return ordered_list
            
            
    def find_min(self) -> int:
        current = self.root
        while current.left is not None:
            current = current.left
        return current.value

    def find_max(self) -> int:
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value


    def height(self) -> int:
        current = self.root
        left_count = 0
        right_count = 0
        while current.left is not None:
            left_count += 1
            current = current.left
        current = self.root
        while current.right is not None:
            right_count += 1
            current = current.right
    
        if left_count == right_count:
            return left_count
        elif left_count < right_count:
            return right_count
        elif left_count > right_count:
            return left_count

    def count_leaves(self) -> int:
        def leaf_counter(node: Node) -> int:
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return 1
            left_leaves = leaf_counter(node.left)
            right_leaves = leaf_counter(node.right)
            return left_leaves + right_leaves
        
        return leaf_counter(self.root)



    def serialize(self) -> str:    
        if self.root is None:
            return ""

        stack = []
        current: Node = self.root
        serialized_str = ""

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                serialized_str += str(current.value) + ","
                current = current.right
            else:
                break

        return serialized_str 

    def deserialize(self, tree: str) -> None:
        
        def split_string_by_commas(input_string):
            substrings = [substring.strip() for substring in input_string.split(',')]
            return substrings
        
        substrings = split_string_by_commas(tree)
        
        for i in substrings:
            self.insert(int(i))


def main():
    bst = BST()
    bst.insert(5)
    bst.insert(1)
    bst.insert(6)
    bst.insert(3)
    bst.insert(10)
    bst.insert(-1)
    bst.insert(4)
    
    
    print(bst.search(1))
    print(bst.search(10))
    print(bst.search(11))
    
    print(bst.height())
    
    print(bst.count_leaves())
    
    print(bst.serialize())
    
    minimum = bst.find_min()
    print(minimum)
    
    ordered_list = bst.in_order_traversal()
    
    print(ordered_list)
    
    bst = BST()
    
    bst.deserialize("5,2,8,3,9,87,65")
    ordered_list = bst.in_order_traversal()
    print(ordered_list)
    
    
    
main()


