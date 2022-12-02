import re
from typing import Dict, List


def get_start_end_indexs(
    substring: str, string: str, find_first=False
) -> List[str | Dict[str, str]]:
    """
    Get the start and end index of a substring within a string.

    Returns:
        `indexes`: A List containing the model with its start and end index
    """
    indexes = [substring]

    if find_first:
        start_index = string.find(substring)
        end_index = start_index + len(substring)

        indexes.append({"start_index": start_index, "end_index": end_index})

    else:
        start_indexes = [m.start() for m in re.finditer(substring, string)]

        indexes = indexes + [
            {"start_index": i, "end_index": i + len(substring)}
            for i in start_indexes
        ]

    return indexes
