#!/usr/bin/env python3
'''this module contains a funtion tthat paginates'''
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    '''returns a tuple containing the start and end index of a given page
    params: page int, the page of interest
        page_size int, the size of each page '''
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        '''initializez server'''
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
        '''returns a page'''
        assert isinstance(page, int) and page > 0, "page: positive integer"
        assert isinstance(page_size, int) and page > 0, "positive integer"
        self.dataset()
        tup = index_range(page, page_size)
        try:
            page_ = self.__dataset[tup[0]:tup[1]]
            return page_
        except IndexError:
            return []
