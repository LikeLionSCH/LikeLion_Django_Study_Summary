import os

list = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, "A"
]
count = 0
sum = 0

for pwd in list:
    for path, dirs, files in os.walk("./" + str(pwd)):
        count = 0
        list = []

        print("===== Folder =====")
        print("|       ./" + str(pwd) + "       |")
        print("====== List ======")

        for file in files:
            if os.path.splitext(file)[1].lower() == '.py':
                list.append(file)
                count += 1

        sum += count
        print(sorted(list))

        print("Count : ", count)
        print()

print("Total count : " + str(sum))
