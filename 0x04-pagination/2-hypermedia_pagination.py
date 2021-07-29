#!/usr/bin/env python3
""" Module - pagination """
import csv
import math
from typing import List, Dict, Any

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get page from dataset
        """
        assert(isinstance(page, int))
        assert(isinstance(page_size, int))
        assert(page > 0)
        assert(page_size > 0)

        index = index_range(page, page_size)
        self.dataset()
        rtn_li = []
        for row in range(index[0], index[1]):
            try:
                rtn_li.append(self.__dataset[row])
            except IndexError:
                return []
        return rtn_li

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """ get page from dataset
        """
        assert(isinstance(page, int))
        assert(isinstance(page_size, int))
        assert(page > 0)
        assert(page_size > 0)

        g_page = self.get_page(page, page_size)
        t_pages = math.ceil(len(self.__dataset) / page_size)

        data = {}
        data["page_size"] = len(g_page)
        data["page"] = page
        data["data"] = g_page

        if len(g_page) != 0 and page != t_pages:
            data["next_page"] = page + 1
        else:
            data["next_page"] = None

        data["prev_page"] = page - 1 if page != 1 else None
        data["total_pages"] = t_pages

        return data
