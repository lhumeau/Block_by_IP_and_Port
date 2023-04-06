import os
import re
import sys
import ctypes
import win32com.client
from ipwhois import IPWhois
from scapy.all import sniff
from scapy.layers.inet import IP
import win32api 
import subprocess
import socket
import netifaces
import threading



def run_as_admin():
    if not is_admin():
        # Ejecutar el script como administrador
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit(0)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
           
run_as_admin()

blocked_ips = set()


def bloquear_ip(ip):
    if ip in blocked_ips:
        print(f"IP {ip} ya está bloqueada.")
        return

    cmd = f"netsh advfirewall firewall add rule name=\"Bloquear IP {ip}\" dir=in action=block protocol=any remoteip={ip}"
    result = os.system(cmd)

    if result == 0:
        print(f"IP {ip} bloqueada.")
        blocked_ips.add(ip)  # Agregar la IP al conjunto de IPs bloqueadas
    else:
        print(f"Error al bloquear la IP {ip}.")

def desbloquear_ip(ip):
    result = os.system(f"netsh advfirewall firewall delete rule name='Bloquear IP {ip}'")
    if result == 0:
        print(f"IP {ip} desbloqueada.")
    else:
        print(f"Error al desbloquear la IP {ip}.")

def ip_pertenece_a_rd(ip):
    try:
        obj = IPWhois(ip)
        resultados = obj.lookup_rdap()
        pais = resultados.get("asn_country_code")
        print(f"IP {ip} pertenece a {pais}")
        return pais == "DO"
    except Exception as e:
        print(f"Error al consultar información de la IP {ip}: {e}")
        return False

def mostrar_ips_bloqueadas():
    result = subprocess.run(['netsh', 'advfirewall', 'firewall', 'show', 'rule', 'name=all'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print("Error al obtener las reglas del firewall.")
        return
    output = result.stdout.decode('utf-8')
    blocked_ips = re.findall(r"RemoteIP:\s+([\d\.]+)", output)
    if not blocked_ips:
        print("No hay direcciones IP bloqueadas.")
    else:
        print("Direcciones IP bloqueadas:")
        for ip in blocked_ips:
            print(ip)


def mostrar_menu():
    print("\nMenú:")
    print("1. Ver IPs bloqueadas")
    print("2. Bloquear IP")
    print("3. Desbloquear IP")
    print("4. Salir")

def bloquear_ip_scapy(ip):
    bloquear_ip(ip)
    print(f"IP {ip} bloqueada por Scapy")



def process_packet(packet):
   try:

    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet.sport
        dst_port = packet.dport
        
        # Obtener la dirección IP de la interfaz de red local
        local_ip = socket.gethostbyname(socket.gethostname())
        # Obtener las direcciones IP de todas las interfaces de red
        all_ips = [iface['addr'] for iface in netifaces.interfaces() 
                    for link in netifaces.ifaddresses(iface).values() 
                    for iface in link 
                    if 'addr' in iface]

        if dst_port == 3389 or dst_port == 443:
            if src_ip not in all_ips and src_ip != local_ip and not ip_pertenece_a_rd(src_ip):
                # Bloquear la IP de origen si no pertenece a RD
                bloquear_ip_scapy(src_ip)
        elif src_port == 3389 or src_port == 443:
            if dst_ip not in all_ips and dst_ip != local_ip and not ip_pertenece_a_rd(dst_ip):
                # Bloquear la IP de destino si no pertenece a RD
                bloquear_ip_scapy(dst_ip)
  
   except Exception as e:
     print(f"Error al procesar el paquete: {e}")



if __name__ == "__main__":
    def main():
        try:
            local_ip = socket.gethostbyname(socket.gethostname())
            all_ips = [iface['addr'] for iface in netifaces.interfaces() 
                    for link in netifaces.ifaddresses(iface).values() 
                    for iface in link 
                    if 'addr' in iface and not iface['addr'].startswith('127.')] # Filtrar solo direcciones IPv4

            # Construir una cadena de filtro BPF que excluya todas las IPs locales
            src_filter = " and ".join(f"not src host {ip}" for ip in all_ips)
            dst_filter = " and ".join(f"not dst host {ip}" for ip in all_ips)
            filter = f"ip and ({src_filter}) and ({dst_filter})"
            all_ips.append(local_ip)

            print("Capturando paquetes en tiempo real...")
            sniff_thread = threading.Thread(target=sniff, kwargs={"filter": filter, "prn": process_packet})
            sniff_thread.start()

            while True:
                mostrar_menu()
                opcion = input("Ingrese una opción: ")
                if opcion == "1":
                    mostrar_ips_bloqueadas()
                elif opcion == "2":
                    ip = input("Ingrese la IP a bloquear: ")
                    if ip_pertenece_a_rd(ip):
                        bloquear_ip(ip)
                    else:
                        print(f"La IP {ip} no pertenece a RD.")
                elif opcion == "3":
                    ip = input("Ingrese la IP a desbloquear: ")
                    desbloquear_ip(ip)
                elif opcion == "4":
                    print("Hasta luego!")
                    sys.exit(0)
                else:
                    print("Opción inválida.")
        except Exception as e:
            print(f"Error en el programa: {e}")


    if not is_admin():
        run_as_admin()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(script_dir, 'auth.log')
    umbral_intentos = 3
    intentos_por_ip = {}
main()

with open(log_path, "r") as f:
        sniff(filter="tcp and (port 3389 or port 443) and not src net 192.168.0.0/16", prn=process_packet, store=0)

  
