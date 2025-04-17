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