import sa

while True:
    text = input('\nसम्स्कृतम् > ')
    result, error = sa.run('<सम्स्>', text)

    if error: print(error.as_string())
    else: print(result)