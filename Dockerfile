FROM python:3.7-alpine
WORKDIR /Users/suresh/mywork 
ENV FLASK_APP myapplication.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 8080
ENV FLASK_APP_VERSION 1.1.0
RUN pip install flask 
RUN pip install requests
CMD ["flask", "run"]
