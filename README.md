# Gerador de Senhas Personalizadas

Este é um gerador de senhas personalizadas, desenvolvido em Python utilizando a biblioteca Tkinter para a interface gráfica. Este programa oferece a funcionalidade de gerar senhas seguras e personalizadas com base nos critérios definidos pelo usuário.

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/IvandeCoelho/geradorSenha/blob/main/LICENSE)

<div align="center">

[**Recursos Principais**](#recursos-principais)&nbsp; &nbsp; &nbsp; &nbsp;|&nbsp; &nbsp; &nbsp; &nbsp;[**Funcionalidades**](#funcionalidades)&nbsp; &nbsp; &nbsp; &nbsp;|&nbsp; &nbsp; &nbsp; &nbsp;[**Como Utilizar**](#como-utilizar)

</div>


## Recursos Principais

- **Personalização da Senha**: Permite ao usuário escolher o tamanho da senha e os tipos de caracteres a serem incluídos (números, letras maiúsculas, letras minúsculas e símbolos).
- **Geração de Senhas Seguras**: Utiliza um algoritmo que combina os caracteres selecionados aleatoriamente para criar senhas fortes e seguras.
- **Interface Gráfica Intuitiva**: A interface oferece opções claras e simples para selecionar os parâmetros da senha, além de exibir a senha gerada de forma clara para o usuário.

## Funcionalidades

- **Escolha do Tamanho da Senha**: O usuário pode definir o comprimento da senha por meio de uma escala deslizante (de 6 a 30 caracteres).
- **Seleção de Caracteres Específicos**: Oferece opções para incluir ou excluir números, letras maiúsculas, letras minúsculas e símbolos na senha.
- **Cópia de Senha para a Área de Transferência**: Possibilita copiar a senha gerada para a área de transferência do sistema, facilitando o uso imediato da senha em outros contextos.

## Imagem
<div align="center">
<img src="https://private-user-images.githubusercontent.com/47482589/287499948-2a4e91c7-9426-4b9b-8730-0bf313c58d69.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDE1ODQzMDgsIm5iZiI6MTcwMTU4NDAwOCwicGF0aCI6Ii80NzQ4MjU4OS8yODc0OTk5NDgtMmE0ZTkxYzctOTQyNi00YjliLTg3MzAtMGJmMzEzYzU4ZDY5LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzEyMDMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMjAzVDA2MTMyOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTIwNGM1NDBiNjE4Y2E4YmJlNTYyOTI4MDhhZDU0ZTZkZTJmYjk2ODRhZjk2YTMxNzYzNTQyZTQxNzkwM2M4YTAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.QZCkxooueNawDQ3989yPZlTbkF9LC7RsSWtauJG0x40">
<br>
![image](https://private-user-images.githubusercontent.com/47482589/287499948-2a4e91c7-9426-4b9b-8730-0bf313c58d69.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDE1ODQzMDgsIm5iZiI6MTcwMTU4NDAwOCwicGF0aCI6Ii80NzQ4MjU4OS8yODc0OTk5NDgtMmE0ZTkxYzctOTQyNi00YjliLTg3MzAtMGJmMzEzYzU4ZDY5LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzEyMDMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMjAzVDA2MTMyOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTIwNGM1NDBiNjE4Y2E4YmJlNTYyOTI4MDhhZDU0ZTZkZTJmYjk2ODRhZjk2YTMxNzYzNTQyZTQxNzkwM2M4YTAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.QZCkxooueNawDQ3989yPZlTbkF9LC7RsSWtauJG0x40)
</div>


### Como Utilizar

1. Escolha os tipos de caracteres desejados para a senha marcando as caixas correspondentes (Números, Letras Maiúsculas, Letras Minúsculas e/ou Símbolos).
2. Defina o tamanho da senha deslizando a barra de escala para o comprimento desejado.
3. Clique no botão "Gerar Senha" para criar uma senha segura.
4. Use os botões "Limpar Senha" para apagar a senha gerada na interface ou "Copiar Senha" para copiá-la para a área de transferência.

Este projeto visa fornecer uma solução prática e customizável para a criação de senhas robustas, oferecendo controle e segurança ao usuário na geração de suas senhas.
