# POC-4: Hitting ENTER on form inputs does not submit forms (BUG)

```
TAGS: frontend, live
```

For both creating lists and adding addresses to lists, hitting `ENTER`
on a form input when the form is in a "valid" state does not
successfully submit the form.

## To Reproduce

1. Go to the new list form
2. Focus the "Name" text field input
3. Type in a valid name and hit `ENTER`
4. Notice the page reloads and the list has not been created.
