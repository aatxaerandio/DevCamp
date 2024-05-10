""" ENUNCIADO
remove_first_and_last(list_to_clean)         -> type of sintaxis to call the function
    return cleaned_list

# example 1:
html = ['<h1>', 'some content', '</h1>']

remove_first_and_last(html)
=> ['some content']


# example 2:
html2 = ['<h1>', 'some content', 'more', '</h1>']

remove_first_and_last(html2)
=> ['some content', 'more']
"""

""" MY RESULT
def remove_first_and_last(list_to_clean):
    if len(list_to_clean) < 3:
        return list_to_clean

    return list_to_clean[1:-1]
"""

""" RESULT FROM DEVCAMP
uses destructuring to assign the first and last value to a variable 
('_' because we are not going to use them) and everything else is 
stored in another ('*content')

The * serves to indicate that it saves ALL the elements it can in 
that variable, like the first and last ones we save in '_', it 
takes everything else and then returns it using 'return content'


EXAMPLE:
one, *two, three = [1, 2, 3, 4]
    - one -> 1
    - two -> [2, 3]
    - three -> 4
"""

def remove_first_and_last(list_to_clean):
    if len(list_to_clean) < 3:
        return list_to_clean
    
    _, *content, _ = list_to_clean
    return content

html = ['<h1>', 'some content', '</h1>']
print(remove_first_and_last(html))                  # ['some content']

html2 = ['<h1>', 'some content', 'more', '</h1>']
print(remove_first_and_last(html2))                 # ['some content', 'more']