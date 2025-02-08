import requests
from bs4 import BeautifulSoup
import pandas as pd

# Criar uma sessão para reutilizar conexões e melhorar o desempenho
session = requests.Session()

# Função para obter o número total de páginas em uma categoria
def get_total_pages(category_url):
    response = session.get(category_url)
    response.encoding = "utf-8"
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        pager = soup.find("ul", class_="pager")
        
        if pager:
            last_page = pager.find("li", class_="current")
            if last_page:
                return int(last_page.text.strip().split()[-1])
    
    return 1  # Se não houver paginação, retorna 1

# Função para extrair dados de livros de uma página
def scrape_books(page_url):
    book_list = []
    try:
        response = session.get(page_url)
        response.encoding = "utf-8"
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            books = soup.find_all("article", class_="product_pod")
            
            for book in books:
                title = book.h3.a.attrs["title"]
                price_text = book.find("p", class_="price_color").text
                price = float(price_text.replace("£", "").strip())  # Convertendo para float
                rating = book.p.attrs["class"][1]
                book_list.append([title, price, rating])
    
    except Exception as e:
        print(f"Erro ao acessar a página {page_url}: {e}")
    
    return book_list

# Função para extrair dados de livros com categorias
def scrape_books_with_category(base_url):
    book_list = []
    try:
        response = session.get(base_url)
        response.encoding = "utf-8"
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            categories = soup.find("ul", class_="nav nav-list").find_all("a")[1:]  # Ignorar "Books"
            
            for category in categories:
                category_name = category.text.strip()
                category_url = base_url + "/" + category['href']
                total_pages = get_total_pages(category_url)

                for page in range(1, total_pages + 1):
                    page_url = category_url.replace("index.html", f"page-{page}.html")
                    books = scrape_books(page_url)
                    
                    for book in books:
                        book_list.append([book[0], book[1], book[2], category_name])
    
    except Exception as e:
        print(f"Erro ao processar categorias: {e}")
    
    return book_list

# URL base
domain = "https://books.toscrape.com"
books_data = scrape_books_with_category(domain)

# Criar um DataFrame
df = pd.DataFrame(books_data, columns=["Título", "Preço (£)", "Classificação", "Categoria"])

# Salvar os dados em um arquivo CSV
df.to_csv("books_with_categories.csv", index=False, encoding="utf-8")
print("✅ Dados extraídos com sucesso!")
