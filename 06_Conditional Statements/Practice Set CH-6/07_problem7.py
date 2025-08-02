#WAP in python to check wheather the post is talking about War or not.

post = input("Enter your post = ")
if("War".lower() in post.lower()):
    print("This post is talking about war.")
    print("\n", post)
else:
    print("This post is not talking about war.")
    print("\n", post)