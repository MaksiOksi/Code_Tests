from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input('PLs enter your name...')
    if first == 'q':
        break
    last = input('Pls enter your lat name...')
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"That is what we have | {formatted_name}")
