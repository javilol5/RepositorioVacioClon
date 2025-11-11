```mermaid
flowchart TB
    A(["Start<br>RecorrerTablero()"]) --> B["tablero = [<br>  [4, 4, 4, 4, 0],<br>  [0, 0, 0, 0, 2],<br>  [0, 0, 0, 0, 2],<br>  [0, 1, 0, 0, 0],<br>  [0, 0, 0, 0, 0]<br>]"]
    B --> C["i = 0"]
    C --> D{"i < longitud tablero"}
    D -- No --> n1["Fin"]
    D -- Si --> n2["i += 1"]
    n3["tablero[i]"] --> D
    E(["Start<br>RecorrerFila()"]) --> n4["fila = RecorrerTablero()"]
    n4 --> n5["j = 0"]
    n5 --> n6{"j < longitud fila"}
    n6 -- Si --> n7["j += 1"]
    n6 -- No --> n8["Fin"]
    n7 --> n9["fila[j]"]
    n9 --> n6
    n2 --> n3
    Q(["Start<br>EsNavio()"]) --> n10["navio = RecorrerFila()"]
    n10 --> n11["navios = [1,2,4]"]
    n11 --> n12{"navio in navios"}
    n12 -- Si --> n13["navio"]
    n12 -- No --> n14["False"]
    n13 --> n16["Fin"]
    n14 --> n16
    n17(["Start<br>QueNavioEs()"]) --> n18["quenavio = EsNavio()"]
    n18 --> n23["nombres = {<br>1 : submarino,<br>2 : buque,<br>4 : portaaviones<br>}"]
    n19{"quenavio != 0"} -- No --> n20["False"]
    n19 -- Si --> n21["nombres[quenavio]"]
    n20 --> n22["Fin"]
    n23 --> n19
    n21 --> n22
    n24(["Start<br>SalidaPorPantalla()"]) --> n25{"QueNavioEs() == False"}
    n25 -- Si --> n26["Agua"]
    n25 -- No --> n27["QueNavioEs()"]
    n26 --> n28["Fin"]
    n27 --> n28
    n29(["Start"]) --> n30["RecorrerTablero()"]
    n30 --> n31["RecorrerFila()"]
    n31 --> n32["EsNavio()"]
    n32 --> n33["QueNavioEs()"]
    n33 --> n34["SalidaPorPantalla()"]
    n34 --> n35(["Fin"])
