# Multi-Class Classification Tutorial with the Keras Deep Learning Library

Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro

Este script foi baseado no [Machine Learning Mastery](https://machinelearningmastery.com/multi-class-classification-tutorial-keras-deep-learning-library/).

Outro link de estudo:

* [Basic Usage](https://colab.research.google.com/github/adriangb/scikeras/blob/docs-deploy/refs/heads/master/notebooks/Basic_Usage.ipynb#scrollTo=ad6e07d9)


`Keras` é uma biblioteca Python para aprendizado profundo que envolve as bibliotecas numéricas eficientes `Theano` e `TensorFlow`.

Neste tutorial, você descobrirá como usar o Keras para desenvolver e avaliar modelos de rede neural para problemas de classificação multiclasse.

Depois de concluir este tutorial passo a passo, você saberá:

* Como carregar dados de CSV e disponibilizá-los para Keras.

* Como preparar dados de classificação multiclasse para modelagem com redes neurais.

* Como avaliar modelos de rede neural Keras com scikit-learn.


## Descrição do problema

Neste tutorial, usaremos o problema de aprendizado de máquina padrão chamado conjunto de dados de flores de íris .

Este conjunto de dados é bem estudado e é um bom problema para praticar em redes neurais porque todas as 4 variáveis ​​de entrada são numéricas e têm a mesma escala em centímetros. Cada instância descreve as propriedades de medições de flores observadas e a variável de saída é uma espécie de íris específica.

Este é um problema de classificação multiclasse, o que significa que existem mais de duas classes a serem previstas, na verdade, existem três espécies de flores. Este é um tipo importante de problema para praticar com redes neurais porque os três valores de classe requerem tratamento especializado.

O conjunto de dados da flor da íris é um problema bem estudado e podemos esperar alcançar uma precisão do modelo na faixa de 95% a 97%. Isso fornece um bom alvo para mirar ao desenvolver nossos modelos.

Você pode baixar o conjunto de dados de flores de íris do [repositório UCI Machine Learning](https://archive.ics.uci.edu/ml/datasets/Iris) e colocá-lo em seu diretório de trabalho atual com o nome de arquivo `iris.csv`.


## Importar Classes e Funções

Podemos começar importando todas as classes e funções que precisaremos neste tutorial.

Isso inclui a funcionalidade que exigimos do Keras, mas também o carregamento de dados dos pandas , bem como a preparação de dados e a avaliação do modelo do scikit-learn .


## Carregar o conjunto de dados

O conjunto de dados pode ser carregado diretamente. Como a variável de saída contém strings, é mais fácil carregar os dados usando pandas. Podemos então dividir os atributos (colunas) em variáveis ​​de entrada (X) e variáveis ​​de saída (Y).


## Codifique a variável de saída

A variável de saída contém três valores de string diferentes.

Ao modelar problemas de classificação multiclasse usando redes neurais, é uma boa prática remodelar o atributo de saída de um vetor que contém valores para cada valor de classe para ser uma matriz com um booleano para cada valor de classe e se uma determinada instância tem ou não esse valor. valor da classe ou não.

Isso é chamado de [one-hot-encoding](https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning/) ou criação de variáveis ​​fictícias de uma variável categórica.

Por exemplo, neste problema três valores de classe são Iris-setosa, Iris-versicolor e Iris-virginica. Se tivéssemos as observações:

Iris-setosa
Iris-versicolor
Iris-virginica

Podemos transformar isso em uma matriz binária codificada one-hot para cada instância de dados que teria a seguinte aparência:


Podemos fazer isso primeiro codificando as strings consistentemente para inteiros usando a classe LabelEncoder do scikit-learn. Em seguida, converta o vetor de inteiros em uma codificação hot usando a função Keras `to_categorical()`.


# Defina o modelo de rede neural

A biblioteca `Keras` fornece classes wrapper para permitir que você use modelos de rede neural desenvolvidos com `Keras` no `scikit-learn`.

Existe uma classe ``KerasClassifier`` no Keras que pode ser usada como um estimador no scikit-learn, o tipo básico de modelo na biblioteca. O KerasClassifier recebe o nome de uma função como argumento. Esta função deve retornar o modelo de rede neural construído, pronto para treinamento.

Abaixo está uma função que criará uma rede neural de linha de base para o problema de classificação da íris. Ele cria uma rede simples totalmente conectada com uma camada oculta que contém $8$ neurônios.

A camada oculta (hidden layer) usa uma função de ativação do retificador que é uma boa prática. Como usamos uma codificação one-hot para nosso conjunto de dados de íris, a camada de saída deve criar $3$ valores de saída, um para cada classe. O valor de saída com o maior valor será tomado como a classe prevista pelo modelo.

A topologia de rede desta rede neural simples de uma camada pode ser resumida como:

```
inputs -> [8 hidden nodes] -> 3 outputs
```

Observe que usamos uma função de ativação `softmax` na camada de saída. Isso é para garantir que os valores de saída estejam na faixa de $0$ e $1$ e possam ser usados ​​como probabilidades previstas.

Finalmente, a rede usa o eficiente algoritmo de otimização de gradiente descendente `Adam` com uma função de `perda logarítmica`, que é chamada de `categorical_crossentropy` em Keras.


Agora podemos criar nosso `KerasClassifier` para uso no `scikit-learn`.

Também podemos passar argumentos na construção da classe KerasClassifier que serão passados ​​para a função `fit()` usada internamente para treinar a rede neural. Aqui, passamos o número de épocas como $200$ e o tamanho do lote como $5$ para usar ao treinar o modelo. A depuração também é desativada durante o treinamento, definindo verbose como $0$.

## Avalie o modelo com validação cruzada k-Fold

Agora podemos avaliar o modelo de rede neural em nossos dados de treinamento.

O scikit-learn tem excelente capacidade de avaliar modelos usando um conjunto de técnicas. O padrão-ouro para avaliar modelos de aprendizado de máquina é a validação cruzada k-fold.

Primeiro podemos definir o procedimento de avaliação do modelo. Aqui, definimos o número de dobras para 10 (um padrão excelente) e para embaralhar os dados antes de particioná-los.





Thanks God!