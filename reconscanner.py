import socket
import json
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

listadeportas = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3306, 3389, 8080]
def grab_banner(alvo, port):
    try:
        s = socket.socket()
        s.settimeout(2.0)
        s.connect((alvo, port))
        if port in listadeportas:
            s.send(b"HEAD / HTTP/1.1\r\nHost: localhost\r\n\r\n")
            banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
            s.close()
            return banner if banner else "Sem banner retornado"
    except:
        return "Nao foi possivel retornar o banner"
def scanport(alvo, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.5)
        aberto = s.connect_ex((alvo, port))
        if aberto == 0:
            banner = grab_banner(alvo, port)
            print(f"[+] Porta {port} aberta \n    Servico/Banner: {banner[:50] if banner else 'Nenhum'}")
            s.close()
            return {"port": port, "status": "open", "banner": banner}
        else:
            s.close()
    except:
        try:
            s.close()
        except:
            pass
    return None
def main():
    print("================================================================================================")
    print("                      FERRAMENTA DE CONHECIMENTO E ENUMERACAO")
    print("================================================================================================")
    alvo = input("Digite o IP do seu alvo (ex: 127.0.0.1): ").strip()
    try:
        IPalvo = socket.gethostbyname(alvo)
    except socket.gaierror:
        print("\nErro: Nao foi possivel analisar o nome/IP do alvo.")
        return
    portasabertas = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(scanport, IPalvo, port) for port in listadeportas]
        for future in futures:
            try:
                resultado = future.result()
                if resultado:
                    portasabertas.append(resultado)
            except Exception as e:
                pass
                    
    report = {
        "alvo": alvo, 
        "IPalvo": IPalvo, 
        "scan_time": str(datetime.now()), 
        "portasabertas": portasabertas
    }
    
    report_filename = f"scan_{IPalvo}.json"
    with open(report_filename, "w") as f:
        json.dump(report, f, indent=4)
        
    txt_filename = f"scan_{IPalvo}.txt"
    with open(txt_filename, "w") as f_txt:
        f_txt.write("================================================================================================\n\n")
        f_txt.write("                  RELATORIO DE RECONHECIMENTO E ENUMERACAO\n")
        f_txt.write("\n")
        f_txt.write(f"Alvo digitado: {alvo}\n")
        f_txt.write(f"IP do alvo: {IPalvo}\n")
        f_txt.write(f"Data do Scan: {str(datetime.now())}\n")
        f_txt.write("================================================================================================\n")
        f_txt.write("PORTAS ABERTAS ENCONTRADAS:\n================================================================================================\n")
        
        if portasabertas:
            for item in portasabertas:
                f_txt.write(f"Porta: {item['port']} | Status: {item['status']}\n")
                f_txt.write(f"	Banner: {item['banner']}\n\n")
        else:
            f_txt.write("Nenhuma porta aberta encontrada nas portas comuns.\n")
            
    print(f"\nRelatorio TXT tambem salvo em: {txt_filename}")

if __name__ == "__main__":
    main()
