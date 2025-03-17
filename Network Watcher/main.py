import psutil
import time
from pywifi import PyWiFi, const

def run_monitorNetwork():
    connections = psutil.net_connections(kind='inet')

    for conn in connections:
        local_ip = conn.laddr.ip
        remote_ip = conn.raddr.ip if conn.raddr else "N/A"
        status = conn.status
        print(f"Local IP: {local_ip.ljust(17)} -> Remote IP: {remote_ip.ljust(17)} | Status: {status.ljust(17)}")

    time.sleep(0)

def run_wifiStrength():
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(2)

    networks = iface.scan_results()
    for network in networks:
        ssid = network.ssid
        signal_strength = network.signal
        print(f"SSID: {ssid}, Signal Strength: {signal_strength} dBm")

    time.sleep(0)

def monitor_network():
    while True:
        print("\n[X] Ağ Bağlantıları Kontrol Ediliyor.\n")

        run_monitorNetwork()
        
        print("\n" + "-" * 100)
        time.sleep(10)

def monitor_wifi_strength():
    while True:
        print("\n[X] Wi-Fi Sinyal Gücü Kontrol Ediliyor.\n")

        run_wifiStrength()

        print("\n" + "-" * 100)
        time.sleep(10)

def monitor_wifi_and_network():
    while True:
        print("\n[X] Wi-Fi Sinyal Gücü ve Ağ Bağlantıları Kontrol Ediliyor.\n")

        print("Wi-Fi Sinyal Gücü: \n")
        run_wifiStrength()
        print("\nAğ Bağlantıları: \n")
        run_monitorNetwork()

        print("\n" + "-" * 100)

        time.sleep(10)
        

def main():
    menu = """
1- Ağda bulunan cihazları takip et
2- Wi-Fi Sinyal Gücünü Ölç
3- Her iki özelliği de aktif et
4- Menü
           """

    print(menu)
    while True:
        choice = input("Yapılacak işlemi seçiniz: ")
        if choice == "1":
            monitor_network()
        elif choice == "2":
            monitor_wifi_strength()
        elif choice == "3":
            monitor_wifi_and_network()
        elif choice == "4":
            print(menu)
        else:
            print("Geçersiz seçim.")
            
if __name__ == "__main__":
    main()
