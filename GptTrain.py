import openai
import pandas as pd

import Config


class QA:

    def __init__(self):
        # self.data = data
        self.apikey = Config.API_KEY
        self.df = pd.DataFrame()

    # def cut_text(self):
    #    (too long text has a problem of excessive tokens)

    def get_questions(self, context):
        openai.api_key = self.apikey
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Write questions based on the text below\n\nText: {context}\n\nQuestions:\n1.",
                temperature=0,
                max_tokens=257,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                stop=["\n\n"]
            )
            return response['choices'][0]['text']
        except:
            return ""

    def get_answers(self, context, question):
        openai.api_key = self.apikey
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Write answer based on the text below\n\nText: {context}\n\nQuestions:\n{question}\n\nAnswers:\n1.",
                temperature=0,
                max_tokens=257,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            return response['choices'][0]['text']
        except Exception as e:
            print (e)
            return ""
