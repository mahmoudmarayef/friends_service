# Testing
Start the development server:

```
python manage.py runserver
```

Use a tool such as Postman to test the API endpoints.

### To register a new user, 
send a POST request to /api/register/ 
with a JSON payload containing username, email, and password.

### To obtain a token for a user, 
send a POST request to /api/token/ with a JSON payload containing username and password.


### To send a friend request, 
send a POST request to /api/request/ with a JSON payload containing from_user, to_user.


### To list incoming friend requests, 
send a GET request to /api/incoming-requests/.


### To list outgoing friend requests, 
send a GET request to /api/outgoing-requests/.


### To update a friend request, 
send a PUT request to /api/friendship/<int:pk>/update/ with a JSON payload containing status.


### To delete a friendship, 
send a DELETE request to /api/friendship/<int:pk>/delete/.