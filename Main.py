import Config
import PdfToTxt
import openai

obj = PdfToTxt.Dataset()
obj.pdf_to_text()

context = obj.docs["general_sts2013.pdf"][:2000]
openai.api_key = Config.API_KEY
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

print(response['choices'][0]['text'])


# df['questions']= df.context.apply(get_questions)
# df['questions'] = "1." + df.questions
# print(df[['questions']].values[0][0])