# src/test_leafnode.py
import unittest
from htmlnode import LeafNode  # Only import LeafNode here

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_props(self):
        node = LeafNode("span", "No attributes")
        self.assertEqual(node.to_html(), "<span>No attributes</span>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just text with no tag")
        self.assertEqual(node.to_html(), "Just text with no tag")

    def test_leaf_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", value=None)
