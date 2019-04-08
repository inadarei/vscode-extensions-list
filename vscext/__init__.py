name="vscext"

def vscode_extensions():
  """
    List installed VS Code extensions as a list of markdown links
  """
  
  import subprocess

  shell = subprocess.run(["code", "--list-extensions"], capture_output=True)
  extensions = shell.stdout.decode("utf-8").splitlines()

  url_prefix = "https://marketplace.visualstudio.com/items?itemName="


  out = [f"1. [{item.split('.')[1]}]({url_prefix}{item})" 
      for item in extensions]

  return out
