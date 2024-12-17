# Automated Twitter/X Tweet/Post Scraper

This Python script automates the process of logging into Twitter (now known as X), searching for tweets based on specific hashtags or keywords, and saving the collected tweets into an Excel file.

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

---
## Features

- Automatically logs into Twitter using credentials stored in environment variables.
- Searches for tweets based on specified hashtags or keywords.
- Scrolls through the search results to load more tweets.
- Collects and saves unique tweet texts into an Excel file.
- Handles pop-ups and notifications during the login process.
---
## Requirements

- Python 3.x
- Selenium
- Pandas
- Openpyxl
- Python-dotenv
---
## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/olusegunajibola/x-scraping.git
   cd twitter-tweet-scraper
   ```
2. Install the required Python packages:
    ```python
    pip install selenium pandas openpyxl python-dotenv
    ```
    OR

    use the `scrape_env.yaml` file by:
    ```python
    conda env create -f scrape_env.yaml
    ```
3. Ensure you have the Chrome WebDriver installed and added to your system PATH. You can download it from [here](https://sites.google.com/a/chromium.org/chromedriver/).
---
## Usage

1. Create a `.env` file in the root directory of the project and add your Twitter credentials:
    ````text
   x_username=your_twitter_username
    password=your_twitter_password
   ````
   
2. Run the script:
    ````python
    python scrap_X.py
   ````
3. The script will log into Twitter, search for tweets based on the specified hashtags or keywords, and save the collected tweets into an Excel file in the `Data/Testv1` directory.

---

## Configuration

- **Hashtags/Keywords**: Modify the hashtags_keywords list in the script to include the hashtags or keywords you want to search for.  
- **Language Filter**: Modify the language variable to filter tweets by language (e.g., " lang:en" for English).  
- **Excel File Path**: Modify the file path in the save_to_excel function call to change where the Excel file is saved.  

---
## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

---
## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---
## Acknowledgments

- Inspired by the need to automate tweet collection for analysis since the free X API is no longer available.
- Built using Selenium for web automation and Pandas for data manipulation.