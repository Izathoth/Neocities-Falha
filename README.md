# **Pentest Request Flooder - Documentação**

Este software foi desenvolvido durante meus estudos de Python, quando a ideia de criar uma ferramenta para testar sites hospedados na NeoCities surgiu. A ferramenta simula tráfego de múltiplos usuários, enviando várias requisições para um site específico. O objetivo é aumentar a visibilidade do site na plataforma, fazendo com que ele apareça mais frequentemente nas áreas populares da NeoCities.

**Observação importante:** Eu não sou responsável pelo uso do software.

## **Como Funciona**

1. **Entrada do URL**: O URL do site a ser testado é fornecido pelo usuário.
2. **Envio de requisições**: O software envia requisições de forma automatizada, com intervalos aleatórios entre 1 e 5 segundos.
3. **Uso de fake user agents**: A biblioteca **fake-useragent** é utilizada para disfarçar a origem das requisições, simulando acessos de diferentes usuários.

## **Objetivo**

Este software não se trata de um ataque de DoS, mas sim de uma ferramenta para simular tráfego e potencialmente aumentar a visibilidade de sites nas seções populares da NeoCities.
