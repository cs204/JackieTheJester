def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    s = input()
    ctext = convert(s)
    print(ctext)
main()