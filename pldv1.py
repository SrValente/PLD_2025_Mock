import streamlit as st
from datetime import datetime

# -------- Mock Layout com Login e Consulta --------
USUARIO_TESTE = "fulano@matrizeducacao.com.br"
SENHA_TESTE = "teste123"

# Dados mockados de Unidades e Turmas
unidades = [
    "COLEGIO E CURSO MATRIZ EDUCACAO BANGU",
    "COLEGIO E CURSO MATRIZ EDUCACAO NOVA IGUACU"
]
mapa_turmas = {
    "COLEGIO E CURSO MATRIZ EDUCACAO BANGU": [
        ("BG-9VES11", "História"),
        ("BG-2VES11", "História"),
    ],
    "COLEGIO E CURSO MATRIZ EDUCACAO NOVA IGUACU": [
        ("NI-9VES11", "História"),
        ("NI-1VES11", "História"),
        ("NI-2VES11", "História"),
    ],
}

# Tópicos completos para cada Turma
common_topics = [
    "Semana de acolhimento - Capítulo 1 - A Primeira Guerra Mundial e a Revolução Russa",
    "Capítulo 2 - A Crise de 1929 e o fascismo italiano",
    "Semana de exercícios",
    "Capítulo 3 - O nazismo alemão",
    "Capítulo 4 - O nascimento da República no Brasil",
    "Semana de exercícios",
    "Capítulo 5 - A consolidação da República brasileira",
    "Semana de revisão e exercícios",
    "Semana AV2",
    "Capítulo 6 - A Segunda Guerra Mundial",
    "Capítulo 7 - A Era Vargas",
    "Semana de exercícios",
    "Capítulo 8 - Guerra Fria: o mundo bipolar",
    "Capítulo 9 - As revoluções socialistas",
    "Semana de exercícios",
    "Capítulo 10 - Os processos de descolonização",
    "Semana de ajustes e exercícios",
    "Semana de revisão e exercícios",
    "Semana AV2",
    "Capítulo 11 - Democracia no Brasil do pós-guerra: de Dutra a JK",
    "Capítulo 12 - Democracia no Brasil do pós-guerra: de Jânio ao golpe de 1964",
    "Semana de exercícios",
    "Capítulo 13 - Ditadura Militar no Brasil I",
    "Capítulo 14 - Ditadura Militar no Brasil II",
    "Semana de exercícios",
    "Capítulo 15 - O processo de redemocratização do Brasil",
    "Semana de ajustes e exercícios",
    "Semana de revisão e exercícios",
    "Semana AV2",
    "Capítulo 16 - As experiências ditatoriais no restante da América",
    "Capítulo 17 - O fim da Guerra Fria e o processo de globalização",
    "Capítulo 18 - A Nova República brasileira: de Collor a Lula",
    "Capítulo 19 - O Brasil dos dias atuais: questões culturais e identitárias",
    "Capítulo 20 - Os conflitos do século XXI e a questão do terrorismo",
    "Semana de revisão e exercícios",
    "Semana AV2",
    "Aulas revisionais",
    "Aulas revisionais",
    "Provas de Recuperação",
]

topicos = {
    "BG-9VES11": [
        "Semana de acolhimento - Capítulo 1 - A Primeira Guerra Mundial e a Revolução Russa",
        "Capítulo 2 - A Crise de 1929 e o fascismo italiano",
        "Semana de exercícios",
        "Capítulo 3 - O nazismo alemão",
        "Capítulo 4 - O nascimento da República no Brasil",
        "Semana de exercícios",
        "Capítulo 5 - A consolidação da República brasileira",
        "Semana de revisão e exercícios",
        "Semana AV2",
        "Capítulo 6 - A Segunda Guerra Mundial",
        "Capítulo 7 - A Era Vargas",
        "Semana de exercícios",
        "Capítulo 8 - Guerra Fria: o mundo bipolar",
        "Capítulo 9 - As revoluções socialistas",
        "Semana de exercícios",
        "Capítulo 10 - Os processos de descolonização",
        "Semana de ajustes e exercícios",
        "Semana de revisão e exercícios",
        "Semana AV2",
        "Capítulo 11 - Democracia no Brasil do pós-guerra: de Dutra a JK",
        "Capítulo 12 - Democracia no Brasil do pós-guerra: de Jânio ao golpe de 1964",
        "Semana de exercícios",
        "Capítulo 13 - Ditadura Militar no Brasil I",
        "Capítulo 14 - Ditadura Militar no Brasil II",
        "Semana de exercícios",
        "Capítulo 15 - O processo de redemocratização do Brasil",
        "Semana de ajustes e exercícios",
        "Semana de revisão e exercícios",
        "Semana AV2",
        "Capítulo 16 - As experiências ditatoriais no restante da América",
        "Capítulo 17 - O fim da Guerra Fria e o processo de globalização",
        "Capítulo 18 - A Nova República brasileira: de Collor a Lula",
        "Capítulo 19 - O Brasil dos dias atuais: questões culturais e identitárias",
        "Capítulo 20 - Os conflitos do século XXI e a questão do terrorismo",
        "Semana de revisão e exercícios",
        "Semana AV2",
        "Aulas revisionais",
        "Aulas revisionais",
        "Provas de Recuperação",
    ],
    "NI-9VES11": [],  # será preenchido abaixo
    "NI-1VES11": [
        "1º dia de aula (04/02): Acolhimento / Capítulo 1: A transição da Idade Média para a Modernidade",
        "Capítulo 2: Idade Média - Renascimento e Reformas",
        "Semana de exercícios/ajustes",
        "Capítulo 3: Idade Moderna - Formação dos Estados nacionais e a estrutura do Antigo Regime",
        "Capítulo 4: Os povos americanos e a chegada dos europeus à América",
        "Capítulo 5: A África na Idade Média e na Idade Moderna",
        "Semana de exercícios/ajustes",
        "Semana de revisão",
        "Semana AV2",
        "Entrega de AV2 - Início do 2º bimestre / Capítulo 6: Brasil Colonial I - Séculos XVI e XVII",
        "Capítulo 6: Brasil Colonial I - Séculos XVI e XVII",
        "Capítulo 7: Brasil Colonial II - Séculos XVIII",
        "Semana de exercícios/ajustes",
        "Capítulo 8: Revoluções Inglesas e a Revolução Industrial",
        "Capítulo 9: Iluminismo e Independência dos Estados Unidos",
        "Capítulo 10: Reformismo e crise na colônia",
        "Semana de exercícios/ajustes",
        "Semana de revisão",
        "Semana AV2",
        "Entrega de AV2 - Início do 3º bimestre / Capítulo 11: Revolução Francesa",
        "Capítulo 11: Revolução Francesa",
        "Capítulo 12: Período Napoleônico",
        "Semana de exercícios/ajustes",
        "Capítulo 13: Restauração europeia e revoluções liberais do século XIX",
        "Capítulo 14: O período joanino e o processo de Independência do Brasil",
        "Capítulo 15: Os processos de Independência da América Latina",
        "Semana de exercícios/ajustes",
        "Semana de revisão",
        "Semana AV2",
        "Entrega de AV2 - Início do 4º bimestre / Capítulo 16: Unificações, doutrinas sociais e a Comuna de Paris",
        "Capítulo 17: O Primeiro Reinado",
        "Capítulo 18: O Período Regencial",
        "Capítulo 19: América Latina e EUA no século XIX",
        "Capítulo 20: O Segundo Reinado",
        "Semana de revisão",
        "Semana AV2",
        "Revisão para recuperação",
        "Revisão para recuperação",
        "Semana de provas",
    ],
    "NI-2VES11": [
        "1º dia de aula (04/02): Acolhimento / Capítulo 1: Imperialismo e Primeira Guerra Mundial",
        "Capítulo 2: Revolução Russa",
        "Semana de exercícios/ajustes",
        "Capítulo 3: Crise do Segundo Reinado, Proclamação da República e República das Espadas",
        "Capítulo 4: República Oligárquica",
        "Capítulo 5: Movimentos sociais na Primeira República",
        "Semana de exercícios/ajustes",
        "Semana de revisão",
        "Semana AV2",
        "Entrega de AV2 - Início do 2º bimestre / Capítulo 6: Crise da Primeira República",
        "Capítulo 7: Crise de 29",
        "Semana de exercícios/ajustes",
        "Capítulo 8: Totalitarismo",
        "Capítulo 9: Segunda Guerra Mundial",
        "Semana de exercícios/ajustes",
        "Capítulo 10: Era Vargas",
        "Capítulo 11: Ditadura Militar no Brasil",
        "Semana de revisão",
        "Semana AV2",
        "Entrega de AV2 - Início do 3º bimestre / Capítulo 12: Guerra Fria I - pós-2 Guerra Mundial",
        "Capítulo 13: Guerra Fria II - China, Coreia e Cuba",
        "Semana de exercícios/ajustes",
        "Capítulo 14: República liberal democrática - Dutra e Vargas",
        "Capítulo 15: República liberal democrática - JK e Jânio",
        "Semana de exercícios/ajustes",
        "Capítulo 16: Jango, o golpe de 1964 e o governo Castelo Branco",
        "Semana de revisão",
        "Semana AV2",
        "Entrega de AV2 - Início do 4º bimestre / Capítulo 17: Costa e Silva e Médici",
        "Capítulo 18: Independências afro-asiáticas",
        "Capítulo 19: Fim da Guerra Fria",
        "Capítulo 20: Fim da ditadura brasileira e processo de redemocratização",
        "Semana de revisão",
        "Semana AV2",
        "Revisão para recuperação",
        "Revisão para recuperação",
        "Semana de provas",
    ],
    "BG-2VES11": [
        "1º dia de aula (04/02): Acolhimento / Capítulo 1: Imperialismo e Primeira Guerra Mundial",
        "Capítulo 2: Revolução Russa",
        "Semana de exercícios/ajustes",
        "Capítulo 3: Crise do Segundo Reinado, Proclamação da República e República das Espadas",
        "Capítulo 4: República Oligárquica",
        "Capítulo 5: Movimentos sociais na Primeira República",
        "Semana de exercícios/ajustes",
        "Semana de revisão",
        "Semana AV2",
        "Entrega de AV2 - Início do 2º bimestre / Capítulo 6: Crise da Primeira República",
        "Capítulo 7: Crise de 29",
        "Semana de exercícios/ajustes",
        "Capítulo 8: Totalitarismo",
        "Capítulo 9: Segunda Guerra Mundial",
        "Semana de exercícios/ajustes",
        "Capítulo 10: Era Vargas",
        "Capítulo 11: Ditadura Militar no Brasil",
        "Semana de revisão",
        "Semana AV2",
        "Entrega de AV2 - Início do 3º bimestre / Capítulo 12: Guerra Fria I - pós-2 Guerra Mundial",
        "Capítulo 13: Guerra Fria II - China, Coreia e Cuba",
        "Semana de exercícios/ajustes",
        "Capítulo 14: República liberal democrática - Dutra e Vargas",
        "Capítulo 15: República liberal democrática - JK e Jânio",
        "Semana de exercícios/ajustes",
        "Capítulo 16: Jango, o golpe de 1964 e o governo Castelo Branco",
        "Semana de revisão",
        "Semana AV2",
        "Entrega de AV2 - Início do 4º bimestre / Capítulo 17: Costa e Silva e Médici",
        "Capítulo 18: Independências afro-asiáticas",
        "Capítulo 19: Fim da Guerra Fria",
        "Capítulo 20: Fim da ditadura brasileira e processo de redemocratização",
        "Semana de revisão",
        "Semana AV2",
        "Revisão para recuperação",
        "Revisão para recuperação",
        "Semana de provas",
    ],
}

# -------- Interface --------
st.set_page_config(page_title="Mock Aulas Dadas", layout="wide")
st.title("📚 Registro de Aulas Dadas")

# Login mock
if "logado" not in st.session_state:
    st.text_input("E-mail institucional", key="email_input")
    st.text_input("Senha", type="password", key="senha_input")
    if st.button("Entrar"):
        st.session_state.logado = True
        st.session_state.email = st.session_state.email_input
    st.stop()

# Pós-login
st.success(f"Bem-vindo, {st.session_state.email.split('@')[0].capitalize()}")

# Seleção de Unidade e Turma
unidade = st.selectbox("Selecione a Unidade", unidades)
turma, disciplina = st.selectbox(
    "Selecione Turma e Disciplina",
    options=mapa_turmas[unidade],
    format_func=lambda x: f"{x[0]} - {x[1]}"
)

# Botão consultar caixa PLD
if "consultado" not in st.session_state:
    if st.button("Consultar PLD"):
        st.session_state.consultado = True
    else:
        st.stop()

# Marcação salva
if "salvo" not in st.session_state:
    st.session_state.salvo = False

# Exibição de tabela de tópicos (3 colunas)
st.markdown("---")
st.subheader(f"Tópicos para {turma} - {disciplina}")
for idx, tema in enumerate(topicos[turma], start=1):
    col1, col2, col3 = st.columns([1, 6, 1])
    col1.write(idx)
    col2.write(tema)
    # Marcagem inicial (primeiros 10 sempre marcados)
    if idx <= 10:
        default = True
        disabled = True
    else:
        default = st.session_state.get(f"chk_{idx}", False)
        # Após salvar, bloqueia apenas as marcadas
        if st.session_state.salvo and idx in st.session_state.get("saved_idxs", []):
            disabled = True
        else:
            disabled = False
    col3.checkbox("", value=default, disabled=disabled, key=f"chk_{idx}")

# Botão de Salvar Marcações
if st.button("💾 Salvar marcações", key="save_btn"):
    # Identifica novos marcados além dos 10 iniciais
    saved = [i for i in range(11, len(topicos[turma]) + 1) if st.session_state.get(f"chk_{i}")]
    # Armazena para bloqueio futuro
    st.session_state.salvo = True
    st.session_state.saved_idxs = saved
    # Nenhuma mensagem exibida; apenas congelamento de checkboxes
    # Você pode adicionar um toast ou pequeno feedback se desejar
