# --- Librerías estándar ---
import os
from io import BytesIO
from datetime import datetime, date

# --- Librerías de terceros ---
import requests
from dotenv import load_dotenv
import discord
from discord import option
from PIL import Image, ImageDraw, ImageFont, ImageOps

# Intents (necesarios para leer mensajes y eventos)
intents = discord.Intents.default()
intents.message_content = True  

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")
    await bot.sync_commands()

@bot.slash_command(description="¡Rellena la info y crea tu ficha!")
@option("nombre", description="Tu nombre o usuario", required=True)
@option("cumpleaños", description="Debe tener el formato dd/mm/yy. Por ejemplo: 01/12/98", required=True)
@option("signo", description="Tu signo del zodiaco", required=True)
@option("pais", description="En dónde naciste", required=True)
@option("ubicacion", description="País donde estás ahora", required=True)
@option("profesion", description="A qué te dedicas? / Qué estudiaste?", required=True)
@option("estatura", description="Cuánto mides? (en metros)", required=True)
@option("gustos", description="Qué cosas te gustan?", required=True)
@option("disgustos", description="Qué cosas no te gustan?", required=True)
@option("funfact", description="Cuéntamos algo curioso sobre ti, o una frase", required=True)
#@option("avatar", description="Pon acá el link de la imagen que quieres que aparezca", required=True)
@option("anime_fav", description="(OPCIONAL) Cuál es tu anime favorito?", required=False, default="")
@option("muslos", description="(OPCIONAL) Diametro en centímetros (?", required=False, default="")

async def ficha(ctx,
                nombre: str = None,
                cumpleaños: str = None,
                signo: str = None,
                pais: str = None,
                ubicacion: str = None,
                profesion: str = None,
                estatura: str = None,
                gustos: str = None,
                disgustos: str = None,
                funfact: str = None,
                #avatar: str = None,
                anime_fav: str = None,
                muslos: str = None
                ):

    # Carga imagen de fondo
    img_raw = Image.open("img/bg.png").convert("RGBA")
    img = img_raw.resize((800,500))

    # Tablas de fondo
    tabla_raw = Image.open("img/tabla.png").convert("RGBA")
    tabla = tabla_raw.resize((770,400))

    # Marco para el avatar
    frame_raw = Image.open("img/box.png").convert("RGBA")
    frame = frame_raw.resize((155,170))

    # Cajita para las respuestas
    box_raw = Image.open("img/box-2.png").convert("RGBA")
    box = box_raw.resize((375,20))
        
    img.paste(tabla, (15,50), tabla)
    img.paste(frame, (70,85), frame)

    draw = ImageDraw.Draw(img) 

    # Fuente (usa una básica si no tienes ttf instalado)
    try:
        #font = ImageFont.truetype("fonts/Stardew_Valley.ttf", size=20)
        #font_thin = ImageFont.truetype("fonts/svthin.ttf", size=17)
        font_thin = ImageFont.truetype("fonts/LSANS.ttf", size=12)
        font_bold = ImageFont.truetype("fonts/svbold.ttf", size=18)
        #font_caps = ImageFont.truetype("fonts/Stardew Valley ALL CAPS.ttf", size=40)
        font_caps = ImageFont.truetype("fonts/Stardew Valley Regular.ttf", size=48)
        #font = ImageFont.truetype("arial.ttf", 20)
    except:
        font_thin = ImageFont.load_default()

    # Titulo
    draw.text((380, 85), "FICHA", fill=(0, 0, 0), font=font_caps)

    # Dibujar texto en el centro
        # X
    margen = 240
    margen2 = margen+140
    
        # Y
    linea = 110
        
        # Interlineado
    espacio = 22
    
    # Nombre
    try:
        indice = 1
        img.paste(box, (margen2-15, (linea + espacio*indice)+2), box)
        draw.text((margen, linea + espacio*indice), "Nombre", fill=(0, 0, 0), font=font_bold)
        draw.text((margen2, (linea + espacio*indice)+5), nombre, fill=(0, 0, 0), font=font_thin)
    except: 
        await ctx.respond("Error: Debes llenar el campo 'nombre'.", ephemeral=True)
    
    # Cumpleaños
    try:
        indice = indice + 1
        img.paste(box, (margen2-15, (linea + espacio*indice)+2), box)
        draw.text((margen, linea + espacio*indice), "Cumpleanos", fill=(0, 0, 0), font=font_bold)
        draw.text((margen2, (linea + espacio*indice)+5), cumpleaños, fill=(0, 0, 0), font=font_thin)
    except:
        await ctx.respond("Error: Debes llenar el campo 'cumpleaños'.", ephemeral=True)
    
    # Edad
    try:
        nacimiento = datetime.strptime(cumpleaños, "%d/%m/%y").date()
        hoy = date.today()
        edad = hoy.year - nacimiento.year
        if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
            edad -= 1

        indice = indice + 1
        img.paste(box, (margen2-15, (linea + espacio*indice)+2), box)
        draw.text((margen, linea + espacio*indice), "Edad", fill=(0, 0, 0), font=font_bold)
        draw.text((margen2, (linea + espacio*indice)+5), f"{str(edad)} años", fill=(0, 0, 0), font=font_thin)
    except:
        await ctx.respond("Error: Coloca tu cumpleaños en este formato: dd/mm/yy.", ephemeral=True)
        return

    # Signo
    try:
        indice = indice + 1
        img.paste(box, (margen2-15, (linea + espacio*indice)+2), box)
        draw.text((margen, linea + espacio*indice), "Signo", fill=(0, 0, 0), font=font_bold)
        draw.text((margen2, (linea + espacio*indice)+5), signo, fill=(0, 0, 0), font=font_thin)
    except:
        await ctx.respond("Error: Debes llenar el campo 'signo'.", ephemeral=True)
        
    # Pais
    try:
        indice = indice + 1
        img.paste(box, (margen2-15, (linea + espacio*indice)+2), box)
        draw.text((margen, linea + espacio*indice), "Pais", fill=(0, 0, 0), font=font_bold)
        draw.text((margen2, (linea + espacio*indice)+5), pais, fill=(0, 0, 0), font=font_thin)
    except:
        await ctx.respond("Error: Debes llenar el campo 'pais'.", ephemeral=True)

    # Ubicación
    try:
        indice = indice + 1
        img.paste(box, (margen2-15, (linea + espacio*indice)+2), box)
        draw.text((margen, linea + espacio*indice), "Ubicacion", fill=(0, 0, 0), font=font_bold)
        draw.text((margen2, (linea + espacio*indice)+5), ubicacion, fill=(0, 0, 0), font=font_thin)
    except:
        await ctx.respond("Error: Debes llenar el campo 'ubicacion'.", ephemeral=True)

    # Profesión
    try:
        indice = indice + 1
        img.paste(box, (margen2-15, (linea + espacio*indice)+2), box)
        draw.text((margen, linea + espacio*indice), "Profesion", fill=(0, 0, 0), font=font_bold)
        draw.text((margen2, (linea + espacio*indice)+5), profesion, fill=(0, 0, 0), font=font_thin)
    except:
        await ctx.respond("Error: Debes llenar el campo 'profesion'.", ephemeral=True)

    # Estatura
    try:
        indice = indice + 1
        img.paste(box, (margen2-15, (linea + espacio*indice)+2), box)
        draw.text((margen, linea + espacio*indice), "Estatura", fill=(0, 0, 0), font=font_bold)
        draw.text((margen2, (linea + espacio*indice)+5), f"{estatura} metros", fill=(0, 0, 0), font=font_thin)
    except:
        await ctx.respond("Error: Debes llenar el campo 'estatura'.", ephemeral=True)

    # Gustos
    try:
        indice = indice + 1
        img.paste(box, (margen2-15, (linea + espacio*indice)+2), box)
        draw.text((margen, linea + espacio*indice), "Gustos", fill=(0, 0, 0), font=font_bold)
        draw.text((margen2, (linea + espacio*indice)+5), gustos, fill=(0, 0, 0), font=font_thin)
    except:
        await ctx.respond("Error: Debes llenar el campo 'gustos'.", ephemeral=True)

    # Disgustos
    try:
        indice = indice + 1
        img.paste(box, (margen2-15, (linea + espacio*indice)+2), box)
        draw.text((margen, linea + espacio*indice), "Disgustos", fill=(0, 0, 0), font=font_bold)
        draw.text((margen2, (linea + espacio*indice)+5), disgustos, fill=(0, 0, 0), font=font_thin)
    except:
        await ctx.respond("Error: Debes llenar el campo 'disgustos'.", ephemeral=True)

    # Funfact    
    try:
        if len(funfact) < 45:
            indice = indice + 1
            img.paste(box, (margen2-15, (linea + espacio*indice)+2), box)
            draw.text((margen, linea + espacio*indice), "Datos Random", fill=(0, 0, 0), font=font_bold)
            draw.text((margen2, (linea + espacio*indice)+5), funfact, fill=(0, 0, 0), font=font_thin)
        elif len(funfact) >= 45:
            await ctx.respond("Error: 'funfact' no puede tener más de 44 caracteres.", ephemeral=True)
            return
    except:
        await ctx.respond("Error: Debes llenar el campo 'funfact'.", ephemeral=True)

    # Anime
    if anime_fav:
        indice = indice + 1
        img.paste(box, (margen2-15, (linea + espacio*indice)+2), box)
        draw.text((margen, linea + espacio*indice), "Anime Favorito", fill=(0, 0, 0), font=font_bold)
        draw.text((margen2, (linea + espacio*indice)+5), anime_fav, fill=(0, 0, 0), font=font_thin)    

    # Muslos
    if muslos:
        indice = indice + 1
        img.paste(box, (margen2-15, (linea + espacio*indice)+2), box)
        draw.text((margen, linea + espacio*indice), "Muslos (?", fill=(0, 0, 0), font=font_bold)
        draw.text((margen2, (linea + espacio*indice)+5), f"{muslos} cm de diametro", fill=(0, 0, 0), font=font_thin)


    # Avatar
    # Descargar avatar
    user = ctx.author
    avatar_url = user.display_avatar.replace(size=128).url
    response = requests.get(avatar_url)
    avatar = Image.open(BytesIO(response.content)).convert("RGBA")

    # Hacer la imagen cuadrada (por si no lo es)
    size = min(avatar.size)  # lado más pequeño
    avatar = ImageOps.fit(avatar, (size, size), centering=(0.5, 0.5))
    img.paste(avatar, (83,107), avatar)

    # Guardar en un buffer de memoria
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    # Enviar como archivo en Discord
    file = discord.File(fp=buffer, filename="ficha.png")
    await ctx.respond(file=file)


#Este es el token de Trotski
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)


