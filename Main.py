import pandas as pd
import PdfToTxt
import GptTrain

data = PdfToTxt.Dataset()
data.pdf_to_text()
sample = data.docs["general_sts2013.pdf"][:1000]
qna = GptTrain.QA()

sample_questions = qna.get_questions(sample)
print(sample_questions)

sample_answers = qna.get_answers(sample, sample_questions)
print(sample_answers)

df = pd.DataFrame(columns=["dataset", "questions", "answers"])
df["dataset"] = "general_sts2013.pdf"
df["questions"] = sample_questions
df["answers"] = sample_answers
print(df)