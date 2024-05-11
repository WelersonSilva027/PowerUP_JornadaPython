import time
import pyautogui
pyautogui.press("win") #Pressiona Windows
time.sleep(0.5)
pyautogui.write("San")
time.sleep(0.5)
pyautogui.press("enter")
time.sleep(8)
pyautogui.write("141222") # Digite a senha
time.sleep(0.5)
pyautogui.press("enter") # Realizando Login
time.sleep(10)
pyautogui.hotkey('ctrl', 'g') # Seleciona o Campo de Pesquisa da Página
time.sleep(0.8)
pyautogui.write("portal de vendas fatu") # Realiza a pesquisa pelo "Portal de Vendas Faturamento"
time.sleep(3)
pyautogui.press("enter")
pyautogui.sleep(17) # Aguarda portal de vendas carregar por completo
pyautogui.click(x=218, y=190) # Aplicar (DEVE SER ALTERADO COM BASE NO COMPUTADOR QUE FOR RODAR)
time.sleep(5)
pyautogui.click(x=356, y=178) # Filtro de impresso
time.sleep(5)
pyautogui.click(x=380, y=268) # Fedido foi impresso
time.sleep(6) 
pyautogui.click(x=476, y=378) # Remove seleção dos pedidos impressos
time.sleep(6)
pyautogui.click(x=698, y=593) # Aplica o filtro
time.sleep(7)
pyautogui.click(x=888, y=182)
time.sleep(7)
pyautogui.click(x=727, y=274)
time.sleep(7)
pyautogui.click(x=470, y=325)
time.sleep(7)
pyautogui.click(x=473, y=382)
time.sleep(7)
pyautogui.click(x=703, y=598)
time.sleep(7)
pyautogui.press("shift", "")
time.sleep(5)
# Pressiona e segura a tecla Shift
pyautogui.keyDown('shift')

# Pressiona a seta para baixo sete vezes
for _ in range(7):
    pyautogui.press('down')
    time.sleep(0.9)  # Intervalo de espera opcional entre cada pressionamento de tecla

# Libera a tecla Shift
pyautogui.keyUp('shift')
time.sleep(3)
pyautogui.click(x=344, y=151)
time.sleep(3)
pyautogui.click(x=455, y=249)
time.sleep(3)