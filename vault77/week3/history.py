history = {
    'user1': ['google.com', 'teachbase.ru'],
    'user2': ['yandex.ru', 'teachbase.ru'],
    'user3': ['google.com', 'youtube.com', 'mail.ru'],
    'user4': ['google.com', 'stackoverflow.com', 'python.org']
}

def calculate_hits(history):
    hits = {}
    for users, urls in history.items():
        for sites in urls:
            site_counter = hits.get(sites)
            if site_counter is None:
                hits[sites] = 1
            else:
                hits[sites] = site_counter + 1
    print(hits)

calculate_hits(history)