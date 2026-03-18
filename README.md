<h2>- Removedor de Fundo Online</h2>

Este projeto é uma aplicação web simples que permite ao usuário remover o fundo de imagens diretamente pelo navegador, de forma prática e automática.

A ideia foi criar uma solução leve, funcional e fácil de usar, simulando ferramentas como remove.bg — porém utilizando tecnologias acessíveis e open source.

<hr>

<h2>⚙️ Tecnologias utilizadas</h2>

- Python (backend)

- Flask (framework web)

- rembg (remoção de fundo com IA)

- Pillow (PIL) (manipulação de imagens)

- HTML + CSS + JavaScript (frontend)
  
<hr>

<h2>📌 Objetivo do projeto</h2>

- Criar uma aplicação capaz de:

- Receber uma imagem do usuário

- Processar essa imagem removendo o fundo

- Exibir o resultado visualmente

- Permitir o download da imagem final

Tudo isso com uma interface simples e intuitiva.

<hr>

<h2>⚙️ Como o projeto funciona;</h2>
<h3>1. Upload da imagem</h3>

O usuário seleciona uma imagem (PNG ou JPG) através de um formulário.

O formulário envia a imagem para o backend usando método POST.

<h3>2. Validação</h3>

Antes de qualquer processamento, o sistema verifica:

Se um arquivo foi enviado

Se o nome do arquivo não está vazio

Se o formato é válido (PNG/JPG)

Caso algo esteja errado, uma mensagem de erro é exibida na tela.
           
<h3>3. Processamento da imagem</h3>

Após validação:

A imagem é aberta com o Pillow

Caso seja muito grande, ela é redimensionada para até 800px de largura

Isso melhora desempenho e evita sobrecarga
              
<h3>4. Conversão para memória</h3>

A imagem é convertida para bytes (memória) usando BytesIO.

Isso permite trabalhar com a imagem sem precisar salvar imediatamente no disco.
           
<h3>5. Remoção de fundo</h3>

A biblioteca rembg entra em ação:
> output_data = remove(img_byte_arr) <br>

Ela utiliza inteligência artificial para identificar e remover o fundo automaticamente.

<h3>6. Salvamento das imagens</h3>

Duas versões são salvas na pasta > static/

input.png → imagem original (já redimensionada) <br>
output.png → imagem sem fundo
