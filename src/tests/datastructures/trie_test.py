import unittest
from src.datastructures.trie import Trie

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
