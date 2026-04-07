import streamlit as st
import os
from PIL import Image

# ==========================================
# CONFIGURAÇÃO DE ALTA FIDELIDADE - VOZ DA TERRA
# ==========================================
st.set_page_config(
    page_title="Voz da Terra - Marketplace de Storytelling Inteligente",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Customização Visual (CSS) para simular um marketplace premium
# Focado no público de alto valor do turismo (Hotéis e Restaurantes B2B).
# Substitua o bloco st.markdown(""" <style> ... </style> """, ...) por este:

st.markdown("""
<style>
    /* Força o fundo da página e do cabeçalho */
    [data-testid="stHeader"] {background-color: transparent;}
    .stApp {background-color: #F8F5F1 !important;} 
    
    /* Força a cor de todos os textos Markdown para garantir visibilidade */
    .stMarkdown, p, span {
        color: #444444 !important;
        font-family: 'Arial', sans-serif;
    }

    /* Estilização específica dos Títulos com '!important' para vencer o Dark Mode */
    h1 {
        color: #4A3E30 !important; 
        font-family: 'Helvetica Neue', sans-serif; 
        font-weight: 300; 
        text-align: center;
    }
    h2 {
        color: #5D4D3D !important; 
        font-family: 'Helvetica Neue', sans-serif; 
        font-weight: 400; 
        font-size: 1.5rem;
        margin-top: 20px;
    }
    h3 {
        color: #7D6C5D !important; 
        font-family: 'Helvetica Neue', sans-serif; 
        font-weight: 500; 
        font-size: 1.2rem;
    }
    
    /* Tags de artesão e preço */
    .artisan-tag {
        background-color: #DFD7CD !important;
        color: #4A3E30 !important;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 0.95rem;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 20px;
    }
    
    .price-tag {
        font-size: 2.5rem !important;
        color: #4A3E30 !important;
        font-weight: 500;
        margin-top: 25px;
    }
    
    .impact-text {
        color: #9D8771 !important;
        font-style: italic;
        font-size: 1.05rem;
    }

    /* Ajuste para o botão não sumir no mobile */
    .stButton button {
        background-color: #4A3E30 !important;
        color: white !important;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# DADOS OFICIAIS (Simulação de RAG/Entrada da Artesã)
# ==========================================
LOGO_PATH = "logo_voz_da_terra.png" 
PRODUTO_PATH = "filtro_sonhos_vermelho.png" 
AUDIO_PATH = "artesao_audio_kaingang.mp3"   # Opcional

ARTESAO = "Dona Marize"
COMUNIDADE = "Comunidade Kaingang (Ponta Grossa, PR)"
TITULO_ARTESANATO = "Filtro dos Sonhos Kanhgág"
PRECO = 100.00 # Valor B2B premium para hotel boutique

# O Storytelling Inteligente (RAG + GPT-4/Llama3)
HISTORIA_STORYTELLING = f"""
### A Trama da Criação de Dona Marize

Este Filtro dos Sonhos é a materialização de séculos de resistência e sabedoria Kaingang na região de Ponta Grossa. Cada fio vermelho que se entrelaça na teia representa o sangue que corre na terra ancestral, o *kujà*, a força vital que nos conecta.

Conta-se na tradição Kaingang que este objeto não apenas retém pesadelos, mas é um receptor de bons agouros e visões de cura. **Dona Marize**, anciã de sua comunidade, dedicou semanas para colher as sementes de **Lágrimas de Nossa Senhora**, conhecidas por suas propriedades protetoras. Estas sementes, duras e brilhantes, são as contas que pontuam a teia, cada uma representando uma prece de paz. As penas, tingidas de vermelho vibrante, são de galinhas criadas em liberdade na comunidade, simbolizando o sopro da vida e a liberdade que as histórias dos nossos avós nos trazem. 

Ao adquirir o 'Voz da Terra: Filtro Kanhgág', você não compra um objeto decorativo. Você leva para o seu espaço a proteção de uma herança viva, a voz de uma artesã que, mesmo sem saber ler o português dos homens da cidade, lê a linguagem do vento na mata, transformando-a em dignidade econômica para seu povo.
"""

# ==========================================
# ESTRUTURA DO WEBAPP (Front-end)
# ==========================================

# 1. Cabeçalho com o Novo Logotipo
col_logo1, col_logo2, col_logo3 = st.columns([1,2,1])
with col_logo2:
    if os.path.exists(LOGO_PATH):
        st.image(LOGO_PATH, use_container_width=True)
    else:
        st.error(f"Logo não encontrado: '{LOGO_PATH}'")
    st.markdown("<h1>Plataforma Voz da Terra</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#7D6C5D; font-size:0.9rem'>Storytelling Inteligente - Herança Viva</p>", unsafe_allow_html=True)

# Divisor visual
st.markdown("<hr style='border: 0.5px solid #E6E1DC'>", unsafe_allow_html=True)

# 2. Seção do Produto e Identidade
col1, col2 = st.columns([1.1, 1])

with col1:
    # Carregamento da imagem do Filtro dos Sonhos
    if os.path.exists(PRODUTO_PATH):
        image_prod = Image.open(PRODUTO_PATH)
        # Corta a imagem para centralizar o foco (pode pular se o upload original estiver bom)
        # image_prod = image_prod.crop((0, 200, image_prod.width, image_prod.height - 200))
        st.image(image_prod, caption=f"Filtro Kanhgág por: {ARTESAO} (Ponta Grossa/PR)", use_container_width=True)
    else:
        st.error(f"Arquivo do produto '{PRODUTO_PATH}' não encontrado.")
        st.image("https://via.placeholder.com/600x600.png?text=Filtro+Sonhos+Placeholder", caption="Placeholder", use_container_width=True)

with col2:
    st.markdown(f"<span class='artisan-tag'>🌍 Herança Kaingang</span>", unsafe_allow_html=True)
    st.markdown(f"<h2>{TITULO_ARTESANATO}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='margin-top:-10px; color:gray'>{COMUNIDADE}</p>", unsafe_allow_html=True)
    
    st.markdown("<h3>Descrição & Materiais</h3>", unsafe_allow_html=True)
    st.markdown("Fio de algodão tingido, sementes de Lágrimas de Nossa Senhora colhidas sustentavelmente, penas de galinha tingidas de vermelho.")
    
    st.markdown("<h3>Rastreabilidade Kaingang</h3>", unsafe_allow_html=True)
    st.markdown("Item Certificado pela Associação Kaingang de Ponta Grossa. Origem e autoria verificadas por nossa plataforma de RAG e Blockchain.")
    
    st.markdown(f"<div class='price-tag'>R$ {PRECO:,.2f}</div>", unsafe_allow_html=True)
    st.markdown("<p class='impact-text'>Preço B2B Premium. 85% do valor vai para a artesã.</p>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.button("❤️ Adicionar aos Favoritos", key="fav_btn")

# Divisor visual
st.markdown("<hr style='border: 0.5px solid #E6E1DC'>", unsafe_allow_html=True)

# 3. Seção do Storytelling (O Coração da Plataforma)
st.markdown("<h2>📖 A Voz por Trás da Peça: O Coração da Tradição Kaingang</h2>", unsafe_allow_html=True)

col_audio1, col_audio2 = st.columns([2.1, 1.1])

with col_audio1:
    st.markdown(HISTORIA_STORYTELLING)

with col_audio2:
    # Mostra a transcrição original bruta (simulando a IA RAG removendo ruído)
    with st.expander("Ver transcrição original bruta (Áudio Base)", expanded=True):
        st.markdown(f"*[Voz Bruta da {ARTESAO} - Áudio processado]*")
        # Carregamento robusto do áudio (Opcional)

# Divisor visual
st.markdown("<hr style='border: 0.5px solid #E6E1DC'>", unsafe_allow_html=True)

# 4. CTA de Compra e Rastreabilidade
col_cta1, col_cta2 = st.columns([1.8, 1])

with col_cta1:
    st.markdown("<h3>🤝 Apoio à Economia Ancestral Kaingang</h3>", unsafe_allow_html=True)
    st.markdown("Ao adquirir esta peça, você financia diretamente projetos de inclusão digital e logística de transporte para a Comunidade Kaingang de Ponta Grossa. O Conexão Ancestral garante a rastreabilidade financeira via Blockchain.")

with col_cta2:
    # Botão de compra premium
    st.markdown("<br>", unsafe_allow_html=True)
    st.button(f"Comprar agora (R$ {PRECO:,.2f})", type="primary", use_container_width=True, key="buy_btn")
    st.markdown("<p style='text-align:center; font-size:0.8rem; color:gray; margin-top:10px'>Frete grátis para hotéis parceiros em Ponta Grossa e Curitiba.</p>", unsafe_allow_html=True)
