import requests
import pandas as pd
from datetime import datetime
import os

def get_random_users(num_users=10):
    '''
    Function to get random users from the randomuser.me API
    
    Args:
        num_users (int): Number of random users to fetch
    
    Returns:
        list: Processed user data
    '''
    url = f'https://randomuser.me/api/?results={num_users}'

    try:
        # Lakukan request ke API
        response = requests.get(url)
        response.raise_for_status()  # Akan mengangkat exception jika request gagal
        data = response.json()
        
        processed_users = []
        for user in data['results']:
            processed_user = {
                'first_name': user['name']['first'],
                'last_name': user['name']['last'],
                'full_name': f"{user['name']['first']} {user['name']['last']}",
                'email': user['email'],
                'age': user['dob']['age'],
                'gender': user['gender'],
                'country': user['location']['country'],
                'city': user['location']['city'],
                'street': f"{user['location']['street']['number']} {user['location']['street']['name']}",
                'phone': user['phone'],
                'profile_picture': user['picture']['large'],
                'nationality': user['nat']  # Tambahan: kode nasionalitas
            }
            processed_users.append(processed_user)

        return processed_users
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching random users: {e}")
        return []

def main():
    # Ambil 50 data pengguna acak
    user_data = get_random_users(50)

    # Konversi ke DataFrame
    df = pd.DataFrame(user_data)

    # Analisis Statistik Dasar
    print("Dataset Info:")
    print(df.info())

    print('\nAge Statistics:')
    print(df['age'].describe())

    print('\nGender Distribution:')
    print(df['gender'].value_counts(normalize=True) * 100)

    print('\nTotal Users by Country:')
    country_counts = df['country'].value_counts()
    print(country_counts)

    # Buat direktori 'data' jika belum ada
    os.makedirs('data', exist_ok=True)

    # Ekspor ke CSV dalam folder 'data'
    output_filename = os.path.join('data', f'random_users_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv')
    df.to_csv(output_filename, index=False, encoding='utf-8')
    print(f'\nDataset saved to {output_filename}')

    # Tambahan: Simpan statistik ke file teks
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
    main()