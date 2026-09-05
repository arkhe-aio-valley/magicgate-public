# Política de Validação de Métricas

🌐 **Idioma:** [Português](METRICS_VALIDATION_POLICY.md) | [English](METRICS_VALIDATION_POLICY.en.md)

## Princípio

Somente métricas derivadas de testes efetivamente executados podem ser apresentadas como métricas validadas do MagicGate.

## Métrica validada

Uma métrica só pode ser classificada como validada quando todas as condições abaixo forem verdadeiras:

- o teste foi executado;
- o objeto medido e as condições do teste estão identificados em nível suficiente para interpretação;
- a evidência relevante foi capturada;
- o resultado pode ser rastreado até o teste executado;
- o método de comparação, quando aplicável, está definido;
- o resultado foi aprovado para divulgação pública.

## Informação quantitativa não validada

Os itens abaixo não são métricas validadas até que sejam sustentados por um teste executado:

- estimativas;
- hipóteses;
- metas;
- projeções;
- cenários modelados;
- exemplos conceituais;
- faixas esperadas;
- benchmarks teóricos;
- extrapolações.

Eles só podem ser publicados quando claramente identificados conforme seu status real.

## Métricas comparativas

Afirmações comparativas devem identificar uma baseline significativa e preservar comparabilidade suficiente entre a baseline e a execução observada.

## Evidência

A evidência pode incluir saídas de testes, timestamps, registros de execução, observações validadas, resultados de quality gates, evidências de entrega ou outros registros apropriados à afirmação.

O repositório público não precisa expor detalhes privados de implementação para validar uma métrica. Evidências públicas devem se limitar ao necessário para sustentar a afirmação sem divulgar material proprietário ou sensível.

## Revisão e correção

Se uma métrica publicada for posteriormente considerada sem suporte, enganosa, classificada incorretamente ou baseada em evidência inválida, ela deve ser corrigida, reclassificada ou retirada.
