from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Allows all origins
    allow_credentials = True,
    allow_methods=['*'],  # Allows all methods
    allow_headers=['*'],  # Allows all headers
)

@app.get('/')
def root():
    response = {
        'greeting': 'Servus, griaß di!',    # This is a typical Bavarian greeting ;)
        'timestamp': datetime.now(),
        'how are you?': 'I am fine, thank you! How are you?',
        'what time is it?': 'It is ' + datetime.now().strftime('%H:%M:%S') + ' o\'clock.'
    }

    return response
