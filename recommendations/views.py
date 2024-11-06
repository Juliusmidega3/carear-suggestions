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
        try:
            # Retrieve user input from the form using get() to avoid KeyError
            eq_score = int(request.POST.get('eq_score', 0))  # Default to 0 if not provided
            personality_traits = {
                'openness': int(request.POST.get('openness', 0)),  # Default to 0 if not provided
                'conscientiousness': int(request.POST.get('conscientiousness', 0)),
                'extroversion': int(request.POST.get('extroversion', 0)),
                'agreeableness': int(request.POST.get('agreeableness', 0)),
                'neuroticism': int(request.POST.get('neuroticism', 0))
            }
            academic_background = request.POST.get('academic_background', '').split(',')
            interests = request.POST.get('interests', '').split(',')

            # Create user data dictionary
            user_data = {
                'eq_score': eq_score,
                'personality_traits': personality_traits,
                'academic_background': [bg.strip() for bg in academic_background if bg.strip()],
                'interests': [interest.strip() for interest in interests if interest.strip()]
            }

            # Check if all required fields are provided (simple validation)
            if all(value >= 0 for value in personality_traits.values()) and eq_score >= 0:
                # Run recommendation function
                recommendations = recommend_careers(user_data, career_data)

                # Debugging: print recommendations to console
                print("Recommendations:", recommendations)

                # Ensure recommendations is a list of dicts and round match_score
                if isinstance(recommendations, list) and all(isinstance(career, dict) for career in recommendations):
                    for career in recommendations:
                        # Ensure the career dictionary has a 'match_score' key
                        if 'match_score' in career:
                            # Round the match score to 2 decimal places before passing to the template
                            career['match_score'] = round(career['match_score'], 2)
                        else:
                            print(f"Warning: 'match_score' not found in career: {career}")

                    # Pass recommendations to results page
                    return render(request, 'results.html', {'careers': recommendations})
                else:
                    raise ValueError("Invalid recommendation format: Expected a list of dicts with 'career' and 'match_score'.")

            else:
                error_message = 'Please ensure all personality traits and EQ score are provided and valid.'
                return render(request, 'index.html', {'error': error_message})

        except ValueError as e:
            error_message = f'There was an error processing your input. Please check your entries. {str(e)}'
            return render(request, 'index.html', {'error': error_message})

    return render(request, 'index.html')
