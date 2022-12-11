FROM python:3.10

COPY . .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# expore the required port
EXPOSE 5005

# gunicorn
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "run:app"]
