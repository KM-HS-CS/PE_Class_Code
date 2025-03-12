   # Example 1: Creating a list
    fruits = ["apple", "banana", "cherry"]
    print("\nExample 1: Creating a list")
    print("Fruits list:", fruits)

    # Example 2: Accessing elements in a list
    print("\nExample 2: Accessing elements in a list")
    print("First fruit:", fruits[0])
    print("Second fruit:", fruits[1])
    print("Last fruit:", fruits[-1])

    # Example 3: Modifying elements in a list
    print("\nExample 3: Modifying elements in a list")
    fruits[1] = "grape"
    print("Modified fruits list:", fruits)

    # Example 4: Adding elements to a list
    print("\nExample 4: Adding elements to a list")
    fruits.append("orange")
    print("Fruits list after adding 'orange':", fruits)

    # Example 5: Removing elements from a list
    print("\nExample 5: Removing elements from a list")
    removed_fruit = fruits.pop(2)
    print("Removed fruit:", removed_fruit)
    print("Fruits list after removing cherry:", fruits)

    # Example 6: Slicing a list
    print("\nExample 6: Slicing a list")
    print("First two fruits:", fruits[:2])
    print("Last two fruits:", fruits[-2:])
