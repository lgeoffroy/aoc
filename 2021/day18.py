import json
import math


def solve(lines):
    return lvl1(lines), lvl2(lines)


def lvl1(lines):
    node = array_to_node(json.loads(lines[0]))
    for line in lines[1:]:
        node = add(node, array_to_node(json.loads(line)))
    return node.magnitude()


def lvl2(lines):
    maximum = 0
    for line in lines:
        for line2 in [x for x in lines if x != line]:
            node = add(
                array_to_node(json.loads(line)),
                array_to_node(json.loads(line2))
            )
            m = node.magnitude()
            if m > maximum:
                maximum = m
    return maximum


class Node:
    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

    def depth(self):
        if self.root is None:
            return 0
        return self.root.depth() + 1

    def traverse_nodes(self):
        if type(self.left) == Node:
            yield from self.left.traverse_nodes()
        yield self
        if type(self.right) == Node:
            yield from self.right.traverse_nodes()

    def traverse_leafs(self):
        for n in self.traverse_nodes():
            if type(self.left) == int:
                yield self.left
            if type(self.right) == int:
                yield self.right

    def contains(self, n):
        for x in self.traverse_nodes():
            if x == n:
                return True
        return False

    def get_left_node(self, n):
        left_node = None
        dir = None
        for x in self.traverse_nodes():
            if type(x.right) == Node and x.right.contains(n):
                if type(x.left) == Node:
                    left_node = next(reversed(list(x.left.traverse_nodes())))
                    dir = "right"
                else:
                    left_node = x
                    dir = "left"
        return left_node, dir

    def get_right_node(self, n):
        right_node = None
        dir = None
        for x in reversed(list(self.traverse_nodes())):
            if type(x.left) == Node and x.left.contains(n):
                if type(x.right) == Node:
                    right_node = next(x.right.traverse_nodes())
                    dir = "left"
                else:
                    right_node = x
                    dir = "right"
        return right_node, dir

    def add_on_edge(self, value, dir):
        if dir == "right":
            if type(self.right) == int:
                self.right += value
            else:
                self.right.add_on_edge(value, dir)
        else:
            if type(self.left) == int:
                self.left += value
            else:
                self.left.add_on_edge(value, dir)

    def add_left(self, n):
        left_node, dir = self.get_left_node(n)
        if left_node is not None:
            left_node.add_on_edge(n.left, dir)


    def add_right(self, n):
        right_node, dir = self.get_right_node(n)
        if right_node is not None:
            right_node.add_on_edge(n.right, dir)

    def explode(self):
        for n in self.traverse_nodes():
            if n.depth() >= 4 and type(n.left) == int and type(n.right) == int:
                self.add_left(n)
                self.add_right(n)
                if n == n.root.left:
                    n.root.left = 0
                elif n == n.root.right:
                    n.root.right = 0
                return True
        return False

    def split(self):
        for n in self.traverse_nodes():
            if type(n.left) == int and n.left >= 10:
                n.left = Node(n, math.floor(n.left/2), math.ceil(n.left/2))
                return True
            if type(n.right) == int and n.right >= 10:
                n.right = Node(n, math.floor(n.right/2), math.ceil(n.right/2))
                return True
        return False

    def reduce(self):
        while self.explode() or self.split():
            pass

    def magnitude(self):
        if type(self.left) == int:
            left = 3 * self.left
        else:
            left = 3 * self.left.magnitude()
        if type(self.right) == int:
            right = 2 * self.right
        else:
            right = 2 * self.right.magnitude()
        return left + right

    def to_string(self):
        left_string = self.left.to_string() if type(self.left) == Node else str(self.left)
        right_string = self.right.to_string() if type(self.right) == Node else str(self.right)
        return f"[{left_string},{right_string}]"

    def __repr__(self):
        return self.to_string()


def array_to_node(input, root=None):
    left, right = input[0], input[1]
    node = Node(root)
    left_node = left if type(left) == int else array_to_node(left, node)
    right_node = right if type(right) == int else array_to_node(right, node)
    node.left = left_node
    node.right = right_node
    return node


def add(left, right):
    parent = Node(None, left, right)
    left.root = parent
    right.root = parent
    parent.reduce()
    return parent


def test_explode():
    for line, result in [
        ("[[[[[9,8],1],2],3],4]", "[[[[0,9],2],3],4]"),
        ("[7,[6,[5,[4,[3,2]]]]]", "[7,[6,[5,[7,0]]]]"),
        ("[[6,[5,[4,[3,2]]]],1]", "[[6,[5,[7,0]]],3]"),
        ("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"),
        ("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"),
        ("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]", "[[[[0,7],4],[7,[[8,4],9]]],[1,1]]"),
        ("[[[[0,7],4],[7,[[8,4],9]]],[1,1]]", "[[[[0,7],4],[15,[0,13]]],[1,1]]"),
        ("[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]", "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")
    ]:
        node = array_to_node(json.loads(line))
        node.explode()
        assert node.to_string() == result


def test_split():
    for line, result in [
        ("[[[[0,7],4],[15,[0,13]]],[1,1]]", "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]"),
        ("[[[[0,7],4],[[7,8],[0,13]]],[1,1]]", "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]"),
    ]:
        node = array_to_node(json.loads(line))
        node.split()
        assert node.to_string() == result


def test_reduce():
    line = "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"
    result = "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"
    node = array_to_node(json.loads(line))
    node.reduce()
    assert node.to_string() == result


def test_magnitude():
    for line, result in [
        ("[[1,2],[[3,4],5]]", 143),
        ("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", 1384),
        ("[[[[1,1],[2,2]],[3,3]],[4,4]]", 445),
        ("[[[[3,0],[5,3]],[4,4]],[5,5]]", 791),
        ("[[[[5,0],[7,4]],[5,5]],[6,6]]", 1137),
        ("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", 3488),
    ]:
        node = array_to_node(json.loads(line))
        assert node.magnitude() == result


def test_lvl1():
    for lines, result in [
        (["[[[[4,3],4],4],[7,[[8,4],9]]]", "[1,1]"], "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"),
        ([
            "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]",
            "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]",
            "[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]",
            "[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]",
            "[7,[5,[[3,8],[1,4]]]]",
            "[[2,[2,2]],[8,[8,1]]]",
            "[2,9]",
            "[1,[[[9,3],9],[[9,0],[0,7]]]]",
            "[[[5,[7,4]],7],1]",
            "[[[[4,2],2],6],[8,7]]",
        ], "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]")
    ]:
        node = array_to_node(json.loads(lines[0]))
        for line in lines[1:]:
            node = add(node, array_to_node(json.loads(line)))
        assert node.to_string() == result


def test_lvl2():
    for lines, result in [
        ([
            "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
            "[[[5,[2,8]],4],[5,[[9,9],0]]]",
            "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
            "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
            "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
            "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
            "[[[[5,4],[7,7]],8],[[8,3],8]]",
            "[[9,3],[[9,9],[6,[4,9]]]]",
            "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
            "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]",
        ], 3993),
    ]:
        assert lvl2(lines) == result


test_explode()
test_split()
test_reduce()
test_magnitude()
test_lvl1()
test_lvl2()
