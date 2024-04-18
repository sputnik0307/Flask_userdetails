#Base Image
FROM python:3.9

#set the working directory inside the calender
WORKDIR /app

# copy requirements.txt file
COPY requirements.txt .

#install the dependencies
RUN pip install -r requirements.txt

#copy the application code into the container
COPY . .

#Expose the port the flask will be listening on
EXPOSE 5000

CMD [ "python", "app.py" ]

