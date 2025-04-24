# _WEB_SCRAPPING_
This Python script scrapes laptop data from an e-commerce site, extracting details such as product names, prices, descriptions, and reviews. It handles multiple pages using pagination and stores the data in lists. Finally, the script compiles the information into a Pandas DataFrame, allowing easy analysis or export to a CSV file.
Laptop Scraper
🌟 Welcome to the Laptop Scraper Project! 🌟
This is a Python-based web scraping project that fetches laptop details from a test e-commerce site. The data scraped includes the name, price, description, and reviews for each laptop. It's a simple way to collect and organize laptop information for analysis or further use.

📦 What You’ll Need
Before running the scraper, make sure you have Python installed along with the following libraries:

requests: To make HTTP requests to the site.

beautifulsoup4: To parse the HTML and extract useful data.

pandas: To store and manipulate the data in an easy-to-read table format.

"pip install requests beautifulsoup4 pandas"


📝 How the Scraper Works
Collect Data: It scrapes data from multiple pages (up to page 4 for this example).

Store Data: Each laptop’s name, price, description, and reviews are stored in neat lists.

Create DataFrame: The lists are converted into a structured Pandas DataFrame, making it easy to work with the data.

Save or Print: You can either print the data directly to the console or save it as a CSV for future use.

Example Output
Once the script runs, it will display a table like:

Name	Price	Description	Reviews
Laptop Model A	$500	Best laptop for work.	100
Laptop Model B	$600	Great laptop for gaming.	200

🖥️ How to Run the Project
Clone the repo:


git clone https://github.com/your-username/laptop-scraper.git
cd laptop-scraper

2.Install dependencies:
pip install requests beautifulsoup4 pandas

3.Run the script:
python laptop_scraper.py

The script will scrape data from the website and print it in a clean tabular format. You can also save the data as a .csv file by uncommenting a line in the code.

💡 Key Features
Scrapes data from multiple pages.

Extracts useful laptop details like name, price, and reviews.

Stores data neatly in a Pandas DataFrame.

Option to save the data as a CSV for later use.

