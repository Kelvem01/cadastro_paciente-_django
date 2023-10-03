from django.db import models

class Contato(models.Model):
   
   SOLICITACAO_DE_PACIENTE =(
       ('todos','Todos'),
       ('consulta','Consultas'),
       ('exame','Exames'),
       ('paciente','Pacientes'),
       
   )
   nome = models.CharField(verbose_name= 'Nome',max_length=50)
   email = models.EmailField(verbose_name='E-mail')
   preferencia_evento = models.CharField(
       
       verbose_name='Solicitação',max_length=20,default='todos',
       choices= SOLICITACAO_DE_PACIENTE
       
   )
   observacao = models.TextField(verbose_name='Observação',blank= True)
   enviado_em = models.DateTimeField(verbose_name='Enviado em',auto_now_add=True)
   modificado_em = models.DateTimeField(verbose_name='Modificado em',auto_now=True)
   