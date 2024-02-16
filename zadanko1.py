from bs4 import BeautifulSoup

def extract_book_info(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    books = []

    # Znajdź wszystkie elementy reprezentujące książki
    book_elements = soup.find_all('div', class_='book-info')

    total_price = 0
    num_books = 0

    # Przejdź przez każdy element książki i wyodrębnij tytuł i cenę
    for book_elem in book_elements:
        title = book_elem.find('h3', class_='book-title').text.strip()
        price = float(book_elem.find('div', class_='price').text.strip().replace(' zł', '').replace(',', '.'))
        
        books.append({'title': title, 'price': price})

        total_price += price
        num_books += 1

    average_price = total_price / num_books

    # Wyświetl książki, których cena jest wyższa od średniej ceny
    for book in books:
        if book['price'] > average_price:
            print(f"Tytuł: {book['title']}, Cena: {book['price']} zł")

if __name__ == "__main__":
    html_file = 'helion.html'  # Zmień nazwę pliku na odpowiednią nazwę zapisanej strony HTML
    extract_book_info(html_file)
