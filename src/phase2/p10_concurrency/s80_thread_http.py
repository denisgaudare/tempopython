import concurrent.futures
import threading
import requests

from phase1.p15_decorateurs.decorators import timeit

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)

@timeit
def main():
    URLS = [
               "https://www.cnn.com",
               "https://www.pypy.org",
               "https://fr.wikipedia.org/wiki/Dune_(roman)",
               "https://www.allocine.fr/film/fichefilm_gen_cfilm=249.html"
           ] * 100
    download_all_sites(URLS)
    print("Fin test Thread Downloads")

main()
