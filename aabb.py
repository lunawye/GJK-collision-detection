import numpy
def collides_with(lower_bound,upper_bound,lower_bound_compare,upper_bound_compare):
    
    a=lower_bound[0]
    b=lower_bound[1]
    c=upper_bound[0]
    d=upper_bound[1]
    e=lower_bound_compare[0]
    f=lower_bound_compare[1]
    g=upper_bound_compare[0]
    h=upper_bound_compare[1]


    x1=a<=e<=c
    x2=a<=g<=c
    y1=b<=f<=d
    y2=b<=h<=d

    collision=False

    if (x1 or x2) and (y1 or y2): collision=True

    return collision

v1 = [[0,0,0],[1,0,0],[1,1,0],[0,1,0],[0,0,1],[1,0,1],[1,1,1],[0,1,1]]
v1=numpy.array(v1)
v1xmin=min(v1[:,0])
v1xmax=max(v1[:,0])
v1ymin=min(v1[:,1])
v1ymax=max(v1[:,1])
v1zmin=min(v1[:,2])
v1zmax=max(v1[:,2])
F1 = [[1,4,5,8],[1,2,3,4],[1,2,5,6],[2,3,6,7],[3,4,7,8],[5,6,7,8]]; 
v2 = [[3,3,2],[5,3,2],[4,5,2], [4,4,4]];
v2=numpy.array(v2)
v2xmin=min(v2[:,0])
v2xmax=max(v2[:,0])
v2ymin=min(v2[:,1])
v2ymax=max(v2[:,1])
v2zmin=min(v2[:,2])
v2zmax=max(v2[:,2])
F2 = [[1,2,3],[1,2,4],[1,3,4],[2,3,4]];
v3 = [[1,1,1],[2,1,1],[2,2,1],[1,2,1],[1,1,2],[2,1,2],[2,2,2],[1,2,2]];
v3=numpy.array(v3)
F3 = [[1,4,5,8],[1,2,3,4],
    [1,2,5,6],
    [2,3,6,7],
    [3,4,7,8],
    [5,6,7,8],
];
v3xmin=min(v3[:,0])
v3xmax=max(v3[:,0])
v3ymin=min(v3[:,1])
v3ymax=max(v3[:,1])
v3zmin=min(v3[:,2])
v3zmax=max(v3[:,2])

v1lower_bound=(v1xmin,v1ymin,v1zmin)
v1upper_bound=(v1xmax,v1ymax,v1zmax)
v2lower_bound=(v2xmin,v2ymin,v2zmin)
v2upper_bound=(v2xmax,v2ymax,v2zmax)
v3lower_bound=(v3xmin,v3ymin,v3zmin)
v3upper_bound=(v3xmax,v3ymax,v3zmax)
v1.__init__()


collision1=collides_with(v1lower_bound,v1upper_bound,v2lower_bound,v2upper_bound)
collision2=collides_with(v1lower_bound,v1upper_bound,v3lower_bound,v3upper_bound)
collision3=collides_with(v2lower_bound,v2upper_bound,v3lower_bound,v3upper_bound)

if collision1: 
    print(collision1)
    print('collision between object 1 and object 2')
if collision2: 
    print(collision2) 
    print('collision between object 1 and object 3')
if collision3: 
    print(collision3)
    print('collision between object 2 and object 3') 
