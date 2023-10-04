# Localised Chatbot for Bank Customer Care

## Introduction
The Localised Chatbot for Bank Customer Care project aims to develop an intelligent and interactive chatbot system to enhance customer support services for users who communicate in the native Sri Lankan (Sinhala or Tamil) language. This innovative chatbot will serve as a virtual assistant, providing quick and efficient assistance to customers seeking information regarding various banking services, account-related queries, and general inquiries.

## Screenshots and Features

## Screenshots and Features

<img src="Screenshot 5.jpg" alt="Screenshot 5" width="250"/>
<img src="Screenshot 1.jpg" alt="Screenshot 1" width="250"/>
<img src="Screenshot 2.jpg" alt="Screenshot 2" width="250"/>
<img src="Screenshot 3.jpg" alt="Screenshot 3" width="250"/>
<img src="Screenshot 4.jpg" alt="Screenshot 4" width="250"/>

## Objectives
1. **Language Adaptability**: Build a chatbot that can seamlessly understand and respond in either Sinhala or Tamil language.
2. **Automated Customer Support**: Automate responses to frequently asked questions and routine inquiries.
3. **Personalization and Context Awareness**: Recognize returning customers and retrieve their historical data for personalized assistance.
4. **Security and Compliance**: Ensure data security and privacy, adhering to banking regulations and privacy laws.

## Expected Benefits
- Enhanced customer experience
- Increased efficiency
- Cost savings
- 24/7 availability
- Reduced workload for the staff

## Technologies Used
- **Rasa**: An open-source machine learning framework to automate text-and voice-based conversations.
- **Docker**: Used for containerizing the application components, ensuring consistent environments.
- **Ngrok**: A tool to expose local servers to the public internet, facilitating webhook integrations.
- **Python**: The primary programming language used for developing the chatbot logic and custom actions.

## How to Run

### Train:
```bash
conda activate rasa
rasa train
```

### Run:
```bash
create a credentials.yml file from the credentials.yml.example file
ngrok.exe http 5005 #starts forwarding server to telegram webhook #make sure forwarding url is same in credentials.yml
docker run -p 8000:8000 rasa/duckling #starts duckling entitity extractor
conda activate rasa
rasa run actions --port 5056 #starts action server
conda activate rasa
rasa run #starts a server with trained model # use --debug flag for traceback
chat with https://t.me/mora_bank_en_bot - English (Currently deployed)
chat with https://t.me/mora_bank_ta_bot - Tamil
chat with https://t.me/mora_bank_si_bot - Sinhala
```

### Testing:
```bash
conda activate rasa
docker run -p 8000:8000 rasa/duckling #starts duckling entitity extractor
conda activate rasa
rasa test
```

### Test http:
```bash
rasa run --enable-pi
check with postman localhost:5005/model/parse
body json {text:"hi"}
Check with Postman: localhost:5005/model/parse with body JSON {text:"hi"}
```

