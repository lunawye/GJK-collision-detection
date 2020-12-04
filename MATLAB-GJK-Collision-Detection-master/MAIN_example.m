% Example script for GJK function
%   Animates two objects on a collision course and terminates animation
%   when they hit each other. Loads vertex and face data from
%   SampleShapeData.m. See the comments of GJK.m for more information
%
%   Most of this script just sets up the animation and transformations of
%   the shapes. The only key line is:
%   collisionFlag = GJK(S1Obj,S2Obj,iterationsAllowed)
clc;clear all;close all

%How many iterations to allow for collision detection.
iterationsAllowed = 6;

% Make a figure
fig = figure;
hold on

% Load sample vertex and face data for two convex polyhedra
SampleShapeData;

% Make shape 1
S1.Vertices = V1;
S1.Faces = F1;
S1.FaceVertexCData = jet(size(V1,1));
S1.FaceColor = 'interp';
S1Obj = patch(S1);

% Make shape 2
S2.Vertices = V2;
S2.Faces = F2;
S2.FaceVertexCData = jet(size(V2,1));
S2.FaceColor = 'interp';
S2Obj = patch(S2);

% Make shape 3
S3.Vertices = V3;
S3.Faces = F3;
S3.FaceVertexCData = jet(size(V3,1));
S3.FaceColor = 'interp';
S3Obj = patch(S3);

hold off
axis equal
axis([-5 5 -5 5 -5 5])
ax = get(fig,'Children');
set(ax,'Visible','off'); % Turn off the axis for more pleasant viewing.
set(fig,'Color',[1 1 1]);
rotate3d on;

%Move them through space arbitrarily.
S1Coords = get(S1Obj,'Vertices');
S2Coords = get(S2Obj,'Vertices');
S3Coords = get(S2Obj,'Vertices');



% Animation loop. Terminates on collision.
for i = 3:-0.01:0.2;
    
    % Do collision detection
    collisionFlag1 = GJK(S1Obj,S2Obj,iterationsAllowed);
    collisionFlag2 = GJK(S1Obj,S3Obj,iterationsAllowed);
    collisionFlag3 = GJK(S3Obj,S2Obj,iterationsAllowed);
    drawnow;
    
    if collisionFlag1
        t = text(3,3,3,'1-Collision!','FontSize',30);
        break;
    %else 
        %t = text(3,3,3,'No 1-Collision!','FontSize',30);
        %break;
    end
    if collisionFlag2
        t = text(3,3,3,'2-Collision!','FontSize',30);
        break;
    end
    if collisionFlag3
        t = text(3,3,3,'3-Collision!','FontSize',30);
        break;
    end
end
