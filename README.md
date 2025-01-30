![banner][1]

## Requirements

- Tener instaladas las librerias (`pwntools`, `requests`)
- Todas las url deben terminar con "/"
- `-w`: Es opcional, por defecto toma "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"
- `-hc`: El status code a ocultar, por defecto 404

## Preview

```bash
Usage: python dirSleuth.py -t "target" -w "wordlist" -hc 404
```

![example][2]

- Solo nos mostrara aquellas coincidencias que sean diferentes a la respuesta 404

![eg][3]

[1]: https://github.com/user-attachments/assets/f7de8a5b-ad5e-4718-9a83-cdc0091aa14d
[2]: https://github.com/user-attachments/assets/5b7ce764-be76-4e7f-9c72-92540c3d3fc7
[3]: https://github.com/user-attachments/assets/d6aa1899-216e-4906-baae-35d40993f815
