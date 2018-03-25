from app import models
from app import db
from sqlalchemy import func, desc


class BaseStores(object):
	
	def __init__(self, data_provider):
		self.data_provider = data_provider
	
	def add(self, item):
		db.session.add(item)
		db.session.commit()
	
	def get_all(self):
		return self.data_provider.query.all()
	
	def get_by_id(self, id_):
		return self.data_provider.query.get(id_)
	
	def entity_exist(self, id_):
		result = True
		if self.get_by_id(id_) is None:
			result = False
		return result
	
	def delete(self, id_):
		result = self.data_provider.get(id_)
		db.session.delete(result)
		db.session.commit()
		return result
	
	def update(self, item_, entity):
		result = self.data_provider.query.filter_by(id=item_.id).update(entity)
		db.session.commit()
		return result

class MemberStores(BaseStores):

	def __init__(self):
		super(MemberStores,self).__init__(models.Member)
	
	def update(self, member):
		return super(MemberStores, self).update(member,{"name": member.name, "age": member.age})
	
	def get_by_name(self, name):
		return self.data_provider.query.filter_by(name=name).all()	
	
	def get_member_with_posts(self):
		return self.data_provider.query.join(models.Member.posts).all()
		

	def get_top_two(self):
		pass

class PostStores(BaseStores):

	def __init__(self):
		super(PostStores,self).__init__(models.Post)
	
	def update(self, post):
		return super(PostStores, self).update(post, {"title": post.title, "content": post.content})

	def get_posts_by_date(self):
		pass