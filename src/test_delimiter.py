from delimiter import split_nodes_delimiter
from textnode import TextNode, TextType
import unittest


class TestHTMLNode(unittest.TestCase):

    def test_single_code(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes,[
        TextNode("This is text with a ", TextType.NORMAL),
        TextNode("code block", TextType.CODE),
        TextNode(" word", TextType.NORMAL),
        ] )

