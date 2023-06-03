def remove_url_anchor(url):
    return url.split("#")[0]

if __name__ == '__main__':
    urls = ["www.rat.mil#fenduan", "egg.org#fragman", "http://www.toast.org#fenduan", "http://sausage.mil#shaziya"]
    
    for url in urls:
        print(f"{url} -> {remove_url_anchor(url)}")