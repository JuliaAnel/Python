
count = 0

range_count = 10

for_count = 0

run = True

while run:
    print("Step =", count)
    count += 1

    print("===========================")


while count < range_count:
    print("Step =", count)
    count = count + 1

    print("===========================")


while count < range_count:
    print("Step =", count)
    count = count + 1
    if count == 3:
       print("Step = ", count, 'If body')


print("===========================")


while count < range_count:
    print("Step =", count)
    count = count + 1
    if count == range_count:
        print("STOP ", count)
        break


print("===========================")


for item in range(for_count, range_count):
    print("Step =", item)


    print("===========================")


for item in range(0, 30):
    print("Step =", item)
    if item == 5:
        print("Item =", item)
    elif item == 10:
        print("Item =", item)
    elif item < 4:
        print("Item <", item)
    elif item >= 27:
        print("Item >=", item)

print("====================================")

for item in range(0, range_count+1):
    print("Step =", item)
    if item == 7:
        inner_count = 0
        print("-- inner_count =", inner_count)
        for inner_item in range(0, item):
            print("-------- Inner_Step =", inner_item)
            if inner_item == 5:
                inner_count = inner_item
                print("-- inner_count =", inner_count)

