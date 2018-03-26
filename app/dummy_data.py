from app import models
import datetime


members = [
	models.Member(user="luffy20", name="Monkey De Luffy", age=20),
	models.Member(user="kirua15", name="Kirua Zoldyck", age=13),
	models.Member(user="nico30", name="Nico Robin", age=28)
]

posts = [
	models.Post(title="First Heading", content="Lorem ipsum dolor ", member_id=1),
	models.Post(title="Second Heading", content="Lorem ipsum dolor", member_id=1),
	models.Post(title="Third Heading", content="Lorem ipsum dolor sit.", member_id=2),
	models.Post(title="Fourth Heading", content="Lorem ipsum dolor.", member_id=2),
	models.Post(title="Fifth Heading", content="Lorem ipsum dolor", member_id=2),
	models.Post(title="Sixth Heading", content="Lorem ipsum dolor.", member_id=2),
	models.Post(title="Seventh Heading", content="Lorem ipsum dolor", member_id=1),
	models.Post(title="eighth Heading", content="Lorem ipsum dolor", member_id=3),
	models.Post(title="nineth Heading", content="Lorem ipsum dolor ", member_id=3),
	models.Post(title="tenth Heading", content="Lorem ipsum dolor", member_id=3)
]
