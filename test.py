book = {"max": 97, "Anna" : 89, "Chris" : 91, "Bob" : 85, "Raj" : 96}

total_score = 0
for score in book.values():
    total_score += score 

    average_score = total_score / len(book)
    print("Average score:", average_score)

    top_kid = None
    top_score = 0

    last_kid = None
    last_score = 0

    for kid, score in book.items():
        if score > top_score:
            top_kid="max"
            top_score=score
        if score < last_score:
                last_kid="bob"           
                last_score=score
            
print("Top kid:", top_kid, "with score", top_score)                                                                                  print("Last kid:", last_kid, "with score", last_score)
search_name = input('Enter a name to search for:')
if search_name in book:
    grade = book[search_name]
    print(f"{search_name} has a score of {grade}")