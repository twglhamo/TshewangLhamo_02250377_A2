def linear_find(data_list, key):
    count = 0
    for idx in range(len(data_list)):
        count += 1
        if data_list[idx] == key:
            return idx + 1, count
    return None, count


def binary_find(sorted_list, key):
    left_side = 0
    right_side = len(sorted_list) - 1
    steps = 0

    while left_side <= right_side:
        mid_point = (left_side + right_side) // 2
        steps += 1

        if sorted_list[mid_point] == key:
            return mid_point + 1, steps
        elif sorted_list[mid_point] < key:
            left_side = mid_point + 1
        else:
            right_side = mid_point - 1

    return None, steps


def main_menu():
    ids = [
        1001, 1005, 1003, 1008, 1002, 1007, 1004, 1010, 1006, 1009,
        1011, 1015, 1013, 1018, 1012, 1014, 1017, 1020, 1016, 1019
    ]

    scores = [
        42, 52, 58, 65, 70, 72, 75, 78, 82, 85,
        88, 90, 92, 95, 98, 100, 102, 105, 108, 110
    ]

    while True:
        print("\n=== SEARCHING OPTIONS ===")
        print("1) Linear Search (Student ID)")
        print("2) Binary Search (Scores)")
        print("3) Quit")

        user_option = input("Choose an option (1-3): ").strip()

        if user_option == "1":
            while True:
                print("\nCurrent ID list:", ids)
                user_input = input("Enter ID to search: ").strip()

                if not user_input.isdigit():
                    print("Please enter a valid whole number.")
                    continue

                key = int(user_input)
                pos, tries = linear_find(ids, key)

                if pos:
                    print(f"> Found ID {key} at position {pos} after {tries} checks.")
                else:
                    print(f"> ID {key} not found. Total comparisons: {tries}")

                again = input("Search another ID? (y/n): ").lower().strip()
                if again != "y":
                    break

            back = input("Return to main menu? (y/n): ").lower()
            if back != "y":
                print("Thanks for using the search tool!")
                break

        elif user_option == "2":
            while True:
                print("\nSorted scores:", scores)
                user_input = input("Enter score to locate: ").strip()

                if not user_input.isdigit():
                    print("Please enter a valid whole number.")
                    continue

                key = int(user_input)
                pos, steps = binary_find(scores, key)

                if pos:
                    print(f"> Score {key} found at position {pos} with {steps} comparisons.")
                else:
                    print(f"> Score {key} not found after {steps} checks.")

                again = input("Search another score? (y/n): ").lower().strip()
                if again != "y":
                    break

            back = input("Return to main menu? (y/n): ").lower()
            if back != "y":
                print("Thanks for using the search tool!")
                break

        elif user_option == "3":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid selection. Try again.")


main_menu()
