# comunidade_ads
 site com python

 # Aplicativo Web da Comunidade ADS

Este é um aplicativo web desenvolvido em Flask que permite aos usuários fazer login, criar postagens, editar seus perfis e interagir com outras funcionalidades da comunidade.

## Funcionalidades

- **Autenticação de Usuário**:
  - Os usuários podem fazer login e criar contas.
  - As senhas são armazenadas de forma segura com hash.
  - A autenticação é feita com a extensão Flask-Login.

- **Gerenciamento de Perfil**:
  - Os usuários podem editar seus perfis, incluindo foto de perfil.
  - As imagens de perfil são redimensionadas e armazenadas no servidor.
  - Os cursos são gerenciados e atualizados no perfil.

- **Criação e Edição de Postagens**:
  - Os usuários podem criar postagens e editá-las.
  - Os autores podem atualizar títulos e conteúdo de postagens.

- **Listagem de Usuários e Postagens**:
  - Os usuários podem ver uma lista de outros usuários e suas postagens.
  - Os posts são exibidos na página inicial em ordem decrescente.

## Uso

1. **Execução**:
   - Certifique-se de ter o Flask instalado em seu ambiente Python.
   - Execute o aplicativo:
     ```bash
     python seu_app.py
     ```

2. **Navegação**:
   - Abra um navegador e acesse `http://localhost:5000/` para começar a usar o aplicativo.

## Notas

- Este é um exemplo de aplicativo Flask e pode ser expandido e personalizado para atender às suas necessidades.
- Certifique-se de ajustar as configurações do aplicativo, como a configuração de armazenamento de imagens, em seu ambiente de produção.
- Este script não lida com persistência de dados em um banco de dados real.



