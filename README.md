# Guess-the-number_player

- Game, where the player selects the number and computer tries to guess it.

# Description:

In this game, you think of a secret number within a specified upper bound. The program will attempt to guess your number within five tries.

1. Specify the Upper Bound: You set the maximum limit for the number.
   
2. User Feedback: After each guess, you'll provide input:

- 'L' if the guessed number is lower than your secret number.
- 'H' if the guessed number is higher than your secret number.
- 'C' if the guessed number is correct.
The program will dynamically adjust its guesses based on your feedback until it either correctly identifies your number or exhausts its five attempts.

# Download Procedure:

1. Prerequisites:

- Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).

2. Clone or Download the Repository:

- You can either clone the repository using Git or download it as a ZIP file.
- To clone, use the following command in your terminal:
  git clone https://github.com/username/repo-name.git
- Alternatively, you can download the ZIP file directly from the repository and extract it to your desired location.

3. Navigate to the Project Directory:

-  Open your terminal or command prompt and navigate to the project folder:
  cd repo-name

4. Run the Program:

- Execute the program using Python:
  python guessing_game.py

5. Follow the Prompts:
   The program will guide you through the process of thinking of a number and providing feedback on its guesses.

## Additional Notes
- Make sure to check for any additional dependencies or instructions specific to your program if applicable.

# Usage

1. Start the Program:

- Run the program in your terminal or command prompt using the following command:
   python guessing_game.py

2. Input the Upper Bound:

- When prompted, enter an upper bound for the guessing range (e.g., 10). This number should be greater than 1.

3. Think of a Secret Number:

- Choose a number within the range of 1 to the upper bound you specified. Keep this number secret!

4. Provide Feedback:

- The program will make a guess. After each guess, respond with one of the following:
- 'L': If the guessed number is lower than your secret number.
- 'H': If the guessed number is higher than your secret number.
- 'C': If the guessed number is correct.

5. Continue Until the Guess is Correct or Attempts are Exhausted:
- The program will continue to guess based on your feedback until it either correctly identifies your number or runs out of attempts (maximum of five tries).

# Features

1. Dynamic User Input: The program dynamically adjusts its guesses based on user input ('L' for lower, 'H' for higher, 'C' for correct), making the game interactive and responsive.

2. Randomized Guesses: The program generates random guesses within a specified range, ensuring variety in gameplay.

3. Five Attempt Limit: The game challenges the program to guess the number within a maximum of five attempts, adding a sense of urgency and challenge.

4. Adjustable Upper Bound: Users can set the upper bound for the guessing range, allowing flexibility and customization of the difficulty level.

5. Real-Time Feedback: Immediate feedback allows the program to fine-tune its guesses, creating a logical flow of interaction.

6. Simple and Intuitive Interface: The program is easy to use, with clear prompts guiding users through the game.

#Contributing

We welcome contributions to improve the Number Guessing Game! If you'd like to contribute, please follow these steps:

1. Fork the Repository:

- Click the Fork button at the top right of the repository page to create your own copy of the project.

2. Clone the Forked Repository:

- Use the following command to clone the repository to your local machine:
  git clone https://github.com/your-username/repo-name.git

3. Create a New Branch:

- Before making changes, create a new branch to keep your work separate from the main branch:

  git checkout -b feature/your-feature-name

4. Make Your Changes:

- Add new features, fix bugs, or improve documentation in your new branch.

5. Commit Your Changes:

- After making changes, commit them with a clear and descriptive message:
  git commit -m "Add/Improve [feature/bug-fix]: brief description"

6. Push Your Changes:

- Push your changes to your forked repository:
  git push origin feature/your-feature-name

7. Open a Pull Request:

- Go to the original repository and open a pull request, explaining the changes you've made and why they should be merged.

## Contribution Guidelines

- Follow Python PEP 8 coding style.
- Ensure your code is well-documented.
- Write meaningful commit messages.
- Test your code before submitting.
- Be respectful and collaborative in discussions.

# License
This project is licensed under the MIT License - see the [LICENSE](License.md) file for details.

# Acknowledgments
- Special thanks to [Freecodecamp](https://www.youtube.com/watch?v=8ext9G7xspg&t=443s) for amazing tutorial that helped me guide the development of this project!
