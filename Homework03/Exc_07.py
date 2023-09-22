def first(size, *args):
    size = size + len(args)
    return size


def second(size, **kwargs):
    size = size + len(kwargs)
    return size


print(first(5, "first", "second", "third"))
first(1, "Alex", "Boris")
second(3, comment_one="first", comment_two="second", comment_third="third")
second(10, comment_one="Alex", comment_two="Boris")
