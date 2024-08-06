#!/usr/bin/python3

import argparse
import subprocess
import os
import shutil




def download_mimikatz(arch):
    url = "https://github.com/gentilkiwi/mimikatz/releases/download/2.2.0-20220919/mimikatz_trunk.zip"
    
    try:
        # Descargar el archivo
        subprocess.run(["wget", url, "-O", "mimikatz_trunk.zip"], check=True)
        
        # Descomprimir el archivo zip
        subprocess.run(["unzip", "mimikatz_trunk.zip"], check=True)
        
        # Eliminar el directorio correspondiente según la arquitectura
        if arch == "x64":
            shutil.rmtree("./Win32", ignore_errors=True)
        elif arch == "x86":
            shutil.rmtree("./x64", ignore_errors=True)
        
        # Copiar el ejecutable a la raíz del directorio
        if arch == "x64":
            shutil.copy("./x64/mimikatz.exe", "mimikatz.exe")
        elif arch == "x86":
            shutil.copy("./x86/mimikatz.exe", "mimikatz.exe")
        
        # Eliminar el archivo zip y el directorio temporal
        os.remove("./mimikatz_trunk.zip")
        #os.remove("./kiwi_passwords.yar")
        #os.remove("./mimicom.idl")
        os.remove("./README.md")
        print("Mimikatz downloaded and extracted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during download or extraction: {e}")
    except FileNotFoundError as e:
        print(f"File not found error: {e}")





def download_kerbrute(platform, arch):

    if platform == "linux":
        if arch == "x86": 
            url = "https://github.com/ropnop/kerbrute/releases/download/v1.0.3/kerbrute_linux_386" 
        else:
            url = "https://github.com/ropnop/kerbrute/releases/download/v1.0.3/kerbrute_linux_amd64"
    
    elif platform == "windows":
        if arch == "x86":
            url = "https://github.com/ropnop/kerbrute/releases/download/v1.0.3/kerbrute_windows_386.exe" 
        else:
            url = "https://github.com/ropnop/kerbrute/releases/download/v1.0.3/kerbrute_windows_amd64.exe"
    
    else:
        print("Unsupported platform specified.")
        return

    try:
        #os.makedirs("kerbrute", exist_ok=True)
        filename = os.path.basename(url)
        subprocess.run(["wget", url, "-O", filename], check=True)
        if platform == "linux":
            subprocess.run(["chmod", "+x", filename], check=True)
        print(f"Kerbrute for {platform} {arch} downloaded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during download: {e}")





def download_impacket(platform, arch):
    if platform == "linux":
        url = "https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/impacket_linux_binaries.tar.gz"
    elif platform == "windows":
        url = "https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/impacket_windows_binaries.zip"
    else:
        print("Unsupported platform specified.")
        return

    try:
        subprocess.run(["wget", url], check=True)
        if platform == "linux":
            subprocess.run(["mkdir", "-p", "impacket"], check=True)
            subprocess.run(["tar", "-xf", "impacket_linux_binaries.tar.gz", "-C", "impacket"], check=True)
            subprocess.run(["rm", "impacket_linux_binaries.tar.gz"], check=True)
        elif platform == "windows":
            subprocess.run(["unzip", "impacket_windows_binaries.zip"], check=True)
            subprocess.run(["mv", "dist", "impacket_ropnop"], check=True)
            subprocess.run(["rm", "impacket_windows_binaries.zip"], check=True)
        print(f"Impacket for {platform} downloaded and extracted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during download or extraction: {e}")


def download_windows_exploit_suggester():
    url = "https://raw.githubusercontent.com/AonCyberLabs/Windows-Exploit-Suggester/master/windows-exploit-suggester.py"
    output_file = "windows-exploit-suggester.py"
    
    try:
        # Ejecutar el comando wget para descargar el archivo
        subprocess.run(["wget", url, "-O", output_file], check=True)
        print(f"Downloaded {output_file} successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during download: {e}")      



def download_linenum():
    url = "https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh"
    output_file = "LinEnum.sh"
    
    try:
        # Ejecutar el comando wget para descargar el archivo
        subprocess.run(["wget", url, "-O", output_file], check=True)
        print(f"Downloaded {output_file} successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during download: {e}")


def download_linuxprivchecker():
    url = "https://raw.githubusercontent.com/sleventyeleven/linuxprivchecker/master/linuxprivchecker.py"
    output_file = "linuxprivchecker.py"
    
    try:
        # Ejecutar el comando wget para descargar el archivo
        subprocess.run(["wget", url, "-O", output_file], check=True)
        print(f"Downloaded {output_file} successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during download: {e}")

def download_linux_exploit_suggester2():
    url = "https://raw.githubusercontent.com/jondonas/linux-exploit-suggester-2/master/linux-exploit-suggester-2.pl"
    output_file = "linux-exploit-suggester-2.pl"
    
    try:
        # Ejecutar el comando wget para descargar el archivo
        subprocess.run(["wget", url, "-O", output_file], check=True)
        print(f"Downloaded {output_file} successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during download: {e}")


def download_rpcenum():
    url = "https://raw.githubusercontent.com/KermitPurple96/rpcenum/master/rpcenum.sh"
    output_file = "rpcenum.sh"
    
    try:
        # Ejecutar el comando wget para descargar el archivo
        subprocess.run(["wget", url, "-O", output_file], check=True)
        print(f"Downloaded {output_file} successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during download: {e}")


def download_pywerview():
    url = "https://github.com/the-useless-one/pywerview/archive/refs/tags/v0.6.zip"
    output_file = "pywerview_v0.6.zip"
    
    try:
        # Ejecutar el comando wget para descargar el archivo
        subprocess.run(["wget", url, "-O", output_file], check=True)
        subprocess.run(["unzip", output_file], check=True)
        subprocess.run(["rm", output_file], check=True)

        print(f"Downloaded {output_file} successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during download: {e}")


def download_socat(platform, arch):
    if platform == "windows":
        if arch == "x86":
            url = "https://sourceforge.net/projects/unix-utils/files/socat/1.7.3.2/socat-1.7.3.2-1-i686.zip/download"
            output_file = "socat-1.7.3.2-1-i686.zip"
        elif arch == "x64":
            url = "https://sourceforge.net/projects/unix-utils/files/socat/1.7.3.2/socat-1.7.3.2-1-x86_64.zip/download"
            output_file = "socat-1.7.3.2-1-x86_64.zip"
        else:
            print("Unsupported architecture specified for Linux.")
            return
    elif platform == "linux":
        if arch == "x64":
            url = "https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/socat"
            output_file = "socat"
        else:
            print("Unsupported architecture specified for Windows.")
            return
    else:
        print("Unsupported platform specified.")
        return

    try:
        # Descargar el archivo usando wget
        subprocess.run(["wget", url, "-O", output_file], check=True)
        print(f"Downloaded {output_file} successfully.")
        
        # Si el archivo es un zip, descomprimirlo
        if output_file.endswith(".zip"):
            subprocess.run(["unzip", output_file], check=True)
            print(f"Extracted {output_file} successfully.")
            
            # Borrar el archivo zip después de la extracción
            os.remove(output_file)
            print(f"Deleted {output_file} successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during download or extraction: {e}")


def download_dnstools():

    subprocess.run(["pip", "install", "git+https://github.com/dirkjanm/adidnsdump#egg=adidnsdump"], check=True)
    subprocess.run(["wget", "https://raw.githubusercontent.com/dirkjanm/krbrelayx/master/addspn.py"], check=True)
    subprocess.run(["wget", "https://raw.githubusercontent.com/dirkjanm/krbrelayx/master/dnstool.py"], check=True)
    subprocess.run(["wget", "https://raw.githubusercontent.com/dirkjanm/krbrelayx/master/krbrelayx.py"], check=True)
    subprocess.run(["wget", "https://raw.githubusercontent.com/dirkjanm/krbrelayx/master/printerbug.py"], check=True)


def download_sprying():

    subprocess.run(["git", "clone", "https://github.com/cube0x0/HashSpray.py"], check=True)
    subprocess.run(["git", "clone", "https://github.com/Hackndo/sprayhound"], check=True)

def download_pkinit():
    subprocess.run(["git", "clone", "https://github.com/dirkjanm/PKINITtools"], check=True)
    
def download_adcskiller():
    subprocess.run(["git", "clone", "https://github.com/grimlockx/ADCSKiller"], check=True)

def sccme_hunter():
    subprocess.run(["wget", "https://github.com/garrettfoster13/sccmhunter/archive/refs/tags/v.1.0.5.zip"], check=True)
    subprocess.run(["unzip", "v.1.0.5.zip"], check=True)
    subprocess.run(["rm", "v.1.0.5.zip"], check=True)


def download_maz_windows_binaries():
    subprocess.run(["wget", "https://github.com/maaaaz/impacket-examples-windows/releases/download/v0.9.17/impacket-examples-windows-v0.9.17.zip"], check=True)
    subprocess.run(["unzip", "impacket-examples-windows-v0.9.17.zip"], check=True)
    subprocess.run(["rm", "impacket-examples-windows-v0.9.17.zip"], check=True)

def download_sysinternalsSuite():
    subprocess.run(["wget", "https://download.sysinternals.com/files/SysinternalsSuite.zip"], check=True)
    subprocess.run(["unzip", "SysinternalsSuite.zip", "-d", "sysinternals"], check=True)
    subprocess.run(["rm", "SysinternalsSuite.zip"], check=True)


def download_sharpcollection():
    subprocess.run(["git", "clone", "https://github.com/Flangvik/SharpCollection"], check=True)

def download_nc_exe():
    subprocess.run(["wget", "https://eternallybored.org/misc/netcat/netcat-win32-1.12.zip"], check=True)
    subprocess.run(["unzip", "netcat-win32-1.12.zip"], check=True)
    subprocess.run(["rm", "netcat-win32-1.12.zip"], check=True)


def download_powersharppack():
    subprocess.run(["wget", "https://raw.githubusercontent.com/S3cur3Th1sSh1t/PowerSharpPack/master/PowerSharpPack.ps1"], check=True)

def download_powerupsql():
    subprocess.run(["wget", "https://raw.githubusercontent.com/NetSPI/PowerUpSQL/master/PowerUpSQL.ps1"], check=True)

def download_invoke_psexec():
    subprocess.run(["wget", "https://raw.githubusercontent.com/HarmJ0y/Misc-PowerShell/master/Invoke-PsExec.ps1"], check=True)

def download_invoke_conptyshell():
    subprocess.run(["wget", "https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1"], check=True)

def download_conptyshell_exe():
    subprocess.run(["wget", "https://github.com/antonioCoco/ConPtyShell/releases/download/1.5/ConPtyShell.zip"], check=True)
    subprocess.run(["unzip", "ConPtyShell.zip"], check=True)
    subprocess.run(["rm", "ConPtyShell.zip"], check=True)

def download_powercat():
    subprocess.run(["wget", "https://raw.githubusercontent.com/besimorhino/powercat/master/powercat.ps1"], check=True)

def download_nishang():
    subprocess.run(["git", "clone", "https://github.com/samratashok/nishang"], check=True)

def download_invoke_thehash():
    subprocess.run(["git", "clone", "https://github.com/Kevin-Robertson/Invoke-TheHash"], check=True)


def privesc():
    sys.exit(0)
def pivoting():
    sys.exit(0)


def main():
    parser = argparse.ArgumentParser(description="Download various tools.")
    parser.add_argument("-t", "--tool", required=True, choices=["checker", "linenum", "pywerview", "socat", "rpcenum", "mimikatz", "kerbrute", "impacket","suggester", "suggester2"], help="Specify the tool to download.")
    parser.add_argument("-s", "--system", required=True, choices=["windows", "linux"], help="Specify the system (platform) for the tool.")
    parser.add_argument("-a", "--arch", required=True, choices=["x86", "x64"], help="Specify the architecture for the tool.")

    args = parser.parse_args()

    if args.tool == "privesc":
        privesc(args.arch)

    if args.tool == "mimikatz":
        download_mimikatz(args.arch)
    elif args.tool == "kerbrute":
        download_kerbrute(args.system, args.arch)
    elif args.tool == "impacket":
        download_impacket(args.system, args.arch)
    elif args.tool == "suggester":
        download_windows_exploit_suggester(args.system, args.arch)
    elif args.tool == "suggester2":
        download_linux_exploit_suggester2(args.system, args.arch)
    elif args.tool == "checker":
        download_linuxprivchecker(args.system, args.arch)
    elif args.tool == "linenum":
        download_linenum(args.system, args.arch)
    elif args.tool == "pywerview":
        download_pywerview(args.system, args.arch)
    elif args.tool == "rpcenum":
        download_rpcenum(args.system, args.arch)
    elif args.tool == "socat":
        download_socat(args.system, args.arch)
    elif args.tool == "dnstools":
        download_dnstools(args.system, args.arch)
    elif args.tool == "sprying":
        download_sprying(args.system, args.arch)
    elif args.tool == "pkinit":
        download_pkinit(args.system, args.arch)
    elif args.tool == "adcskiller":
        download_adcskiller(args.system, args.arch)
    elif args.tool == "sccme_hunter":
        sccme_hunter(args.system, args.arch)
    elif args.tool == "maz_windows_binaries":
        download_maz_windows_binaries(args.system, args.arch)
    elif args.tool == "sysinternalsSuite":
        download_sysinternalsSuite(args.system, args.arch)
    elif args.tool == "sharpcollection":
        download_sharpcollection(args.system, args.arch)
    elif args.tool == "nc_exe":
        download_nc_exe(args.system, args.arch)
    elif args.tool == "powersharppack":
        download_powersharppack(args.system, args.arch)
    elif args.tool == "powerupsql":
        download_powerupsql(args.system, args.arch)
    elif args.tool == "invoke_psexec":
        download_invoke_psexec(args.system, args.arch)
    elif args.tool == "invoke_conptyshell":
        download_invoke_conptyshell(args.system, args.arch)
    elif args.tool == "conptyshell_exe":
        download_conptyshell_exe(args.system, args.arch)
    elif args.tool == "powercat":
        download_powercat(args.system, args.arch)
    elif args.tool == "nishang":
        download_nishang(args.system, args.arch)
    elif args.tool == "invoke_thehash":
        download_invoke_thehash(args.system, args.arch)

            

if __name__ == "__main__":
    main()
