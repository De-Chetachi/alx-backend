#!/usr/bin/env python3
'''this module contains a funtion tthat paginates'''


def index_range(page: int, page_size: int) -> tuple:
    '''returns a tuple containing the start and end index of a given page
    params: page int, the page of interest
        page_size int, the size of each page '''
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
