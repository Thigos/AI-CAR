# AI-CAR
AI-CAR, um projeto de IA que tem como objetivo melhorar a segurança no trânsito a partir de diversas detecções utilizando Machine Learning e Deep Learning.

- [Requisitos](#requisitos)
- [Último Resultado](#último-resultado)
- [DATASET](#dataset)
- [Objetivos](#objetivos)

# Requisitos
- Linux GCC>=4.9 ou [Windows MS Visual Studio 2015 (v140)](https://go.microsoft.com/fwlink/?LinkId=532606&clcid=0x409)<br>
- [CUDA 9.1](https://developer.nvidia.com/cuda-downloads)<br>
- [OpenCV 3.4.0](https://sourceforge.net/projects/opencvlibrary/files/opencv-win/3.4.0/opencv-3.4.0-vc14_vc15.exe/download) ou [OpenCV 2.4.13](https://sourceforge.net/projects/opencvlibrary/files/opencv-win/2.4.13/opencv-2.4.13.2-vc14.exe/download)<br>
- GPU com CC> = 2.0 se você usar CUDA, ou GPU CC> = 3.0 se você usar cuDNN + CUDA: https://en.wikipedia.org/wiki/CUDA#GPUs_supported
- TensorFlow == 1.13.2

# Último Resultado
> ![result](preview.gif)<br>
 ```Versão 0.2```
 
# DATASET
O Dataset está sofrendo atualizações constantemente, na ultima atualização foram usadas ```1728``` imagens, algo ainda muito pequeno para que aja resultados precisos.

# Objetivos
1. Detecção de proximidade<br>
  1.1 Detectar veículos<br>
  1.2 Detectar distância dos carros
2. Detectar mudanças de faixa<br>
  2.1 Detectar faixas na estrada
3. Detectar fadiga<br>
  3.1 Analisar tempo entre piscadas dos olhos<br>
  3.2 Analisar quanto tempo o motorista está dirigindo 

