FROM python:3.6

WORKDIR /stock_lib

COPY stock_lib/ .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt  --trusted-host=pypi.org --trusted-host=pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir

WORKDIR /stock_api

COPY stock_api/ .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt  --trusted-host=pypi.org --trusted-host=pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir

CMD ["flask", "run"]