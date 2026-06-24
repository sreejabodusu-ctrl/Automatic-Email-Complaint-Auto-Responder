Before executing this project install ollama from this link

https://ollama.com/download



git clone https://github.com/codingacharya/assignment7.git

cd assignment7

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

ollama pull llama3

ollama serve

streamlit run app.py

