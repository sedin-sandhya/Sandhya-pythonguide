import random
import time

#Bubble Sort O(n^2)

def bubble_sort(players):
    length = len(players)

    for i in range(length):
        swapped = False
        for j in range(0, length-i-1):

            if players[j]["score"] > players[j+1]["score"]:
                players[j], players[j+1] = players[j+1], players[j]
                swapped = True
        
        if not swapped:
            break
    return players

# Merge Sort O(n log n)

def merge_sort(players):

    if len(players) <= 1:
        return players
    
    mid = len(players) // 2
    left = merge_sort(players[:mid])
    right = merge_sort(players[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i]["score"] <= right[j]["score"]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Quick Sort O(n log n)

def quick_sort(players):
    if len(players) <= 1:
        return players
    
    pivot = players[-1]

    left = []
    equal = []
    right = []

    for player in players:

        if player["score"] > pivot["score"]:
            left.append(player)

        elif player["score"] == pivot["score"]:
            equal.append(player)

        else:
            right.append(player)

    return (
        quick_sort(right)
        + equal
        + quick_sort(left)
    )

def generate_players(n):
    players = []

    for i in range(n):

        players.append({
            "name": f"Player{i}",
            "score": random.randint(0, 100000)
        })
    return players

def compare_sorts(players):

    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
    ]

    for name, algorithm in algorithms:

        # data = players.copy()
        start = time.time()

        result = algorithm(players)
        end = time.time()

        print(
            f"{name}: {end-start:.6f} seconds"
        )

def main():
    players = generate_players(5000)
    compare_sorts(players)

if __name__ == "__main__":
    main()