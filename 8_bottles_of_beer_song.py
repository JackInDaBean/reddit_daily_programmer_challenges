def print_beer_song():
    """ Print the song '99 Bottles of Beer' - do not allow the program to print each loop on a new line. """
    for i in range(99, 0, -1):
        if i > 2:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.", end = " ")
            print(f" Take one down and pass it around,", end = " ")
            print(f"{i - 1} bottles of beer on the wall.", end = " ")

        elif i == 2:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.", end = " ")
            print(f" Take one down and pass it around,", end = " ")
            print(f"{i - 1} bottle of beer on the wall.", end = " ")

        elif i == 0:
            print("No more bottles of beer on the wall, No more bottles of beer.", end = " ")
            print(f"Go to the store and buy some more, {i + 99} bottles of beer on the wall.")

print_beer_song()