
import urllib.request


base = 'https://raw.githubusercontent.com/devincornell/intro_to_text_analysis/master/duke_workshop/nss/'
urls = (
    base+'trump_nss.txt',
    base+'obama_nss.txt',
)


if __name__ == '__main__':
	all_texts = [urllib.request.urlopen(url).read().decode('utf-8') for url in urls]
	print(texts)

