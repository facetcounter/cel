FROM python:3.9
RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
CMD ["bash","./starter.sh"]
