FROM python:3.6

WORKDIR /stock_lib

RUN python -m pip install --upgrade pip

COPY stock_lib/ .

RUN pip install -r requirements.txt  --trusted-host=pypi.org --trusted-host=pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir

RUN rm requirements.txt

WORKDIR /stock_api

COPY stock_api/ .

RUN pip install -r requirements.txt  --trusted-host=pypi.org --trusted-host=pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir

RUN rm requirements.txt

CMD ["flask", "run"]