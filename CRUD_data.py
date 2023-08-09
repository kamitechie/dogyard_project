from sqlalchemy.orm import sessionmaker
from dogyard_models import Dog, engine
import base64

Session = sessionmaker(bind=engine)
session = Session()
all_dogs = session.query(Dog).all()

# Generate HTML content
html_content = ""
for dog in all_dogs:
    image_bytes = dog.photo
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')
    html_content += f"""
    <div class="dog">
        <img src="data:image/jpeg;base64,{image_base64}" alt="{dog.dogs_name}">
        <h2>{dog.dogs_name}</h2>
        <p>{dog.birth_date}</p>
        <p>{dog.pool}</p>
    </div>
    """

# Insert the generated HTML content into the index.html file
with open('index.html', 'w') as html_file:
    html_file.write(f"""<!DOCTYPE html>
    <html>
    <head>
        <title>Dogyard Dogs</title>
        <link rel="stylesheet" type="text/css" href="style.css">
    </head>
    <body>
        <h1>All dogs</h1>
        <div class="Dogs">
            {html_content}
        </div>
    </body>
    </html>""")
