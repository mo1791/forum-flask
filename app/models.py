import datetime


class Members(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age
		self.member_posts = []
		self.id = 0
	"""	
	@property
	def name(self):
		return self._name
	@property
	def age(self):
		return self._age
	def __repr__(self):
		return "%s::%x @name='%s',@age='%d',@id='%d'>"\
		%\
		(str(self.__class__)[:-1],id(self),self.name,self.age,self.id)
	"""
	def __str__(self):
		return "Name: %s,Age: %d" % (self.name, self.age)
	def __dict__(self):
		return {
			"id": self.id,
			"name": self.name,
			"age": self.age,
			"posts": self.member_posts
		}

class Posts(object):
	def __init__(self, title, content, member_id=0):
		self.id = 0
		self.title = title
		self.content = content
		self.member_id = member_id
		self.date  = datetime.datetime.now()
	def __str__(self):
		return "Title: %s, Content: %s" % (self.title, self.content)		
	def __dict__(self):
		return {
			"id": self.id,
			"title": self.title,
			"content": self.content,
			"member_id": self.member_id,
			"create_at": self.date.strftime("%Y-%m-%d %H:%M:%S")
		}


	"""	
	@property
	def title(self):
		return self._title
	@property
	def content(self):
		return self._content
	"""