FROM pytorch/pytorch

WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgl1-mesa-glx \
    git && \
    # cleanup 
    apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rdddf /var/lib/apt/li

RUN pip install easyocr Flask
ENV FLASK_APP app.py

# CMD ["flask", "run"]
CMD ["python", "app.py"]