# recommendations/views.py
from django.shortcuts import render
import pandas as pd
from main import recommend_careers  # Import recommendation function

# Sample career data (or load this from a database or data file)
career_data = pd.DataFrame({
    'career': ['Data Scientist', 'Psychologist', 'Software Engineer', 'Product Manager'],
    'required_traits': [
        {'openness': 80, 'conscientiousness': 75, 'extroversion': 60, 'agreeableness': 70, 'neuroticism': 40},
        {'openness': 85, 'conscientiousness': 65, 'extroversion': 50, 'agreeableness': 80, 'neuroticism': 45},
        {'openness': 60, 'conscientiousness': 80, 'extroversion': 70, 'agreeableness': 65, 'neuroticism': 50},
        {'openness': 75, 'conscientiousness': 70, 'extroversion': 75, 'agreeableness': 70, 'neuroticism': 45}
    ],
    'relevant_fields': [['Data Science', 'Computer Science'], ['Psychology'], ['Computer Science'], ['Business']],
    'related_interests': [['Machine Learning', 'Data Analysis'], ['Psychology'], ['Software Development'], ['Product Design', 'Management']]
})

def index(request):
    return render(request, 'index.html')

def get_recommendations(request):
    if request.method == 'POST':
        # Retrieve user input from the form
        eq_score = int(request.POST['eq_score'])
        personality_traits = {
            'openness': int(request.POST['openness']),
            'conscientiousness': int(request.POST['conscientiousness']),
            'extroversion': int(request.POST['extroversion']),
            'agreeableness': int(request.POST['agreeableness']),
            'neuroticism': int(request.POST['neuroticism'])
        }
        academic_background = request.POST['academic_background'].split(',')
        interests = request.POST['interests'].split(',')

        # Create user data dictionary
        user_data = {
            'eq_score': eq_score,
            'personality_traits': personality_traits,
            'academic_background': academic_background,
            'interests': interests
        }

        # Run recommendation function
        recommendations = recommend_careers(user_data, career_data)

        # Pass recommendations to results page
        return render(request, 'results.html', {'careers': recommendations})

    return render(request, 'index.html')
