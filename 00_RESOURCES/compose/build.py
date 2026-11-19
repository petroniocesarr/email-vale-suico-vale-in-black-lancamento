# Gera as imagens compostas do e-mail Vale in Black (HTML -> PNG via Chrome headless -> JPG)
import subprocess, pathlib, sys
from PIL import Image
J = pathlib.Path(__file__).resolve().parents[2]
SRC = J/'00_RESOURCES'/'src'; OUT = J/'assets'; TMP = J/'00_RESOURCES'/'compose'
CHROME = r'C:/Program Files/Google/Chrome/Application/chrome.exe'
u = lambda p: (SRC/p).as_uri()
BASE = f"""<style>@font-face{{font-family:RHD;src:url('{u('red-hat-display.woff2')}') format('woff2');font-weight:300 900}}
*{{margin:0;padding:0;box-sizing:border-box}}html,body{{background:#090909;overflow:hidden}}
body{{font-family:RHD,Arial,sans-serif;color:#fcf8f0;position:relative}}
.gold{{background:linear-gradient(180deg,#ffe8a6 0%,#f2c65c 45%,#ab8439 100%);-webkit-background-clip:text;background-clip:text;color:transparent}}</style>"""

def render(name, w, h, body, crop=None):
    html = TMP/f'{name}.html'
    html.write_text(f'<!doctype html><meta charset="utf-8">{BASE}<body style="width:{w}px;height:{h}px">{body}</body>', encoding='utf-8')
    png = TMP/f'{name}.png'
    subprocess.run([CHROME,'--headless=new','--disable-gpu','--hide-scrollbars','--force-device-scale-factor=1',
        '--allow-file-access-from-files',f'--window-size={w},{h}','--virtual-time-budget=4000',f'--screenshot={png}',html.as_uri()],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    Image.open(png).convert('RGB').save(OUT/f'{name}.jpg', quality=84, optimize=True, progressive=True)
    print(name, (OUT/f'{name}.jpg').stat().st_size//1024, 'KB')

# 1) HERO 1200x1250 — base da LP: aérea noturna + mãe e filho + logo + "70 ofertas"
render('01-hero-70-ofertas', 1200, 1250, f"""
<div style="position:absolute;left:0;right:0;top:-70px;bottom:0;background:url('{u('bg-aerea-noite.webp')}') 55% 0/auto 1340px no-repeat"></div>
<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(9,9,9,0) 35%,rgba(9,9,9,.78) 62%,rgba(9,9,9,.9) 100%)"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(9,9,9,.35) 0%,rgba(9,9,9,0) 25%,rgba(9,9,9,0) 70%,rgba(9,9,9,.9) 100%)"></div>
<img src="{u('mae-filho-recorte.webp')}" style="position:absolute;left:-190px;top:340px;width:960px">
<img src="{u('logo-vale-in-black.webp')}" style="position:absolute;left:50%;top:40px;width:800px;transform:translateX(-50%);filter:drop-shadow(0 10px 24px rgba(0,0,0,.75))">
<div style="position:absolute;left:640px;right:36px;top:520px;text-align:center;text-shadow:0 3px 16px rgba(0,0,0,.6)">
  <div style="font-size:260px;font-weight:900;line-height:.86;letter-spacing:-6px;text-shadow:none;filter:drop-shadow(0 4px 14px rgba(0,0,0,.7))" class="gold">70</div>
  <div style="font-size:84px;font-weight:900;line-height:1;margin-top:4px">ofertas</div>
  <div style="font-size:64px;font-weight:700;line-height:1.05">para viajar</div>
  <div style="height:3px;background:#f2c65c;margin:30px 40px 22px"></div>
  <div style="font-size:34px;font-weight:700;letter-spacing:3px;color:#f2c65c;text-transform:uppercase;line-height:1.3">de Janeiro<br>a Outubro 2027</div>
</div>""")

# 2) CARDS 560x780 — foto 4:5 + logo oval + texto + barra de CTA
def card(name, img, pos, l1, l2, cta):
    render(name, 560, 780, f"""
<div style="position:absolute;left:0;top:0;width:560px;height:700px;background:url('{u(img)}') {pos}/cover no-repeat"></div>
<div style="position:absolute;left:0;top:0;width:560px;height:700px;background:linear-gradient(180deg,rgba(9,9,9,.45) 0%,rgba(9,9,9,0) 30%,rgba(9,9,9,0) 50%,rgba(9,9,9,.92) 100%)"></div>
<img src="{u('logo-vale-in-black-oval.webp')}" style="position:absolute;left:50%;top:22px;width:250px;transform:translateX(-50%);filter:drop-shadow(0 6px 14px rgba(0,0,0,.6))">
<div style="position:absolute;left:24px;right:24px;bottom:110px;text-align:center;text-shadow:0 2px 12px rgba(0,0,0,.6)">
  <div style="font-size:52px;font-weight:900;line-height:1.02;text-shadow:none;filter:drop-shadow(0 2px 8px rgba(0,0,0,.8))" class="gold">{l1}</div>
  <div style="font-size:36px;font-weight:700;line-height:1.15;margin-top:6px">{l2}</div></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:80px;background:#f2c65c;color:#090909;display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:900;letter-spacing:2px">{cta}</div>""")

card('02-card-jan-piscinas', 'jan-aerea.webp', 'center 60%', 'Belíssimas Férias', 'com 17 piscinas quentes', 'ESCOLHA QUANDO!')
card('03-card-fev-beach-tenis', 'fev-beach-tenis.webp', 'center 30%', 'Vai dar muito jogo', 'viajar com os amigos', 'CONFIRA QUANTO!')
card('04-card-abr-piscina-ondas', 'abr-piscina-ondas.webp', 'center 40%', 'Tchauzinho', 'finais de semana comuns!', 'CORRE AQUI!')
card('05-card-jun-thermas-caverna', 'jun-thermas-caverna.jpg', 'center 55%', 'Outono &amp; Inverno', 'surpreendentes', 'GARANTA AGORA!')

# 3) LOFT 1200x760 — "OS DESCONTOS VALE IN BLACK SÃO APENAS O COMEÇO."
render('06-loft-descontos-comeco', 1200, 760, f"""
<div style="position:absolute;left:0;top:90px;width:1200px;height:675px;background:url('{u('casal-loft-cachorro.webp')}') center/cover no-repeat"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,#090909 0%,#090909 12%,rgba(9,9,9,.55) 28%,rgba(9,9,9,0) 45%)"></div>
<div style="position:absolute;left:0;right:0;top:34px;text-align:center;text-shadow:0 2px 14px rgba(0,0,0,.55)">
  <div style="font-size:40px;font-weight:800;letter-spacing:5px">OS DESCONTOS <span class="gold" style="font-size:62px;font-weight:900;letter-spacing:1px;text-shadow:none">VALE IN BLACK</span></div>
  <div style="font-size:40px;font-weight:800;letter-spacing:5px;margin-top:2px">SÃO APENAS O COMEÇO.</div></div>""")
