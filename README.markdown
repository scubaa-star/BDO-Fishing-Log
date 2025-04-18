# BDO Fishing Profit Tracker

A Python tool to track your fishing profits in Black Desert Online (BDO). Log fishing sessions, view monthly and lifetime profits, and manage logs easily. Ideal for active and AFK fishers aiming to maximize silver earnings.

## Features

- **Log Fishing Sessions**: Record fishing location (e.g., Velia), sell location (e.g., Valencia), date, and profit.
- **View Monthly Profits**: Check total profits for a specific month.
- **Create Monthly Logs**: Start a new log for a month (e.g., April 2025).
- **Delete Monthly Logs**: Remove logs if needed (e.g., for typos).
- **View Lifetime Profit**: See your total earnings across all sessions.
- **User-Friendly**: Enter profits with commas (e.g., 1,000,000) and select months from a menu.

## Prerequisites

- **Python 3.6+**: Uses standard libraries (`json`, `os`, `calendar`, `datetime`), so no external packages are needed.
- A computer (Windows, macOS, or Linux) with Python installed.

## Installation

1. **Install Python**:

   - Download from python.org.

   - Ensure "Add Python to PATH" is checked during installation.

   - Verify with:

     ```bash
     python --version
     ```

2. **Download the Code**:

   - Click the green "Code" button on this repository and select "Download ZIP".

   - Extract to a folder (e.g., `bdo-fishing-profit-tracker`).

   - Or, with Git installed:

     ```bash
     git clone https://github.com/your-username/bdo-fishing-profit-tracker.git
     ```

## Running the Program

1. **Open a Terminal**:

   - **Windows**: Press `Win + R`, type `cmd`, press Enter.
   - **macOS**: Open `Terminal` from Applications &gt; Utilities.
   - **Linux**: Open your terminal app.

2. **Navigate to the Source Folder**:

   - Use `cd` to enter the `src` folder:

     ```bash
     cd path/to/bdo-fishing-profit-tracker/src
     ```

3. **Run the Script**:

   - Use:

     ```bash
     python fishingTotal.py
     ```

     Or:

     ```bash
     python3 fishingTotal.py
     ```

4. **Use the Program**:

   - Menu options:

     ```
     BDO Fishing Profit Tracker
     1. Log a fishing session
     2. View total profits for a month
     3. Create a new monthly log
     4. Delete a monthly log
     5. View lifetime profit
     6. Exit
     ```

   - Example: Select `3` to create "April 2025", then `1` to log a session with fishing location (`Velia`), sell location (`Valencia`), day (`18`), and profit (`1,000,000`).

## Data Storage

- Logs are saved in `fishing_logs.json` in the root directory (`bdo-fishing-profit-tracker/`, not `src/`).

- Example:

  ```json
  {
      "April 2025": [
          {
              "date": "2025-04-18",
              "fishing_location": "Velia",
              "sell_location": "Valencia",
              "profit": 1000000
          }
      ]
  }
  ```

- Ensure write permissions in the root directory. Don’t delete `fishing_logs.json` unless resetting logs.

## Troubleshooting

- **Python not found**: Verify installation and PATH setup.
- **File not found**: Ensure you’re in the `src` folder with `fishingTotal.py`.
- **Permission issues**: Run in a non-system folder (e.g., Desktop) and check write permissions for the root directory.
- **Input errors**: Use numbers for day (e.g., `18`), commas for profit (e.g., `1,000,000`).

## Contributing

- Report bugs or suggest features via GitHub issues.
- Propose enhancements (e.g., trade distance bonuses) via pull requests.
- Share feedback on `r/blackdesertonline` or BDO forums.

## License

MIT License. See `LICENSE` file.

## Contact

- Created by \[Your Name/Username\].
- Contact via GitHub issues or BDO community platforms.

Enjoy tracking your fishing profits!