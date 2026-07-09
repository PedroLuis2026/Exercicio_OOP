from notificacao import *

def main():

# Testando envios válidos
        email = NotificacaoEmail("professor@cursoemvideo.com")
        sms = NotificacaoSMS("5581999998888")
        
        email.enviar("Sua aula de POO já está disponível!")
        sms.enviar("Código de verificação: 4002")

        print("\n[bold yellow]Testando barreira de segurança...[/]")
# Tentando forçar um e-mail podre (O sistema vai travar aqui!)
        email_ruim = NotificacaoEmail("email_sem_ponto_com@com")

   

if __name__ == "__main__":
    main()