class Opcoes:
    def __init__(self,ambiente,tipodeatendimento,tipodedocumento,tipodepessoa,atendente,tarefa,resultado,motivo,titulo):
        self._ambiente = ambiente
        self._tipodeatendimento = tipodeatendimento
        self._tipodedocumento = tipodedocumento
        self._tipodepessoa = tipodepessoa
        self._atendente = atendente
        self._tarefa = tarefa
        self._resultado = resultado
        self._motivo = motivo
        self._titulo = titulo

    def inserirOpcoes(self):
        sql = f'''
        INSERT INTO "Opcoes"
        VALUES ('{self._ambiente}', '{self._tipodeatendimento}','{self._tipodedocumento}','{self._tipodepessoa}',
        '{self._atendente}','{self._tarefa}',
        '{self._resultado}','{self._motivo}','{self._titulo}')
        '''    
        return sql