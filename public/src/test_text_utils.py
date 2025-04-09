import unittest
from textnode import TextNode, TextType
from text_utils import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_code_delimiter(self):
        old_node = TextNode("This is `code` text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([old_node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" text", TextType.TEXT),
            ]
        )

if __name__ == "__main__":
    unittest.main()
