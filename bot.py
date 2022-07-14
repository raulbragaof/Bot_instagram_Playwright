from playwright.sync_api import sync_playwright
print(
    '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
    'Bot comentarios Instagram\n'
    'Autor @__raulbraga\n'
    'Biblioteca utilizada Playwright\n'
    'Linkdin @raulbragaof\n'
    '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
)

usuario = input("Usuario: ")
password_user = input("Password: ")
link_post = input("Link: ")
comment_text = input("Comentario: ")
quant_repetir = input("Numero de comentarios: ")
quant_repetir = int(quant_repetir)

inicio = 0

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.instagram.com/")
    page.fill('xpath=//*[@id="loginForm"]/div/div[1]/div/label/input', usuario)
    page.wait_for_timeout(3000)
    page.fill('//*[@id="loginForm"]/div/div[2]/div/label/input', password_user)
    page.wait_for_timeout(5000)
    page.locator('//*[@id="loginForm"]/div/div[3]').click()
    page.wait_for_timeout(3100)
    page.goto(link_post)
    page.wait_for_timeout(3000)
    while inicio <= quant_repetir:
        page.locator('//html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div/article/div/div[2]/div/div[2]/section[3]/div/form/textarea').click()
        page.fill('//html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div/article/div/div[2]/div/div[2]/section[3]/div/form/textarea', comment_text)
        page.wait_for_timeout(3000)
        page.keyboard.press('Enter')
        page.wait_for_timeout(5000)
        print(f'Enviando comentario {inicio} de {quant_repetir}')
        inicio += 1
    else:
        print("Comentarios enviados!")
