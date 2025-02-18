import requests
import pandas as pd
from datetime import datetime
import os

def get_random_users(num_users=10):
    '''
    Function to fetch random users from the randomuser.me API.
    
    Args:
        num_users (int): Number of random users to fetch from the API.
    
    Returns:
        list: A list of dictionaries containing processed user data.
    '''
    # Construct the API URL with the desired number of results
    url = f'https://randomuser.me/api/?results={num_users}'

    try:
        # Send a GET request to the API
        response = requests.get(url)
        # Raise an exception if the request returned an unsuccessful status code
        response.raise_for_status()
        # Parse the JSON response into a Python dictionary
        data = response.json()
        
        processed_users = []
        # Iterate over each user in the results
        for user in data['results']:
            # Process and extract relevant user information
            processed_user = {
                'first_name': user['name']['first'],  # User's first name
                'last_name': user['name']['last'],      # User's last name
                'full_name': f"{user['name']['first']} {user['name']['last']}",  # Concatenated full name
                'email': user['email'],                 # Email address
                'age': user['dob']['age'],              # Age from date of birth data
                'gender': user['gender'],               # Gender of the user
                'country': user['location']['country'], # Country of residence
                'city': user['location']['city'],       # City of residence
                'street': f"{user['location']['street']['number']} {user['location']['street']['name']}",  # Street address
                'phone': user['phone'],                 # Phone number
                'profile_picture': user['picture']['large'],  # URL to the user's profile picture
                'nationality': user['nat']              # Nationality code
            }
            # Add the processed user to the list
            processed_users.append(processed_user)

        return processed_users
    
    except requests.exceptions.RequestException as e:
        # Print an error message if the request fails
        print(f"Error fetching random users: {e}")
        return []

def main():
    # Fetch 50 random user records from the API
    user_data = get_random_users(50)

    # Convert the list of user data dictionaries to a Pandas DataFrame
    df = pd.DataFrame(user_data)

    # Display basic dataset information and statistics
    print("Dataset Info:")
    print(df.info())

    print('\nAge Statistics:')
    print(df['age'].describe())

    print('\nGender Distribution:')
    # Print the percentage distribution of genders
    print(df['gender'].value_counts(normalize=True) * 100)

    print('\nTotal Users by Country:')
    # Count and display the number of users per country
    country_counts = df['country'].value_counts()
    print(country_counts)

    # Create a directory named 'data' if it doesn't already exist
    os.makedirs('data', exist_ok=True)

    # Generate a unique filename using the current date and time
    output_filename = os.path.join('data', f'random_users_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv')
    # Export the DataFrame to a CSV file without the index column
    df.to_csv(output_filename, index=False, encoding='utf-8')
    print(f'\nDataset saved to {output_filename}')

    # Save additional statistics to a text file for reference
    with open(os.path.join('data', 'user_stats.txt'), 'w', encoding='utf-8') as f:
        f.write("Random Users Dataset Statistics\n")
        f.write("===============================\n\n")
        f.write("Age Statistics:\n")
        f.write(str(df['age'].describe()) + "\n\n")
        f.write("Gender Distribution (%):\n")
        f.write(str(df['gender'].value_counts(normalize=True) * 100) + "\n\n")
        f.write("Users by Country:\n")
        f.write(str(country_counts))

if __name__ == '__main__':
    # Execute the main function when the script is run
    main()
