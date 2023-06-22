import requests
ipv4 = requests.get('https://checkip.amazonaws.com/').text
print('Colab running on network with IPV4', ipv4)