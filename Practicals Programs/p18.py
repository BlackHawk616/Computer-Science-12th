stack = []

def push(item):
    stack.append(item)

def pop():
    if not is_empty():
        return stack.pop()
    else:
        return None

def peek():
    if not is_empty():
        return stack[-1]
    else:
        return None

def is_empty():
    return len(stack) == 0

def size():
    return len(stack)

def display():
    return stack

def main():
    while True:
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if empty")
        print("5. Size")
        print("6. Display")
        print("7. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            item = int(input("Enter item to push: "))
            push(item)
        elif choice == 2:
            print("Popped item:", pop())
        elif choice == 3:
            print("Top item:", peek())
        elif choice == 4:
            print("Is empty:", is_empty())
        elif choice == 5:
            print("Size:", size())
        elif choice == 6:
            print("Stack:", display())
        elif choice == 7:
            break
        else:
            print("Invalid choice")


main()