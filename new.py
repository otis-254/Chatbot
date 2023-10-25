import tkinter as tk

# Function to handle user input
def submit():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    age = age_entry.get()
    location = location_entry.get()
    part_of_location = location_part_entry.get()
    duration_in_location = location_duration_entry.get()
    live_with = live_with_entry.get()
    student_status = student_status_var.get()
    graduation_date = graduation_date_entry.get()
    marital_status = marital_status_var.get()
    job_status = job_status_var.get()
    job_applicant = job_applicant_var.get()
    reason_to_hire = reason_to_hire_entry.get()
    expected_salary = expected_salary_entry.get()
    start_date = start_date_entry.get()
    how_heard_about = how_heard_about_entry.get()
    
    # Display collected information or perform chatbot actions
    print(f"Hello: {greet}")
    print(f"What is your first name: {first_name}")
    print(f"What is your last name: {last_name}")
    print(f"Nice to meet you, {first_name} {last_name}. How old are you? {age}")
    print(f"Pleasure to know you are {age} years old. Where do you live? {location}")
    print(f"Which part of {location}? {part_of_location}")
    print(f"For how long have you lived in {location}? {duration_in_location}")
    print(f"Who do you live with, {first_name}? {live_with}")
    if student_status == "Yes":
        print(f"Are you still a student? Yes, when are you graduating? {graduation_date}")
    else:
        print("Are you still a student? No")
        print(f"If you are not a student, when did you graduate? {graduation_date}")
    print(f"Are you married? {marital_status}")
    print(f"Do you have a job? {job_status}")
    print(f"Have you tried applying to this job before? {job_applicant}")
    print(f"Why do you think we should hire you for this role? {reason_to_hire}")
    print(f"What is your expected salary? {expected_salary}")
    print(f"When are you available to report to work? {start_date}")
    print(f"Tell us how you heard about Merit? {how_heard_about}")
    print(f"Thanks for your time, Mr. {last_name}. It was a great pleasure meeting you.")
    print(f"Goodbye, {first_name}")

# Create the main window
root = tk.Tk()
root.title("Chatbot Form")

# Create and pack a label for the greeting
greet_label = tk.Label(root, text="Hello:")
greet_label.pack()

# Create and pack an entry widget for the greeting
greet = tk.StringVar()
greet_entry = tk.Entry(root, textvariable=greet)
greet_entry.pack()

# Create and pack labels and entry widgets for the chatbot questions
# (you can extend this as needed)
first_name_label = tk.Label(root, text="What is your first name:")
first_name_label.pack()
first_name_entry = tk.Entry(root)
first_name_entry.pack()

last_name_label = tk.Label(root, text="What is your last name:")
last_name_label.pack()
last_name_entry = tk.Entry(root)
last_name_entry.pack()

age_label = tk.Label(root, text="How old are you?")
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

location_label = tk.Label(root, text="Where do you live?")
location_label.pack()
location_entry = tk.Entry(root)
location_entry.pack()

location_part_label = tk.Label(root, text=f"Which part of")
location_part_label.pack()
location_part_entry = tk.Entry(root)
location_part_entry.pack()

location_duration_label = tk.Label(root, text=f"For how long have you lived in")
location_duration_label.pack()
location_duration_entry = tk.Entry(root)
location_duration_entry.pack()

live_with_label = tk.Label(root, text="Who do you live with?")
live_with_label.pack()
live_with_entry = tk.Entry(root)
live_with_entry.pack()

student_status_label = tk.Label(root, text="Are you still a student?")
student_status_label.pack()
student_status_var = tk.StringVar()
student_status_yes = tk.Radiobutton(root, text="Yes", variable=student_status_var, value="Yes")
student_status_no = tk.Radiobutton(root, text="No", variable=student_status_var, value="No")
student_status_yes.pack()
student_status_no.pack()

graduation_date_label = tk.Label(root, text="When are you graduating?")
graduation_date_label.pack()
graduation_date_entry = tk.Entry(root)
graduation_date_entry.pack()

# (Continue adding more labels and entry widgets for the other questions)

# Create a button to submit the form
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

# Start the Tkinter main loop
root.mainloop()
