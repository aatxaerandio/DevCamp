"""
heading_generator(title, heading_type)

heading_generator('Greeting', '1')
<h1>Greeting</h1>

heading_generator('Greeting', '3')
<h3>Greeting</h3>

"""

def heading_generator(title, heading_type):
  return f"<h{heading_type}> {title} </h{heading_type}>"

print(heading_generator('Greeting', '1'))     # <h1> Greeting </h1>
print(heading_generator('Greeting', '3'))     # <h3> Greeting </h3>