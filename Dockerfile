FROM python:latest

COPY anagram_finder anagram_finder
WORKDIR /anagram_finder
ENV TERM=xterm

CMD ./ana.py -d
