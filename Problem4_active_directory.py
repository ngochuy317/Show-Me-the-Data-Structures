class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group: Group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    find = False
    if user in group.get_users():
        return True
    
    for gr in group.get_groups():
        find = is_user_in_group(user, gr)
        if find:
            return True
        
    return find

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print(f"{'*'*4} Test Case 1: Group with no Users test {'*'*4}")
empty_grp = Group("empty")
user = "user"
print(empty_grp.get_name(), "group has user?", is_user_in_group(user, empty_grp))
print(f"{'-'*50}")

# Test Case 2
print(f"{'*'*4} Test Case 2: Group with several users test {'*'*4}")
grp = Group("test_grp")
user1 = "user1"
user2 = "user2"
user3 = "user3"
user4 = "user4"

grp.add_user(user1)
grp.add_user(user2)
grp.add_user(user3)

print(grp.get_name(), "group have user1?", is_user_in_group(user1, grp))
print(grp.get_name(), "group have user2?", is_user_in_group(user2, grp))
print(grp.get_name(), "group have user3?", is_user_in_group(user3, grp))
print(grp.get_name(), "group have user4?", is_user_in_group(user4, grp))
print(f"{'-'*50}")

# Test Case 3
print(f"{'*'*4} Test Case 3: Test Code {'*'*4}")

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user_a = "sub_child_user_a"
sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
print(parent.get_name(), "group has sub_child_user?", is_user_in_group(sub_child_user, parent))
print(child.get_name(), "group has sub_child_user?", is_user_in_group(sub_child_user, child))
print(sub_child.get_name(), "group has sub_child_user?", is_user_in_group(sub_child_user, sub_child))
print(parent.get_name(), "group has sub_child_user_a?", is_user_in_group(sub_child_user_a, parent))