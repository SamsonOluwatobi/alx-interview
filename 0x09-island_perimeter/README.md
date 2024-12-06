# Island Perimeter

This project involves solving a classic grid-based problem: calculating the perimeter of an island represented in a 2D grid. The grid consists of cells, where each cell can either represent land (`1`) or water (`0`). The objective is to compute the perimeter of the island based on the provided grid.

---

## Requirements

- **Environment**: Ubuntu 20.04 LTS
- **Python Version**: Python 3.4.3
- **Editor**: Allowed editors include `vi`, `vim`, and `emacs`
- **Code Style**: PEP 8 (version 1.7)
- **Execution**: All scripts must be executable (`chmod +x`)

---

## Task: Island Perimeter

### Problem Statement
Write a function, `island_perimeter(grid)`, that calculates the perimeter of the island described in the `grid`.

### Function Prototype
```python
def island_perimeter(grid):
    """
    Calculates the perimeter of an island in a grid.
    """
```

### Input
- `grid`: A list of lists of integers:
  - `0` represents water.
  - `1` represents land.
- Each cell is square, with a side length of 1.
- Cells are connected horizontally or vertically (not diagonally).
- The grid is rectangular, with dimensions not exceeding 100x100.
- The island is surrounded by water and does not have lakes (internal water completely surrounded by land).

### Output
- Returns the perimeter of the island.

---

### Example
#### Input Grid
```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
```

#### Output
```
12
```

---

## Installation and Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/username/alx-interview.git
   cd alx-interview/0x09-island_perimeter
   ```

2. **Ensure File Permissions**:
   ```bash
   chmod +x 0-island_perimeter.py
   chmod +x 0-main.py
   ```

3. **Run the Test File**:
   ```bash
   ./0-main.py
   ```

---

## Algorithm Explanation

1. **Traverse the Grid**:
   - For each cell in the grid:
     - If it represents land (`1`), add 4 to the perimeter.
     - Subtract 2 for each shared edge with adjacent land cells to avoid overcounting.

2. **Complexity**:
   - **Time Complexity**: \(O(n \times m)\), where \(n\) and \(m\) are the dimensions of the grid.
   - **Space Complexity**: \(O(1)\), as the solution uses a constant amount of extra space.

---

## File Structure

- **`0-island_perimeter.py`**: Contains the `island_perimeter` function implementation.
- **`0-main.py`**: Main file to test the `island_perimeter` function.
- **`README.md`**: Documentation for the project.

---

## Example Usage

#### Run the Script
```bash
./0-main.py
```

#### Expected Output
```
12
```

---

## Author

This project is part of the **ALX Interview Prep Curriculum**.  
Created by **[Samson Oluwatobi]**.

---