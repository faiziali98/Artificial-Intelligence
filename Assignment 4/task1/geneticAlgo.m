
clear all
clc

target_image=(imread('img.jpg'));
 random_image1=(imread('1.jpg'));
 random_image2=(imread('2.jpg'));
 random_image3=(imread('3.jpg'));
 random_image4=(imread('4.jpg'));
 random_image5=(imread('5.jpg'));
 random_image6=(imread('6.jpg'));
imageArray={random_image1,random_image2,random_image3,random_image4,random_image5,random_image6};

for iter=1:100000
            disp(iter);
            %%fitness function values
            fitness = zeros(1,6);
            for i=1:6
                fitness(i) = computeFitness(imageArray{i},target_image);
            end
        
            fitnessArray=sort(fitness);
            fittest=[fitnessArray(1),fitnessArray(2),fitnessArray(3)];
            total=sum(fittest);
            participation = zeros(1,6);
            for i=1:3
                participation(i) = round(((fitnessArray(i))/total) * 6);
            end
            oldArray = imageArray;
            imageArray={};
            for j=1:3
                for i=1:6
                    if(fitness(i) == fittest(j))
                        correctImage = oldArray{i};
                        for k=1:participation(j)
                            imageArray{end+1} = correctImage;
                        end
                        break;
                    end
                end
            end
            %%crossover 
            crossover_probability=0.3;
            rand_num_crossover=rand(1);
              if(rand_num_crossover >=crossover_probability)
                [array{1}]=crossOver(imageArray{1},imageArray{3});
                [array{2}]=crossOver(imageArray{3},imageArray{1});
                [array{3}]=crossOver(imageArray{5},imageArray{2});
                [array{4}]=crossOver(imageArray{2},imageArray{5});
                [array{5}]=crossOver(imageArray{6},imageArray{4});
                [array{6}]=crossOver(imageArray{4},imageArray{6});
                imageArray=array;
                imageArray=mutationFunction(imageArray);
              else
                imageArray=mutationFunction(imageArray); 
              end 
    if(mod(iter,1000) == 0)
    final_image1=strcat('image1',int2str(iter),'.bmp');
    imwrite(imageArray{1},final_image1,'BMP');
     final_image2=strcat('image2',int2str(iter),'.bmp');
    imwrite(imageArray{2},final_image2,'BMP');
    final_image3 =strcat('image3',int2str(iter),'.bmp');
    imwrite(imageArray{3},final_image3,'BMP');
    end

end
