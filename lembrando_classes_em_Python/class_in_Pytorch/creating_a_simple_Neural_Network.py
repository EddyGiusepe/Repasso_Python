'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
# Importando as bibliotecas necessárias
import torch
import torch.nn as nn # Módulo! Incluem camadas Lineares, ativação, pooling, etc
import torch.nn.functional as F
'''
Em resumo, o módulo nn é usado para construir camadas de redes neurais,
enquanto o módulo nn.functional é usado para aplicar funções de processamento de dados a tensores.
'''
# Criamos a nossa Rede Neural
class RedeNeural(nn.Module):
    def __init__(self):
        super(RedeNeural, self).__init__()
        self.fc1 = nn.Linear(2, 4)
        self.fc2 = nn.Linear(4, 1)


    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return torch.sigmoid(x)


# Instancia a rede neural
model = RedeNeural()


# Define a entrada e o alvo
inputs = torch.tensor([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]], dtype=torch.float32)
targets = torch.tensor([[0.0], [1.0], [1.0], [0.0]], dtype=torch.float32)

# Define a função de perda e o otimizador
criterion = nn.BCELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)


# Treina a rede neural
for epoch in range(1000):
    optimizer.zero_grad()
    outputs = model(inputs)
    loss = criterion(outputs, targets)
    loss.backward()
    optimizer.step()


# Verifica as saídas da rede neural para cada entrada
with torch.no_grad():
    outputs = model(inputs)
    print(outputs)
