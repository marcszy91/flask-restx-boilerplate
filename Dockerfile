FROM python:3.9.10-slim-buster

# update and install packages
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# upgrade pip if nessessary
RUN python -m pip install --upgrade pip

# copy sources 
COPY . /app

# use /app als working directory
WORKDIR /app

# install requirements
RUN pip install -r requirements.txt

# set flask app env
ENV FLASK_APP run

# set entry point for the application
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0" ]