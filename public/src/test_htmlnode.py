# src/test_htmlnode.py
import unittest
from htmlnode import LeafNode  # Only import LeafNode here

# src/test_htmlnode.py
import unittest
from htmlnode import LeafNode  # Ensure we're importing LeafNode only

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = LeafNode("a", "Click here", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')

    def test_props_to_html_no_props(self):
        node = LeafNode("p", "Just a paragraph")
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        # No need for an empty list as children
        node = LeafNode("div", "Some content", {"class": "container"})
        self.assertEqual(repr(node), "LeafNode(tag=div, value=Some content, props={'class': 'container'})")
