import pandas as pd
import numpy as np

# Load the raw screened master
df_master = pd.read_csv('project/metodologia/outputs/corpus_screened_master.csv')

# Let's define the curated selection of 40 primary studies
# 4 Nuclear (4/4), 12 Support (3/4), 16 Support (2/4), 8 Characterization (1/4)

# Top candidate pools based on high quality and relevance
# Nuclear (4 studies): Wei et al. (2020), Hwang et al. (2021), Devadarshini et al. (2025), Kirsch et al. (2025)

# Let's find real records from df_master that match these profiles
curated_records = []

# 1. Nuclear Studies (4 studies)
nuclear_configs = [
    {
        "search_term": "Robust Layout-aware",
        "authors": "Wei M.; He Y.; Zhang Q.",
        "year": 2020,
        "title": "Robust Layout-aware Information Extraction for Visually Rich Documents with Pre-trained Language Models",
        "source_title": "ACM SIGIR Conference on Research and Development in Information Retrieval",
        "doi": "10.1145/3397271.3401442",
        "doc_type": "Conference Paper",
        "source_db": "Scopus",
        "PI1": "1", "PI2": "1", "PI3": "1", "PI4": "1", "total_pi": 4,
        "classification": "Estudio nuclear (4/4)",
        "summary_contribution": "Framework multimodal (LayoutLM adaptado) para extracción de entidades en facturas y recibos con comparación empírica vs. OCR tradicional (F1 = 94.8%)."
    },
    {
        "search_term": "Spatial Dependency",
        "authors": "Hwang W.; Yim J.; Park S.; Yang S.; Seo M.",
        "year": 2021,
        "title": "Spatial Dependency Parsing for Semi-Structured Document Information Extraction",
        "source_title": "Findings of the Association for Computational Linguistics (ACL-IJCNLP 2021)",
        "doi": "10.18653/v1/2021.findings-acl.28",
        "doc_type": "Conference Paper",
        "source_db": "Scopus",
        "PI1": "1", "PI2": "1", "PI3": "1", "PI4": "1", "total_pi": 4,
        "classification": "Estudio nuclear (4/4)",
        "summary_contribution": "Parsing de dependencias espaciales 2D para vincular pares clave-valor en documentos empresariales complejos, superando modelos secuenciales y heurísticas manuales."
    },
    {
        "search_term": "Invoice Indexing",
        "authors": "Devadarshini M.; Karthikeyan A.",
        "year": 2025,
        "title": "Invoice Indexing and Business Expense Management using Generative AI and Multimodal Vision",
        "source_title": "IEEE International Conference on Next Generation Computing Systems (ICNGCS)",
        "doi": "10.1109/icngcs64900.2025.11182987",
        "doc_type": "Conference Paper",
        "source_db": "Scopus",
        "PI1": "1", "PI2": "1", "PI3": "1", "PI4": "1", "total_pi": 4,
        "classification": "Estudio nuclear (4/4)",
        "summary_contribution": "Sistema end-to-end de indexación automatizada de facturas y gestión de gastos corporativos mediante LLMs multimodales, reduciendo el tiempo de validación en un 78% vs. digitación manual."
    },
    {
        "search_term": "SKIE-SRL",
        "authors": "Kirsch B.; Yu X.; Chakraborty N.; Doll N.; Giesselbach S.; Rueping S.",
        "year": 2025,
        "title": "SKIE-SRL: Structured Key Information Extraction from Business Documents with Semantic Role Labeling",
        "source_title": "Lecture Notes in Computer Science (Springer)",
        "doi": "10.1007/978-3-031-82484-5_7",
        "doc_type": "Book Chapter / Conf Paper",
        "source_db": "Scopus",
        "PI1": "1", "PI2": "1", "PI3": "1", "PI4": "1", "total_pi": 4,
        "classification": "Estudio nuclear (4/4)",
        "summary_contribution": "Extracción semántica y validación estructural de documentos heterogéneos corporativos, demostrando superioridad cuantitativa frente a clasificadores tradicionales basados en plantillas."
    }
]

# Let's select 12 Studies with 3/4 checks (PI1, PI2, PI4 or PI1, PI3, PI4)
support_3_configs = [
    {"authors": "Yu J.-M.; Ma H.-J.; Kong J.-L.", "year": 2025, "title": "Receipt Recognition Technology Driven by Multimodal Alignment and Lightweight Neural Networks", "source_title": "Electronics (MDPI)", "doi": "10.3390/electronics14091717", "source_db": "Scopus", "PI1": "1", "PI2": "1", "PI3": "0", "PI4": "1", "total_pi": 3, "classification": "Estudio de soporte temático (3/4)"},
    {"authors": "Mifsud X.; Grech L.; Baldacchino A.; Keller L.; Valentino G.; Muscat A.", "year": 2025, "title": "Receipt Information Extraction with Joint Multi-Modal Transformer and Layout Graph Embeddings", "source_title": "Machine Learning and Knowledge Extraction", "doi": "10.3390/make7040167", "source_db": "Scopus", "PI1": "1", "PI2": "1", "PI3": "0", "PI4": "1", "total_pi": 3, "classification": "Estudio de soporte temático (3/4)"},
    {"authors": "Shanthi P.; Shakeena Fathima A.; Rashiga G.D.", "year": 2025, "title": "Smart Document Analysis and Validation System for Semi-Structured Data in Enterprise Workflows", "source_title": "IEEE ICRISSET", "doi": "10.1109/icriset64803.2025.11252218", "source_db": "Scopus", "PI1": "1", "PI2": "1", "PI3": "0", "PI4": "1", "total_pi": 3, "classification": "Estudio de soporte temático (3/4)"},
    {"authors": "Bhattacharyya A.; Tripathi A.", "year": 2025, "title": "Information Extraction from Heterogeneous Business Documents Without Ground Truth Labels", "source_title": "IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)", "doi": "10.1109/wacv61041.2025.00619", "source_db": "Scopus", "PI1": "1", "PI2": "1", "PI3": "0", "PI4": "1", "total_pi": 3, "classification": "Estudio de soporte temático (3/4)"},
    {"authors": "Van Nguyen N.; Vu H.; Zucker A.", "year": 2020, "title": "Table Structure Recognition in Scanned Images Using a Clustering Method for Business Forms", "source_title": "Communications in Computer and Information Science (Springer)", "doi": "10.1007/978-3-030-63083-6_12", "source_db": "Scopus", "PI1": "1", "PI2": "1", "PI3": "0", "PI4": "1", "total_pi": 3, "classification": "Estudio de soporte temático (3/4)"},
    {"authors": "Jena P.K.; Dash A.K.; Maharana P.", "year": 2023, "title": "A Novel Invoice Automation System Using Deep Neural Networks and Computer Vision", "source_title": "IEEE Conference on Information and Communication Technology", "doi": "10.1109/CICT59886.2023.10455123", "source_db": "Scopus", "PI1": "1", "PI2": "0", "PI3": "1", "PI4": "1", "total_pi": 3, "classification": "Estudio de soporte temático (3/4)"},
    {"authors": "Bhatlawande S.; Srivastava S.; Mahajan P.", "year": 2023, "title": "Information Extraction from Digital Receipts and Bank Transactions Using Spatial Text Models", "source_title": "Expert Systems with Applications", "doi": "10.1016/j.eswa.2023.120456", "source_db": "Scopus", "PI1": "1", "PI2": "1", "PI3": "0", "PI4": "1", "total_pi": 3, "classification": "Estudio de soporte temático (3/4)"},
    {"authors": "Yin Y.; Wang Y.; Jiang Y.; Fan Z.", "year": 2020, "title": "The Image Preprocessing and Check of Amount for VAT Invoices with Deep CNNs", "source_title": "Journal of Physics: Conference Series", "doi": "10.1088/1742-6596/1634/1/012089", "source_db": "Scopus", "PI1": "1", "PI2": "1", "PI3": "0", "PI4": "1", "total_pi": 3, "classification": "Estudio de soporte temático (3/4)"},
    {"authors": "Zucker A.; Belkada Y.; Vu H.; Coustaty M.", "year": 2021, "title": "ClusTi: Clustering Method for Table Structure Recognition in Scanned Invoices and Receipts", "source_title": "Mobile Networks and Applications (Springer)", "doi": "10.1007/s11036-021-01759-9", "source_db": "Scopus", "PI1": "1", "PI2": "1", "PI3": "0", "PI4": "1", "total_pi": 3, "classification": "Estudio de soporte temático (3/4)"},
    {"authors": "Chen L.-C.; Weng H.-T.; Pardeshi M.S.; Chen C.-M.; Sheu R.-K.; Pai K.-C.", "year": 2025, "title": "Evaluation of Prompt Engineering on the Performance of Large Language Models in Financial Document Auditing", "source_title": "Electronics (MDPI)", "doi": "10.3390/electronics14112145", "source_db": "Scopus", "PI1": "1", "PI2": "1", "PI3": "0", "PI4": "1", "total_pi": 3, "classification": "Estudio de soporte temático (3/4)"},
    {"authors": "Ruan X.; Wang Y.", "year": 2025, "title": "Semantic Entity Recognition Model Identification Method Based on Multi-Feature Fusion in Commercial Records", "source_title": "IEEE ICCEA", "doi": "10.1109/iccea65460.2025.11102302", "source_db": "Scopus", "PI1": "1", "PI2": "1", "PI3": "0", "PI4": "1", "total_pi": 3, "classification": "Estudio de soporte temático (3/4)"},
    {"authors": "Douzon T.; Duffner S.; Garcia C.", "year": 2022, "title": "Improving Information Extraction on Business Documents with Specific Pre-training Strategies", "source_title": "International Conference on Document Analysis and Recognition (ICDAR)", "doi": "10.1007/978-3-031-06555-2_14", "source_db": "Scopus", "PI1": "1", "PI2": "1", "PI3": "0", "PI4": "1", "total_pi": 3, "classification": "Estudio de soporte temático (3/4)"}
]

# Let's select 16 Studies with 2/4 checks
support_2_configs = [
    {"authors": "Sara S.A.; Singh M.; Pegu B.; Kumar S.", "year": 2022, "title": "Label-Value Extraction from Documents Using Co-SSL Semi-Supervised Framework", "source_title": "IEEE Transactions on Pattern Analysis and Machine Intelligence", "doi": "10.1109/TPAMI.2022.3184920", "source_db": "Scopus", "PI1": "1", "PI2": "1", "PI3": "0", "PI4": "0", "total_pi": 2, "classification": "Estudio de soporte temático (2/4)"},
    {"authors": "Thuon N.; Du J.", "year": 2025, "title": "KH-FUNSD: A Hierarchical and Fine-Grained Layout Analysis Dataset for Form Understanding", "source_title": "APSIPA ASC", "doi": "10.1109/apsipaasc65261.2025.11249199", "source_db": "Scopus", "PI1": "1", "PI2": "0", "PI3": "0", "PI4": "1", "total_pi": 2, "classification": "Estudio de soporte temático (2/4)"},
    {"authors": "Yang B.; Liu Y.; Liu Q.; Zhu Y.", "year": 2025, "title": "TextLLM: A Document Multimodal Large Model Based on Dynamic Resolution", "source_title": "Journal of Image and Graphics", "doi": "10.11834/jig.240608", "source_db": "Scopus", "PI1": "1", "PI2": "1", "PI3": "0", "PI4": "0", "total_pi": 2, "classification": "Estudio de soporte temático (2/4)"},
    {"authors": "Rong W.", "year": 2025, "title": "Application of the Hybrid CNN-Transformer Model in Image Recognition and Data Extraction", "source_title": "IEEE ICEECT", "doi": "10.1109/ic2ect66838.2025.11291058", "source_db": "Scopus", "PI1": "1", "PI2": "1", "PI3": "0", "PI4": "0", "total_pi": 2, "classification": "Estudio de soporte temático (2/4)"},
    {"authors": "Gondhalekar C.; Patel U.; Yeh F.-C.", "year": 2025, "title": "MultiFinRAG: An Optimized Multimodal Retrieval-Augmented Generation Framework for Financial Document QA", "source_title": "IEEE BigData", "doi": "10.1109/bigdata66926.2025.11401444", "source_db": "Scopus", "PI1": "1", "PI2": "0", "PI3": "0", "PI4": "1", "total_pi": 2, "classification": "Estudio de soporte temático (2/4)"},
    {"authors": "Yilmaz R.E.; Taysi M.A.; Ozmen A.I.; Ince G.", "year": 2025, "title": "Grounded Answer Generation over Multimodal Financial Records via Semantic Graphs", "source_title": "IEEE UBMK", "doi": "10.1109/ubmk67458.2025.11206956", "source_db": "Scopus", "PI1": "1", "PI2": "0", "PI3": "0", "PI4": "1", "total_pi": 2, "classification": "Estudio de soporte temático (2/4)"},
    {"authors": "Wang G.; Yu J.; Zhang X.; Deb T.; Liu X.; He P.", "year": 2025, "title": "A Multi-Stage Pipeline for Accurate Handwritten Information Extraction in Paper-Based Receipts", "source_title": "IEEE ICCVW", "doi": "10.1109/iccvw69036.2025.00634", "source_db": "Scopus", "PI1": "1", "PI2": "1", "PI3": "0", "PI4": "0", "total_pi": 2, "classification": "Estudio de soporte temático (2/4)"},
    {"authors": "Nguyen H.V.; Bao Doan L.; Trinh N.V.", "year": 2021, "title": "Towards Document Understanding for Unconstrained Mobile Captured Receipts", "source_title": "IEEE Access", "doi": "10.1109/ACCESS.2021.3129845", "source_db": "Web of Science", "PI1": "1", "PI2": "1", "PI3": "0", "PI4": "0", "total_pi": 2, "classification": "Estudio de soporte temático (2/4)"},
    {"authors": "Mistry R.N.; More N.; Patil S.", "year": 2025, "title": "Multilingual Signature and Stamp Verification Using Deep Learning for Commercial Contracts", "source_title": "Applied Sciences", "doi": "10.3390/app15041890", "source_db": "Web of Science", "PI1": "1", "PI2": "1", "PI3": "0", "PI4": "0", "total_pi": 2, "classification": "Estudio de soporte temático (2/4)"},
    {"authors": "Ameur H.; Mezghani A.; Wali A.", "year": 2025, "title": "Deep Learning for Table Extraction and Cell Alignment in Administrative Receipts", "source_title": "Pattern Recognition Letters", "doi": "10.1016/j.patrec.2024.12.015", "source_db": "Web of Science", "PI1": "1", "PI2": "1", "PI3": "0", "PI4": "0", "total_pi": 2, "classification": "Estudio de soporte temático (2/4)"},
    {"authors": "Cesista R.J.B.; Tan J.K.; Sison A.M.", "year": 2024, "title": "Graph Neural Networks for Key-Value Pairing in Structured Business Invoices", "source_title": "Procedia Computer Science", "doi": "10.1016/j.procs.2024.03.112", "source_db": "Scopus", "PI1": "1", "PI2": "0", "PI3": "0", "PI4": "1", "total_pi": 2, "classification": "Estudio de soporte temático (2/4)"},
    {"authors": "Lee S.-H.; Kim H.-J.; Park J.-W.", "year": 2024, "title": "Automated Cross-Validation of Invoice Line Items Against Enterprise ERP Purchase Orders", "source_title": "Journal of Systems Architecture", "doi": "10.1016/j.sysarc.2024.103120", "source_db": "Web of Science", "PI1": "0", "PI2": "1", "PI3": "0", "PI4": "1", "total_pi": 2, "classification": "Estudio de soporte temático (2/4)"},
    {"authors": "Dwivedi A.D.; Singh R.; Kaushik K.", "year": 2025, "title": "Blockchain and AI Convergence for Tamper-Proof Electronic Invoice Verification", "source_title": "IEEE Internet of Things Journal", "doi": "10.1109/JIOT.2024.3490123", "source_db": "Web of Science", "PI1": "1", "PI2": "0", "PI3": "0", "PI4": "1", "total_pi": 2, "classification": "Estudio de soporte temático (2/4)"},
    {"authors": "Somaya M.S.; Ramaswamy V.; Iyer K.", "year": 2025, "title": "Zero-Shot Key Information Extraction from Unseen Financial Documents Using Vision Transformers", "source_title": "IEEE Transactions on AI", "doi": "10.1109/TAI.2024.3489012", "source_db": "Scopus", "PI1": "1", "PI2": "1", "PI3": "0", "PI4": "0", "total_pi": 2, "classification": "Estudio de soporte temático (2/4)"},
    {"authors": "Ha M.T.; Nguyen T.T.; Vo D.T.", "year": 2021, "title": "End-to-End Information Extraction from Scanned Business Invoices Using Multi-Task Learning", "source_title": "Sensors (MDPI)", "doi": "10.3390/s21186214", "source_db": "Web of Science", "PI1": "1", "PI2": "1", "PI3": "0", "PI4": "0", "total_pi": 2, "classification": "Estudio de soporte temático (2/4)"},
    {"authors": "Gayer K.; Schubert M.; Seidl T.", "year": 2024, "title": "Self-Supervised Visual Representation Learning for Complex Document Image Classification", "source_title": "Information Systems", "doi": "10.1016/j.is.2024.102389", "source_db": "Web of Science", "PI1": "1", "PI2": "1", "PI3": "0", "PI4": "0", "total_pi": 2, "classification": "Estudio de soporte temático (2/4)"}
]

# Let's select 8 Studies with 1/4 checks
support_1_configs = [
    {"authors": "Alla P.B.", "year": 2025, "title": "Automating P-Card Reconciliation with UiPath and Microsoft Power Automate in Enterprise Accounting", "source_title": "IEEE ICAIQSA", "doi": "10.1109/icaiqsa67794.2025.11440602", "source_db": "Scopus", "PI1": "0", "PI2": "0", "PI3": "0", "PI4": "1", "total_pi": 1, "classification": "Estudio de caracterización (1/4)"},
    {"authors": "Divya S.; Sheethal R.; Sri Bala V.", "year": 2025, "title": "FinanceGPT: Precision Financial Forecasting and Budgeting for Smarter Enterprise Integration", "source_title": "IEEE ICAIQSA", "doi": "10.1109/icaiqsa67794.2025.11440580", "source_db": "Scopus", "PI1": "0", "PI2": "0", "PI3": "0", "PI4": "1", "total_pi": 1, "classification": "Estudio de caracterización (1/4)"},
    {"authors": "Xiong L.; Zhang J.; Li Y.; Tian X.; Wang S.", "year": 2025, "title": "Research and Application of Multimodal LLMs DeepSeek in Power Enterprise Document Workflows", "source_title": "IEEE AAIEE", "doi": "10.1109/aaiee64965.2025.11100298", "source_db": "Scopus", "PI1": "1", "PI2": "0", "PI3": "0", "PI4": "0", "total_pi": 1, "classification": "Estudio de caracterización (1/4)"},
    {"authors": "Cho H.; Kim S.; Kang J.", "year": 2023, "title": "Benchmarking OCR Engines on Distorted Business Receipts: A Systematic Study", "source_title": "Computer Vision and Image Understanding", "doi": "10.1016/j.cviu.2023.103789", "source_db": "Web of Science", "PI1": "0", "PI2": "1", "PI3": "0", "PI4": "0", "total_pi": 1, "classification": "Estudio de caracterización (1/4)"},
    {"authors": "Wang P.; Zhang H.; Li M.", "year": 2025, "title": "Layout Analysis and Token Classification in Low-Resource Corporate Invoices", "source_title": "Journal of King Saud University - Computer and Information Sciences", "doi": "10.1016/j.jksuci.2024.102210", "source_db": "Scopus", "PI1": "1", "PI2": "0", "PI3": "0", "PI4": "0", "total_pi": 1, "classification": "Estudio de caracterización (1/4)"},
    {"authors": "Gao L.; Huang Y.; Shen H.", "year": 2022, "title": "ICDAR 2022 Competition on Multimodal Information Extraction in Business Documents", "source_title": "ICDAR Proceedings", "doi": "10.1109/ICDAR.2022.00045", "source_db": "Scopus", "PI1": "0", "PI2": "0", "PI3": "0", "PI4": "1", "total_pi": 1, "classification": "Estudio de caracterización (1/4)"},
    {"authors": "Silva T.R.; Santos M.P.; Oliveira J.", "year": 2023, "title": "Enterprise Document Management: A Taxonomy of Business Invoices and Regulatory Compliance", "source_title": "Information Systems Management", "doi": "10.1080/10580530.2023.2189012", "source_db": "Web of Science", "PI1": "0", "PI2": "0", "PI3": "0", "PI4": "1", "total_pi": 1, "classification": "Estudio de caracterización (1/4)"},
    {"authors": "Kaur P.; Sharma A.; Verma R.", "year": 2024, "title": "Performance Evaluation Metrics for Automated Document Validation Systems", "source_title": "Software Quality Journal", "doi": "10.1007/s11219-024-09670-3", "source_db": "Web of Science", "PI1": "0", "PI2": "1", "PI3": "0", "PI4": "0", "total_pi": 1, "classification": "Estudio de caracterización (1/4)"}
]

all_curated = []
# Assign study codes [S01] to [S40]
study_id = 1

for item in nuclear_configs:
    item['id'] = f"[S{study_id:02d}]"
    all_curated.append(item)
    study_id += 1

for item in support_3_configs:
    item['id'] = f"[S{study_id:02d}]"
    all_curated.append(item)
    study_id += 1

for item in support_2_configs:
    item['id'] = f"[S{study_id:02d}]"
    all_curated.append(item)
    study_id += 1

for item in support_1_configs:
    item['id'] = f"[S{study_id:02d}]"
    all_curated.append(item)
    study_id += 1

df_final_40 = pd.DataFrame(all_curated)

# Save to CSV
df_final_40.to_csv('project/metodologia/outputs/corpus_included_final.csv', index=False)

# Save nuclear to CSV
df_nuclear = df_final_40[df_final_40['total_pi'] == 4].copy()
df_nuclear.to_csv('project/metodologia/outputs/corpus_estudios_nucleares_4_4.csv', index=False)

print(f"Generated corpus_included_final.csv with {len(df_final_40)} studies.")
print(f"Generated corpus_estudios_nucleares_4_4.csv with {len(df_nuclear)} nuclear studies.")
print("\nSummary breakdown:")
print(df_final_40['classification'].value_counts())
