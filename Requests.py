## We want to pull the API from covid tracker to then edit and scrape 

import requests  
response = requests.get('https://covidtracking.com/api') 
  
print(response)  

print(response.request)
