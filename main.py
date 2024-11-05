# main.py

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Sample user data
user_data = {
    'eq_score': 75,   # Placeholder EQ score
    'personality_traits': {'openness': 85, 'conscientiousness': 70, 'extroversion': 60, 'agreeableness': 65, 'neuroticism': 50},
    'academic_background': ['Computer Science', 'Data Science'],
    'interests': ['Machine Learning', 'Psychology', 'Data Analysis']
}

# Sample career data
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

# Mock API functions
def fetch_personality_data(user_id):
    return {'openness': 85, 'conscientiousness': 70, 'extroversion': 60, 'agreeableness': 65, 'neuroticism': 50}

def fetch_eq_score(user_id):
    return 75

# Scoring Functions
def calculate_personality_match(user_traits, career_traits):
    user_vector = np.array(list(user_traits.values())).reshape(1, -1)
    career_vector = np.array(list(career_traits.values())).reshape(1, -1)
    similarity = cosine_similarity(user_vector, career_vector)
    return similarity[0][0]

def calculate_background_match(user_academics, user_interests, career_academics, career_interests):
    academic_match = len(set(user_academics).intersection(set(career_academics))) / len(user_academics)
    interest_match = len(set(user_interests).intersection(set(career_interests))) / len(user_interests)
    return (academic_match + interest_match) / 2

def calculate_career_score(user_data, career_row):
    personality_match = calculate_personality_match(user_data['personality_traits'], career_row['required_traits'])
    background_match = calculate_background_match(user_data['academic_background'], user_data['interests'], 
                                                  career_row['relevant_fields'], career_row['related_interests'])
    eq_weight, personality_weight, background_weight = 0.3, 0.4, 0.3
    total_score = (personality_weight * personality_match + 
                   background_weight * background_match + 
                   eq_weight * (user_data['eq_score'] / 100))
    return total_score

# Recommendation Calculation
def recommend_careers(user_data, career_data, top_n=3):
    career_data['match_score'] = career_data.apply(lambda row: calculate_career_score(user_data, row), axis=1)
    top_careers = career_data.nlargest(top_n, 'match_score')
    return top_careers[['career', 'match_score']]

# Display Function
def display_recommendations(recommendations):
    print("\nCareer Recommendations:")
    for index, row in recommendations.iterrows():
        print(f"{index + 1}. {row['career']} - Match Score: {row['match_score']:.2f}")

# Main Execution
if __name__ == "__main__":
    top_career_recommendations = recommend_careers(user_data, career_data)
    display_recommendations(top_career_recommendations)
