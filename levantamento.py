# Exercício 9 — POO e Levantamento de Requisitos (sugestão)
# ============================
# Como orientação para o exercício 9 (trabalho em grupo / 5W2H):
#
# 5W2H simplificado para um problema: "Controle de Empréstimo de Notebooks na Faculdade"
#
# - WHAT? Controle de empréstimo e devolução de notebooks.
# - WHY? Evitar perda, saber localização e histórico de uso.
# - WHO? Professores (retiram/entregam), alunos (solicitam), técnico (manutenção), admin.
# - WHERE? Sala de TI, laboratórios, salas de aula.
# - WHEN? Durante horário letivo; prazo de devolução 7 dias.
# - HOW? Sistema com cadastro de equipamentos, RFID para leitura, registro de movimentações.
# - HOW MUCH? Orçamento para leitores RFID, etiquetas, e horas de desenvolvimento.
#
# Entidades (classes) propostas: Equipamento (com tag RFID), Usuario (roles), Movimentacao, Local, Relatorio.
# Exemplos de atributos/metodos: Equipamento: id, descricao, tag_rfid, local_atual, movimentar(novo_local).
#
# Recomenda-se desenhar casos de uso e diagramas de sequência para: associar tag, leitura automática, movimentar, gerar relatório.