# MagicGate

🌐 **Idioma:** [Português](README.md) | [English](README.en.md)

**Da intenção à execução. Da execução à evidência. Da evidência à escala.**

> **Release de referência:** v0.3.0  
> **Domínio oficial:** [magicgate.dev](https://magicgate.dev)  
> **Código-fonte do produto:** privado por design

## O que é

MagicGate é uma camada de execução para engenharia de software. Ele transforma planos estruturados em fluxos controlados de execução, validação, evidência e medição.

A proposta é reduzir o trabalho operacional repetitivo entre uma intenção de software e uma entrega verificável, preservando sob responsabilidade humana as decisões críticas, o contexto, a arquitetura e o julgamento profissional.

Ciclo conceitual:

**definir → planejar → executar → testar → validar → registrar → medir → evoluir**

## Capacidades atuais da v0.3.0

A baseline atual inclui:

- execução orientada por planos determinísticos;
- formato de plano `magicgate-plan-v1`;
- ordenação de tarefas e controle de dependências;
- execução controlada, retomada e persistência de estado;
- evidências obrigatórias para conclusão;
- políticas de segurança com comportamento fail-closed;
- proteção contra ações destrutivas e material com aparência de segredo;
- controle de custo;
- autenticação ChatGPT delegada ao Codex CLI, sem custódia de tokens pelo MagicGate;
- métricas de duração, autonomia, qualidade, retries e intervenção humana;
- MagicGate Productivity Index (MGPI);
- diagnóstico de ambiente com `magicgate doctor`;
- validação de releases;
- CLI canônica para execução e leitura de resultados;
- Investor Hunter para pesquisa e priorização de investidores, com controles de divulgação;
- baseline técnica do Remote Link;
- extensão privada para VS Code com Control Center em evolução.

## Evidências públicas

Os resultados abaixo são específicos das execuções registradas e não constituem garantia universal de desempenho:

| Validação | Resultado observado |
|---|---:|
| Control Center — plano de 3 tarefas | progresso canônico 33% → 66% → 100% |
| Bateria funcional registrada | 100% de sucesso e autonomia |
| Remote Link — baseline v0.3.0 | 58/58 testes aprovados, typecheck e build aprovados |
| Execução operacional adicional | 14,90 s, 100% de autonomia e 0 s de intervenção humana |
| MGPI observado em execuções registradas | 99,97–99,99 |

Uma métrica só é apresentada como validada quando deriva de uma execução real e possui evidência observável. Projeções, metas e comparações humano-equivalentes permanecem identificadas como estimativas.

## VS Code Control Center

A extensão privada em evolução oferece uma interface para:

- Doctor;
- Run Plan;
- Resume;
- Safety;
- Metrics;
- Active Plans;
- acompanhamento baseado no estado real da execução.

A extensão ainda precisa concluir a preparação comercial e operacional para publicação no Visual Studio Code Marketplace, incluindo empacotamento final, metadados, validação e credenciais de publicação.

## Oferta de lançamento

A referência comercial inicial definida para validação é:

| Item | Condição |
|---|---:|
| Avaliação | 10 dias grátis |
| Assinatura após o período gratuito | US$ 19/mês |
| Renovação | mensal |

Cadastro, elegibilidade do trial, cobrança, licenças, API Keys e consoles comerciais ainda pertencem à camada comercial em evolução.

## Chamada para investidores

O MagicGate está aberto a conversas com investidores estratégicos interessados em infraestrutura de engenharia de software, automação responsável, inteligência artificial aplicada e aumento de produtividade técnica.

Estamos em estágio de lançamento e validação comercial, com a versão v0.3.0, CLI operacional, evidências públicas de execução e evolução planejada para distribuição, integração comercial e expansão controlada.

Buscamos investidores que possam contribuir com:

- capital para acelerar produto, nuvem, segurança, operação e distribuição;
- experiência em software, IA, ferramentas para desenvolvedores ou SaaS;
- conexões estratégicas com equipes de engenharia, startups e empresas de tecnologia;
- orientação para validação comercial e expansão internacional.

Os materiais para investidores são apresentados de forma controlada e não incluem código-fonte, credenciais, tokens, dados pessoais, arquitetura interna ou informações confidenciais.

Para iniciar uma conversa, acesse [magicgate.dev](https://magicgate.dev) e utilize o canal oficial de contato.

## Roadmap

### Operacional na v0.3.0

- CLI e planos determinísticos;
- execução, retomada, estado e evidências;
- SafetyPolicy e CostGuard;
- Doctor multiplataforma;
- métricas e MGPI;
- pipeline de release com gates;
- baseline técnica do Remote Link.

### Em evolução

- VS Code Control Center;
- cenários de Remote Link e execução remota controlada;
- benchmarks comparáveis baseados em execuções reais;
- operação distribuída controlada;
- integração ampliada entre execução, métricas, custo e segurança.

### Próxima camada comercial

- cadastro e autenticação de usuários;
- trial de 10 dias e controle de elegibilidade;
- cobrança recorrente;
- licenças e MagicGate API Keys;
- Customer Console e Admin Console;
- telemetria sanitizada.

## Segurança e divulgação

Este repositório contém somente informações aprovadas para divulgação. Não devem ser publicados aqui:

- código-fonte proprietário;
- credenciais, tokens, chaves privadas ou segredos;
- configurações e infraestrutura internas;
- logs sensíveis;
- dados pessoais ou financeiros não autorizados;
- mecanismos proprietários que permitam reconstrução indevida do produto;
- estratégias internas não aprovadas.

Automação não autoriza divulgação externa. O fluxo de divulgação deve permanecer sujeito a validação e governança apropriadas.

## Documentação

- [Licença](LICENSE.md)
- [Política de segurança](SECURITY.md)
- [Política de divulgação pública](DISCLOSURE_POLICY.md)
- [Política de validação de métricas](METRICS_VALIDATION_POLICY.md)
- [Governança](GOVERNANCE.md)
- [Contribuição](CONTRIBUTING.md)
- [Código de conduta](CODE_OF_CONDUCT.md)
- [Suporte](SUPPORT.md)

---

**Plan. Execute. Measure. Scale.**
