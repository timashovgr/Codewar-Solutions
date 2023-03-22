#For this exercise you will be strengthening your page-fu mastery. You will complete the PaginationHelper class, which is a utility class helpful for querying paging information related to an array.
#The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page. The types of values contained within the collection/array are not relevant.

import math
class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        return round(math.ceil((len(self.collection))/self.items_per_page))

    def page_item_count(self, page_index):
        if page_index > (math.ceil(float((len(self.collection))/self.items_per_page))-1) or page_index < 0:
            return -1
        if page_index < (math.ceil(float((len(self.collection))/self.items_per_page))-1):
            return self.items_per_page
        return len(self.collection) % (self.items_per_page * page_index)
        
    def page_index(self, item_index):
        if item_index > (len(self.collection)-1) or item_index < 0:
            return -1
        return item_index // self.items_per_page