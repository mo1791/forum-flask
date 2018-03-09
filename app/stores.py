import itertools
import copy


class BaseStores(object):
	def __init__(self, data_provider, last_id):
		self._last_id = last_id
		self._data_provider = data_provider
	def add(self, item_instance):
		item_instance.id = self._last_id
		self._data_provider.append(item_instance)
		self._last_id += 1
	def get_all(self):
		return self._data_provider
	def get_by_id(self, id_):
		all_items = self.get_all()
		result = None
		for item in all_items:
			if id_ == item.id:
				result = item
				break
		return result
	def entity_exist(self, id_):
		result = True
		if self.get_by_id(id_) is None: 
			result = False
		return result
	def delete(self, id_):
		result = None
		item = self.get_by_id(id_)
		if item is not None :
			result = item
			self._data_provider.remove(item)
		return result
	def update(self, item_):
		all_items = self.get_all()
		done = False
		for index, item in enumerate(all_items):
			if item_.id == item.id:
				all_items[index] = item_
				done = True
				break
		return done
class MemberStores(BaseStores):
	members = []
	last_id = 1
	def __init__(self):
		super(MemberStores,self).__init__(MemberStores.members, MemberStores.last_id)
	def get_by_name(self, name):
		name = name.lower()
		all_members = self.get_all()
		for member in all_members:
			member_name = member.name.lower()
			if name == member_name:
				yield member	
	def get_member_with_posts(self, all_posts):
		all_members = copy.deepcopy(self.get_all())
		for member,post in itertools.product(all_members, all_posts):
			if member.id == post.member_id:
				member.member_posts.append(post)

		for member in all_members:
			yield member
	def get_top_two(self, posts):
		members = list(self.get_member_with_posts(posts))
		top_members = sorted(members, key=lambda m: len(m.member_posts) * -1)[:2]
		for top_member in top_members:
			yield top_member
class PostStores(BaseStores):
	posts = []
	last_id = 1
	def __init__(self):
		super(PostStores,self).__init__(PostStores.posts, PostStores.last_id)
	def get_posts_by_date(self):
		all_posts = self.get_all()
		sorted_posts = sorted(all_posts, key=lambda post: post.date, reverse=True)
		for post in sorted_posts:
			yield post