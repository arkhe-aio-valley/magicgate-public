# Política mandatória de segurança para repositórios públicos

[Português](PUBLIC_REPOSITORY_SECURITY_POLICY.md) | [English](PUBLIC_REPOSITORY_SECURITY_POLICY.en.md)

## Regra permanente

Todo repositório público do ecossistema ARKHE | AIO deve conter somente artefatos deliberadamente públicos.

É proibido versionar, em qualquer branch ou histórico alcançável:

- código-fonte de produto, serviço, aplicativo, automação interna, infraestrutura ou banco de dados;
- credenciais, tokens, chaves privadas, certificados privados ou segredos;
- arquivos de ambiente e variáveis com valores sensíveis;
- dados pessoais, operacionais, financeiros, internos ou qualquer dado não destinado à divulgação pública;
- arquivos de configuração que revelem credenciais, endpoints privados, service accounts ou material de autenticação.

## Conteúdo permitido

O repositório público pode conter documentação, políticas, metadados públicos e workflows de GitHub Actions estritamente necessários para validar ou publicar artefatos públicos.

A presença de um arquivo permitido por extensão não autoriza conteúdo sensível dentro dele. Todo conteúdo continua sujeito à varredura de segredos.

## Gate obrigatório

O workflow `Public Repository Daily Guard` executa:

1. em todo pull request para `main`;
2. em todo push para `main`;
3. diariamente;
4. sob demanda.

O gate verifica a árvore atual e o histórico Git alcançável. Qualquer violação encerra o workflow com falha.

## Tratamento de incidente

Quando uma violação for detectada, a correção deve remover o material da árvore pública e, quando ele tiver existido no histórico, reescrever ou expurgar o histórico antes de considerar o incidente encerrado. Credenciais expostas devem ser revogadas e rotacionadas imediatamente. Não é permitido apenas adicionar o arquivo ao `.gitignore` e manter o segredo no histórico.

## Custo e dependências

A validação usa somente GitHub Actions, Git e Python presentes no runner, sem serviço pago obrigatório e sem depender de scanner SaaS externo.
