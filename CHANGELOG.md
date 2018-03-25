# CHANGELOG

## 07.03.2018 - Minor changes in API

### ADDED
--- ```GET-method``` for profile: ```.../api/users/profile/```
### REMOVED
--- ```GET-method``` for profile: ```.../api/profile/```
### CHANGED


## 09.03.2018 - changes in booking system

### CHANGED

Now user can order any book 1 time even no copies left, but librarian can accept booking only if copies available.
Also user can extend book only if no request on this book exist (copies_available == 0)

## 25.03.2018 - changes in order model

### ADDED

New type of date - data_attach when copy was attach to the order

### ADDED

model document: take_copy, return_copy