import streamlit as st

generos={
    "Hip Hop":{
        "Hungria":'http://youtube.com/watch?v=B7RCImlm2Og&list=RDB7RCImlm2Og&start_radio=1',
        "Racionais MCs": 'https://www.youtube.com/watch?v=tWSr-NDZI4s&list=RDtWSr-NDZI4s&start_radio=1',
        "Tribo da Periferia": 'https://www.youtube.com/watch?v=A2HvRcZlHvg&list=RDA2HvRcZlHvg&start_radio=1',
        "Projota": 'https://www.youtube.com/watch?v=h50UX7FvQks&list=RDh50UX7FvQks&start_radio=1'
        } , 
    "Rock":{
        "Bon Jovi": 'https://www.youtube.com/watch?v=vx2u5uUu3DE&list=RDvx2u5uUu3DE&start_radio=1',
        "Linkin Park": 'https://www.youtube.com/watch?v=kXYiU_JCYtU&list=RDkXYiU_JCYtU&start_radio=1',
        "Nickelback":'https://www.youtube.com/watch?v=_JQiEs32SqQ&list=RD_JQiEs32SqQ&start_radio=1',
        "Evanescence": 'https://www.youtube.com/watch?v=3YxaaGgTQYM&list=RD3YxaaGgTQYM&start_radio=1'
    },
    "Pagode":{
        "Menos É Mais": 'https://www.youtube.com/watch?v=eAIivxKZYZw&list=RDeAIivxKZYZw&start_radio=1',
        "Pericles": 'https://www.youtube.com/watch?v=T3Y6RRSDm4o&list=RDT3Y6RRSDm4o&start_radio=1',
        "Ferrugem":'https://www.youtube.com/watch?v=o3dknP3jclw&list=RDo3dknP3jclw&start_radio=1',
        "Turma do Pagode": 'https://www.youtube.com/watch?v=KZy4J2a8UPc&list=RDKZy4J2a8UPc&start_radio=1'
    },
    "Funk":{
        "MC Livinho":'https://www.youtube.com/watch?v=dgD0F0it90k&list=RDdgD0F0it90k&start_radio=1',
        "MC Negão": 'https://www.youtube.com/watch?v=P1CXiQ1KgFU&list=RDP1CXiQ1KgFU&start_radio=1',
        "Dj Guuga": 'https://www.youtube.com/watch?v=A6vsyCQ4jK4&list=RDA6vsyCQ4jK4&start_radio=1',
        "Anitta": 'https://www.youtube.com/watch?v=kDhptBT_-VI&list=RDkDhptBT_-VI&start_radio=1'
    }
}

# -------------------------------------------------------sidebar

st.sidebar.title("Melodize")
st.sidebar.image('logo.png')

genero = st.sidebar.selectbox('Escolha um genero musical',generos.keys())

artista = st.sidebar.selectbox("Escolha um artista" , generos[genero])

#------------------------------------------------------ Body
st.title(artista)
st.markdown("---")
video , sobre = st.tabs(["video" , "sobre o artista"])

with video:
    st.video(generos[genero][artista])
with sobre:
    if artista =="Hungria":
        st.markdown ("""
                     Nascido em Ceilândia, Distrito Federal, cresceu em Cidade Ocidental, Goiás.[1] Hungria é filho de uma ex-empregada doméstica, e de um funcionário público. Hungria concluiu o ensino médio e chegou a iniciar um curso superior, porém trancou devido a faltas, pois estava dedicando seu tempo à carreira musical.[7] Na época em que estudou o ensino médio, Hungria trabalhou de garçom em um restaurante ao lado da escola em que estudava, e muitas vezes teve de servir prato para seus colegas de sala.[8] Como a música ainda não lhe dava retorno financeiro suficiente, sua mãe reprovava a ideia, e o queria dedicando-se aos estudos e que buscasse um emprego formal.""")
        
    elif artista == "Racionais MCs":
        st.markdown("""   
                   Racionais MC's é um grupo brasileiro de rap fundado em 1988 na cidade de São Paulo.[2][3] É formado por Pedro Paulo Soares Pereira (Mano Brown), Paulo Eduardo Salvador (Ice Blue), Edivaldo Pereira Alves (Edi Rock) e Kleber Geraldo Lelis Simões (KL Jay).[1][4][5] É o maior grupo de rap do Brasil, e está entre os grupos musicais mais influentes do país e da música brasileira.[6][7][8][9][10] Suas canções demonstram a preocupação em denunciar a destruição da vida de jovens negros e pobres das periferias brasileiras e o resultado do racismo e da violência policial, ao sustentarem a miséria diretamente ligada com a violência e o crime.[11][12][13][14] Temas como a brutalidade da polícia, do crime organizado e do estado, bem como o preconceito, as drogas e a exclusão social são recorrentes nas letras do conjunto.[15][16][17][18] Embora inicialmente conhecido apenas na capital paulista, o grupo conseguiu alcançar sucesso nacional e internacional a partir dos álbuns Raio X Brasil (1993), Sobrevivendo no Inferno (1997)[19][20] e Nada como um Dia após o Outro Dia (2002) """)
    elif artista == "Tribo da Periferia":
        st.markdown ("""
                Tribo da Periferia é uma dupla de rap formada em Brasília, Distrito Federal, atualmente integrada por Look e DuckJay.[1][2] Tribo da Periferia é conhecida nacionalmente pelos singles "Insônia" e "Insônia 2" com Hungria Hip Hop, "Imprevisível", "Nosso Plano", e "Conspiração" com Marília Mendonça.[3][4] Com oito álbuns lançados, dois discos de platina,[5] e uma vitória em premiação musical,[1] a dupla, por década é considerada uma das maiores bandas de rap do Brasil[6], sendo também considerados pioneiros do subgênero trap.     """)
    elif artista == "Projota":
        st.markdown ("""
                   Em 2014, lançou seu álbum de estreia, Foco, Força e Fé.[2] Em 2016, foi lançado seu primeiro DVD, 3Fs ao Vivo, que recebeu certificação de disco de ouro pelas 40 mil cópias vendidas.[3] Seu segundo álbum de estúdio foi lançado em 2017 e recebeu certificado de disco de ouro pelas 40 mil cópias vendidas.[4] Em 2019, lançou o álbum Tributo dos Sonhadores, que recebeu certificado de disco de ouro pelas 40 mil cópias vendidas.  """)

    elif artista == "Bon Jovi":
        st.markdown   ("""
                    Bon Jovi é uma banda americana de rock, formada em 1983, em Sayreville, Nova Jersey. A formação atual da banda consiste no cantor Jon Bon Jovi, no tecladista David Bryan, no baterista Tico Torres, no guitarrista Phil X e no baixista Hugh McDonald.[1]

A banda mantém algumas características do estilo hard rock dos anos 1980 até hoje, mas assimilou influências dos variados estilos surgidos no rock e heavy metal desde o seu álbum de estreia, em 1984. Com passar dos anos veio a se tornar uma das bandas mais bem sucedidas da história do rock, quando se trata de turnês pelo mundo, sua marca, músicas em seriados, e aparições em programas de tv, a banda em 2011 foi eleita pela revista Rolling Stone como a segunda banda de rock mais cara do planeta, perdendo o topo posteriormente para a banda irlandesa    """)

    elif artista == "Linkin Park":
        st.markdown ("""
                     Linkin Park é uma banda de rock dos Estados Unidos formada em Agoura Hills, Califórnia.[10] A formação atual da banda inclui o vocalista e multi-instrumentista Mike Shinoda, o guitarrista Brad Delson, o baixista Dave Farrell, o DJ Joe Hahn, a vocalista Emily Armstrong e o baterista Colin Brittain. A formação do grupo em seus sete primeiros álbuns de estúdio incluía o vocalista Chester Bennington e o baterista Rob Bourdon; após o suicídio de Bennington em julho de 2017, a banda entrou em um hiato por tempo indeterminado. Em setembro de 2024, Linkin Park retornou as atividades com as adições de Armstrong e Brittain.[9] O vocalista Mark Wakefield e o baixista Kyle Christner são ex-membros da banda.""")

    elif artista == "Nickelback":
        st.markdown ("""
                    Nickelback é uma banda de rock canadense formada em Hanna em 1995 por Chad Kroeger, Mike Kroeger, Ryan Peake e Brandon Kroeger. O nome da banda vem do nickel (moeda de cinco centavos canadense) que Mike Kroeger frequentemente tinha de devolver no seu trabalho numa cafeteria (here's your nickel back!).[11] Nickelback é composto atualmente pelo vocalista e guitarrista Chad Kroeger, pelo guitarrista, tecladista e backing vocal Ryan Peake, o baixista Mike Kroeger e o baterista Daniel Adair. A banda passou por diversas alterações em sua formação entre 1995 e 2005, atingindo sua formação atual quando Daniel Adair substituiu o baterista Ryan Vikedal. """)
    elif artista == "Evanescence":
        st.markdown ("""
                    A banda era popular na região de Little Rock, consolidando-se na cena musical da cidade no final da década de 1990 com os EPs: Evanescence (1998) e Sound Asleep (1999), além do álbum demo Origin, lançado em 2000. Porém foi apenas com o disco de 2003, Fallen, que a banda ganhou reconhecimento internacional e vendeu mais de 17 milhões de cópias em todo o mundo, recebendo Disco de Diamante (dez Discos de Platina) pela RIAA nos Estados Unidos. Os singles "Bring Me to Life" e "My Immortal" permaneceram por semanas no topo das paradas musicais, tornando-se os maiores sucesso da banda até então. Tamanho triunfo permitiu ao grupo realizar diversas turnês ao redor do mundo nos anos posteriores, e gerou o lançamento do álbum ao vivo Anywhere but Home em 2004. """)

    elif artista == " Menos É Mais ":
        st.markdown("""
                    Menos É Mais é um grupo brasileiro de pagode formado em 2016 na cidade do Gama no Distrito Federal por Duzão (vocais), Gustavo Goes (percussão), Paulinho Félix (percussão) e Ramon Alvarenga (percussão).[1] O grupo ganhou notoriedade por regravar faixas antigas de sucesso de outros cantores.""")

    
    elif artista == "Pericles":
        st.markdown("""
                   Péricles Aparecido Fonseca de Faria (Santo André, 22 de junho de 1969) é um cantor, compositor e instrumentista brasileiro de samba, da vertente pagode. Foi o vocalista do grupo Exaltasamba desde os primeiros anos da carreira do grupo até o final de fevereiro de 2012, quando decidiu seguir carreira solo. """)

    elif artista == "Ferrugem":
        st.markdown("""
                   Após ganhar destaque com a canção "Climatizar" nas rádios, Ferrugem assinou com a gravadora Warner Music Brasil e lançou em 2015 seu álbum de estreia Climatizar. Seu segundo álbum Seja o Que Deus Quiser foi lançado em 2017.[2] Porém Ferrugem só obteve visibilidade nacional após o lançamento do seu primeiro DVD Prazer, eu sou Ferrugem, lançado em 2018.[3] O álbum lhe rendeu uma indicação ao Grammy Latino na categoria Melhor Disco de Samba e Pagode.[4] Em 2019, lançou seu segundo DVD Chão de Estrelas """)

    elif artista == "Turma do Pagode":
        st.markdown("""
                  Turma do Pagode é um grupo brasileiro de samba formado em 1994 no bairro de Parada Inglesa, Zona Norte de São Paulo.[2] Ficaram famosos pela sua música que alcançou o primeiro lugar nas paradas de sucesso, "Lancinho". Atualmente, a banda é composta pelos integrantes Leiz, Caramelo, Fabiano Art, Rubinho, Neni Art, Marcelinho TDP, Thiago e Leandro Filé e fazem shows por todo o Brasil.  """)

    elif artista == "MC Livinho":
        st.markdown("""
                   Livinho iniciou sua carreira na música em 2008, com o lançamento da canção "Origem", mas alcançou o primeiro reconhecimento apenas aos dezoito anos, em 2012, com a música "Mulher Kama Sutra". Tornou-se reconhecido pela mídia como um dos principais expoentes do estilo musical conhecido como funk ousadia, o qual se destaca pelo erotismo lírico e conotação sexual das canções. """)

    elif artista == "MC Negão":
        st.markdown("""
                  MC Negão Original (João Vitor) é um funkeiro paulista que iniciou sua carreira em 2020 e ganhou destaque com hits como "Set do DJ GM 6.0" e projetos como "Nóis é Chefe" e "Medley de Igaratá". Sua biografia é marcada por uma transição de sua vida religiosa como pastor para o funk, influenciada por decepções no meio evangélico. Ele é conhecido por seu estilo irreverente, seu bordão "Tá Raul em bigode?" e por consolidar sua carreira no funk, acumulando milhões de streams e reconhecimento nacional.   """)
              
    elif artista == "Dj Guuga":
        st.markdown("""
               DJ Guuga, nome artístico de Wagner Marinho de Santana (São Paulo, 6 de março de 1994) é um cantor, compositor, produtor musical e DJ brasileiro. Ganhou notoriedade no Brasil a partir de 2018 como um dos principais nomes de uma nova vertente do funk brasileiro chamada arrocha funk     """)

    elif artista == "Anitta":
        st.markdown("""
            Larissa de Macedo Machado, mais conhecida como Anitta (Rio de Janeiro, 30 de março de 1993),[3] é uma cantora, compositora, atriz e empresária brasileira.[4] Uma das artistas mais proeminentes do Brasil, tornou-se conhecida por seu estilo versátil e por misturar gêneros como pop, funk brasileiro, reggaeton e música eletrônica. Já recebeu ao longo da carreira oito MTV Europe Music Awards, quatro Latin American Music Awards, três MTV Video Music Award de Melhor Artista Latino do Ano e um Prêmio da Música Brasileira, e duas indicações ao Grammy Awards e dez ao Grammy Latino,[5][6][7] além de ser a artista feminina brasileira com mais entradas na Billboard Hot 100. É comumente conhecida como a "Rainha do pop brasileiro"        """)

