import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def generate_beauty_website():
    """Genera la struttura HTML/CSS del sito web per Bellezza e Benessere."""
    
    html_content = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Elegance & Wellness - Bellezza e Benessere</title>
    <style>
        body { font-family: 'Helvetica Neue', sans-serif; margin: 0; padding: 0; background: #faf9f6; color: #333; }
        header { background: #d8a7b1; color: white; padding: 40px 20px; text-align: center; }
        header h1 { margin: 0; font-size: 2.5em; font-weight: 300; }
        header p { font-size: 1.1em; opacity: 0.9; }
        nav { background: #b68973; padding: 10px; text-align: center; }
        nav a { color: white; margin: 0 15px; text-decoration: none; font-weight: bold; }
        .container { max-width: 1000px; margin: 40px auto; padding: 0 20px; }
        .services { display: flex; gap: 20px; justify-content: space-between; flex-wrap: wrap; }
        .card { background: white; border-radius: 8px; padding: 20px; flex: 1; min-width: 250px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center; }
        .card h3 { color: #b68973; }
        footer { text-align: center; padding: 20px; background: #333; color: white; margin-top: 50px; }
    </style>
</head>
<body>

    <header>
        <h1>Elegance & Wellness</h1>
        <p>Il tuo rifugio digitale per la cura della pelle, trattamenti spa e benessere olistico.</p>
    </header>

    <nav>
        <a href="#servizi">Trattamenti</a>
        <a href="#chi-siamo">Chi Siamo</a>
        <a href="#contatti">Prenota</a>
    </nav>

    <div class="container">
        <h2 style="text-align:center; margin-bottom: 30px;">I Nostri Servizi Esclusivi</h2>
        <div class="services" id="servizi">
            <div class="card">
                <h3>Cura della Pelle & Spa</h3>
                <p>Trattamenti viso personalizzati e scrub corpo con ingredienti naturali e biologici.</p>
            </div>
            <div class="card">
                <h3>Massaggi Olistici</h3>
                <p>Tecnica rilassante e decontratturante per ritrovare l'equilibrio tra mente e corpo.</p>
            </div>
            <div class="card">
                <h3>Consulenza di Bellezza</h3>
                <p>Piani di skincare personalizzati e consiglia sui prodotti più adatti a te.</p>
            </div>
        </div>
    </div>

    <footer>
        <p>&copy; 2026 Elegance & Wellness. Tutti i diritti riservati. Contact: cleanfootprint@gmail.com</p>
    </footer>

</body>
</html>
"""
    
    # Salva il file HTML generato
    output_filename = "index.html"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"✅ Sito Web Generato con successo: {output_filename}")
    return output_filename

def send_notification_email():
    """Invia un'email di notifica via Gmail."""
    email_user = os.getenv("MAIL_USERNAME", "cleanfootprint@gmail.com")
    email_password = os.getenv("MAIL_PASSWORD")  # La tua password per le app di Google
    
    recipient = "cleanfootprint@gmail.com"
    subject = "✨ Generatore Siti: Nuovo Sito Bellezza & Benessere Creato!"
    body = "Ciao!\n\nIl tuo agente automatico ha generato con successo il nuovo sito web dedicato a Bellezza & Benessere (Elegance & Wellness).\n\nI file sono pronti sul tuo repository GitHub."

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    if not email_password:
        print("⚠️ Attenzione: MAIL_PASSWORD non impostata. L'email non verrà inviata.")
        return

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_user, email_password)
        server.send_message(msg)
        server.quit()
        print("📧 Email di notifica inviata con successo a cleanfootprint@gmail.com!")
    except Exception as e:
        print(f"❌ Errore durante l'invio dell'email: {e}")

if __name__ == "__main__":
    generate_beauty_website()
    send_notification_email()
