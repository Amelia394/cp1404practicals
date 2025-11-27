# Amelia Wilson
"""
CP1404 Practical 10
Wikipedia API usage with exception handling
"""

import wikipedia


def main():
    user_input = input("Enter page title: ").strip()

    while user_input != "":
        try:
            # Try to get the exact page the user requested
            page = wikipedia.page(user_input, autosuggest=False)

            print(page.title)
            print(page.summary)
            print(page.url)

        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)  # List of possible pages

        except wikipedia.exceptions.PageError:
            print(f'Page id "{user_input}" does not match any pages. Try another id!')

        # Ask again
        print()  # blank line for readability
        user_input = input("Enter page title: ").strip()

    print("Thank you.")


if __name__ == "__main__":
    main()
