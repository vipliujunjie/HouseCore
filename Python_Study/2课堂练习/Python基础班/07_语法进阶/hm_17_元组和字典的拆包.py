def demo(*args, **kwargs):

    print(args)
    print(kwargs)


# 元组变量/字典变量
gl_nums = (1, 2, 3, 4)
gl_dict = {"name": "小明", "age": 18}

# demo(gl_nums, gl_dict)

demo(*gl_nums, **gl_dict)
