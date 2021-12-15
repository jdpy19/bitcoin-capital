# POC-1: Deleting list does not delete addresses on that list (BUG)

```
TAGS: backend, live
```


The spec demands that addresses not associated with any list should be
deleted from the database and not displayed on the address "index"
page.

When deleting an address from a list, if that address is not on any
other list, then the address is also deleted.  This is correct.

When deleting an entire list, addresses on that list which are not on
any other list persist in the database.  This is the bug.

## To Reproduce

1. Create a new list
2. Add an address to that list
3. Delete the list
4. See the address appearing with "0 lists" on the address index page
