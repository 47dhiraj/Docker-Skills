# Dockerfile ko line of instructions ko help batw image build garincha

# yesari specific version of python image lai docker hub batw download garincha
FROM python:3        

ENV PYTHONUNBUFFERED=1

# container ko working directory
WORKDIR /usr/src/app     

# requirements.txt lai copy garera container ko root directory ma lagera haleko ho           
COPY requirements.txt ./

# yo tala ko run command chai image build hudai garda execute huncha
RUN pip install -r requirements.txt
