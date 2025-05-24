from encode.encoder import Encoder
import datetime

class Bot:
    def __init__(self,
                 data_path='data/questions.json',
                 log_path='data/history.json'):
        
        self.data_encoder = Encoder(data_path)
        self.log_encoder = Encoder(log_path)
        self.items = self.data_encoder.load()  # lista de dicts
        
        self.map = { item['question']: item for item in self.items }

    def get_response(self, question):
        entry = self.map.get(question)
        if entry:
            response = entry.get('answer')
            image = entry.get('image')
        else:
            response = "No conozco la respuesta a eso aún."
            image = None

        log_entry = {
            "user_question": question,
            "bot_response": response,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.save_history(log_entry)
        return response, image

    def save_history(self, entry):
        history = self.log_encoder.load()
        if not isinstance(history, list):
            history = []
        history.append(entry)
        self.log_encoder.save(history)

    def get_all_questions(self):
        return [ item['question'] for item in self.items ]
