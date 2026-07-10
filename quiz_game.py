import customtkinter as ctk
from tkinter import messagebox
from questions import questions

# ---------------- Appearance ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ---------------- Variables ----------------
current_question = 0
score = 0
def load_question():
    """Display the current question and options."""

    progress_label.configure(
        text=f"Question {current_question + 1} of {len(questions)}"
    )

    target = (current_question + 1) / len(questions)

    current = progress.get()

    while current < target:
       current += 0.01
       progress.set(current)
       app.update()

    question = questions[current_question]

    question_label.configure(text="")

    app.update()

    question_label.after(
       120,
       lambda: question_label.configure(
          text=question["question"]
    )
)

    selected_option.set("")

    for i in range(4):
        option_buttons[i].configure(
            text=question["options"][i],
            value=question["options"][i]
        )


def next_question():
    global current_question
    global score

    # Check if an option is selected
    if selected_option.get() == "":
        messagebox.showwarning(
            "No Answer",
            "Please select an answer first."
        )
        return

    # Check answer
    if selected_option.get() == questions[current_question]["answer"]:
        score += 1
    
    score_label.configure(
    text=f"⭐ Score : {score}",
    text_color="#FACC15"
)

    # Move to next question
    current_question += 1

    if current_question < len(questions):
        load_question()

    else:
        show_result()


def previous_question():
    global current_question

    if current_question > 0:
        current_question -= 1
        load_question()


def show_result():

    # Hide Quiz Widgets
    card.pack_forget()

    # ---------------- Result Frame ----------------
    result_frame = ctk.CTkFrame(
        app,
        width=700,
        height=450,
        corner_radius=20
    )
    result_frame.pack(pady=40)

    percentage = int((score / len(questions)) * 100)

    # Performance Message
    if percentage >= 90:
        badge = "🏆 Outstanding!"
        color = "#FFD700"

    elif percentage >= 80:
        badge = "🥇 Excellent!"
        color = "#00FF7F"

    elif percentage >= 60:
        badge = "🥈 Good Job!"
        color = "#00BFFF"

    elif percentage >= 40:
        badge = "🥉 Keep Practicing!"
        color = "#FFA500"

    else:
        badge = "📚 Don't Give Up!"
        color = "#FF4C4C"

    # Title
    ctk.CTkLabel(
        result_frame,
        text="🎉 QUIZ COMPLETED",
        font=("Segoe UI",30,"bold")
    ).pack(pady=20)

    # Score
    ctk.CTkLabel(
        result_frame,
        text=f"{score} / {len(questions)}",
        font=("Segoe UI",55,"bold"),
        text_color=color
    ).pack()

    # Percentage
    ctk.CTkLabel(
        result_frame,
        text=f"{percentage}% Score",
        font=("Segoe UI",22)
    ).pack(pady=10)

    # Badge
    ctk.CTkLabel(
        result_frame,
        text=badge,
        font=("Segoe UI",24,"bold"),
        text_color=color
    ).pack(pady=15)

    # Play Again
    def restart():

        global current_question, score

        current_question = 0
        score = 0

        result_frame.destroy()

        card.pack(pady=25)

        score_label.configure(text="⭐ Score : 0")

        load_question()

    ctk.CTkButton(
        result_frame,
        text="🔄 Play Again",
        width=180,
        height=45,
        command=restart
    ).pack(pady=10)

    # Exit
    ctk.CTkButton(
        result_frame,
        text="❌ Exit",
        width=180,
        height=45,
        fg_color="red",
        hover_color="darkred",
        command=app.destroy
    ).pack(pady=10)

# ---------------- Window ----------------
app = ctk.CTk()
app.title("🧠 Smart Quiz Game Pro")
app.geometry("900x650")
app.resizable(False, False)

# ================= HEADER =================

header = ctk.CTkFrame(
    app,
    height=90,
    corner_radius=0
)
header.pack(fill="x")

title = ctk.CTkLabel(
    header,
    text="🧠 SMART QUIZ GAME PRO",
    font=("Segoe UI", 34, "bold"),
    text_color="#60A5FA"
)

title.pack(pady=(15,5))

subtitle = ctk.CTkLabel(
    header,
    text="Python • Cybersecurity • Computer Science",
    font=("Segoe UI", 15),
    text_color="#CBD5E1"
)
subtitle.pack()

# ================= MAIN CARD =================

card = ctk.CTkFrame(
    app,
    width=780,
    height=470,
    corner_radius=25,
    fg_color="#1E293B",
    border_width=2,
    border_color="#3B82F6"
)
card.pack(pady=25)

# Progress

progress_label = ctk.CTkLabel(
    card,
    text="Question 1 of 10",
    font=("Arial",18,"bold")
)
progress_label.pack(pady=(20,10))

progress = ctk.CTkProgressBar(
    card,
    width=600
)
progress.pack()
progress.set(0.1)

# Question

question_label = ctk.CTkLabel(
    card,
    text="Question will appear here...",
    wraplength=650,
    justify="left",
    font=("Arial",22,"bold")
)
question_label.pack(pady=30)

selected_option = ctk.StringVar(value="")

# Options

option_buttons = []

for i in range(4):

    btn = ctk.CTkRadioButton(
        card,
        text="",
        variable=selected_option,
        value="",
        font=("Arial",17)
    )

    btn.pack(anchor="w", padx=90, pady=10)

    option_buttons.append(btn)

# Score

score_label = ctk.CTkLabel(
    card,
    text="⭐ Score : 0",
    font=("Arial",18,"bold")
)
score_label.pack(pady=25)

# Buttons Frame

button_frame = ctk.CTkFrame(
    card,
    fg_color="transparent"
)

button_frame.pack(pady=15)

previous_button = ctk.CTkButton(
    button_frame,
    text="⬅ Previous",
    width=170,
    height=45,
    font=("Segoe UI",16,"bold"),
    fg_color="#64748B",
    hover_color="#475569",
    corner_radius=15,
    command=previous_question
)

previous_button.grid(row=0,column=0,padx=15)

next_button = ctk.CTkButton(
    button_frame,
    text="Next ➜",
    width=170,
    height=45,
    font=("Segoe UI",16,"bold"),
    fg_color="#3B82F6",
    hover_color="#2563EB",
    corner_radius=15,
    command=next_question
)
next_button.grid(row=0,column=1,padx=15)

exit_button = ctk.CTkButton(
    button_frame,
    text="Exit",
    width=150,
    height=45,
    font=("Segoe UI",16,"bold"),
    fg_color="#EF4444",
    hover_color="#DC2626",
    corner_radius=15,
    command=app.destroy
)

exit_button.grid(row=0,column=2,padx=15)

load_question()

app.mainloop()