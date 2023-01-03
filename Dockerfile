FROM python:3.8
RUN mkdir /diffusion
COPY . /diffusion/
WORKDIR /diffusion/
RUN pip3 install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["/bin/sh"]
CMD [ "./scripts/finetune_gen.sh" ]
