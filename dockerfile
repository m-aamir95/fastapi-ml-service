FROM python:3.9-slim

# This is where our fastapi-ml-app will be copied into
WORKDIR /app 

# Installing linux dependencies, these are required for the mysql-client
# Which is used by python and sqlAlchemy to communicate with mysql database
RUN apt update
RUN apt install pkg-config libssl-dev libmariadb-dev build-essential -y

# Installing the torch seperately because 
# Pytorch does not distribute the CPU only version via PyPy
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu

# Copy the requirements.txt to the working directory which is currently set above
COPY requirements.txt .


# The commands which are triggered using 
RUN pip install -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

EXPOSE 8080 

# The actual command to start our application
CMD [ "uvicorn", "main:app" , "--host", "0.0.0.0", "--port" ,"8080" ]