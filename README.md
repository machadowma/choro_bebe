# choro_bebe

Algoritmo para determinar a valência do som emitido por um bebê como positiva ou negativa. Em caso de valência negativa, o algoritmo classifica a necessidade do bebê como: fome, eructação, dor, sono, frio/calor ou desconforto.

Os arquivos de áudio utilizados para treinar o algoritmo devem estar separados em diretórios de acordo com a classificação do som do bebê:
 * training_data/bp-belly_pain
* training_data/bu-needs_burping
* training_data/ch-cold_hot
* training_data/dc-discomfort
* training_data/hu-hungry
* training_data/la-laughter
* training_data/ti-tired

Os arquivos de áudio que serão classificados automaticamente pelo algoritmo devem estar no diretório:
 * testing_data
 
 O resultado da classificação é copiado para o arquivo:
  * result.txt
