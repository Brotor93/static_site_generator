import unittest
from textnode import TextNode, TextType, text_node_to_html_node  # Import the function for testing

class TestTextNode(unittest.TestCase):
    
    # Existing tests...
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_neq_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.example.com")
        node2 = TextNode("This is a link", TextType.LINK, "https://www.example.com")
        self.assertEqual(node, node2)

    def test_neq_url(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.example.com")
        node2 = TextNode("This is a link", TextType.LINK, "https://www.different.com")
        self.assertNotEqual(node, node2)

    def test_url_is_none(self):
        node = TextNode("This is a plain text", TextType.TEXT)
        self.assertEqual(node.url, None)

    # New tests for the text_node_to_html_node function
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")

    def test_italic(self):
        node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")

    def test_code(self):
        node = TextNode("Code text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Code text")

    def test_link(self):
        node = TextNode("Click here", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click here")
        self.assertEqual(html_node.props["href"], "https://example.com")

    def test_image(self):
        node = TextNode("Image description", TextType.IMAGE, "https://example.com/image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props["src"], "https://example.com/image.jpg")
        self.assertEqual(html_node.props["alt"], "Image description")

    def test_invalid_text_type(self):
        node = TextNode("Invalid type", "INVALID_TYPE")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()
