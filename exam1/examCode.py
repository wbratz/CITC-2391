# def get_username(first, last):
#     s = first + "." + last
#     return s.lower()

# def main():
#     first_name = input("Enter your first name: ")
#     last_name = input("Enter your last name: ")
#     username = get_username(first_name, last_name)
#     print("Your username is: " + username)
   
# if __name__ == "__main__":
#     main()

# def get_volume(width, height, length=2):
#     volume = width * height * length
#     return volume

# def main():
#     l = 3
#     w = 4
#     h = 5
#     v = get_volume(l, w, h)
#     print(v)
   
# if __name__ == "__main__":
#     main()


# def add(x = 4, y = 2):
#     z = x + y
#     return z

# def main():
#     num1 = 5
#     num2 = 6
#     result = add(num1, num2)
#     print("The sum is", result)
   
# if __name__ == "__main__":
#     main()

# sum = 0
# for i in range(0, 25, 5):
#     sum += i
# print(sum)

# x = 7
# y = 2 
# z = 1.5
# new_num = x / y + z

# print(new_num)

# print("lions", "tigers", "bears", sep = ' & ', end = ' oh, my!!')

prices = [10, 15, 12, 8]
total = 0
i = 1
while i < len(prices):
    total += prices[i]
    i += 1
print(total) 