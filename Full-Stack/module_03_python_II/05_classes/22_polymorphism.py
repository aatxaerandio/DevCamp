
"""
We have the Html class, which has a method called 'render',
but not so that it can be used from this class (it would 
throw an error), but so that its child classes can have that
method and, using polymorphism, although each instance uses 
the same method, for each instance the method will be different
"""

# OTHER WAY OF MAKING THE SAME BUT WITH POLYMORPHISM FUNCTIONS
class Heading2:
    def __init__(self, content):
        self.content = content
    
    def render(self):
        return f"<h1>{self.content}</h1>"
    

class Div2:
    def __init__(self, content):
        self.content = content
    
    def render(self):
        return f"<div>{self.content}</div>"


div_one = Div("Some content")
heading = Heading("Some big heading")
div_two = Div("Another div")

def html_render(tag_object):
    print(tag_object.render())

html_render(div_one)        # <div>Some content</div>
html_render(heading)        # <h1>Some big heading</h1>
html_render(div_two)        # <div>Another div</div>



# WHEN USING ONE OR THE OTHER
"""
if you only have one parent class with a shared method, it is
better to use the second way of doing it, but if your child 
classes share more data with the parent class, it is better
to use the first way
"""