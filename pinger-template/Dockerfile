# start by pulling the python image
FROM ubuntu:23.10

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN apt update && apt install -y python3-pip python3-flask
RUN apt install -y iputils-ping net-tools traceroute iproute2
#RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python3" ]

CMD ["microservice.py" ]