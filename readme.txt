para criar o banco de dados necessario utilizar o terminar com o seguinte comando:
from app import db
db.create_all()


====================================================================
Entregua da avaliação 2 já com inicio de alguns aspectos visto em aula, estão em desenvolvimento favor desconsiderar.

Considerar Apenas o que foi solicitado:

a) descreva as relações entre essas classes; (1pt)
    Print "relacaoTabelas" demonstrando que é relação 1:N de Funcionario para EngenheiroCivil ou VendedorExterno, 
    pois um Funcionario pode ser EngenheiroCivil mas tambem N EngenheiroCivil podem ser Funcionarios.

b) apresente a implementação e teste dessas classes em python com uso do framework SQLAlchemy; (2pt)
    Codigo será disponibilizado via github para verificação.

c) apresente a implementação e teste das rotas de listagem de dados das três classes, em um back-end com uso do framework flask; (2.5pts)
    Listagem de Dados realizada pelo backend enviada ao front-end para exibição em tela, conforme print "aparenciaBrowser" ou "mensagemSucesso"

d) apresente a implementação e teste das rotas de inclusão de dados das três classes, em um back-end; (2.5pts)
    Metodo de inserir funcionando conforme solicitado e emite mensagem de sucesso ao inserir.

e) faça demonstração do funcionamento dos testes (vídeo, gif animado, sequência de prints, etc) (2pts)
    sequencia de Prints disponivel dentro da pasta "SequenciaDePrints"


tabelas escolhidas:

Funcionario (nome, cpf), VendedorExterno (número da CNH), EngenheiroCivil (número do CREA);