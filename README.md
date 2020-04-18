# Book Management
Python Learning Project 1

Assuming that we have many books that member can read. To manage and use them effectively, the management and reviewing system is needed

The system has modules with corresponding function as below:
1. **User**:
   1. Can register for app
   2. Can signin/signout
   3. Can see the list of all books
   4. Can search books by title, category, rating, favorite
   5. Can rate and write a review for book (also can edit, delete it)
   6. Can mark a book as reading
   7. Can mark a book as read
   8. Can see reading history
   9. Can follow/unfollow other users
   10. Can see other users' favorite book list
   11. Can see the activities on the timeline on home page
   12. Can send admin a request to buy a new book (also cancel it)
   13. Can see the list of the request he/she sent
   14. Can like/unline to an activity
2.  **Admin:**
    1.  Account is made by rake task
    2.  Cannot register on browser
    3.  Can manage (CRUD) books
    4.  Can manage users
    5.  Can manage the request to buy a new book sent from  users
3.  **Book:**
    1.  Must belong to a category
    2.  Must have information at least: title, publish date, author, the number of pages, catgory
4.  **Activities:**
    1.  Follow/Unfollowed
    2.  Mark as read
    3.  Mark as favorite
    4.  Write review
    5.  Write comment
