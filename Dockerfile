FROM TheMafiaBot/MafiaSpamUserbot

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip -y
RUN pip3 install -U pip
RUN mkdir /MafiaBot/
WORKDIR /MafiaBot/
COPY . /MafiaBot/
RUN pip3 install -U -r requirements.txt
CMD python3 -m spambot