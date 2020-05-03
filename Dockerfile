FROM python:latest

COPY ana.py ana.py
COPY kotus-siivottu.txt kotus-siivottu.txt
ENV TERM=xterm

CMD ./ana.py -d
