FROM python:3.10
RUN apt install git
WORKDIR /bot
RUN cd /bot/
RUN git clone https://github.com/ainura-z/chatbot
RUN pip3 install -r /bot/chatbot/requirements.txt
ENV BOT_TOKEN=
WORKDIR /bot/chatbot/bot/

CMD ["python3","-u" ,"main.py" ] 
