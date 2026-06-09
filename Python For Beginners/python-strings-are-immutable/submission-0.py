def remove_fourth_character(word: str) -> str:
    modifier = word[:3] + word[4:]
    return modifier


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
