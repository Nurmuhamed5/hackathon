from urls import url_pattern

def main():
    url, arg = input("Please select url: create/ listing/ retrieve/ delete/ update/ :\n").split("/")
    print(url, arg)
    try:
        view = url_pattern[url]
        if arg:
            view(arg)
        else:
            view()
    except KeyError:
        print("Invalid url.")


if __name__ == "__main__":
    main()
