## Description:

FlaskStringify is a Flask-based API designed for string processing tasks. It currently provides basic functionalities for manipulating and transforming strings. However, it's designed to be extensible, allowing for the addition of more advanced functionalities based on user needs and preferences.

## Simple Python API

This repository contains a simple Python API built with Flask. The API provides endpoints for cleaning strings by removing 'NULL' values and reversing substrings.

## Structure
```

├── Python
│   └── api
│       ├── Dockerfile
│       ├── api.py
│       ├── requirements.txt
│       ├── run.sh
│       ├── simple_python
│       │   ├── __init__.py
│       │   ├── src.py
│       │   └── tests.py
│       └── tests.py
└── readme.md

```

## Usage

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Haabiy/FlaskStringify.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Python/api
   ```

3. Install dependencies using pip:

   ```bash
   pip3 install -r requirements.txt
   ```

4. Run the Flask application:

   ```bash
   python3 api.py
   ```

5. Send a POST request to the `/clean_string` endpoint with a JSON payload containing the string to clean:

   ```json
   {
       "string": "2076,3B,19C,138D,NULL,NULL"
   }
   ```

6. The API will respond with the cleaned string and reverse it:

   ```json
   {
       "cleaned_string": "138D,19C,3B,2076"
   }
   ```

## Testing

This project includes unit tests for the API endpoints. To run the tests:

```bash
python3 -m unittest
```
or 

```bash
python3 unitTest.py
```

## Docker

To run the application using Docker, execute the `run.sh` script:

```bash
./run.sh
```

This script builds the Docker image and runs a container with the Flask app.

## Structure

- `api/`: Contains the Flask application code.
- `src.py`: Contains the source code for the functions to clean strings and find missing numbers.
- `tests.py`: Contains the test code for the functions in `src.py`
- `unitTest.py`: Contains unit tests for the API endpoints.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

---