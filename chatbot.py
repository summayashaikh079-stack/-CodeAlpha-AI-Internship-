import tkinter as tk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

faqs = {
    "What is CodeAlpha?": "CodeAlpha is a software development company offering internships.",
    "How do I apply?": "You can apply through the CodeAlpha website or LinkedIn.",
    "What is the internship duration?": "The internship duration is typically 1 month.",
    "Do I get a certificate?": "Yes, you get a certificate upon successful completion.",
    "Is the internship paid?": "The internship is unpaid but offers great learning experience.",
    "What tasks do I need to complete?": "You need to complete at least 2 out of 4 assigned tasks.",
}

questions = list(faqs.keys())
answers = list(faqs.values())

def get_response():
    user_input = entry.get()
    if not user_input:
        return
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(questions + [user_input])
    similarity = cosine_similarity(vectors[-1], vectors[:-1])
    idx = similarity.argmax()
    response = answers[idx]
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"You: {user_input}\n")
    chat_box.insert(tk.END, f"Bot: {response}\n\n")
    chat_box.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("FAQ Chatbot - CodeAlpha")
root.geometry("500x400")

chat_box = tk.Text(root, state=tk.DISABLED, height=20)
chat_box.pack()

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

tk.Button(root, text="Send", command=get_response).pack()

root.mainloop()