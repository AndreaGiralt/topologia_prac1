FROM python:3
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#CMD [ "python", "-u", "./your-script.py"]


#always runningº
CMD tail -f /dev/null