from app import books

def print_best_books():
    best_books = sorted(books, key = lambda x : (x.rating * -1, x.price))[:10]
    for book in best_books:
        print(book)

def print_cheapest_books():
    cheapest_books = sorted(books, key = lambda x : (x.price, x.rating *-1))[:10]
    for book in cheapest_books:
        print(book)

print('------The Best Books------')
print_best_books()
print('-----The Cheapest Books-----')
print_cheapest_books()