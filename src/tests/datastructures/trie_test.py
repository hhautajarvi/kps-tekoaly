import unittest
from datastructures.trie import Trie, Node

class TrieTest(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_add_node(self):
        self.trie.add_node("1")
        isnode, _ = self.trie.find_node("1")
        self.assertTrue(isnode)
        self.assertEqual(self.trie.get_value("1"), 1)

    def test_add_node_long_path(self):
        self.trie.add_node("10121001")
        isnode, _ = self.trie.find_node("101")
        self.assertTrue(isnode)
        self.assertIsNone(self.trie.get_value("101"))
        isnode2, _ = self.trie.find_node("10121001")
        self.assertTrue(isnode2)
        self.assertEqual(self.trie.get_value("10121001"), 1)

    def test_find_node_no_node(self):
        isnode, node = self.trie.find_node("1")
        self.assertFalse(isnode)
        self.assertIsNone(node)

    def test_find_node_invalid_path(self):
        self.trie.add_node("11")
        self.trie.add_node("22")
        isnode, node = self.trie.find_node("0")
        self.assertFalse(isnode)
        self.assertIsNone(node)

    def test_has_key(self):
        self.trie.add_node("11")
        self.assertTrue(self.trie.has_key("11"))

    def test_has_key_no_node(self):
        self.assertFalse(self.trie.has_key("111"))

    def test_has_key_no_value_root(self):
        self.assertFalse(self.trie.has_key(""))

    def test_has_key_no_value_path(self):
        self.trie.add_node("10121001")
        self.assertFalse(self.trie.has_key("101"))

    def test_has_subtrie(self):
        self.trie.add_node("10121001")
        self.assertTrue(self.trie.has_subtrie("1"))
        self.assertTrue(self.trie.has_subtrie("101"))
        self.assertTrue(self.trie.has_subtrie("1012100"))

    def test_has_subtrie_negative(self):
        self.assertFalse(self.trie.has_subtrie("1"))
        self.trie.add_node("10121001")
        self.assertFalse(self.trie.has_subtrie("102"))
        self.assertFalse(self.trie.has_subtrie("10121001"))

    def test_get_value(self):
        self.trie.add_node("101")
        self.assertEqual(self.trie.get_value("101"), 1)

    def test_get_value_no_value(self):
        self.trie.add_node("101")
        self.assertFalse(self.trie.get_value("11"))

    def test_update_value(self):
        self.trie.add_node("101")
        self.trie.update_value("101")
        self.assertEqual(self.trie.get_value("101"), 2)
        self.trie.update_value("101")
        self.trie.update_value("101")
        self.assertEqual(self.trie.get_value("101"), 4)

    def test_update_value_update_wrong(self):
        self.trie.add_node("101")
        self.trie.update_value("11")
        self.assertEqual(self.trie.get_value("101"), 1)
        self.trie.update_value("101")
        self.assertEqual(self.trie.get_value("101"), 2)
        self.trie.update_value("101000")
        self.assertEqual(self.trie.get_value("101"), 2)

class NodeTest(unittest.TestCase):
    def setUp(self):
        self.node = Node()
        self.node2 = Node("a")

    def test_constructor(self):
        self.assertEqual(len(self.node._children), 0)
        self.assertIsNone(self.node._char)
        self.assertIsNone(self.node._value)

    def test_constructor_with_char(self):
        self.assertEqual(len(self.node2._children), 0)
        self.assertEqual(self.node2._char, "a")
        self.assertIsNone(self.node2._value)

    def test_return_char_no_char(self):
        self.assertIsNone(self.node.return_char())

    def test_return_char(self):
        self.assertEqual(self.node2.return_char(), "a")

    def test_return_children(self):
        self.node.add_child(self.node2)
        child_list = self.node.return_children()
        self.assertEqual(len(child_list), 1)
        self.assertEqual(child_list[0].return_char(), "a")

    def test_return_children_no_children(self):
        self.assertEqual(len(self.node.return_children()), 0)

    def test_return_value(self):
        self.node.add_value()
        self.assertEqual(self.node.return_value(), 1)

    def test_return_value_no_value(self):
        self.assertIsNone(self.node.return_value())

    def test_add_child(self):
        self.assertEqual(len(self.node.return_children()), 0)
        self.node.add_child(self.node2)
        self.assertEqual(len(self.node.return_children()), 1)

    def test_add_value(self):
        self.assertIsNone(self.node.return_value())
        self.node.add_value()
        self.assertEqual(self.node.return_value(), 1)

    def test_increase_value(self):
        self.node2.add_value()
        self.assertEqual(self.node2.return_value(), 1)
        self.node2.increase_value()
        self.assertEqual(self.node2.return_value(), 2)

    def test_increase_value_several_increases(self):
        self.node2.add_value()
        self.node2.increase_value()
        self.node2.increase_value()
        self.node2.increase_value()
        self.node2.increase_value()
        self.node2.increase_value()
        self.assertEqual(self.node2.return_value(), 6)
