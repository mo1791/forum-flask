from app import models


members = [
	models.Members("Monkey De Luffy", 20),
	models.Members("Kirua Zoldyck", 13),
	models.Members("Nico Robin", 28)
]

posts = [
	models.Posts("First Heading", "Lorem ipsum dolor sit amet, consectetur adipisicing elit\
		sed do eiusmod tempor incididunt ut labore et dolore magna aliqua\
		Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi\
		ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit\
		in voluptate velit esse cillum dolore eu fugiat nulla pariatur."),
	models.Posts("Second Heading", "Lorem ipsum dolor sit amet, consectetur adipisicing elit\
		sed do eiusmod tempor incididunt ut labore et dolore magna aliqua\
		Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi\
		ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit\
		in voluptate velit esse cillum dolore eu fugiat nulla pariatur."),
	models.Posts("Third Heading", "Lorem ipsum dolor sit amet, consectetur adipisicing elit\
		sed do eiusmod tempor incididunt ut labore et dolore magna aliqua\
		Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi\
		ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit\
		in voluptate velit esse cillum dolore eu fugiat nulla pariatur."),
	models.Posts("Fourth Heading", "Lorem ipsum dolor sit amet, consectetur adipisicing elit\
		sed do eiusmod tempor incididunt ut labore et dolore magna aliqua\
		Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi\
		ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit\
		in voluptate velit esse cillum dolore eu fugiat nulla pariatur."),
	models.Posts("Fifth Heading", "Lorem ipsum dolor sit amet, consectetur adipisicing elit\
		sed do eiusmod tempor incididunt ut labore et dolore magna aliqua\
		Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi\
		ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit\
		in voluptate velit esse cillum dolore eu fugiat nulla pariatur."),
	models.Posts("Sixth Heading", "Lorem ipsum dolor sit amet, consectetur adipisicing elit\
		sed do eiusmod tempor incididunt ut labore et dolore magna aliqua\
		Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi\
		ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit\
		in voluptate velit esse cillum dolore eu fugiat nulla pariatur."),
	models.Posts("Seventh Heading", "Lorem ipsum dolor sit amet, consectetur adipisicing elit\
		sed do eiusmod tempor incididunt ut labore et dolore magna aliqua\
		Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi\
		ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit\
		in voluptate velit esse cillum dolore eu fugiat nulla pariatur."),
	models.Posts("eighth Heading", "Lorem ipsum dolor sit amet, consectetur adipisicing elit\
		sed do eiusmod tempor incididunt ut labore et dolore magna aliqua\
		Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi\
		ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit\
		in voluptate velit esse cillum dolore eu fugiat nulla pariatur."),
	models.Posts("nineth Heading", "Lorem ipsum dolor sit amet, consectetur adipisicing elit\
		sed do eiusmod tempor incididunt ut labore et dolore magna aliqua\
		Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi\
		ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit\
		in voluptate velit esse cillum dolore eu fugiat nulla pariatur."),
	models.Posts("tenth Heading", "Lorem ipsum dolor sit amet, consectetur adipisicing elit\
		sed do eiusmod tempor incididunt ut labore et dolore magna aliqua\
		Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi\
		ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit\
		in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")
]

def store(members_store, posts_store):
	for member in members:
		members_store.add(member)

	for index, post in enumerate(posts):
		post.date += models.datetime.timedelta(0,index)
		posts_store.add(post)