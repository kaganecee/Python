myFile=open("books.txt","w")
booknames=[]
bookgenres=[]
bookprices=[]
books=[]
exit=0
while exit!= "-1":
    book=input("Enter a book name please:")
    booknames.append(book)
    genre = input("Enter a book genre please:")
    bookgenres.append(genre)
    price = input("Enter a book price please:")
    bookprices.append(str(price))
    exit = input("If you want to exit the program , input -1:")

for i in range(len(booknames)):
    record=booknames[i] + "," + bookgenres[i] + "," + bookprices[i]
    myFile.write(record)
myFile.close()
myFile=open("books.txt","r")
for line in myFile:
    books.append(line)
    print(books)