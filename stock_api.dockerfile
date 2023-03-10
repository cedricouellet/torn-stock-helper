FROM python:3.6

# Update pip
RUN python -m pip install --upgrade pip

# Import stock_lib and related dependencies
WORKDIR /stock_lib
COPY stock_lib/ .
RUN pip install -r requirements.txt  --trusted-host=pypi.org --trusted-host=pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir
RUN rm requirements.txt

# Import stock_api and related dependencies
WORKDIR /stock_api
COPY stock_api/ .
RUN pip install -r requirements.txt  --trusted-host=pypi.org --trusted-host=pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir
RUN rm requirements.txt

# Start flask app (listen for requests)
CMD ["flask", "run"]