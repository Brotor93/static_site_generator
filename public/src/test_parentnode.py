# test_parentnode.py

import unittest
from htmlnode import LeafNode, ParentNode  # Ensure the import is correct

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_to_html_with_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, ["child"])

    def test_to_html_with_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", [])

if __name__ == "__main__":
    unittest.main()
