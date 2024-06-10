import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern = r'<iframe[^>]*\s+src\s*=\s*"(https?://(?:www\.)?youtube\.com/embed/[a-zA-Z0-9_-]+)"'
    match = re.search(pattern, s)
    if match:
        return "https://youtu.be/" + match.group(1).split('/')[-1]
    else:
        return None

if __name__ == "__main__":
    main()
