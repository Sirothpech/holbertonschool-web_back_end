**Readme - Pagination**

0. **Simple Helper Function**

   **Objective:**

   Implement a function called `index_range` that takes two integer arguments: `page` and `page_size`. This function should return a tuple containing a start index and an end index, representing the range of indexes for a list based on the given pagination parameters.

   - `page` and `page_size` are both 1-indexed, meaning the first page is referred to as page 1.

   **Example:**

   ```python
   res = index_range(1, 7)
   # Output: (0, 7)

   res = index_range(page=3, page_size=15)
   # Output: (30, 45)
   ```

1. **Simple Pagination**

   **Objective:**

   Create a class called `Server` for pagination of a database of popular baby names. The class should include a method called `get_page` that retrieves data from the database based on the specified page and page size.

   - `get_page` should take two integer arguments: `page` (default value 1) and `page_size` (default value 10).
   - Use `index_range` to find the appropriate range of indexes for pagination.
   - If the input arguments are out of range for the dataset, return an empty list.

   **Example:**

   ```python
   server = Server()

   server.get_page(1, 3)
   # Output: Returns the first 3 rows of data

   server.get_page(3, 2)
   # Output: Returns the 3rd and 4th rows of data

   server.get_page(3000, 100)
   # Output: Returns an empty list (out of range)
   ```

2. **Hypermedia Pagination**

   **Objective:**

   Extend the `Server` class to include a method called `get_hyper` that provides hypermedia pagination.

   - `get_hyper` should take the same arguments as `get_page` and return a dictionary with the following key-value pairs:
     - `page_size`: Length of the returned dataset page.
     - `page`: Current page number.
     - `data`: The dataset page.
     - `next_page`: Number of the next page (None if no next page).
     - `prev_page`: Number of the previous page (None if no previous page).
     - `total_pages`: Total number of pages in the dataset as an integer.

   **Example:**

   ```python
   server = Server()

   server.get_hyper(1, 2)
   # Output: Returns a dictionary with pagination information

   server.get_hyper(2, 2)
   # Output: Returns a dictionary for the next page

   server.get_hyper(100, 3)
   # Output: Returns a dictionary with pagination for page 100

   server.get_hyper(3000, 100)
   # Output: Returns a dictionary with empty data (out of range)
   ```

3. **Deletion-Resilient Hypermedia Pagination**

   **Objective:**

   Enhance the `Server` class further to support deletion-resilient hypermedia pagination.

   - Implement a method called `get_hyper_index` with two integer arguments: `index` (default None) and `page_size` (default 10).
   - The method should return a dictionary with the following key-value pairs:
     - `index`: Current start index of the returned page.
     - `next_index`: Next index to query with.
     - `page_size`: Current page size.
     - `data`: The actual page of the dataset.
   - Ensure that the method handles deleted rows between queries gracefully.

   **Example:**

   ```python
   server = Server()

   server.get_hyper_index(3, 2)
   # Output: Returns a dictionary with pagination information

   # Simulate row deletion
   del server._Server__indexed_dataset[3]

   server.get_hyper_index(3, 2)
   # Output: Returns a dictionary with adjusted data due to deletion
   ```

This README provides an overview of the tasks and objectives for the "Pagination" project. Each task involves developing functionality related to pagination and managing data within a dataset of baby names.

## Author
Christophe NGAN @Sirothpech
