#practical3
#Implement Greedy search algorithm for any of the following application:
I. Selection Sort
II. Minimum Spanning Tree
III. Single-Source Shortest Path Problem
IV. Job Scheduling Problem
V. Prim's Minimal Spanning Tree Algorithm
VI. Kruskal's Minimal Spanning Tree Algorithm
VII. Dijkstra's Minimal Spanning Tree Algorithm

# selection sort 

def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def main():
    try:
        user_input = input("Enter numbers separated by spaces: ")
        arr = list(map(int, user_input.split()))
        print("Original list:", arr)
        sorted_arr = selectionSort(arr)
        print("Sorted list:", sorted_arr)
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()



output :

anishka@tanishka-Latitude-5490:~$ python3 selectionsort3.py
Enter numbers separated by spaces: 89 56 34 45 65 78
Original list: [89, 56, 34, 45, 65, 78]
Sorted list: [34, 45, 56, 65, 78, 89]
tanishka@tanishka-Latitude-5490:~$ 

