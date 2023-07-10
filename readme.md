# Learning fastapi
This app is the result of following the fastapi [tutorial](https://fastapi.tiangolo.com/tutorial).

## Installation
Set up a installation usin python [venv](https://docs.python.org/3/library/venv.html)

```bash
python -m venv /path/to/new/virtual/environment
source <venv>/bin/activate
pip install -r requirements.txt
```

## Run it
To run it initialize the uvicorn server using the flag `--reload` to reload te server every time that the codes change

```bash
uvicorn app.main:app --reload
```

## Tutorial - User Guide
 - [x] First Steps
 - [x] Path Parameters
 - [x] Query Parameters
 - [x] Request Body
 - [x] Query Parameters and String Validations 
 - [ ] Path Parameters and Numeric Validations
 - [ ] Body - Multiple Parameters
 - [ ] Body - Fields
 - [ ] Body - Nested Models
 - [ ] Declare Request Example Data
 - [ ] Extra Data Types
 - [ ] Cookie Parameters
 - [ ] Header Parameters
 - [ ] Response Model - Return Type
 - [ ] Extra Models
 - [ ] Response Status Code
 - [ ] Form Data
 - [ ] Request Files
 - [ ] Request Forms and Files
 - [ ] Handling Errors
 - [ ] Path Operation Configuration
 - [ ] JSON Compatible Encoder
 - [ ] Body - Updates
