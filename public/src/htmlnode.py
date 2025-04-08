# src/htmlnode.py
from abc import ABC, abstractmethod

class HTMLNode(ABC):
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}

    @abstractmethod
    def to_html(self):
        pass

    def props_to_html(self):
        return " ".join([f'{key}="{value}"' for key, value in self.props.items()])

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


# src/htmlnode.py
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError("Value must be provided for LeafNode")
        super().__init__(tag, value, None, props)  # No children, so passing None for children

    def to_html(self):
        if self.tag:
            # If there is a tag, render it as HTML
            return f"<{self.tag}{' ' + self.props_to_html() if self.props else ''}>{self.value}</{self.tag}>"
        else:
            # If no tag, return as raw text
            return self.value

    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"

# htmlnode.py

from htmlnode import HTMLNode, LeafNode  # Ensure this import is at the top

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not tag:
            raise ValueError("Tag must be provided for ParentNode")
        if not children:
            raise ValueError("Children must be provided for ParentNode")
        
        self.tag = tag
        self.children = children
        self.props = props if props else {}

    def to_html(self):
        # Raise an error if the tag is not provided
        if not self.tag:
            raise ValueError("Tag is required for ParentNode")

        # Raise an error if there are no children
        if not self.children:
            raise ValueError("ParentNode must have children")

        # Generate the opening tag with props
        opening_tag = f"<{self.tag}{self.props_to_html()}>"

        # Recursively generate HTML for each child
        children_html = "".join(child.to_html() for child in self.children)

        # Closing tag
        closing_tag = f"</{self.tag}>"

        return f"{opening_tag}{children_html}{closing_tag}"

    def __repr__(self):
        return f"ParentNode(tag={self.tag}, children={self.children}, props={self.props})"
