"""
#include <iostream>
#include <memory.h>
using namespace std;
#define Maxnum 505
#define Infinity 1e8
int Graph[Maxnum][Maxnum];//两点之间边长
int Length[Maxnum];//从c1到i的长度
int MaxRanks[Maxnum];//从c1到i的救援队最大数
int RoadNum[Maxnum];//从c1到i的最短路径数
int Weight[Maxnum];//开始时顶点i处救援队数
bool Final[Maxnum];//用于Dijkstra算法标记顶点已加入最短路径集合
void Dijkstra(int n)
{
    for (int i = 0; i < n; ++i) {
        int min=Infinity;
        int v=-1;
        for (int j = 0; j < n; ++j) {
            if(!Final[j]&&Length[j]<min){
                v=j;min=Length[j];
            }
        }
        if(v==-1)break;
        else
            Final[v]=true;
        for (int j = 0; j < n; ++j) {
            if(!Final[j]&&(Length[j]==Length[v]+Graph[v][j])){
            //在Dijkstra基础上增加的
                RoadNum[j]+=RoadNum[v];
                MaxRanks[j]=(MaxRanks[v]+Weight[j])>MaxRanks[j]?
                        (MaxRanks[v]+Weight[j]):MaxRanks[j];
            }
            else if(!Final[j]&&((Length[j]>Length[v]+Graph[v][j]))){
                Length[j]=Length[v]+Graph[v][j];
                MaxRanks[j]=MaxRanks[v]+Weight[j];
                RoadNum[j]=RoadNum[v];
            }
        }
    }
}
int main(){
    fill(Graph[0],Graph[0]+Maxnum*Maxnum,Infinity);
    fill(Length,Length+Maxnum,Infinity);
    fill(MaxRanks,MaxRanks+Maxnum,0);
    fill(RoadNum,RoadNum+Maxnum,0);
    memset(Final, false, sizeof(Final));
    int n,m,c1,c2;
    cin>>n>>m>>c1>>c2;
    for (int i = 0; i < n; ++i) cin>>Weight[i];
    for (int i = 0; i < m; ++i) {
        int row,col,dist;
        cin>>row>>col>>dist;
        Graph[row][col]=Graph[col][row]=dist;
    }
    Length[c1]=0;
    MaxRanks[c1]=Weight[c1];
    RoadNum[c1]=1;//c1到c1有一条路
    Dijkstra(n);
    cout<<RoadNum[c2]<<" "<<MaxRanks[c2];
    return 0;
    }

"""