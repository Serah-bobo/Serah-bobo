import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Replace with your GitHub username and token
username = 'YOUR_GITHUB_USERNAME'
token = 'YOUR_GITHUB_TOKEN'

headers = {
    'Authorization': f'token {token}',
}

# Get user data
response = requests.get(f'https://api.github.com/users/{username}', headers=headers)
user_data = response.json()

# Total contributions (example, adjust as needed)
total_contributions = user_data.get('public_repos', 0)

# Example contribution data (dummy data for illustration)
dates = [datetime.now().strftime('%Y-%m-%d')]
contributions = [total_contributions]

# Create contribution graph
plt.figure(figsize=(10, 5))
plt.plot(dates, contributions, marker='o')
plt.title('Contributions Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Contributions')
plt.grid(True)
plt.savefig('contribution_graph.png')
