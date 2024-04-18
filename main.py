# Moebius Assessment done by Zach Akin

# Question 1

# Why does the following program print `prime` for input `6`? How should
# it be modified to print only when the value is one of the first four
# primes?

# x = 6
# if x == 2 or 3 or 5 or 7:
#     print('prime')

# # Answer 1
# if x in [2, 3, 5, 7]:
#     print('Prime')
# else:
#     print(f'Didnt find {x} in the list')

# Question 2

# Which of these is the most efficient, and why?

# x in set([2, 3, 5, 7])
# x in list([2, 3, 5, 7])
# x in tuple([2, 3, 5, 7])

# Answer 2

# set() is the most efficient in this scenario because we are working with a list of non repeating numbers. Set has
# the time complexity of O(1) vs list and tuple has a time complexity of O(n). Set uses hash tables being able to
# find what we are looking for without iterating over the entire list.

# Question 3

# The following code should print `[5], [5]`. Why doesn't it produce
# the expected output? How should it be fixed?

# def init_data(data=[]):
#     """Create a list containing the value 5."""
#     data.append(5)
#     return data
#
# x = init_data()
# y = init_data()
# print(x, y)


# Answer 3
# def init_data(data):
#     """Create a list containing the value 5."""
#     data.append(5)
#     return data
#
# x = init_data([])
# y = init_data([])
# print(x, y)
# print(f"{x}, {y}") # If you want the comma in between the lists.


# Question 4

# What does the following code do? What is the difference between the two
# versions?

# values = [2,4,6]
#
# if any([value % 2 for value in values]):
#     print('done')
#
# # or
#
# if any(value % 2 for value in values):
#     print('done')

# Answer 4


# Question 5

# What is the equivalent of the following code without using decorator
# syntax? Does order matter when decorating a function multiple times?


# @bp.route('/info')
# @login_required
# def user_info():
#     return jsonify(current_user)


# Answer 5

# def user_info():
#     return jsonify(current_user)
#
# user_info = login_required(user_info)
# user_info = bp.route('/info')(user_info)

# The order matters for sure when adding decorations. If the login_required was after the route then it wouldn't
# check if the user was authenticated. This would be a huge security flaw.

# Question 6

# A list contains instances of the following class. Write a function that
# will produce a sorted list ordered first by name descending, then id
# ascending.
#
# class User:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#
# def sort_name_desc_id_asc(users):
#     # complete this function
#     pass
#
# users = [User(...), User(...), ...]
# sorted_users = sort_name_desc_id_asc(users)

# Answer 6

# class User:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#
# def sort_name_desc_id_asc(users):
#     # Sorting by the UserID in ascending order
#     users.sort(key=lambda user: user.id)
#     # Sorting by Username in descending order
#     users.sort(key=lambda user: user.name, reverse=True)
#     return users
#
# users = [User(2, 'Zach'), User(1, 'John'), User(3, 'Zach')] # Sample data
# sorted_users = sort_name_desc_id_asc(users)
#
# # Printing out results for testing
# for user in sorted_users:
#     print(f'Name: {user.name}, ID: {user.id}')


# Bonus Question

# What does the following output, and why?

# x = [1, 2, 3, 4]
#
# for x[-1] in x:
#     print(x)

# Bonus Answer

# In python you can use x[-1] to access the last item in the list. Here is the output.
# [1, 2, 3, 1]
# [1, 2, 3, 2]
# [1, 2, 3, 3]
# [1, 2, 3, 3]
# The loop essentially takes the position in the list and replaces the last number in the list with that position.
# So the first go through the first number in the list is 1 so then it replaces the last number in the list with 1 getting us [1, 2, 3, 1].
# The second number in the list is 2 so the last number in the list gets replaced with 2 getting us [1, 2, 3, 2]
# The third number in the list is 3 so the last number in the list gets replaced with 3 getting us [1, 2, 3, 3]
# And for the final fourth number in the list it looks at the list and its a 3 from the last loop getting us [1, 2, 3, 3]
