# Política de Paridade de Idiomas da Documentação

🌐 **Idioma:** [Português](DOCUMENTATION_LANGUAGE_POLICY.md) | [English](DOCUMENTATION_LANGUAGE_POLICY.en.md)

## Princípio

A documentação pública do MagicGate trata **PT-BR e inglês como idiomas de primeira classe**.

Nenhum documento Markdown público deve existir em apenas um dos idiomas.

> **Sem paridade de idioma, sem publicação.**

## Convenção de arquivos

- `ARQUIVO.md` é a versão PT-BR.
- `ARQUIVO.en.md` é a versão em inglês.
- Ambos devem conter um seletor de idioma no topo apontando para o respectivo par.

Exemplo:

`README.md` ↔ `README.en.md`

## Paridade semântica

As versões PT-BR e EN devem preservar o mesmo significado material, incluindo:

- versão do produto;
- preço e moeda;
- duração do trial;
- capacidades concluídas;
- funcionalidades em evolução;
- métricas e classificação de evidências;
- status de roadmap;
- regras de segurança e divulgação;
- limites entre conteúdo público e privado.

A versão inglesa deve usar inglês técnico natural, e não tradução mecânica palavra por palavra.

## Regra comercial atual

Enquanto não houver decisão comercial posterior aprovada, a documentação deve manter:

- **10 dias grátis** / **10 days free**;
- **US$ 19/mês** / **US$ 19/month**.

Qualquer alteração comercial deve atualizar ambos os idiomas no mesmo pull request.

## Regra de mudança

Quando um documento for criado, alterado, corrigido ou removido:

1. seu par de idioma deve ser criado, alterado, corrigido ou removido no mesmo pull request;
2. os dois documentos devem preservar equivalência material;
3. nenhuma versão pode divulgar informação restrita que a outra não esteja autorizada a divulgar;
4. terminologia técnica deve permanecer consistente;
5. divergência relevante bloqueia publicação até correção.

## Terminologia

Termos técnicos que já funcionam como nomes de produto, conceitos de engenharia ou padrões do setor podem permanecer em inglês nas duas versões quando isso melhora precisão. Exemplos incluem:

- Control Plane;
- Device ID;
- API Key;
- fail-closed;
- quality gates;
- first-pass success;
- MGPI;
- VS Code Control Center.

## Segurança

A existência de uma tradução nunca amplia a autorização de divulgação.

Se houver dúvida sobre se determinado detalhe pode ser publicado, aplica-se o padrão fail-closed: o conteúdo permanece não publicado até revisão.

## Automação

O CI do repositório verifica estruturalmente que cada arquivo Markdown possui seu par PT-BR/EN e que os dois documentos apresentam links de navegação de idioma.

A equivalência semântica continua exigindo revisão humana.
