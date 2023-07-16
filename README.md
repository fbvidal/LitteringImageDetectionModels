# Reconhecimento de Resíduos Sólidos em Ambientes Não-Estruturados Utilizando Modelos de Aprendizado Profundo.

Esse repositório contém os resultados e outros materiais utilizados na realização do trabalho Detecção e Reconhecimento de Resíduos Sólidos em Ambientes Não-Estruturados Utilizando Modelos de Aprendizado Profundo.

Neste trabalho foi realizado um estudo sobre os principais datasets e modelos utilizados para a resolução do problema de detecção de resíduos sólidos em imagens. Além disso, foi realizado treinamento, sobre os bancos de imagem escolhidos, dos principais modelos de aprendizagem profunda da arquitetura You Only Look Once(YOLO) versão 7, aplicando técnicas de otimização como: Transferência de aprendizagem e aumento de dados manuais e artificiais. Por fim, foi feita também uma comparação com os trabalhos do estado-da-arte na área.

Mais especificamente aqui se encontram os resultados do treino de todos os modelos, localizados na pasta results. Assim como as divisões utilizadas no treino, localizadas na pasta splits. Adicionalmente os scripts próprios utilizados para formatar os bancos de imagem, localizados na pasta scripts. Por fim, abaixo se encontram informações sobre os bancos de imagens utilizados. 

## Conjuntos de Imagem:

* [TACO](https://github.com/pedropro/TACO/tree/master)
  
    Clone o repositório Taco
        `git clone https://github.com/pedropro/TACO.git`
  
    Instale os requirements
        `pip3 install -r requirements.txt`
  
    Baixe as imagens oficiais etiquetadas
        `python3 download.py`

* [TACO extended](https://github.com/wimlds-trojmiasto/detect-waste/tree/main)
  
    Clone o repositório Taco
        `git clone https://github.com/pedropro/TACO.git`
  
    Instale os requirements
        `pip3 install -r requirements.txt`
  
    Baixe as imagens oficiais etiquetadas
        `python3 download.py`
  
    Baixe as imagens da comunidade etiquetadas
        `python3 download.py --dataset_path ./data/annotations_unofficial.json`
  
    Utile as etiquetas refeitas pelas autoras
        `https://github.com/wimlds-trojmiasto/detect-waste/tree/main/annotations`

## Autores: 

Luís Humberto Chaves Senno - betolhcs@protonmail.com - Engenharia Mecatrônica - Universidade de Brasília (UnB).

David Fanchic Chatelard - davidfchatelard@gmail.com - Engenharia Mecatrônica - Universidade de Brasília (UnB).

## Citação: 
```
@masterthesis{LitteringImageDetectionModels,
    author = {Chaves Senno, L., Chatelard, D.},
    title = {Detecção e Reconhecimento de Resíduos
Sólidos em Ambientes Não-Estruturados
Utilizando Modelos de Aprendizado Profundo},
    school = {University of Brasília (UnB)},
    address = {Brasília, Brasil},
    year = {2023},
    type={Bachelor's Thesis}
}
```
