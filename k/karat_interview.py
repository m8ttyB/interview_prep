"""

For this question, you are given a log file from a simple web server. Each line in the log file contains a URL and nothing else. Your job is to write code that will download the log file from the internet, process it, and output the most popular URL in the file. You do not need to normalize the URLs in the log files.


You can find the sample log files at: 

https://public.karat.io/content/q015/urls.txt
https://public.karat.io/content/q015/single_url.txt



Let's say we wanted to extract the top N URLs instead of the single top URL. Can you change your code to make N a configurable parameter?

('http://www.example.com', 1170)
('http://www.example.com/world', 482)
('http://www.example.com/us', 375)
('http://www.example.com/trends', 286)
('http://www.example.com/travel', 269)
('http://www.example.com/tech', 264)
('http://www.example.com/showbiz', 237)
('http://www.example.com/profile', 220)
('http://www.example.com/photos', 204)
('http://www.example.com/politics', 198)
('http://www.example.com/living', 169)
('http://www.example.com/justice', 164)
('http://www.example.com/opinion', 156)
('http://www.example.com/health', 156)
('http://www.example.com/feedback', 152)

"""
import requests


urls = "https://public.karat.io/content/q015/urls.txt"
single_url = "https://public.karat.io/content/q015/single_url.txt"


def count_url_instances(url_list, N):
    resp = requests.get(url_list, stream=True)
    url_dict = {}
    for url in resp.iter_lines():
        # if in dict, += 1 for the k:v 
        # if not in dict, add key and set v = 1
        if url not in url_dict:
            url_dict[url] = 1
        else:
            url_dict[url] = url_dict[url] + 1
    
    # ensure the # of urls is greater than N
    if len(url_dict) < N:
        raise ValueError("The length of url_list is less than N")
    
    # iterate over k,v. Find largest value
    greatest_key =  None
    greatest_value = 0
    for key, value in url_dict.items():
        if value > greatest_value:
            greatest_value = value
            greatest_key = key
    
    # reverse the dictionary
    reversed_url_dict = {value : key for (key, value) in url_dict.items()}
    
    # sort keys an array
    keys = list(reversed_url_dict.keys())
    keys.sort()
    
    # slice on N number of top items to return
    top_N_keys = keys[-N:]
    
    # create list of top N urls
    top_urls = []
    for key in top_N_keys:
        top_urls.append(reversed_url_dict[key])
    
    return top_urls
    

print(count_url_instances(urls, 5))
print(count_url_instances(single_url, 1))
print(count_url_instances(single_url, 2)) # should raise error