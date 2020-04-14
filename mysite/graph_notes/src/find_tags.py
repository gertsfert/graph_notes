from re import findall
from typing import Set


def find_tags(content: str) -> Set[str]:
    pattern = r"(?<=\[).+?(?=\])"  # matches strings enclosed in square brackets

    return set(findall(pattern, content))
