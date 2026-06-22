# Given a binary matrix maze[][] of size n × n containing values 0 and 1
# find all possible paths for a rat to travel from the source cell (0, 0) to the destination cell (n - 1, n - 1).
# The rat can move in four directions: up(U), down(D), left(L), and right(R).

# 1 represents an open cell through which the rat can move.
# 0 represents a blocked cell that cannot be traversed.

# The rat can move only through open cells and cannot visit the same cell more than once in a path. 
# Return all valid paths as strings consisting of 'U', 'D', 'L', and 'R', representing the sequence of moves taken by the rat.

# Input: maze[][] = {{1, 0, 0, 0}, {1, 1, 0, 1}, {1, 1, 0, 0}, {0, 1, 1, 1}}
# Output: ["DDRDRR", "DRDDRR"]

DIRECTIONS = [
            ("D", 1, 0),
            ("L", 0, -1),
            ("R", 0, 1),
            ("U", -1, 0)
        ]

def find_paths(maze):
    
    n = len(maze)

    result = []

    visited = [[False]*n for _ in range(n)]


    def is_safe(row, col):

        return (
            0 <= row < n and
            0 <= col < n and
            maze[row][col] == 1 and
            not visited[row][col]
        )


    def backtrack(row, col, path):

        # reached destination
        if row == n-1 and col == n-1:
            result.append(path)
            return

        for move, dr, dc in DIRECTIONS:

            new_row = row + dr
            new_col = col + dc


            if is_safe(new_row, new_col):

                visited[new_row][new_col] = True

                backtrack(
                    new_row,
                    new_col,
                    path + move
                )

                # undo choice
                visited[new_row][new_col] = False



    # starting cell blocked
    if maze[0][0] == 0 or maze[n-1][n-1] == 0:
        return []


    visited[0][0] = True

    backtrack(0,0,"")


    return result



maze = [
    [1,1,1],
    [1,1,1],
    [0,0,1]
]


print(find_paths(maze))


                    #                (0,0)
                    #                 ""
                    #                 |
                    #                 D
                    #                 |
                    #               (1,0)
                    #               "D"
                    #       __________|__________
                    #      |          |          |
                    #      D          L          R
                    #      |          |          |
                    # (2,0) X       invalid    (1,1)
                    #                          "DR"
                    #               ___________|____________
                    #              |       |       |        |
                    #              D       L       R        U
                    #              |       |       |        |
                    #           (2,1)X  visited  (1,2)   (0,1)
                    #                           "DRR"     "DRU"
                    #                             |          |
                    #               ______________|__        |
                    #              |       |       | |       |
                    #              D       L       R U       R
                    #              |       |       | |       |
                    #            (2,2)   visited  invalid   (0,2)
                    #             |                        "DRUR"
                    #             |                       |
                    #           DRRD             _________|________
                    #                           |    |    |       |
                    #                           D    L    R       U
                    #                           |    |    |       |
                    #                         (1,2) visited invalid invalid
                    #                           |
                    #                           D
                    #                           |
                    #                         (2,2)
                    #                      
                    #                        DRURDD