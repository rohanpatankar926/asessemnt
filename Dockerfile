FROM python:3.8
RUN mkdir /diffusion
COPY . /diffusion/
WORKDIR /diffusion/
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD [ "app.py" ]
