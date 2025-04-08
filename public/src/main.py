from textnode import TextNode, TextType

def main():
    node1 = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    node2 = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    node3 = TextNode("This is some plain text", TextType.TEXT)
    
    print(node1)  # Should use __repr__ method
    print(node2)  # Should use __repr__ method
    
    print(node1 == node2)  # Should print True
    print(node1 == node3)  # Should print False

if __name__ == "__main__":
    main()
