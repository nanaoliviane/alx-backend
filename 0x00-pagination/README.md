# 0x00. Pagination
Back-end

# Resources
Read or watch:

REST API Design: Pagination
HATEOAS
# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

How to paginate a dataset with simple page and page_size parameters
How to paginate a dataset with hypermedia metadata
How to paginate in a deletion-resilient manner

#  Simple helper function
Write a function named index_range that takes two integer arguments page and page_size.

The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.

# Simple pagination
Copy index_range from the previous task and the following class into your code

# Hypermedia pagination
Replicate code from the previous task.

Implement a get_hyper method that takes the same arguments (and defaults) as get_page and returns a dictionary containing the following key-value pairs:

page_size: the length of the returned dataset page
page: the current page number
data: the dataset page (equivalent to return from previous task)
next_page: number of the next page, None if no next page
prev_page: number of the previous page, None if no previous page
total_pages: the total number of pages in the dataset as an integer
Make sure to reuse get_page in your implementation.

You can use the math module if necessary.

# Deletion-resilient hypermedia pagination
The goal here is that if between two queries, certain rows are removed from the dataset, the user does not miss items from dataset when changing page.

Start 3-hypermedia_del_pagination.py with this code:


