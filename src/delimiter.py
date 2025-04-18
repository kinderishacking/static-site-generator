from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []

    for old_node in old_nodes:

        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue

        inner_texts = old_node.text.split(delimiter)

        if len(inner_texts) % 2 == 0:
            raise ValueError("Unmatched delimiter found in text.")

        for i, inner_text in enumerate(inner_texts):

            if i % 2 != 0:
                new_nodes.append(TextNode(inner_text, text_type ))
            else:
                new_nodes.append(TextNode(inner_text, TextType.NORMAL))

    return new_nodes
    



        





        