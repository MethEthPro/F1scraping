
![Screenshot (358)](https://github.com/user-attachments/assets/8b6a4858-57e8-496a-a336-fa18477028df)
![individual peformance](https://github.com/user-attachments/assets/01fce150-d07b-4294-a403-e988582426d3)



# F1 Scraping

F1 Scraping is a Python project designed to scrape Formula 1 data from various online sources. This tool extracts detailed statistics, race results, driver information, and other relevant F1 data for analysis and use in various applications.I highly recommend to take a look at the csv files generated under each directory , it will give you a much more in depth grasp of what we are looking at.

YOU CAN GET ANYTHING FROM QUALIFYING TIMES OF Q1,Q2,Q3 to fastest laps of the race , the driver standings , the constructor standings , the performance of an individual team or a driver , and all of this is not limited to a single year rather to a range of years .

## Features

- **Race Results**: Scrapes race results including the finishing order, lap times, and points.
- **Driver Information**: Gathers detailed driver data such as standings, nationality, team, and race history.
- **Live Updates**: Includes functionality to fetch and display live F1 data (if supported).
- **Data Storage**: Stores scraped data in CSV or JSON format for further analysis.

## Technologies Used

- **Python**: Core programming language used.
- **BeautifulSoup**: For web scraping and parsing HTML.
- **Requests**: For handling HTTP requests.
- **Pandas**: For storing and manipulating data.
- **JSON/CSV**: For outputting and storing the scraped data.

## Installation

1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/MethEthPro/F1scraping.git
   \`\`\`
2. Navigate to the project directory:
   \`\`\`bash
   cd F1scraping
   \`\`\`
3. (Optional) Create and activate a virtual environment:
   \`\`\`bash
   python3 -m venv venv
   source venv/bin/activate  # For Windows, use \`venv\Scripts\activate\`
   \`\`\`
4. Install the dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

## Usage

1. **Set up the scraping targets**: Define the F1 data source in the configuration or target URL.
2. **Run the scraper**: Execute the main script to start scraping:
   \`\`\`bash
   python f1_scraper.py
   \`\`\`
3. **View the results**: The scraped data will be saved in the output directory in CSV or JSON format.

### Command-Line Arguments

The scraper supports the following optional arguments:
- \`--year\`: Specify the year of the season to scrape data for:
  \`\`\`bash
  python f1_scraper.py --year 2023
  \`\`\`
- \`--output\`: Choose the output format (CSV or JSON):
  \`\`\`bash
  python f1_scraper.py --output csv
  \`\`\`

For more options, run:
\`\`\`bash
python f1_scraper.py --help
\`\`\`


