import re

# SLI & TD transcripts


file = open('TD-10.txt', "r")
file1 = file.read()
file1 = file1.replace("\n\t", "")
file2 = file1.split("\n")

statements = []
for items in file2:
    if "*CHI:" in items:
        statements.append(items[6:])


def filtering(statements):
    cleaned_statements = []
    keep = ["[/]", "[//]", "[* m:+ed]"]
    for parts in statements:
        target = re.findall(r"\[.*?\]", parts)
        for eye in target:
            if eye not in keep:
                parts = parts.replace(eye, "")
        cleaned_statements.append(parts)
    # print(cleaned_statements)       # correct cleaned list

    square_less = []
    for line in cleaned_statements:
        if "<" in line:
            line = line.replace("<", "")
        if ">" in line:
            line = line.replace(">", "")
        square_less.append(line)
    # print(square_less)


    plus_and_list = []
    for token in square_less:
        # print(token)
        match1 = re.findall(r"\A\+.*?\S+", token)
        match2 = re.findall(r"\A\&.*?\S+", token)
        for occurrence in match1:
            # print(occurrence)
            if occurrence in token:
                token = token.replace(occurrence, "")
        for occurrence in match2:
            if occurrence in token:
                token = token.replace(occurrence, "")
        plus_and_list.append(token)
    # print(plus_and_list)    # list cleared of '&' and '+'

    word_bracketfree = []
    for brackets in plus_and_list:
        open_bracket = re.findall(r"\(\w+", brackets)
        closed_bracket = re.findall(r"\w+\)", brackets)
        for word in open_bracket:
            if "(" in word:
                brackets = brackets.replace("(", "")
        for word in closed_bracket:
            if ")" in word:
                brackets = brackets.replace(")", "")
        word_bracketfree.append(brackets)
    # print(word_bracketfree)

    for lines in word_bracketfree:
        print(lines)


file.close()
filtering(statements)


