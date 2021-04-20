FROM sandy1709/catuserbot:alpine

#clonning repo 
RUN git clone https://github.com/devilvarun/AK-HACKER.git /root/userbot
#working directory
WORKDIR /root/userbot

# Install requirements
RUN sudo pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

# Starting Worker
CMD ["python3","-m","userbot"]
