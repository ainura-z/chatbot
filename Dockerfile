FROM python:3.10
RUN apt install git
WORKDIR /bot
RUN cd /bot/
RUN git clone https://github.com/ainura-z/chatbot
RUN pip3 install -r requirements.txt
ENV BOT_TOKEN=5626960040:AAH2qlqSw54S1kfuN9RLnnWpJveNWk7MUh0
WORKDIR /bot/
CMD ["python3","-u" ,"main.py" ] 