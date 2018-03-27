X=[];
for i=1:3
    for j=2:5
        char1 = imread(strcat('.\set',num2str(i),'\',num2str(j),'.png'));
        % Binarize image
        char1BW = im2bw(char1, 0.4);
        % figure,
        % imshow(char1BW) %show image
        % *** CENTER AND RESIZE CHARACTER ***
        %find all co­ordinates for the character in the image
        [ I, J] = find(char1BW==0);
        %plot the character to see if the coordinates are correct
        % figure,
        %plot(J, I)
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
        imshow(char1Resize);
        sizeChar1 = size(char1Resize);
        charRow = reshape(char1Resize' , 1, sizeChar1(1) *sizeChar1(2) );
        X=horzcat(charRow',X);
    end
end
T = eye(4);
T1=horzcat(T,T);
T=horzcat(T1,T);

setdemorandstream(pi);
net1 = patternnet(3);
net1.divideFcn = '';
net1.trainParam.epochs=150;
net1 = train(net1,X,T,nnMATLAB);
save('net1.mat','net1');

numNoise = 20;
Xn = min(max(repmat(X,1,numNoise)+randn(900,12*numNoise)*0.2,0),1);
Tn = repmat(T,1,numNoise);

net2 = feedforwardnet(4);
net2.divideFcn = '';
net2.trainParam.epochs=150;
net2 = train(net2,Xn,Tn,nnMATLAB);
save('net2.mat','net2');

noiseLevels = 0:.05:1;
numLevels = length(noiseLevels);
percError1 = zeros(1,numLevels);
percError2 = zeros(1,numLevels);
for i = 1:numLevels
  Xtest = min(max(repmat(X,1,numNoise)+randn(900,12*numNoise)*noiseLevels(i),0),1);
  Y1 = net1(Xtest);
  percError1(i) = sum(sum(abs(Tn-compet(Y1))))/(12*numNoise*2);
  Y2 = net2(Xtest);
  percError2(i) = sum(sum(abs(Tn-compet(Y2))))/(12*numNoise*2);
end

figure
plot(noiseLevels,percError1*100,'--',noiseLevels,percError2*100);
title('Percentage of Recognition Errors');
xlabel('Noise Level');
ylabel('Errors');
legend('Network 1','Network 2','Location','NorthWest')
