#!/usr/bin/python3

# dirSleuth v1.0, Author @guguvk (Axel González)

import argparse, requests, signal
from subprocess import getoutput
from pwn import *

signal.signal(signal.SIGINT, signal.SIG_DFL)

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", help="target to analyze", required=True)
parser.add_argument("-w", "--wordlist", help="Wordlist to use", default="/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt", required=False)
parser.add_argument("-hc","--hidecode", help="Hide the status code", default=404, required=False, type=int)
args = parser.parse_args()

if args.target.endswith("/"):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0'}

    try:
        r = requests.get(args.target, headers=headers)
        print()
        if r.status_code == 200:
            try:
                file = open(args.wordlist)
                lines = getoutput(f"cat {args.wordlist} | wc -l")
                p1 = log.progress("")
                counter = 1

                for line in file:
                    word = line.strip()
                    p1.status("Probando [%s/%s]: %s" % (counter, lines, word))
                    furl = args.target + word
                    response = requests.get(furl)
                    counter += 1

                    if response.status_code != args.hidecode:
                        print(str(response.status_code) + ": " + word)

                file.close()
            except FileNotFoundError:
                print(f"Error: No se pudo encontrar el archivo del diccionario: {args.wordlist}")
            except Exception as e:
                print(f"Ocurrió un error al procesar el diccionario: {e}")
        else:
            print(f"Error: La URL no está accesible")
    except requests.RequestException as e:
        print(f"Ocurrió un error al hacer la solicitud: {e}")
else:
    print('\nHa habido algún problema, la url debe terminar con un "/"')

