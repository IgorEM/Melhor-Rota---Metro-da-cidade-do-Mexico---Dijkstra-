from GuiJanela import *

resposta_final=[]

with open('183arestasOrigDestPesoVirgulasSemEspacoNaoDirecional.txt','r', encoding='UTF-8') as arestas:
    data = arestas.read()


d = data.split("\n")

a = [x.split(",") for x in d]  #lista de lista [Pantitlán , Zaragoza, 1320,Zaragoza , Gómez Farías, 762,Gómez Farías  , Boulevard Puerto Aéreo, 611,Boulevard Puerto Aéreo , Balbuena, 595



#tranformando os numeros(str) da lista de lista  em  numeros inteiros
i=0
while i < len(a):
    a[i][2] = int(a[i][2])
    i+=1


#print(a) #[Pantitlán , Zaragoza,1320],Zaragoza , Gómez Farías,762]

with open('163VertEstac.txt','r', encoding='UTF-8') as vertices:
    data1 = vertices.read()


vertices=data1.split("\n") #vertices = [Panti]
#print(vertices[0]) #Pantitlán
#-------------------------criando dicionario com uma chave pra cada vertice/estação
grafo = {}

for i in vertices:
    grafo[i] = {}


grafo1 = {}

#print(grafo) #{}

#------------------------------adicionando arestas em cada vertice com seus respectivos pesos
i=0
j=0
#r=[]
for key in grafo:
    i=0
    while i < len(a):
        if key == a[i][0]:
            #r.append({a[i][1]:a[i][2]})
            #grafo1[key] = {a[i][1]:a[i][2]}
            grafo[key].update({a[i][1]:a[i][2]})
        i+=1


def dmenor_caminho(grafo, partida, chegada):
    noAgora = {}
    dAtualizada = {}
    agora = partida
    control = {}
    no_naoVisitado = []
    noAgora[agora] = 0

    for vertice in grafo.keys():
        no_naoVisitado.append(vertice)
        dAtualizada[vertice] = float('inf')

    dAtualizada[agora] = [0, partida]
    no_naoVisitado.remove(agora)

    while no_naoVisitado:
        for aolado, peso in grafo[agora].items():
            somaPeso = peso + noAgora[agora]
            if dAtualizada[aolado] == float("inf") or dAtualizada[aolado][0] > somaPeso:
                dAtualizada[aolado] = [somaPeso, agora]
                control[aolado] = somaPeso
                
        if control == {}: break
        menorTrajeto = min(control.items(), key=lambda x: x[1])
        agora = menorTrajeto[0]
        noAgora[agora] = menorTrajeto[1]
        no_naoVisitado.remove(agora)
        del control[agora]
    
    resposta = "A menor distância de %s até %s é: %s" % (partida, chegada, dAtualizada[chegada][0])
    resposta1 = "O menor caminho é: %s" % imprimiCaminho(dAtualizada, partida, chegada)
    Resposta = str(resposta)
    Resposta1 = str(resposta1)
    respostafinal = Resposta + "\n" + Resposta1
    print(respostafinal)
    resposta_final.append(respostafinal)
    printarlabel = resposta_final[0]
    ui.Respostalabel.setText(printarlabel)
    del(resposta_final[0])



def imprimiCaminho(distancia, partida, chegada):
    if chegada != partida:
        return "%s>%s" % (imprimiCaminho(distancia, partida, distancia[chegada][1]),chegada)
    else:
        return partida


    
def main(ui):
    
    def a():
        Origem = ui.OrigemlineEdit.text()
        Destino = ui.DestinolineEdit.text()
        origem = str(Origem)
        destino = str(Destino)
        dmenor_caminho(grafo, origem, destino)
        
        

    ui.BotaoPesquisar.clicked.connect(a)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    main(ui)
    sys.exit(app.exec_())