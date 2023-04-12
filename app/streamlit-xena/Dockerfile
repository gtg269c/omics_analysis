FROM python:3.9.1-alpine3.12
EXPOSE 8501
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["streamlit", "run"]
CMD ["main.py"]
