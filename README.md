# MAGICGATE

🌐 **Idioma:** [Português](README.md) | [English](README.en.md)

**Da intenção à execução. Da execução à evidência. Da evidência à escala.**

> **Release atual: MagicGate v0.3.0**  
> **Oferta de lançamento: 10 dias grátis, depois US$ 19/mês para continuar.**  
> **Domínio oficial: `magicgate.dev`**

## Visão

MagicGate é uma plataforma de execução tecnológica orientada por planos, criada para reduzir o trabalho operacional necessário entre uma intenção de software e uma entrega validada.

Sua tese central é:

> A complexidade de um software não deveria exigir crescimento proporcional da quantidade de trabalho humano necessária para construí-lo, validá-lo e evoluí-lo.

O MagicGate busca ampliar a capacidade operacional de profissionais e equipes de engenharia por meio de execução controlada, mensuração, evidências e governança.

O profissional permanece responsável por objetivos, decisões, arquitetura, contexto, validação e julgamento humano.

---

## O problema

Construir e evoluir software complexo continua consumindo grande quantidade de atenção humana.

Entre uma ideia e uma entrega real existem atividades de planejamento, implementação, testes, diagnóstico, validação, integração, operação e evolução.

O custo de engenharia não está apenas na produção de código. Ele também está no volume de trabalho humano necessário para transformar intenção em software funcional, validado e operacional.

> O problema econômico do desenvolvimento de software não é apenas produzir código. É reduzir, com segurança, o trabalho humano necessário para produzir resultados tecnológicos verificáveis.

---

## A proposta do MagicGate

MagicGate transforma planos estruturados em fluxos operacionais controlados.

Sua proposta é reduzir progressivamente o trabalho operacional repetitivo que pode ser executado com segurança, mantendo decisões críticas e julgamento sob responsabilidade humana.

Em termos conceituais, o ciclo do produto envolve:

**definir → executar → testar → validar → registrar → medir → evoluir**

O objetivo é deslocar o profissional de executor permanente de microtarefas para supervisor e orquestrador de capacidade tecnológica.

---

## MagicGate v0.3.0

A v0.3.0 é uma release oficial promovida após os gates obrigatórios de validação no mesmo commit.

Entre as capacidades publicamente declaradas nesta linha estão:

- execução orientada por planos;
- organização determinística de tarefas;
- execução controlada e retomada de atividades;
- persistência de estado e exigência de evidências para conclusão;
- políticas de segurança e comportamento fail-closed;
- controle de custo;
- autenticação delegada;
- métricas operacionais auditáveis;
- indicadores de produtividade, autonomia, qualidade e intervenção humana;
- MGPI, MagicGate Productivity Index;
- cenários de equivalência humana explicitamente classificados como estimativas quando aplicável;
- diagnóstico de ambiente;
- validação de releases;
- CLI canônica de execuções em modo somente leitura;
- Investor Hunter embutido, com divulgação externa subordinada a controles de segurança;
- extensão privada MagicGate para VS Code com Control Center.

A descrição dessas capacidades é propositalmente funcional e conceitual. Este repositório não documenta sua implementação interna.

---

## VS Code Control Center

A linha 0.3.0 inclui uma extensão privada do MagicGate para VS Code voltada à operação do produto diretamente no ambiente de desenvolvimento.

Entre as capacidades públicas do Control Center estão:

- **Doctor** para diagnóstico do ambiente;
- **Run Plan** para iniciar planos estruturados;
- **Resume** para retomada de execução;
- **Safety** para avaliação de ações contra políticas de segurança;
- **Metrics** para leitura de indicadores operacionais;
- **Active Plans** para listar planos em execução;
- barras de progresso baseadas no estado real das tarefas;
- acompanhamento em tempo real sem estimativas cosméticas por cronômetro.

O progresso apresentado deriva do estado canônico da execução. Uma tarefa só avança o indicador quando sua mudança de estado é realmente registrada.

---

## Resultados observados em testes reais

O MagicGate utiliza execuções reais para sustentar resultados divulgados como observados ou validados.

### Validação do Control Center no macOS

Em uma execução ponta a ponta com plano determinístico de 3 tarefas, o progresso canônico observado avançou:

**33% → 66% → 100%**

Na mesma bateria de validação foram observados:

| Indicador | Resultado observado |
|---|---:|
| Taxa de sucesso | 100% |
| Autonomia | 100% |
| First-pass success | 100% |
| MGPI | 99,99 |
| Safety | cenários de allow e deny validados |

Esses números descrevem a execução específica testada. Não representam garantia universal de desempenho para qualquer workload.

### Validação operacional adicional no macOS

Em uma execução validada do ambiente Remote Link foram observados:

| Indicador | Resultado observado |
|---|---:|
| Tempo de execução | 14,90 s |
| Autonomia | 100% |
| First-pass success | 100% |
| Quality gates | 100% |
| Intervenção humana | 0 s |
| MGPI | 99,97 |

Resultados reais variam conforme complexidade, infraestrutura, requisitos, dependências, qualidade do plano e necessidade de julgamento humano.

---

## Métricas

MagicGate foi concebido para medir sua própria operação.

Entre os indicadores que podem ser observados estão:

- duração de execução;
- nível de autonomia;
- necessidade de intervenção humana;
- resultados de testes;
- quality gates;
- retries;
- evidências de entrega;
- produtividade;
- custo operacional;
- estimativas humano-equivalentes quando explicitamente identificadas como tal.

### Regra de validação

Uma métrica somente pode ser classificada publicamente como **validada** quando for derivada de um teste efetivamente executado e possuir evidência suficiente para sustentar o resultado.

**Teste executado + evidência observável = métrica validada**

Estimativas, projeções, hipóteses, metas, cenários conceituais ou referências teóricas não são métricas validadas.

---

## MagicGate Productivity Index

O **MGPI, MagicGate Productivity Index**, consolida diferentes dimensões operacionais da execução para contribuir com uma leitura consistente de produtividade, autonomia, qualidade e evidências.

Um valor de MGPI somente é apresentado como resultado observado ou validado quando seus dados de origem são provenientes de execuções reais devidamente registradas.

> Produtividade deve ser demonstrada por evidência, não apenas por percepção.

---

## Eficiência e expansão de capacidade

O MagicGate possui duas propostas econômicas complementares.

### Eficiência

Reduzir o trabalho operacional necessário para entregar determinada capacidade tecnológica.

### Expansão de capacidade

Utilizar a capacidade operacional adicional para executar mais trabalho com a mesma estrutura humana.

MagicGate representa, portanto, uma tese de eficiência operacional e alavancagem tecnológica.

---

## Oferta de lançamento

A oferta inicial do MagicGate é:

| Item | Oferta |
|---|---:|
| Período de avaliação | **10 dias grátis** |
| Assinatura após o período gratuito | **US$ 19/mês** |
| Renovação | mensal |
| Continuidade após o trial | assinatura necessária |

A proposta é permitir que o usuário avalie o MagicGate em um ambiente real antes de decidir continuar com a assinatura.

O controle de elegibilidade do período gratuito, cadastro, cobrança, painel do cliente e gestão centralizada pertencem à próxima camada comercial do produto e não são apresentados aqui como funcionalidades concluídas da v0.3.0.

---

## Domínio e suporte

O domínio oficial adquirido para o produto é:

**`magicgate.dev`**

O canal de suporte definido para a operação comercial é:

**`support@magicgate.dev`**

A infraestrutura pública do domínio, landing page, roteamento de e-mail e serviços comerciais será ativada de forma progressiva.

---

## Em evolução

Entre as áreas publicamente anunciadas em evolução estão:

- Commercial Control Plane;
- cadastro e autenticação de usuários;
- organizações e memberships;
- cobrança recorrente;
- período de avaliação de 10 dias;
- elegibilidade de trial por conta e dispositivo usando identificadores pseudonimizados;
- geração, rotação e revogação de MagicGate API Keys;
- Customer Console;
- Admin Console;
- telemetria sanitizada e métricas consolidadas;
- execução remota controlada;
- ampliação da orquestração de workloads;
- integração entre métricas, custo e segurança.

Funcionalidades classificadas como em evolução não devem ser interpretadas como funcionalidades comerciais concluídas.

---

## Segurança, privacidade e governança

O MagicGate adota como princípio público a preferência por interrupção segura quando uma execução não pode ser validada adequadamente.

Entre os princípios públicos do produto estão:

- execução controlada;
- comportamento seguro diante de ambiguidade;
- proteção contra ações destrutivas;
- confinamento ao contexto autorizado;
- bloqueio de material com aparência de segredo;
- exigência de evidência para conclusão;
- separação entre automação e decisões que exigem julgamento humano;
- divulgação pública somente após aprovação apropriada;
- minimização de dados na futura telemetria comercial;
- não coleta de código-fonte, credenciais, prompts completos ou conteúdo proprietário por padrão na camada comercial planejada.

No controle futuro de trial por dispositivo, o projeto prevê o uso de **Device ID pseudonimizado e chave criptográfica da instalação**, em vez do armazenamento de endereço MAC bruto.

> Automação sem governança não representa escala sustentável.

---

## Investor Hunter

O Investor Hunter é uma aplicação incorporada ao ecossistema MagicGate para apoiar pesquisa e priorização de potenciais investidores.

Em nível público, sua proposta é:

- pesquisar fundos, investidores-anjo, family offices e corporate VCs;
- cruzar tese, estágio, ticket e localização;
- atribuir score de compatibilidade;
- produzir listas priorizadas para análise humana.

Informações sensíveis, código, dados financeiros privados, estratégias internas e outros conteúdos classificados não são autorizados para divulgação externa pelo fluxo padrão.

---

## Roadmap público

### Fundação de execução

**Status: operacional na v0.3.0**

Execução orientada por planos, persistência, retomada, evidências, segurança, diagnóstico e validação.

### Mensuração

**Status: operacional e em expansão**

Métricas de execução, produtividade, autonomia, qualidade, tempo, intervenção humana e MGPI.

### Interface de desenvolvimento

**Status: operacional na v0.3.0**

VS Code Control Center com diagnóstico, execução, retomada, Safety, métricas e acompanhamento de planos ativos.

### Camada comercial

**Status: próxima evolução**

Cadastro, trial, assinatura, cobrança, API Keys, Customer Console, Admin Console e telemetria sanitizada.

### Orquestração e escala

**Status: evolução planejada**

Workloads mais amplos, operação remota controlada e coordenação entre execução, métricas, custo e segurança.

---

## Política de divulgação pública

Este repositório existe para disponibilizar somente informações aprovadas para divulgação.

Podem ser publicados:

- documentação conceitual;
- posicionamento;
- status aprovado;
- roadmap de alto nível;
- resultados de testes autorizados;
- métricas validadas por testes executados;
- informações comerciais aprovadas;
- atualizações institucionais.

Não devem ser publicados:

- código-fonte proprietário;
- credenciais;
- chaves privadas;
- tokens;
- segredos;
- configurações internas;
- infraestrutura privada;
- logs sensíveis;
- informações pessoais não autorizadas;
- dados financeiros confidenciais;
- mecanismos internos de implementação;
- informações que permitam reconstrução indevida de ativos proprietários;
- estratégias internas não aprovadas.

Nenhum material privado deve ser publicado automaticamente sem validação prévia de divulgação.

---

## Para investidores e parceiros estratégicos

MagicGate está sendo desenvolvido na interseção entre:

**engenharia de software × automação controlada × produtividade mensurável × eficiência operacional × governança × escala empresarial**

Sua ambição é reduzir de forma mensurável o trabalho operacional necessário para transformar intenção em tecnologia.

A proposta é gerar:

**menos trabalho operacional;**  
**mais capacidade por profissional;**  
**mais capacidade por equipe;**  
**mais evidência sobre produtividade;**  
**mais eficiência por unidade de investimento.**

---

## Sobre este repositório

Este é o repositório de divulgação pública oficial do MagicGate.

Ele não é utilizado para disponibilização do código-fonte do produto.

Código, infraestrutura interna, configurações operacionais, credenciais, segredos, mecanismos proprietários, informações internas de implementação e demais ativos não públicos permanecem fora deste repositório.

Documentos complementares:

- [Licença pública](LICENSE.md) ([English](LICENSE.en.md))
- [Política de segurança](SECURITY.md) ([English](SECURITY.en.md))
- [Política de divulgação pública](DISCLOSURE_POLICY.md) ([English](DISCLOSURE_POLICY.en.md))
- [Política de validação de métricas](METRICS_VALIDATION_POLICY.md) ([English](METRICS_VALIDATION_POLICY.en.md))
- [Governança do repositório](GOVERNANCE.md) ([English](GOVERNANCE.en.md))
- [Diretrizes de contribuição](CONTRIBUTING.md) ([English](CONTRIBUTING.en.md))
- [Código de conduta](CODE_OF_CONDUCT.md) ([English](CODE_OF_CONDUCT.en.md))
- [Suporte e perguntas públicas](SUPPORT.md) ([English](SUPPORT.en.md))
- [Política de paridade de idiomas](DOCUMENTATION_LANGUAGE_POLICY.md) ([English](DOCUMENTATION_LANGUAGE_POLICY.en.md))

---

# MAGICGATE

## Plan. Execute. Measure. Scale.

> O futuro da engenharia não será definido apenas pela quantidade de pessoas disponíveis, mas pela capacidade tecnológica que cada profissional consegue colocar em movimento.

**Domínio:** `magicgate.dev`  
**Release:** `v0.3.0`  
**Oferta de lançamento:** 10 dias grátis, depois US$ 19/mês  
**Código-fonte:** privado por design.
