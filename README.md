# micro_brocker_server

This is a microservice broker built using the FastAPI framework. The broker provides a lightweight, high-performance solution for managing and routing requests between microservices.

### Environment Setup

To set up the environment for this project, follow the steps below:

    1. Install Python 3.x and pip.
    2. Create a virtual environment for the project using virtualenv or venv. You can create a virtual environment named "env" using the following command:

```python -m venv env```

    3. Activate the virtual environment. On macOS and Linux, run the following command:
    
```source env/bin/activate```

### Installation

To get started, clone this repository to your local machine and navigate to the project directory. Then, run the following command to install all the necessary dependencies:

```pip install -r requirements.txt```

### Usage

To start the microservice broker, run the following command:

``` uvicorn main:app --reload --port 8088 ```