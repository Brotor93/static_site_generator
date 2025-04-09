import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        image_matches = extract_markdown_images(old_node.text)
        if image_matches:
            sections = [old_node.text]
            # Split the text at each image match and create new sections
            for alt_text, url in image_matches:
                new_sections = []
                for section in sections:
                    parts = section.split(f"![{alt_text}]({url})", 1)
                    new_sections.extend(parts)
                sections = new_sections  # Update sections after splitting
            
            # Process sections and only add non-empty ones
            for section in sections:
                if section.strip():  # Skip empty sections
                    new_nodes.append(TextNode(section, TextType.TEXT))
            # Now add the image nodes
            for alt_text, url in image_matches:
                new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
        else:
            new_nodes.append(old_node)
    
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        link_matches = extract_markdown_links(old_node.text)
        if link_matches:
            sections = [old_node.text]
            # Split the text at each link match and create new sections
            for anchor_text, url in link_matches:
                new_sections = []
                for section in sections:
                    parts = section.split(f"[{anchor_text}]({url})", 1)
                    new_sections.extend(parts)
                sections = new_sections  # Update sections after splitting
            
            # Process sections and only add non-empty ones
            for section in sections:
                if section.strip():  # Skip empty sections
                    new_nodes.append(TextNode(section, TextType.TEXT))
            # Now add the link nodes
            for anchor_text, url in link_matches:
                new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
        else:
            new_nodes.append(old_node)
    
    return new_nodes
