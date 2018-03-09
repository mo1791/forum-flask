from app import models, stores
import time


def creat_members():
	member1 = models.Members("Monkey De Luffy", 20)
	member2 = models.Members("Kirua Zoldyck", 13)
	member3 = models.Members("Nico Robin", 28)
	print("=" * 75)
	return member1, member2, member3

def store_should_add_models(members_instance, store_member_instance):
	for member in members_instance:
		store_member_instance.add(member)

def print_all_members(members_store):
	print("=" * 75)
	for member in members_store.get_all():
		print member
	print("=" * 75)

def get_by_id_should_retrieve_same_object(member_store, member_test):
	print("=" * 75)
	re_member = member_store.get_by_id(member_test.id)
	if re_member is member_test:
		print("same!!!")
	print("=" * 75)

def update_should_modify_object(member_store, member_test):
	print("=" * 75)
	cp_member = models.Members(member_test.name, member_test.age)
	cp_member.id = 3
	
	if cp_member is not member_test:
   		print("member3 and member3_copy are not the same !")

	print(cp_member)
	cp_member.name = "john"
	member_store.update(cp_member)
	print(member_store.get_by_id(member_test.id))
	print("=" * 75)



def create_posts(members):
	post1 = models.Posts("First Heading","Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod\
		tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,\
		quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo\
		consequat.", members[0].id)
	post2 = models.Posts("second Heading","Duis aute irure dolor in reprehenderit in voluptate velit esse\
		cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non\
		proident, sunt in culpa qui officia deserunt mollit anim", members[0].id)
	post3 = models.Posts("Third Heading"," id est laborum.Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod\
		tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,\
		quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo\
		consequat", members[0].id)
	post4 = models.Posts("Fourth Heading","Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod\
		tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,\
		quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo\
		consequat.", members[1].id)
	post5 = models.Posts("Fifth Heading","Duis aute irure dolor in reprehenderit in voluptate velit esse\
		cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non\
		proident, sunt in culpa qui officia deserunt mollit anim", members[1].id)
	post6 = models.Posts("Sixth Heading"," id est laborum.Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod\
		tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,\
		quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo\
		consequat", members[2].id)

	return post1, post2, post3, post4, post5, post6

def store_should_add_post(posts, store_post):
	for post in posts:
		store_post.add(post)


def store_should_get_top_two_members(member_store, post_store):
	print("=" * 75)
	for m in member_store.get_top_two(post_store.get_all()):
		print("%s has posts:" % m)
		for post in m.member_posts:
			print("\t%s" % post)
	print("=" * 75)

def store_should_get_members_with_posts(member_store, post_store):
	members = member_store.get_member_with_posts(post_store.get_all())
	
	for member in members:
		print("%shas posts:" % member)
		for post in member.member_posts:
			print("\t%s" % post)
	print("=" * 75)



def store_should_get_posts_by_date(post_store):
	posts = post_store.get_posts_by_date()
	print("=" * 75)
	for post in posts:
		print(post.date)

if __name__ == "__main__":

	members_instance = creat_members()
	member1,member2,member3 = members_instance
	
	member_store = stores.MemberStores()

	store_should_add_models(members_instance, member_store)

	all_posts = create_posts(members_instance)

	post_store = stores.PostStores()

	store_should_add_post(all_posts, post_store)

	store_should_get_posts_by_date(post_store)

	#store_should_get_members_with_posts(member_store,post_store)
	
	#store_should_get_top_two_members(member_store,post_store)

	#print_all_members(member_store)

	#get_by_id_should_retrieve_same_object(member_store,member1)

	#update_should_modify_object(member_store,member3)