a = "aaabbcccccc"

str_count = 0
for s in a:
    if s.isalpha():
        str_count += 1


def count_each_char(str):
    dict = {}
    for i in str:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    return dict


if __name__ == "__main__":
    res = count_each_char("aaabbcccccc")


    print(res)
