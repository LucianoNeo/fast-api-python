# API REST Python criada com FASTAPI
Api criada com python e FastAPI, utiliza Uvicorn como servidor web, Pydantic para tipagem de dados e UUID para criação dos ids dos dados mockados em memória.
- Faz leitura de todas as vendas (GET)
- Gravação de novas vendas (POST)
- Atualização de vendas (PUT)
- Exclusão de vendas (DELETE)

## Instalar Dependencias

```
pip3 install fastapi
pip3 install uvicorn
```

## Comando para rodar o webserver
```
uvicorn main:app --reload
```