from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        # Ensure that value is provided, and no children allowed
        if not value:
            raise ValueError("LeafNode must have a value")
        
        # Call the parent class (HTMLNode) constructor
        super().__init__(tag=tag, value=value, children=None, props=props)

def to_html(self):
    # If no tag is provided, return raw text
    if not self.tag:
        return self.value
    
    # If tag is provided, render HTML with the props
    props_html = self.props_to_html()
    
    # If there are no props, do not include a space after the tag
    if not props_html:
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
    # Otherwise, include the props with the tag
    return f"<{self.tag} {props_html}>{self.value}</{self.tag}>"
