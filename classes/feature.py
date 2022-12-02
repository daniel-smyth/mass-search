from typing import List
from util.get_start_end_index import get_start_end_indexs


class Feature:
    list_models: List[str]
    """The feature's models"""

    def __init__(self, list_models: List[str]):
        self.list_models = list_models

    def tag_html(self, html: str, find_all=False):
        """
        Given a HTML, locate if any of this feature's models appear in the
        HTML. Returning the model(s) with start and end index in the HTML.

        Args:
            `html`: HTML to tag
            `find_all`: If you want to get all matches (including duplicates)

        Returns:
            `tag`: A List containing the model with its start and end index
        """

        if find_all:
            matches = [model for model in self.list_models if model in html]
            tags = [get_start_end_indexs(m, html) for m in matches]

        else:
            match = next((x for x in self.list_models if x in html), False)
            tags = get_start_end_indexs(match, html, True)

        return tags
