# Python
# Jupyter

import os
import sys
from typing import Any, Union

import numpy as np
import pandas as pd

import example_module

# isort
# autoDocstring - Python Docstring Generator
# black autoformatter


def parse_author_params(
    authors: int,
    year: int,
    is_hsc: bool,
    title: str,
    metadata: Any,
    type_: str,
    supervisors: Union[None, str, list[str]],
) -> list[dict[str, Any]]:
    """
    Function parses informations about authors and their paper into dictionary.
    Parameters
    ----------
    authors:
        List of co-authors of paper
    year:
        Year of publication
    is_hsc:
        Whether the worker is from HSC (they are usually written with bold on the website)
    title:
        Title of paper
    metadata:
        Some metadata like Publisher or article
    type_:
        Type of document (book, thesis, paper...)
    supervisors:
        If type is thesis then it contains list of supervisors
    Returns
    -------
    result:
        List of dictionaries, where each dictionary represents author and paper details
    """
    result = [
        {
            "author": a.strip(),
            "year": year,
            "is_hsc": is_hsc,
            "title": title.strip(),
            "metadata": metadata.strip() if isinstance(metadata, str) else metadata,
            "type": type_,
            "supervisors": supervisors,
        }
        for a in authors
    ]
    return result


# Pylance - language support
# Python indent

# Better Comments

# Bracket Pair Color DLW
# Markdown Preview Enhanced
