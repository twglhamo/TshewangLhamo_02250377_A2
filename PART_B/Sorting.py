def bubble_sort(items):
    length = len(items)
    for i in range(length):
        moved = False
        for j in range(0, length - i - 1):
            if items[j].lower() > items[j + 1].lower():
                items[j], items[j + 1] = items[j + 1], items[j]
                moved = True
        if not moved:
            break
    return items


def insertion_sort(values):
    for i in range(1, len(values)):
        current = values[i]
        pos = i - 1
        while pos >= 0 and values[pos] > current:
            values[pos + 1] = values[pos]
            pos -= 1
        values[pos + 1] = current
    return values


def quick_sort(nums, counter=0):
    counter += 1
    if len(nums) <= 1:
        return nums, counter

    mid = nums[len(nums) // 2]
    left = [x for x in nums if x < mid]
    equal = [x for x in nums if x == mid]
    right = [x for x in nums if x > mid]

    left_sorted, counter = quick_sort(left, counter)
    right_sorted, counter = quick_sort(right, counter)
    return left_sorted + equal + right_sorted, counter


def menu():
    names = ["Kado", "Bobchu", "Zamu", "Nado", "Lemo", "Cemo", "Deki", "Pema", 
             "Tashi", "Kinzang", "Sangay", "Chimi", "Phurba", "Wangdi", "Ugyen"]

    scores = [78, 45, 92, 67, 88, 54, 73, 82, 91, 59, 76, 85, 48, 93, 71,
              89, 57, 80, 69, 60]

    prices = [450, 230, 678, 125, 890, 345, 210, 999, 410, 505, 150, 275,
              320, 199, 600]

    while True:
        print("\n=== Sorting Menu ===")
        print("1. Sort Student Names (Bubble Sort)")
        print("2. Sort Test Scores (Insertion Sort)")
        print("3. Sort Book Prices (Quick Sort)")
        print("4. Exit")

        option = input("Choose an option (1-4): ").strip()

        if option == "1":
            print("Before:", names)
            result = bubble_sort(names.copy())
            print("After:", result)

            again = input("Sort again? (y/n): ").lower()
            if again != "y":
                print("Goodbye!")
                break

        elif option == "2":
            print("Unsorted:", scores)
            sorted_scores = insertion_sort(scores.copy())
            print("Sorted:", sorted_scores)

            print("Top 5 Scores:")
            top = sorted_scores[-5:][::-1]
            for i, value in enumerate(top, 1):
                print(f"{i}. {value}")

            again = input("Sort again? (y/n): ").lower()
            if again != "y":
                print("Goodbye!")
                break

        elif option == "3":
            print("Original:", prices)
            sorted_prices, used_calls = quick_sort(prices.copy())
            print("Sorted:", sorted_prices)
            print("Quick Sort Calls:", used_calls)

            again = input("Sort again? (y/n): ").lower()
            if again != "y":
                print("Goodbye!")
                break

        elif option == "4":
            print("Exiting. Thank you!")
            break

        else:
            print("Invalid input. Try again.")


menu()
