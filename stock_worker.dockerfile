FROM python:3.6

# Update dependencies, install cron
RUN apt-get update && apt-get install -y cron

# Import stock_lib, import PyPi dependencies
WORKDIR /stock_lib
RUN python -m pip install --upgrade pip
COPY stock_lib/ .
RUN pip install -r requirements.txt  --trusted-host=pypi.org --trusted-host=pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir
RUN rm requirements.txt

# Move to root
WORKDIR /

# Add worker and runner (with permissions)
ADD stock_worker/worker.py .
ADD stock_worker/runner.py .
RUN chmod a+x runner.py worker.py

# Add cron to jobs (with permissions)
ADD stock_worker/worker_cron /etc/cron.d
RUN chmod 0644 /etc/cron.d/worker_cron

# Create log directory (supress output if already exists)
RUN mkdir /var/log/worker >> /dev/null 2>&1

# Create log file
RUN touch /var/log/worker/log.txt

# Run worker runner
CMD ["python", "/runner.py"]