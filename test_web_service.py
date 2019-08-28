import requests

dictToSend = {"experience" : "5"}

res = requests.post('http://localhost:5000/experience', json = dictToSend)

print ("Le but est de prédire le salaire en fonction de vos années d'expérience.") 
print("Si vous avez", dictToSend["experience"], "années d'expérience, vous gagnerez", res.text)