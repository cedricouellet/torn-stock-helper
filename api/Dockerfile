# Python 3.6 runtime 
FROM python:3.6

# Expose API port
EXPOSE ${FLASK_RUN_PORT}

# Set current working directory 
WORKDIR /api

# Copy PyPip dependencies, then import
COPY ./api/requirements.txt /api
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt  --trusted-host=pypi.org --trusted-host=pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir

# Copy .env file inside container
COPY .env /api

# Copy source code inside container
COPY ./api/config.py /api
COPY ./api/app /api

# Run app on container launch
CMD ["flask", "run"]