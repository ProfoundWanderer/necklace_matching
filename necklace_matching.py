def create_new_name(original_name):
    removed_char = original_name[0]
    incomplete_name = original_name[1:]
    created_name = incomplete_name + removed_char

    return created_name


def same_necklace(og_name, new_name):
    if og_name == new_name:
        return True

    created_name = create_new_name(og_name)

    for i in range(len(og_name)):
        if og_name == new_name:
            return True
        elif created_name == new_name:
            return True
        else:
            created_name = create_new_name(created_name)

    return False


print(same_necklace("nicole", "icolen"))
print(same_necklace("nicole", "lenico"))
print(same_necklace("nicole", "coneli"))
print(same_necklace("aabaaaaabaab", "aabaabaabaaa"))
print(same_necklace("abc", "cba"))
print(same_necklace("xxyyy", "xxxyy"))
print(same_necklace("xyxxz", "xxyxz"))
print(same_necklace("x", "x"))
print(same_necklace("x", "xx"))
print(same_necklace("x", ""))
print(same_necklace("", ""))
