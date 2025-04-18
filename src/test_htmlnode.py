import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, text_node_to_html_node, TextType


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode()

        self.assertEqual(node1.tag, None )




    def test_diff_tag(self):

        node1 = HTMLNode(
            tag="p",
            value="This is a paragraph."
        )



        self.assertEqual(node1.tag, "p")

    def test_diff_val(self):

        node1 = HTMLNode(
            tag="p",
            value="This is a paragraph."
        )

        node2 = HTMLNode(
            tag="p",
            value="This is a div"
        )

        self.assertNotEqual(node1.value, node2.value)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_div(self):
        node = LeafNode(tag =None,value =  "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_textnode_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    



    
  


if __name__ == "__main__":
    unittest.main()