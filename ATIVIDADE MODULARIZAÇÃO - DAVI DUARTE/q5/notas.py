def media(notas_aluno):
    return sum(notas_aluno) / len(notas_aluno) if notas_aluno else 0

def maior(notas_aluno):
    return max(notas_aluno) if notas_aluno else None

def menor(notas_aluno):
    return min(notas_aluno) if notas_aluno else None