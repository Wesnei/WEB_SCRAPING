
# Web Scraper for Books Data 📚

This Python script scrapes book information from the website Books to Scrape. It collects details such as the title, price, rating, and category of books. The extracted data is saved to a CSV file.

## Requirements

To run this scraper, you need to have the following libraries installed:

- `requests`
- `beautifulsoup4`
- `pandas`

You can install them using pip:

```bash
pip install requests beautifulsoup4 pandas
```

## Usage

### 1. Clone or download this repository.
If you're working on your local machine, you can simply clone the repository (or use the code directly):

```bash
git clone https://github.com/Wesnei/WEB_SCRAPING.git
cd WEB_SCRAPING
```

### 2. Run the script

After ensuring the required libraries are installed, run the Python script:

```bash
python books_scraper.py
```

This will:
- Scrape data from the website.
- Gather book details like **Title**, **Price**, **Rating**, and **Category**.
- Save the data to a CSV file named `books_with_categories.csv`.

### 3. CSV Output

Once the script has finished running, a CSV file will be generated with the following columns:
- **Título**: The book title
- **Preço (£)**: The price of the book (in GBP)
- **Classificação**: The book's rating
- **Categoria**: The category of the book

The output will look something like this:

| Título              | Preço (£) | Classificação | Categoria   |
|---------------------|-----------|---------------|-------------|
| A Light in the Attic | 51.77     | ****          | Poetry      |
| Tipping the Velvet   | 53.74     | *****         | Romance     |
| ...                 | ...       | ...           | ...         |

### 4. How It Works

1. **get_total_pages()**: This function checks how many pages exist in a given category.
2. **scrape_books()**: This function scrapes book details (title, price, and rating) from a given page.
3. **scrape_books_with_category()**: This function collects data from all categories, iterating through pages and scraping books.


## Acknowledgments

- Thanks to [Books to Scrape](https://books.toscrape.com) for providing a freely accessible site for practice. 🙏

