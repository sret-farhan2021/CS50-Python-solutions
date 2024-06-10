import re


def main():
    print(count(input("Text: ")))


def count(s):

    s= s.lower()
    pattern = r'\bum\b\s*[,.?]?'
    matches = re.findall(pattern, s)
    return len(matches)

if __name__ == "__main__":
    main()
