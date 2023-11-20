# Requisitos funcionais pendentes

- [X] Criar usuário
- [X] Atualizar usuário
- [X] Obter os dados do usuário logado
- [X] Criar notificações
- [X] Obter todas as notificações do usuário logado
- [X] Atualizar o **state** da notificação
- [X] Criar um convite
- [ ] Fazer a validação do convite, após o usuário clicar no link do email
- [ ] Implementar bloqueio nos recursos de notificações e convite - Deve ser uma rota privada
- [ ] Alterar senha fora da aplicação (forgot password) - Rota aberta      
      Passos:
      - Busca o usuário por email, se o usuário tem o seu cadastrado pela aplicação, segue os passos abaixo
      - Enviar um token para email com o prazo de expiração de 1 dia
      - Validar o prazo de expiração
      - Redirecionar para a tela de reset password caso o token esteja válido
      - Redirecionar para a tela de expired token caso o token esteja inválido
      - Remover o invite