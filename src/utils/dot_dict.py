class DotDict(dict):
    """
    一个让字典支持类成员符号('.')访问的转换器. 支持递归访问, 惰性转换(只有在使用成员符号 '.'
    访问时才会转换嵌套中的字典).
    """

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __getattr__(self, key):
        if type(self[key]) != dict:
            return self[key]
        self[key] = DotDict(self[key])
        return self[key]


# Test
if __name__ == "__main__":
    d = {"a": {"b": {"c": {"d": "5"}}}, "f": "wefs"}
    dot_d = DotDict(d)
    dot_d.a.b = 2165
    dot_d.g = {"sdf": "sdfsdf"}
    print(dot_d)
