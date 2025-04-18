from enum import Enum
from htmlnode import LeafNode, HTMLNode
import re

class TextType(Enum):
   NORMAL = "normal"
   BOLD = "bold"
   ITALIC = "italic"
   CODE = "code"
   LINK = "link"
   IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        else:
            return False
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node):

    match text_node.text_type:
        case TextType.NORMAL:
            return LeafNode(None, text_node.text)
        
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        
        case TextType.LINK:
            return HTMLNode("a", text_node.text, props = {"href": text_node.url} )
        
        case TextType.IMAGE:
            return HTMLNode("img", "", props = {"src": text_node.url, "alt": text_node.text })
        


def extract_markdown_images(text):

    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    return matches

def extract_markdown_links(text):

    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)")

    return matches