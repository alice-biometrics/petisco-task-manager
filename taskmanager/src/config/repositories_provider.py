from typing import Dict

from petisco import IRepository


def repositories_provider() -> Dict[str, IRepository]:
    return {}
