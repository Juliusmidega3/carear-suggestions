# Career Suggestion System

A career suggestion system powered by machine learning, designed to recommend suitable careers based on a user's personality traits, emotional intelligence (EQ), academic background, and interests. This project leverages the `pandas` library for handling career data and uses a custom recommendation algorithm to provide tailored suggestions to users.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This web application allows users to input their personality traits, emotional intelligence (EQ) score, academic background, and interests to receive personalized career recommendations. The recommendations are based on a dataset of various careers, including their required traits, relevant fields, and related interests. The system matches users to careers with the highest compatibility scores.

---

## Features

- **User Input Form**: Users can input their personality traits, EQ score, academic background, and interests through an intuitive web interface.
- **Career Recommendations**: The system provides career suggestions with a match score based on the input data.
- **User-friendly Interface**: Clean and simple design, allowing users to easily navigate and view their career suggestions.
- **Responsive Design**: Fully responsive layout that works well on mobile and desktop devices.
- **Error Handling**: If the user input is invalid or missing, appropriate error messages are displayed.

---

## Technologies Used

- **Backend**: Python, Django
- **Frontend**: HTML, CSS (Vanilla), JavaScript
- **Machine Learning/Logic**: pandas, custom recommendation algorithm
- **Template Engine**: Django Templates
- **Web Server**: Django Development Server

---

## Installation

Follow these steps to install and run the project locally:

### 1. Clone the repository

```bash
git clone https://github.com/juliusmidega3/career-suggestion-system.git
```

### 2. Navigate to the project directory

```bash
cd career-suggestion-system
```

### 3. Create a virtual environment

If you don't already have a virtual environment, create one using `venv`:

```bash
python -m venv venv
```

Activate the virtual environment:

- **Windows**:

```bash
venv\Scripts\activate
```

- **macOS/Linux**:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

The `requirements.txt` should contain the necessary libraries for the project, such as Django, pandas, etc.

### 5. Apply migrations

Run the following command to set up your database:

```bash
python manage.py migrate
```

### 6. Start the development server

Run the Django development server:

```bash
python manage.py runserver
```

The application should now be running locally at `http://127.0.0.1:8000/`.

---

## Usage

1. **Input Your Data**: Fill out the form with your personality traits, emotional intelligence score, academic background, and interests.
2. **Get Recommendations**: Click the "Get Recommendations" button, and the system will generate a list of career suggestions.
3. **View Results**: The system will display recommended careers, along with a match score indicating how well each career aligns with your profile.
4. **Refine Your Input**: If you'd like new recommendations, simply update your input data and click the button again.

---

## How It Works

1. **User Input**: The user provides their personality traits (such as openness, conscientiousness, extroversion, agreeableness, and neuroticism), EQ score, academic background, and interests.
2. **Matching Algorithm**: The system compares the user’s profile against a dataset of career information (such as required traits and related interests).
3. **Career Suggestions**: Based on the comparison, the system calculates a match score for each career. Careers with the highest scores are recommended to the user.
4. **Display Recommendations**: The results page displays the recommended careers, along with relevant fields and related interests.

### Sample Data (Career Dataset)

The career dataset includes:

- **Career Name**: The name of the career.
- **Required Traits**: Personality traits required for the career (e.g., openness, conscientiousness, etc.).
- **Relevant Fields**: Industries or fields where the career is applicable (e.g., data science, business, etc.).
- **Related Interests**: Topics or interests associated with the career (e.g., machine learning, management, etc.).

---

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit pull requests. Contributions, bug reports, feature requests, and feedback are always welcome!

Steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- The project was inspired by the need for a career recommendation system that considers personality traits and emotional intelligence.
- Thanks to the Django and pandas communities for providing excellent tools and resources.
```

### Key Sections of the README:
1. **Project Overview**: A brief introduction to the project and its purpose.
2. **Features**: A list of the key features that the project offers.
3. **Technologies Used**: A list of technologies, frameworks, and libraries used in the project.
4. **Installation Instructions**: Detailed steps on how to set up the project locally, including setting up a virtual environment, installing dependencies, and running the development server.
5. **Usage**: Instructions for using the web application once it is set up.
6. **How It Works**: A detailed explanation of the recommendation process, from user input to career suggestions.
7. **Contributing**: Instructions for contributing to the project.
8. **License**: Information about the project's license.

### Requirements file (`requirements.txt`):

You should also include a `requirements.txt` file with the necessary libraries. Here’s an example:

```txt
Django==4.2.5
pandas==2.1.0
```

