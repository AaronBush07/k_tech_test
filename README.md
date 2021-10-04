# k_tech_test


## Backend 
Backend is created in Django. 
Navigate to backend folder and run ```python manage.py runserver``` to start the server. Server should be running on port 8000.

## Frontend
Frontend has been developed in Vue using Vue Cli to set up the folder structure. 

The frontend can be run by navigating to the frontend folder and running: 
```npm install```
then
```npm run serve```

This should start the frontend server running on port 8080. 




## Notes
The backend is an extremely simplistic implementation. You will find the implementation in colours.py and views.py. 
The way that colours.py is designed is to be easily extendable should any other colour option be implemented. The team that needs to extend it only needs to add a new class with the new properties of that colour option and add it to the array. BGRB is implemented in the backend as an example. 