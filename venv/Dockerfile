FROM python:3.12.0
COPY requirements.txt .
COPY test_txxx.py .
COPY test_pornq.py .
COPY test_upornia.py .
COPY test_100homemade.py .
COPY test_chikiporn.py .
COPY test_hclips.py .
COPY test_hdzog.py .
COPY test_hotmovs.py .
COPY test_porn555.py .
COPY test_pornforrelax.py .
COPY test_pornl.py .
COPY test_puporn.py .
COPY test_shemalez.py .
COPY test_shemaleztube.py .
COPY test_thegay.py .
COPY test_tubepornclassic.py .
COPY test_vjav.py .
COPY test_voyeurhit.py .
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir allure-results
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update && apt-get install -y google-chrome-stable
RUN apt-get install -y chromium-driver
RUN pip install chromedriver-autoinstaller
CMD ["pytest", "test_txxx.py", "test_pornq.py", "test_upornia.py", "test_100homemade.py", "test_chikiporn.py", "test_hclips.py", "test_hdzog.py", "test_hotmovs.py", "test_porn555.py", "test_pornforrelax.py", "test_pornl.py", "test_puporn.py", "test_shemalez.py", "test_shemaleztube.py", "test_thegay.py", "test_tubepornclassic.py", "test_vjav.py", "test_voyeurhit.py"]
