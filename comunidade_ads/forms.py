from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidade_ads.models import Usuario
from flask_login import current_user



class FormCriarConta(FlaskForm):
   username = StringField('Nome de Usuário', validators=[DataRequired()])
   email = StringField('E-mail', validators=[DataRequired(), Email()])
   senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
   confirmacao = PasswordField('Confirmação de senha', validators=[DataRequired(), EqualTo('senha')])
   botao_submit_criarconta = SubmitField('Criar Conta')

   def validate_email(self, email):
       usuario = Usuario.query.filter_by(email=email.data).first()
       if usuario:
           raise ValidationError('E-mail já cadastrado. Insira outro email ou faça login para continuar')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField("Lembrar Dados de Acesso")
    botao_submit_login = SubmitField('Fazer Login')

class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar foto de Perfil', validators=[FileAllowed(['jpg', 'png'])])
    curso_programacao_web = BooleanField("Programção Web ")
    curso_mobile = BooleanField("Dispositivos Mobile ")
    curso_python = BooleanField("Python Developer")
    curso_frameworks = BooleanField("Frameworks_Back_Front_End ")
    curso_sql = BooleanField("Banco de Dados SQL")
    curso_redes = BooleanField("Redes de Computadores")
    botao_submit_editarperfil = SubmitField('Confirmar Edição')


    def validate_email(self, email):
       if current_user.email != email.data:
           usuario = Usuario.query.filter_by(email=email.data).first()
           if usuario:
              raise ValidationError('Já existe Usuario com esse e-mail. Cadastre outro e-mail')


class FormCriarPost(FlaskForm):
    titulo = StringField('Título do Post', validators=[DataRequired(), Length(2, 140)])
    corpo = TextAreaField('Escreva seu Post Aqui', validators=[DataRequired()])
    botao_submit = SubmitField('Criar Post')