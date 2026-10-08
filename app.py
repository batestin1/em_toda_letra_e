from pathlib import Path
import streamlit as st

BASE = Path(__file__).parent
SUNO = "https://suno.com/album/8b518d75-4217-4dbd-b31e-5799fdc3a9f7"

FAIXAS = [
    (1, "E começa com um passarinho...", "5:04", "passarinho"),
    (2, "É simples assim", "2:45", "simples-assim"),
    (3, "Em vários tempos", "4:04", "varios-tempos"),
    (4, "Espero mesmo", "6:02", "espero-mesmo"),
    (5, "é?", "2:24", "interrogacao"),
    (6, "Estado mínimo", "2:48", "estado-minimo"),
    (7, "Enfezado", "4:52", "enfezado"),
]
SO_LETRA = ["Entusiastas do fim do mundo", "Em toda letra E", "E sonhe comigo"]

st.set_page_config(page_title="Em toda letra E", page_icon="🎵", layout="centered")

st.markdown(
    """
<style>
h1 {font-weight:900; text-transform:uppercase; letter-spacing:-0.02em; font-size:3rem !important; line-height:1;}
h2 {border-top:2px solid #C4204F; padding-top:.6rem; margin-top:2rem;}
.kicker {color:#C4204F; font-weight:700; letter-spacing:.12em; text-transform:uppercase; font-size:.8rem;}
.pull {border-left:4px solid #C4204F; padding:.2rem 1rem; margin:1.5rem 0; font-size:1.3rem; font-style:italic;}
.pull cite {display:block; font-size:.85rem; font-style:normal; opacity:.7; margin-top:.4rem;}
.verdict {background:rgba(196,32,79,.08); border:1px solid #C4204F; padding:1rem 1.2rem; margin:1.5rem 0;}
.verdict .label {color:#C4204F; font-weight:700; text-transform:uppercase; letter-spacing:.1em; font-size:.75rem;}
.nota {font-size:2rem; font-weight:900; color:#C4204F;}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown('<div class="kicker">Estreia · Crítica</div>', unsafe_allow_html=True)
st.title("Em toda letra E")
st.markdown(
    "*O primeiro disco de Maycon Batestin: dez poemas que aprenderam a cantar.*"
)
st.caption(
    "Texto de Claude, a partir das letras, do áudio e da entrevista com o autor · 8 de outubro de 2026"
)

capa = BASE / "capas" / "passarinho.jpg"
c1, c2 = st.columns([1, 2], vertical_alignment="center")
with c1:
    if capa.exists():
        st.image(str(capa), width="stretch")
with c2:
    st.markdown('<div class="nota">4 / 5</div>', unsafe_allow_html=True)
    st.link_button("Ouvir o álbum completo no Suno", SUNO, type="primary")

st.header("Ouvir aqui")
nomes = [f"{n:02d} · {t} ({d})" for n, t, d, _ in FAIXAS]
escolha = st.selectbox("Faixa", nomes, label_visibility="collapsed")
n, titulo, dur, slug = FAIXAS[nomes.index(escolha)]
cc1, cc2 = st.columns([1, 3], vertical_alignment="center")
with cc1:
    img = BASE / "capas" / f"{slug}.jpg"
    if img.exists():
        st.image(str(img), width="stretch")
with cc2:
    st.markdown(f"**{titulo}**  \nFaixa {n} · {dur}")
    audio = BASE / "audio" / f"{n:02d}-{slug}.mp3"
    if audio.exists():
        st.audio(str(audio), format="audio/mpeg")
    else:
        st.info("Áudio indisponível. Ouça no Suno.")

st.markdown((BASE / "conteudo" / "materia.md").read_text(encoding="utf-8"), unsafe_allow_html=True)

st.link_button("Ouvir o álbum no Suno", SUNO)

st.header("As dez faixas")
for n, t, d, slug in FAIXAS:
    a, b = st.columns([1, 6], vertical_alignment="center")
    with a:
        st.image(str(BASE / "capas" / f"{slug}.jpg"), width=60)
    with b:
        st.markdown(f"**{n:02d}. {t}** · {d}")
for i, t in enumerate(SO_LETRA, start=8):
    st.markdown(f"**{i:02d}. {t}** · só letra")

st.divider()
st.markdown((BASE / "conteudo" / "rodape.md").read_text(encoding="utf-8"))
