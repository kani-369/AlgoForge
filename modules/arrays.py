# array_functions.py

# 1. Show array
def show_array(arr):
    print("Array elements:")
    for i in arr:
        print(i, end=" ")
    print()

# 2. Insert element
def insert_element(arr, element):
    arr.append(element)
    print(f"{element} inserted.")

# 3. Delete element
def delete_element(arr, element):
    if element in arr:
        arr.remove(element)
        print(f"{element} deleted.")
    else:
        print("Element not found.")

# 4. Search element
def search_element(arr, element):
    if element in arr:
        print(f"{element} found at index {arr.index(element)}")
    else:
        print("Element not found.")

# 5. Array statistics
def array_stats(arr):
    if len(arr) == 0:
        print("Array is empty.")
        return
    print("Sum:", sum(arr))
    print("Average:", sum(arr) / len(arr))
    print("Minimum:", min(arr))
    print("Maximum:", max(arr))

# Test run
if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]

    show_array(arr)
    insert_element(arr, 60)
    show_array(arr)
    delete_element(arr, 30)
    show_array(arr)
    search_element(arr, 40)
    array_stats(arr)
