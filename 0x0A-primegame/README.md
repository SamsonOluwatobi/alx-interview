# Prime Game

## Description
Maria and Ben play a competitive game involving prime numbers. The game is played in multiple rounds, where players alternately pick a prime number and remove it and all its multiples from a set of integers. The player who cannot make a move loses the round.

This project involves implementing the logic to determine the winner of the game across multiple rounds.

---

## General Requirements
- **Environment**: Ubuntu 20.04 LTS
- **Python Version**: Python 3.4.3
- **Style Guide**: PEP 8 (version 1.7.x)
- **Executable Files**: All scripts must be executable (`chmod +x`)

---

## Function Prototype
```python
def isWinner(x, nums):
    """
    Determines the winner of a prime game.
    """
```

### Parameters
- `x` (int): Number of rounds.
- `nums` (list): A list of integers, where each integer represents the size of the set in a round.

### Return Value
- Returns the name of the player (`"Maria"` or `"Ben"`) who won the most rounds.
- Returns `None` if the winner cannot be determined.

---

## Example

### Input
```python
x = 3
nums = [4, 5, 1]
```

### Output
```
Winner: Ben
```

### Explanation
- **Round 1 (n=4)**:
  - Maria picks `2`, removing `[2, 4]`. Remaining: `[1, 3]`.
  - Ben picks `3`, removing `[3]`. Remaining: `[1]`.
  - Ben wins.
- **Round 2 (n=5)**:
  - Maria picks `2`, removing `[2, 4]`. Remaining: `[1, 3, 5]`.
  - Ben picks `3`, removing `[3]`. Remaining: `[1, 5]`.
  - Maria picks `5`, removing `[5]`. Remaining: `[1]`.
  - Maria wins.
- **Round 3 (n=1)**:
  - No prime numbers. Ben wins.

Result: Ben wins 2 rounds, Maria wins 1 round.

---

## Installation and Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/samsonoluwatobi/alx-interview.git
   cd alx-interview/0x0A-primegame
   ```

2. **Run the Test File**:
   ```bash
   ./main_0.py
   ```

---

## Algorithm

### Steps:
1. **Precompute Primes**: Use the Sieve of Eratosthenes to find all prime numbers up to the maximum value in `nums`.
2. **Simulate Each Round**:
   - Track the removal of primes and their multiples.
   - Alternate turns between players.
3. **Count Wins**:
   - Track the number of wins for Maria and Ben.
4. **Return the Winner**:
   - Compare the number of wins and return the player with the most wins.

### Complexity:
- **Time Complexity**: \(O(k + n \cdot \log(\log(k)))\), where \(k\) is the largest number in `nums` and \(n\) is the number of rounds.
- **Space Complexity**: \(O(k)\) for storing prime numbers.

---

## Files
- `0-prime_game.py`: Contains the `isWinner` function.
- `main_0.py`: Test script for the function.
- `README.md`: Documentation.

