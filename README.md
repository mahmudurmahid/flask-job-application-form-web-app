# 📝 Flask Job Application Form Web App

A lightweight and user-friendly web application built with Flask, enabling organizations to collect and manage job applications efficiently.

---

## 📖 Table of Contents

- [📝 Flask Job Application Form Web App](#-flask-job-application-form-web-app)
- [📖 Table of Contents](#-table-of-contents)
- [🧑‍💼 User Experience (UX)](#-user-experience-ux)
  - [🧾 User Stories](#-user-stories)
- [🎨 Design](#-design)
  - [🗂 Interface Structure](#-interface-structure)
  - [🌈 Color Scheme & Typography](#-color-scheme--typography)
- [🚀 Features](#-features)
  - [✅ Implemented Features](#-implemented-features)
  - [🛠️ Planned Improvements](#-planned-improvements)
- [💻 Technologies Used](#-technologies-used)
  - [🧑‍💻 Languages Used](#-languages-used)
  - [📚 Libraries Used](#-libraries-used)
- [📁 Project Files](#-project-files)
- [🛠 Installation & Usage](#-installation--usage)
  - [⚙️ How to Run](#-how-to-run)
  - [🧾 Configuration](#-configuration)
- [✅ Testing](#-testing)
  - [🧪 Test Scenarios Checklist](#-test-scenarios-checklist)
  - [🧪 Running Tests](#-running-tests)
- [🙌 Credits](#-credits)
  - [👨‍💻 Author](#-author)
  - [🧰 Tools & Technologies](#-tools--technologies)
  - [📚 Learning Resources & Documentation](#-learning-resources--documentation)

---

## 🧑‍💼 User Experience (UX)

The application is designed to streamline the job application process for both applicants and recruiters. It provides a straightforward interface for applicants to submit their information and for recruiters to manage received applications.

### 🧾 User Stories

- **As an applicant**, I want to fill out a job application form online, so that I can apply for a position conveniently.
- **As a recruiter**, I want to receive and store applicant information securely, so that I can review and manage applications effectively.
- **As a system administrator**, I want to deploy the application easily, so that it can be used in various environments.

---

## 🎨 Design

### 🗂 Interface Structure

- **Home Page**: Introduction and navigation to the application form.
- **Application Form**: Fields for personal information, contact details, resume upload, and additional questions.
- **Submission Confirmation**: Acknowledgment message upon successful form submission.

### 🌈 Color Scheme & Typography

- **Color Scheme**: Professional and clean colors, such as blue and white, to maintain a corporate look.
- **Typography**: Readable fonts like Arial or Helvetica for clarity and accessibility.

---

## 🚀 Features

### ✅ Implemented Features

- **Responsive Design**: Ensures usability across various devices.
- **Form Validation**: Checks for required fields and proper input formats.
- **Data Storage**: Saves applicant information securely in a database.
- **Email Notifications**: Sends confirmation emails to applicants and notifications to recruiters.

### 🛠️ Planned Improvements

- **Admin Dashboard**: Interface for recruiters to view and manage applications.
- **Search and Filter**: Tools to search through applications based on criteria.
- **Export Functionality**: Ability to export applicant data to CSV or PDF formats.
- **Authentication**: Secure login for recruiters to access the admin dashboard.

---

## 💻 Technologies Used

### 🧑‍💻 Languages Used

- **Python**: Backend logic and server-side operations.
- **HTML/CSS**: Structure and styling of web pages.
- **JavaScript**: Enhancements for interactivity and form validation.

### 📚 Libraries Used

- **Flask**: Web framework for handling routes and server logic.
- **Flask-WTF**: Simplifies form creation and validation.
- **Flask-Mail**: Manages email sending functionality.
- **SQLite**: Lightweight database for storing applicant data.

---

## 📁 Project Files

- `app.py`: Main application file containing routes and logic.
- `templates/`: HTML templates for rendering pages.
- `static/`: Static files like CSS and JavaScript.
- `requirements.txt`: List of Python dependencies.
- `README.md`: Documentation and instructions.

---

## 🛠 Installation & Usage

### ⚙️ How to Run

1. **Clone the repository**:

```bash
git clone https://github.com/mahmudurmahid/flask-job-application-form-web-app.git
cd flask-job-application-form-web-app
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set environment variables (if required):

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```

5. Run the application:

```bash
flask run
```

6. Access the application:
   Open your browser and navigate to http://localhost:5000.

### 🧾 Configuration

Email Settings: Configure SMTP settings in config.py for email functionality.

Database: The application uses SQLite by default; ensure the database file is accessible and has proper permissions.

---

## ✅ Testing

#### 🧪 Test Scenarios Checklist

This project includes various test cases to ensure the reliability and functionality of the application. Below is a checklist of the key features tested, the corresponding test types, and their current status.

| **Feature**               | **Test Type** | **Status** |
| ------------------------- | ------------- | ---------- |
| **Form Field Validation** | Unit          | ✅ Passed  |
| **Email Sending**         | Integration   | ✅ Passed  |
| **Database Entry**        | Integration   | ✅ Passed  |
| **Responsive Design**     | Manual (GUI)  | ✅ Passed  |
| **Error Handling**        | Unit / Manual | ✅ Passed  |

- **Form Field Validation**: Ensures that the user inputs are properly validated (e.g., required fields, email format).
- **Email Sending**: Validates that the application correctly sends emails upon form submission (e.g., confirmation emails).
- **Database Entry**: Tests if data submitted via the form is successfully stored in the SQLite database.
- **Responsive Design**: Confirms that the web app adjusts appropriately across different devices (mobile, tablet, desktop).
- **Error Handling**: Verifies that appropriate error messages are shown for invalid user input or system failures.

#### 🧪 Running Tests

To ensure your application is functioning as expected, you can run the tests on your local environment.

**Step 1: Install Testing Dependencies**  
First, install the necessary testing dependencies by running the following command:

```bash
pip install pytest
```

**Step 2: Run the Tests**
Once the dependencies are installed, execute the tests with the following command:

```bash
pytest
```

This will run all the test cases in the project, and you will receive a summary of their results.

---

### 🙌 Credits

---

#### 👨‍💻 Author

This project is developed and maintained by Mahmud Urmahid.

- **GitHub**: [@mahmudurmahid](https://github.com/mahmudurmahid)
- **Email**: [mahmudurmahid@gmail.com](mailto:mahmudurmahid@gmail.com)

#### 🧰 Tools & Technologies

This web app uses the following tools and technologies:

| **Tool/Library** | **Purpose**                        |
| ---------------- | ---------------------------------- |
| **Python**       | Core programming language          |
| **Flask**        | Web framework for building the app |
| **Flask-WTF**    | For form handling and validation   |
| **Flask-Mail**   | For email functionality            |
| **SQLite**       | Lightweight database management    |

#### 📚 Learning Resources & Documentation

The following documentation and resources were referenced during development:

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-WTF Documentation](https://flask-wtf.readthedocs.io/)
- [Flask-Mail Documentation](https://pythonhosted.org/Flask-Mail/)
