# Integrantes
## [David Varão Lima Bentes Pessoa](https://github.com/david-pessoa)  10402647
## [João Pedro de Souza Costa Ferreira](https://github.com/j-souzacosta) 10400720
## [João Victor Dallapé](https://github.com/zearus) 10400725
## [Pedro Nomura Picchioni](https://github.com/PedroNomura) 10401616
## [Victor Vaglieri de Oliveira](https://github.com/Victor-Vaglieri) 10400787

# **Resumo da Proposta** 

Atualmente, com o avanço crescente da indústria farmacêutica, podemos tratar cada vez mais doenças através do uso contínuo de remédios. No entanto, esses medicamentos possuem contra-indicações e efeitos adversos que precisam ser levados em consideração antes da substância ser prescrita ao paciente. Por conta disso, essas informações ficam contidas na bula do remédio. Contudo, por geralmente ser muito extensa, pode dificultar o trabalho dos profissionais da saúde ao elaborar receitas e prescrições médicas, tornado-o mais cansativo.  
Portanto, o objetivo deste projeto será desenvolver uma IA aplicada a documentos com o uso de LLMs que possa sanar as dúvidas desses profissionais acerca de medicamentos. Desse modo, esses profissionais poderão fazer consultas mais rápidas e eficientes das informações contidas nas bulas.  
Para treinar o modelo, serão usadas bulas de remédios disponíveis na internet de forma gratuita, como de sites como:
 - https://www.bulas.med.br/
 - https://www.drogaraia.com.br/bulas
 - https://consultas.anvisa.gov.br/#/bulario/
   
Pretendemos utilizar as ferramentas/pacotes:
 - **requests**: para coletar as bulas de sites públicos
 - **BeautifulSoup**: para fazer <i>web scraping</i>
 - **PyMuPDF**: para extrair textos de bulas em PDF obtidas do site do governo
 - **pandas**: para organizar e manipular dados
 - **transformers**: para utilizar modelos LLM pré-treinados
 - **sentence-transformers**: para criar embeddings semânticos das bulas e otimizar buscas rápidas

# **Referências**

ANVISA. Bulário eletrônico. Agência Nacional de Vigilância Sanitária, 2024. Disponível em: https://consultas.anvisa.gov.br/#/bulario/. Acesso em: 7 abr. 2025.

BULAS MED. Bulas de Remédios. Bulas Med, 2025. Disponível em: https://www.bulas.med.br/. Acesso em: 7 abr. 2025.

DROGA RAIA. Bulas de Medicamentos. Droga Raia, 2025. Disponível em: https://www.drogaraia.com.br/bulas. Acesso em: 7 abr. 2025.

PYTHON SOFTWARE FOUNDATION. Requests: HTTP for Humans. Versão 2.31.0. Disponível em: https://docs.python-requests.org/. Acesso em: 7 abr. 2025.

CRUM, Leonard Richardson. Beautiful Soup Documentation. Versão 4.12.2. Disponível em: https://www.crummy.com/software/BeautifulSoup/. Acesso em: 7 abr. 2025.

PYMUPDF DEVELOPMENT TEAM. PyMuPDF: Python bindings for MuPDF. Versão 1.23.6. Disponível em: https://pymupdf.readthedocs.io/. Acesso em: 7 abr. 2025.

PYTHON SOFTWARE FOUNDATION. pandas: Data analysis and manipulation tool. Versão 2.1.3. Disponível em: https://pandas.pydata.org/. Acesso em: 7 abr. 2025.

HUGGING FACE. Transformers: State-of-the-art Machine Learning for PyTorch, TensorFlow and JAX. Versão 4.38.1. Hugging Face, 2024. Disponível em: https://huggingface.co/docs/transformers/index. Acesso em: 7 abr. 2025.

REIMERS, Nils; GUREVYCH, Iryna. Sentence-Transformers: Multilingual Sentence Embeddings using BERT & XLNet. Versão 2.2.0. Disponível em: https://www.sbert.net/. Acesso em: 7 abr. 2025.
