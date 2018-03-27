clear all

load('net1.mat');
load('net2.mat');

filename = uigetfile;

char1 = imread(filename);
% Binarize image
char1BW = im2bw(char1, 0.4);
[ I, J] = find(char1BW==0);
x1 = 1;
if(min(I)-1 > 1)
   x1 = min(I)-1;
end
x2 = 1;
        if(min(I) +1 < length(I) )
            x2 = max(I) +1;
        end
        y1 = 1;
        if(min(J)-1 > 1)
            y1 = min(J)-1;
        end
        y2 = 1;
        if(min(J) +1 < length(J) )
            y2 = max(J)+1;
        end

        %calculate average difference between length and width
        meanDiff = floor(abs(((x2-x1)-(y2-y1) ) /2) );
        %check whether the character has greater length or width
        if(x2-x1 > y2-y1) %if width is greater
            %trim the extra image
            char1BW([ 1: x1, x2: end] , : ) =[ ];
            %add average difference to length and trim the extr image 
            char1BW(: , [ 1: (y1-meanDiff) , (y2+meanDiff) : end] ) =[ ];
        elseif(x2-x1 < y2-y1) %if length is greater
            %add average difference to width and trim the extra image 
            char1BW([ 1: (x1-meanDiff) , (x2+meanDiff) : end] , : ) =[ ];
            char1BW(: , [ 1: y1, y2: end] ) =[ ];
        else %if both are equal
            %trim the extra image
            char1BW([ 1: x1, x2: end] , : ) =[ ];
            char1BW(: , [ 1: y1, y2: end] ) =[ ];
        end
%imshow(char1BW); %check image again
%resize image and check results again
char1Resize = imresize(char1BW, [30,30] );
figure
imshow(char1Resize);
sizeChar1 = size(char1Resize);
charRow = reshape(char1Resize' , 1, sizeChar1(1) *sizeChar1(2) );
Y1 = net2(charRow');
Y1=compet(Y1);
disp(Y1);