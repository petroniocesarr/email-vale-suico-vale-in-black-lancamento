# Ficha técnica — V4P_7-EMKT_NOV_VALE-IN-BLACK-LANCAMENTO

E-mail de lançamento Vale in Black (Vale Suíço Resort), montado conforme o documento "E-mail lançamento Vale in Black".
Visual: o da LP https://valesuico.com.br/vale-in-black/ (preto #090909, dourado #F2C65C, marfim #FCF8F0, Red Hat Display, botões retos).
Estrutura e rodapé: template aprovado V4P_6-EMKT_NOV_NOVEMBRO-COMECA-BOMBANDO (RD Station, largura 600 px, tabelas, estilos inline).

## Arquivos
- `index.html` / `VALE-SUICO_EMAIL_VALE-IN-BLACK-LANCAMENTO.html`: HTML do disparo (os dois são iguais).
- `assets/`: imagens em 2x (~1 MB no total).
- `*_DESKTOP.png` / `*_MOBILE.png`: prévias.
- `00_RESOURCES/compose/build.py`: gera as imagens compostas a partir de `00_RESOURCES/src`.

## Antes de disparar
1. Hospedar `assets/` (GitHub Pages ou o gerenciador de arquivos do RD) e trocar os `src="assets/..."` pelas URLs absolutas.
2. Assunto e pré-cabeçalho: não vieram no briefing, então precisam ser definidos (o pré-cabeçalho atual é uma proposta).
3. O link "gerencie suas preferências" aponta para a página de descadastro do RD; trocar se houver uma central de preferências.

## Links
- Motor de reservas: https://book.omnibees.com/hotel/8164?lang=pt-BR&currencyId=16&version=4 (o mesmo do e-mail aprovado)
- WhatsApp: 11 5031-3000, com a mensagem "Olá, tenho interesse nas ofertas Vale in Black" (a mesma da LP)
- Cards, foto da Missão, hero e loft: LP Vale in Black
- UTM: utm_source=rdstation, utm_medium=email, utm_campaign=vale_in_black_lancamento, utm_content por bloco
