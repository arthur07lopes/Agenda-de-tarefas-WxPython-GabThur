class GerenciadorTarefas:
  def __init__(self):
    self.tarefas = []
    self.proximo_id = 1

  def adicionar_tarefa(self, descricao, prioridade):
      if not descricao.strip():
        return False
      tarefa = {
        "id": self.proximo_id,
        "descricao": descricao.strip(),
        "prioridade": prioridade,
        "status": "Pendente"
      }

      self.tarefas.append(tarefa)
      self.proximo_id += 1
      return True

  def concluir_tarefa(self, tarefa_id):
    for tarefa in self.tarefas:
      if tarefa["id"] == tarefa_id:
        tarefa["status"] = "Concluída"
        return True
    return False

  def remover_tarefa(self, tarefa_id):
    for tarefa in self.tarefas:
      if tarefa["id"] == tarefa_id:
        self.tarefas.remove(tarefa)
        return True
    return False

  def obter_todas_tarefas(self):
    return self.tarefas
