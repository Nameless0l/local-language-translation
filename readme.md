The API for the MLPC language translation project
===

## How to start it ?

>### 1. Install dependencies
>---
>   First, you have to install project dependencies like 
>   fastapi(the framework for the API), uvicorn(as the server)
> to install dependencies you have to open the project folder in a shell/terminal and enter this command: `pip install -r requirements.txt`
>>Note that **you can use an virtual environment**, this is recommanded

>### 2. Launch the server:
> After installing dependencies, you can start the server with the following command:
> `uvicorn server:app --reload` This will launch the server on the *port: 8000*, if you want to change the port, you just have to add the flag __*--port=\<custom_port>*__

>### 3. Open the API Specification to read the documentation
>   After starting the server, you can read the API Specificatation on **`http://localhost:<port>/docs/`** in the your web browser