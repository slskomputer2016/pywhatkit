
import pywhatkit as pw
import time,random,logging
import mysql.connector



def body_html(nama,alamat):
    html  = 'Kepada Yth<br>'
    html += f'Direktur/Pimpinan {nama}<br>'
    html += f'{alamat}<br><br><br>'

    html += 'Dengan hormat<br><br>'
    html += 'Perkenalkan, saya A.Hendra Public Relation dari Kantor Akuntan Publik (KAP) HSE, sebuah kantor akuntan publik yang telah berizin resmi dari Kementerian Keuangan dan terdaftar di Otoritas Jasa Keuangan (OJK).<br><br>'
    html += 'Kami menawarkan layanan audit laporan keuangan, review laporan keuangan, serta jasa atestasi dan non-atestasi lainnya yang sesuai dengan standar profesional dan regulasi yang berlaku di Indonesia.<br><br>'
    html += f'Dengan pengalaman tim auditor kami di berbagai sektor industri, kami siap membantu <b>{nama}</b> dalam memberikan keyakinan atas kewajaran laporan keuangan, meningkatkan kepatuhan terhadap peraturan, serta mendukung tata kelola perusahaan yang lebih baik.<br><br>'
    html += 'Beberapa keunggulan layanan kami :<br>'
    html += '* Tim auditor bersertifikat dan berpengalama<br>'
    html += '* Pendekatan audit berbasis risiko dan efisiens<br>'
    html += '* Komunikasi terbuka dan responsif selama proses audi<br>'
    html += '* Biaya jasa yang kompetitif dan transparan<br><br>'

    html += 'Apabila Bapak/Ibu berkenan, kami sangat terbuka untuk menjadwalkan pertemuan lebih lanjut, baik secara daring maupun langsung, guna membahas kebutuhan audit di perusahaan Bapak/Ibu.<br>'
    html += f'Demikian perkenalan singkat dari kami. Besar harapan kami untuk dapat menjalin kerja sama dengan <b>{nama}</b>.<br><br>'
    html += 'Terima kasih atas perhatian dan waktunya.<br><br>'
    html += 'Hormat kami<br><br>'


    html += 'A. Hendra<br>'
    html += '0851 4832 9822<br><br>'
    html += '<b>Public Relation<br>'
    html += 'KAP Hendro, Sukron, Edy<br>'
    html += 'Cabang Bandung<br>'
    html += 'Jalan Nilem V No.2A Lengkong Bandung</b><br>'
    html += 'https://kaphsebandung.com'
    return html


#--------------------------------------------------
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="app_python"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM klien")
myresult = mycursor.fetchall()

def main():
    for x in myresult:
        html = body_html(x[1],x[2])
        pw.send_hmail(
          email_sender = 'asephendra2018@gmail.com',
          password = 'xxxxxxxxxxxx',
          subject = ' Penawaran Jasa Kantor Akuntan Publik',
          html_code = html,
          email_receiver = x[3]
        )






# def send_mail():
# 	send = pw.send_mail(
# 			email_sender = 'asephendra2018@gmail.com',
# 			email_receiver = 'asephendra2015@gmail.com',
# 			message = 'Ini email dengan pywhtakit',
# 			password = 'ndlaqohjyvukhhlr',
# 			subject = ' Python Email ')
# 	return send



if __name__ == "__main__":
    main()
