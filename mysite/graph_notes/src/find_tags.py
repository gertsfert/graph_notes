from re import findall
from typing import List


def find_tags(content: str) -> List[str]:
    pattern = r"(?<=\[).+?(?=\])"  # matches strings enclosed in square brackets

    return findall(pattern, content)
