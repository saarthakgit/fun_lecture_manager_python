# 📚 Lecture Manager

A simple command-line Python application to help you manage lecture videos — add, update, list, and delete them using a local JSON-like text file.

---

# 🚀 Features

- ✅ List all pending lectures
- ➕ Add new lectures with name and duration
- ✏️ Update lecture name or duration
- ❌ Delete completed lectures
- 💾 Stores data persistently in `lectures.txt` using JSON

---

## 🛠️ Technologies Used

- Python 3.10+
- Standard libraries: `json`

---

# 📁 File Structure

lect_manager/
│
├── lect_manager.py # Main program
├── lectures.txt # JSON data storage (auto-created)
└── .gitignore # Ignore venv, pycache, etc.

---

# 💻 How to Run

1. **Clone the repository**

   git clone https://github.com/saarthakgit/fun_lecture_manager_python.git
   cd fun_lecture_manager_python

2. **Run The App**
   python lect_manager.py

---

**SAMPLE MENU**

```


            +  Lecture Manager  +
            ||Choose an option||
    1.List pending lectures
    2.Add a new lecture
    3.Update/Change existing lecture details
    4.Delete Completed Lecture
    5.Exit


```
