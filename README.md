# Quelea: De SQLite para XML

> [!NOTE]
> Dentro deste repositório existe um arquivo XML com a versão ARA: Almeida Revista e Atualizada.

Para aqueles que utilizam softwares de projeção
em suas igrejas, principalmente o Quelea, sabem
que o formato mais aceito para as bíblias é o
XML. Entretanto, outros softwares (que possuem mais)
bíblias disponíveis em português, requerem um
banco de dados SQLite.

Sendo assi, este software lê o arquivo SQLite e
tem como saída um XML da blíblia.

## Requirements

Não possui.

## Forma de uso

Coloque o arquivo sqlite em qualquer lugar e
no ```main.py``` mude:

```python
sqlite_filename = '<seu arquivo sqlite aqui>'
xml_filename = '<seu arquivo de saída aqui>'
```

e rode o programa.

```bash
python main.py
```
