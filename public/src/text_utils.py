from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        # Leave non-text nodes as-is
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        if len(parts) % 2 == 0:
            raise ValueError(f"Invalid Markdown syntax: unmatched '{delimiter}' in '{node.text}'")

        for i, part in enumerate(parts):
            if i % 2 == 0:
                # Even index = plain text
                if part:
                    new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                # Odd index = inside delimiters
                new_nodes.append(TextNode(part, text_type))

    return new_nodes
