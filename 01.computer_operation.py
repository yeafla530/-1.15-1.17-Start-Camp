import webbrowser

q = ['iron man', 'batman', 'superman', 'avengers']

url = "www.google.com/search?q="

for i in q:
    site = url + i 
    webbrowser.open(site)