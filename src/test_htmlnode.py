import unittest

from htmlnode import HTMLNode


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

    
  


if __name__ == "__main__":
    unittest.main()