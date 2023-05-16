from googlesearch import search
d = search("solulab.com", advanced=True , sleep_interval=2, num_results=10)
 

for j in d:
    print(j)