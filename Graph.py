class Edge:
    def __init__(self,dest_id:int,weight:int) -> None:
        self.dest_id=dest_id
        self.weight=weight

    def setWeight(self,weight:int):
        self.weight=weight
    def setEdgeValues(self,dest_id:int,weight:int):
        self.dest_id=dest_id
        self.weight=weight

    def getWeight(self):
        return self.weight
    def getDest_id(self):
        return self.dest_id

class Vertix:
    Edgelist=[Edge]
    def __init__(self,vertix_id:int=0,data:str="") -> None:
       self.vertix_id=vertix_id
       self.data=data
    def setVertix_id(self,vertix_id:int):
        self.vertix_id=vertix_id  

    def getVertix_id(self):
        return self.vertix_id
    def setData(self,data:str):
        self.data=data
    def getData(self):
        return self.data
    def getEdgeList():
        return Vertix.Edgelist
    def addEdgeToEdgeList(self,tovertixID:int,weight:int):
        Vertix.Edgelist.append(Edge(tovertixID,weight))
        print(f"edge between {self.vertix_id} and {tovertixID} is added")

    def printEdges(self):
        for edge in Vertix.Edgelist:
            print(f"{self.vertix_id}->{edge.dest_id} : {edge.weight}")
    def updateVertixName(self,sname:str):
        self.data=sname
class Graph:
   verties=[]
   def __init__(self) -> None:
       self.verties=[]

   def checkVertixExist(self,id:int):
       is_exist=False
       for vertix in self.verties:
           if vertix.vertix_id==id:
               is_exist=True
       return is_exist       
                
   def addVertix(self,vertix:Vertix):
       is_exist=self.checkVertixExist(vertix.getVertix_id())
       if is_exist==True:
           print("it is already in the list ,change the id ")
       else:
           self.verties.append(vertix)
           print("vertix added")

   def getVertixByID(self,id:int):
       for vertix in self.verties:
           if vertix.getVertix_id()==id:
               return vertix

   def checkIfEdgeExistByID( self,fromVertex:int,toVertex:int):     
       v=Vertix()
       e=[Edge]
       e=v.Edgelist
       flage=False
       for edge in e:
           if edge.getDest_id()==fromVertex:
               flage=True
               return flage      
       return flage
   def updateVertex( self,oldVID:int,vname:str):
       check=Graph.checkVertixExist(oldVID)
       if check :
           for vertix in Graph.verties:
               if vertix.getVertix_id()==oldVID:
                   vertix.setData(vname)
                   print("vertix updated")
                   break
               
   def addEdge(self,v1_id:int,v2_id:int,weight:int):
       v1_exist=self.checkVertixExist(v1_id)
       v2_exist=self.checkVertixExist(v2_exist)
       check=self.checkIfEdgeExistByID(v1_id,v2_id)
       if v1_exist and v2_exist:
           if check:
               print("edge already exist")
           else:
               for vertix in Graph.verties:
                   if vertix.getVertix_id()==v1_id:
                       vertix.addEdgeToEdgeList(v2_id,weight)
                       vertix.EdgeList.append(Edge(v2_id,weight))
                       print("edge added")
                   elif vertix.getVertix_id()==v2_id:
                       vertix.addEdgeToEdgeList(v1_id,weight)
                       vertix.EdgeList.append(Edge(v1_id,weight))
                       print("edge added")
           print("edge added")      
       else:
          print("vertix does not exist")  




           
                   
            
                   

        
       
                 
   



