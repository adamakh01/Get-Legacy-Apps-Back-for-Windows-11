import subprocess
import shutil
from pathlib import Path
def uninstallStoreApps(packageName):
    try:
        # Uninstall the specified package using PowerShell command
        command = f'Get-AppxPackage -Name *"{packageName}"* | Remove-AppxPackage'
        subprocess.run(["powershell", "-Command", command], check=True)
        print(f"Successfully uninstalled {packageName}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to uninstall {packageName}: {e}")
#Uninstall Store Apps
#mspaint windows 11 version
uninstallStoreApps("Microsoft.Paint")

#Installing Files in System32
def installSystemFiles(file):
    #To Get the files into system 32
    filePath = "Legacy Files\\" + file + ".exe"
    source_file = Path(filePath)
    destination = Path("C:/Windows/System32") / source_file.name
    try:
        if not source_file.exists():
            print(f"Source file {source_file} does not exist.")
        else:
            shutil.copy(source_file, destination)
            print(f"Successfully installed {source_file.name} to System32.")
    except PermissionError:
        print(f"Permission denied while trying to install {source_file.name}. Please run as administrator.")
    except Exception as e:
        print(f"Failed to install {source_file.name}: {e}")
    #for en-US files
    filePathEnUS = "Legacy Files\en-US\\" + file + ".exe.mui"
    source_file_enUS = Path(filePathEnUS)
    destinationEnUS = Path("C:/Windows/System32/en-US") / (file + ".exe.mui")
    try:
        if not source_file_enUS.exists():
            print(f"Source file {source_file_enUS} does not exist.")
        else:
            shutil.copy(source_file_enUS, destinationEnUS)
            print(f"Successfully installed {file}.exe.mui to System32/en-US.")
    except PermissionError:
        print(f"Permission denied while trying to install {file}.exe.mui. Please run as administrator.")
    except Exception as e:
        print(f"Failed to install {file}.exe.mui: {e}")
#Install System Files
files = ["mspaint", "wordpad", "SnippingTool", "mip"]
for file in files:
    installSystemFiles(file)
#registry files
def installRegistryFiles(file):
    filePath = "Legacy Files\\" + file + ".reg"
    try:
        subprocess.run(["regedit", "/s", filePath], check=True)
        print(f"Successfully installed {file}.reg.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {file}.reg: {e}")
installRegistryFiles(files[0])
installRegistryFiles(files[1])

#Shortcuts
def addShortcutsToWindowsAccessories(path):
    source_file_shortcut = Path(path)
    destinationShortcut = Path("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories")
    try:
        if not source_file_shortcut.exists():
            print(f"Source file {source_file_shortcut.name} does not exist.")
        else:
            shutil.copy(source_file_shortcut, destinationShortcut)
            print(f"Successfully added {source_file_shortcut.name} to Windows Accessories.")
    except PermissionError:
        print(f"Permission denied. Please run as administrator.")
    except Exception as e:
        print(f"Failed to add {source_file_shortcut.name} to Windows Accessories: {e}")
shortcutPaths = ["Shortcuts\Math Input Panel.lnk", "Shortcuts\Paint.lnk", "Shortcuts\WordPad.lnk", "Shortcuts\Snipping Tool.lnk"]
for path in shortcutPaths:
    addShortcutsToWindowsAccessories(path)
