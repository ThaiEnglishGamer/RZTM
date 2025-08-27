# RZTM - Recreation Zone Ticket Manager

An "over-decorated," terminal-based CLI program built in Python to manage ticket sales for a school event. It features a dynamic, scalable interface that includes real-time ticket stats and full-screen ASCII art.

![RZTM Screenshot](screenshot.png)
*(Note: You will need to take a screenshot of your program running, name it `screenshot.png`, and place it in the folder for this image to appear on GitHub.)*

---

### 🌟 About The Project

This program was created to solve the common problems of manual ticket sales: human error in calculations, slow service, and inefficient tracking of remaining tickets. RZTM provides a robust, error-free, and professional-looking solution that runs entirely within the terminal, requiring no complex setup.

### ✨ Features

- **Automated Sales Flow:** Calculates total price and change automatically, preventing errors.
- **Real-Time Dashboard:** A persistent sidebar shows tickets sold, tickets left, and the price.
- **Scalable Interface:** The layout dynamically adjusts to the size of your terminal window.
- **ASCII Art Display:** Features a beautiful, full-screen ASCII art representation of the event ticket on the main menu.
- **User-Friendly Controls:** Simple, single-key commands ([B], [M], [H], [Q]) for easy operation.
- **Zero Dependencies:** The final version has the ASCII art embedded directly, so it runs with a standard Python installation and requires no external libraries or image files.

---

### 🚀 Getting Started

To get a local copy up and running, follow these simple steps.

#### Prerequisites

- Python 3.x installed on your system.

#### Installation & Running

1.  **Clone the repository (or download the ZIP):**
    ```sh
    git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
    ```
2.  **Navigate to the project directory:**
    ```sh
    cd RZTM-Ticket-Manager 
    ```
3.  **Run the program:**
    ```sh
    python RZTM.py
    ```

---

### 📖 Usage

The program is controlled with simple keyboard commands:

-   `B` or `b`: Opens the **Buying Menu** to process a new sale.
-   `M` or `m`: Returns to the **Main Menu** to view the ticket art.
-   `H` or `h`: Displays the **Help Screen** with a manual.
-   `Q` or `q`: **Quits** the program.

For the best experience, especially for viewing the ASCII art, ensure your terminal window is wide enough (at least 170 columns).```

---

### **Part 2: The `MANUAL.txt` File**

This is a simple text file for more direct, unformatted instructions.

**Create a new file named `MANUAL.txt` in your RZTM folder and paste the following content into it:**

```text
==================================
  RZTM - PROGRAM MANUAL
==================================

INTRODUCTION
------------
RZTM (Recreation Zone Ticket Manager) is a command-line interface (CLI) program for managing event ticket sales. It is designed to be fast, reliable, and easy to use.

THE INTERFACE
-------------
The screen is divided into three main parts:
1.  HEADER: Shows the program's full name at the top.
2.  SIDEBAR (Left): Displays critical information like ticket price, tickets left, tickets sold, and a list of available controls. This is always visible.
3.  CONTENT AREA (Right): The main area where different screens are displayed.

CONTROLS
--------
All commands are single letters followed by the Enter key.

[B] - Buy Tickets
-----------------
This command initiates the sales process. The program will guide you through these steps:
1.  It will ask for the number of tickets the customer wants to purchase.
2.  It will calculate and display the total price.
3.  It will ask for the amount of money received from the customer.
4.  If the money is not enough, it will ask again.
5.  Once sufficient payment is entered, it will calculate and display the change to be given back.
6.  The number of tickets left will be updated automatically.
*NOTE: If tickets are sold out, this menu will display a "SOLD OUT" message.*

[M] - Main Menu (Art)
---------------------
This is the default screen. It displays a large ASCII art version of the event ticket.
*NOTE: Your terminal window must be wide enough (approx. 170 characters wide) to view the art correctly. If it is too narrow, a warning message will be shown instead.*

[H] - Help
----------
Displays a summary of the program's features and a list of controls, similar to this manual.

[Q] - Quit
----------
Exits the RZTM program and returns you to your terminal prompt.

TERMINAL SIZE
-------------
- The program requires a minimum terminal size to run. If it's too small, it will display a "TOO SMALL" message.
- To see the ASCII art, the terminal must be significantly wider than the minimum requirement. Please expand your window if you see the "Terminal is too narrow" message.
