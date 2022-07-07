# Sudoku-Game-cum-Solver 🧩
## Index Of Files Included (A-Z) 🧾
### AddRecord.py ➕
Performs 2 functions. 
1. Add game details to the database (when requested/on button click).
2. To show the details saved in the database.
### DT.py 📅⌚
Provides the Date and Time when the game details requested to be saved.
### EmptySudoku.py 0️⃣
Contains an empty sudoku puzzle with entry in each cell being '0' (meaning empty).
### SaveSudoku.py 💾
Upon requesting, this file tells whether the Game is completed. 
### solver.py ✔
As the name suggests, the file solves the puzzle. Suitability of a number in a cell also checked.
### Sudoku.py 🧩
Driver File. GUI designed inside it. Contains various functions (can be understood by following the comments in the source code).

## How to Play ⁉⚙
1. Run ▶ the "Sudoku.py" file (source code). A window with empty Sudoku board will be shown.
2. To Play a game.
👉 Fill the numbers to set a game.
👉 Click on "Play" button.
👉 Now, start playing (solving) the game. When done, click on "Check" Button.
3. To Solve the game/puzzle.
👉 If stuck & want the solution, click on "Solve" Button.
4. To Save game details.
👉 Click on "Save Record" Button.
5. To peek on the games played so far.
👉 Click on "History" Button.
6. To Clear the values filled in.
👉 Click on "Clear" Button.

## Caution ⚠
1. ⚠ Mandatory to click on "Play" after setting the values. Otherwise, "Check" won't work.
2. ⚠ Unsolvable Sudoku Puzzles not supported till date (Searching for solution to this).
3. ⚠ On clicking "Solve", values filled in the board till that time will be considered.
4. ⚠ Code Specific: For connection to MySQL database, remember to use "username" and "password" as per your system.
5. ⚠ All the files should be in a single directory. Otherwise, You've to make changes to the import statements.
6. ⚠ Remember to install MySQL database & the MySQL Python connector.
7. ⚠ Unsolvable puzzles puts the GUI into a long recursive loop. It may look like the GUI Window has been freezed (which is not).

## References 🔍
1. https://www.youtube.com/watch?v=xAXmfZmC2SI&t=0s
2. https://www.youtube.com/watch?v=OF0H0B0IuFM
## Being updated 💬
