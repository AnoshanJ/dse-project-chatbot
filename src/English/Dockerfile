# Use the official Rasa SDK image
FROM rasa/rasa:3.5.15-full

WORKDIR /app

USER root

# Update pip and install necessary packages
RUN pip3 install --upgrade pip && \
    pip3 install spacy bs4 pymysql && \
    python -m spacy download en_core_web_md

WORKDIR /app

# Copy the necessary files from your host to the container
COPY actions /app/actions
COPY config.yml /app/config.yml
COPY domain.yml /app/domain.yml
COPY credentials.yml /app/credentials.yml
COPY endpoints.yml /app/endpoints.yml

WORKDIR /app

# Expose the port the app runs on
EXPOSE 5005
# RUN rasa train
# RUN pip install -r requirements.txt
