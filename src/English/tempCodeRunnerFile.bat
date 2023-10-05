@echo off
start /B cmd /K "ngrok.exe http 5005"
timeout 10
start /B cmd /K "conda activate rasa && docker run -p 8000:8000 rasa/duckling"
timeout 10
start /B cmd /K "conda activate rasa && rasa run actions --port 5056"
timeout 10
start /B cmd /K "conda activate rasa && rasa run"
start https://t.me/mora_bank_en_bot