**ARDjango Project**

This is an augmented reality (AR) game built with Django and three.js.

**Description**

The ARDjango project is a web-based game that combines augmented reality technology with a word jumble game. It allows users to play a word jumble game in an augmented reality environment. The game presents jumbled letters on the screen, and the user needs to pick the correct letters and place them in the correct order to form a word. The game utilizes the MindAR image processing library and three.js library for the augmented reality and 3D rendering functionality.

**Features**

- Augmented reality (AR) gameplay
- Word jumble game with jumbled letters
- Drag and drop functionality for letter placement
- Undo functionality to revert letter placements
- Timer to track the remaining time
- Score calculation based on moves and time bonus

**Installation**

1. Clone the repository: https://github.com/CharanyaSatpute/ARDjango
2. Install the required dependencies: pip install -r requirements.txt
3. Run database migrations: python manage.py migrate
4. Start the development server: python manage.py runserver
5. Open your web browser and access the application at `http://localhost:8000`.

**Usage**

- On the home page, tap on the "Start Game" button to begin playing the AR word jumble game.
- The game will present jumbled letters on the screen. Tap on a letter to pick it up.
- Place the letter in the correct white slot to form the word. If you picked the wrong letter, you can undo the placement or drop the tile.
- Complete the word by placing all the letters in the correct order within the time limit.
- After completing the game, a score card will be displayed showing your score and the option to submit your score.
- You can refresh the browser window to play again.
