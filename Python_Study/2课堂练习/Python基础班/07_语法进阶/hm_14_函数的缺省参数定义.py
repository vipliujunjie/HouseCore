def print_info(name, title="", gender=True):
    """

    :param title: 职位
    :param name: 班上同学的姓名
    :param gender: True 男生 False 女生
    """

    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("【%s】%s 是 %s" % (title, name, gender_text))


# 假设班上的同学，男生居多！
# 注意：在指定缺省参数的默认值时，应该使用最常见的值作为默认值！
#      如果一个参数的值不能确定，则不应该设置默认值，具体的数值在调用函数时，由外界传递！
print_info("小明", gender=True)
print_info("老王")
print_info("小美", gender=False)
