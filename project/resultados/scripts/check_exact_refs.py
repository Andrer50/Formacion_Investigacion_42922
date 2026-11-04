import docx

user_refs = {
    134: 'J. Thomas and A. Harden, "Methods for the thematic synthesis of qualitative research in systematic reviews," BMC Med. Res. Methodol., vol. 8, art. 45, 2008, doi: 10.1186/1471-2288-8-45.',
    135: 'D. S. Cruzes and T. Dybå, "Recommended steps for thematic synthesis in software engineering," in Proc. Int. Symp. Empirical Softw. Eng. Meas. (ESEM), 2011, pp. 275–284, doi: 10.1109/ESEM.2011.36.',
    136: 'J. Popay et al., "Guidance on the conduct of narrative synthesis in systematic reviews: A product from the ESRC methods programme," Lancaster Univ., Tech. Rep., 2006, doi: 10.13140/2.1.1018.4643.',
    137: 'M. Campbell et al., "Synthesis without meta-analysis (SWiM) in systematic reviews: reporting guideline," BMJ, vol. 368, p. l6890, 2020, doi: 10.1136/bmj.l6890.',
    138: 'K. Petersen, S. Vakkalanka, and L. Kuzniarz, "Guidelines for conducting systematic mapping studies in software engineering: An update," Inf. Softw. Technol., vol. 64, pp. 1–18, 2015, doi: 10.1016/j.infsof.2015.03.007.',
    139: 'N. J. van Eck and L. Waltman, "Software survey: VOSviewer, a computer program for bibliometric mapping," Scientometrics, vol. 84, no. 2, pp. 523–538, 2010, doi: 10.1007/s11192-009-0146-3.',
    143: 'S. Appalaraju, B. Jasani, B. U. Kota, Y. Xie, and R. Manmatha, "DocFormer: End-to-end transformer for document understanding," in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), 2021, pp. 973–983, doi: 10.1109/ICCV48922.2021.00103.',
    144: 'Y. Li et al., "StrucTexT: Structured text understanding with multi-modal transformers," in Proc. 29th ACM Int. Conf. Multimedia (MM), 2021, pp. 1912–1920, doi: 10.1145/3474085.3475345.',
    145: 'T. Hong, D. Kim, M. Ji, W. Hwang, D. Nam, and S. Park, "BROS: A pre-trained language model focusing on text and layout for better key information extraction from documents," in Proc. AAAI Conf. Artif. Intell., vol. 36, no. 10, 2022, pp. 10767–10775, doi: 10.1609/aaai.v36i10.21322.'
}

doc = docx.Document('project/shared/RSL_Sergio_Rupay.docx')

for p in doc.paragraphs:
    t = p.text.strip()
    for num, u_txt in user_refs.items():
        if t.startswith(f'[{num}]'):
            actual = t[len(f'[{num}] '):]
            if actual == u_txt:
                print(f'[{num}] EXACT MATCH')
            else:
                print(f'[{num}] MISMATCH:')
                print('  Expected:', repr(u_txt))
                print('  Actual:  ', repr(actual))

