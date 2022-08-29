books = input().split('&')
current_command = input()
while current_command != 'Done':
    command = current_command.split(' | ')
    if command[0] == 'Add Book':
        book = command[1]
        if book not in books:
            books.insert(0, book)
    elif command[0] == 'Take Book':
        book = command[1]
        if book in books:
            books.remove(book)
    elif command[0] == 'Swap Books':
        swap = command[1]
        swap_with = command[2]
        if swap_with in books and swap in books:
            index1 = books.index(swap)
            index2 = books.index(swap_with)
            books[index1], books[index2] = books[index2], books[index1]
    elif command[0] == 'Insert Book':
        book = command[1]
        if book not in books:
            books.append(book)
    elif command[0] == 'Check Book':
        index = int(command[1])
        if index <= len(books):
            current_book = books[index]
            print(current_book)
    current_command = input()
print(*books, sep=', ')
