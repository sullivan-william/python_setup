def hello():
    print("Hello world")

hello()

def pack(item_1, item_2, item_3):
    return [item_1, item_2, item_3]

print(pack("swimsuit", "toothbrush", "cards"))

def eat_lunch(list):
    if len(list) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(list)):
            if i == 0:
                print(f"First I eat {list[i]}")
            else:
                print(f"Next I eat {list[i]}")

eat_lunch([])
eat_lunch(["sushi"])
eat_lunch(["sandwich","chips","pickle"])