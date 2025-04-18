class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):

        props_str = ""

        for prop, value in self.props.items():
            props_str = props_str + " " + f'{prop}="{value}"'
        
        return props_str

    def __repr__(self):
        return (
            f"tag: {self.tag}\n"
            f"value: {self.value}\n"
            f"children: {self.children}]n"
            f"props: {self.props_to_html}"
        )
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value):
        super().__init__(tag, value)

    def to_html(self):

        if not self.value:
            raise ValueError("value is missing")
        
        if not self.tag:
            return self.value
        
        return f"<{self.tag}>{self.value}</{self.tag}>"
    


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag = tag, children = children, props = props)
    
    def to_html(self):
        
        if not self.tag:
            raise ValueError("tag is missing")
        
        if not self.children:
            raise ValueError("children is missing")
        

        html_string = ""
        
        
        for child in self.children:

            html_string += child.to_html()

        
        return f"<{self.tag}>{html_string}</{self.tag}>"
            



