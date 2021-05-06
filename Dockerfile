#Base Image
FROM python:3.7

#Create working directory
RUN mkdir /app
#Switch to working directory
WORKDIR /app
#Copy all files
ADD . /app

EXPOSE 5000 5000
#Install dependencies
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
#Run
CMD ["python","app.py"]