my_str = input()
target_str = my_str.replace("!", "").replace(",", "").replace(".", "").replace("?", "").lower()
print(target_str)
