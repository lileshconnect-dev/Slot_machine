# Python Slot Machine Game 🎰

## Project Overview

This project is a simple **Slot Machine game built using Python** that
runs in the terminal (no GUI). Players start with a balance of **1000
coins**, and each spin costs **50 coins**.

The game randomly generates slot symbols and rewards the player based on
matching combinations.

------------------------------------------------------------------------

## Features

-   Terminal-based slot machine game
-   Starting balance of **1000 coins**
-   Each spin costs **50 coins**
-   Random slot symbol generation
-   Winning system:
    -   **3 matching symbols → Jackpot (300 coins)**
    -   **2 matching symbols → Small win (100 coins)**
-   Balance tracking
-   Option to quit the game anytime

------------------------------------------------------------------------

## Technologies Used

-   Python
-   `random` module

------------------------------------------------------------------------

## How the Game Works

1.  The player starts with **1000 coins**.
2.  Each roll deducts **50 coins** from the balance.
3.  The slot machine generates **3 random symbols**.
4.  The game checks for matches:
    -   **3 same symbols → Jackpot**
    -   **2 same symbols → Small win**
    -   **No match → Lose the roll**
5.  The balance updates after each spin.

------------------------------------------------------------------------

## How to Run the Program

### Step 1: Install Python

Check Python installation:

    python --version

### Step 2: Save the Program

    slot_machine.py

### Step 3: Run the Game

    python slot_machine.py

------------------------------------------------------------------------

## Example Gameplay

    🎰 Welcome to the Python Slot Machine 🎰
    Starting Balance: 1000

    Press ENTER to roll or type 'q' to quit

    Rolling...
    🍒 | 🍒 | 🍒

    JACKPOT! You won 300
    Balance: 1250

------------------------------------------------------------------------

## Possible Improvements

-   Add GUI using Tkinter
-   Add slot spinning animation
-   Add leaderboard system
-   Save player scores in a file

------------------------------------------------------------------------

## Author

Simple Python Slot Machine project.
