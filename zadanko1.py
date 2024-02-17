from bs4 import BeautifulSoup

def extract_book_info(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    books = []

    book_elements = soup.find_all('div', class_='book-info')

    total_price = 0
    num_books = 0

    for book_elem in book_elements:
        title = book_elem.find('h3', class_='book-title').text.strip()
        price = float(book_elem.find('div', class_='price').text.strip().replace(' zł', '').replace(',', '.'))
        
        books.append({'title': title, 'price': price})

        total_price += price
        num_books += 1

    average_price = total_price / num_books

    for book in books:
        if book['price'] > average_price:
            print(f"Tytuł: {book['title']}, Cena: {book['price']} zł")

if __name__ == "__main__":
    html_file = 'helion.html'
    extract_book_info(html_file)
